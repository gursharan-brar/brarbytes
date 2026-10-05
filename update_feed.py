"""Brar Bytes: add today's episode to the podcast RSS feed (feed.xml).

Rebuilds the show-level metadata every run, puts today's item first, and keeps
every past item. Running twice on the same day replaces that day's item.
"""

import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import date, datetime, timezone
from email.utils import format_datetime
from pathlib import Path

BASE_URL = "https://gursharan-brar.github.io/brarbytes/"  # GitHub Pages root, keep the trailing slash

HERE = Path(__file__).parent
FEED_FILE = HERE / "feed.xml"
SCRIPT_FILE = HERE / "script.txt"
STORIES_FILE = HERE / "stories.json"
EPISODES_DIR = HERE / "episodes"

TITLE = "Brar Bytes"
AUTHOR = "Gursharan Brar"
DESCRIPTION = (
    "Daily AI and tech news, told straight, with an actual take. I go through what actually shipped versus "
    "what's just a demo, cut the hype, and tell you why it matters in a few minutes. Not a bot picking "
    "headlines, an actual person doing the reading. New briefs regularly, so you can stay caught up "
    "without losing an hour to doomscrolling."
)
LANGUAGE = "en-us"
COVER_URL = BASE_URL + "cover.png"
HEADLINE_MAX_CHARS = 60

ITUNES = "http://www.itunes.com/dtds/podcast-1.0.dtd"
ATOM = "http://www.w3.org/2005/Atom"
ET.register_namespace("itunes", ITUNES)
ET.register_namespace("atom", ATOM)


def add(parent, tag, text=None, **attrs):
    el = ET.SubElement(parent, tag, attrs)
    if text is not None:
        el.text = text
    return el


def make_headline(script):
    """First sentence of the first story, trimmed at a word boundary."""
    paragraphs = [p.strip() for p in script.split("\n\n") if p.strip()]
    story = paragraphs[1] if len(paragraphs) > 2 else paragraphs[0]  # skip the intro
    sentence = re.split(r"(?<=[.!?])\s", story, maxsplit=1)[0].strip().rstrip(".!?")
    if len(sentence) > HEADLINE_MAX_CHARS:
        sentence = sentence[:HEADLINE_MAX_CHARS].rsplit(" ", 1)[0].rstrip(",;:-") + "…"
    return sentence


def build_item(today, stories, script, mp3):
    item = ET.Element("item")
    add(item, "title", f"{today.isoformat()}: {make_headline(script)}")
    add(item, "description", "Today: " + "; ".join(s["title"] for s in stories) + ".")
    add(item, "enclosure", url=f"{BASE_URL}episodes/{mp3.name}", length=str(mp3.stat().st_size), type="audio/mpeg")
    add(item, "guid", f"brarbytes-{today.isoformat()}", isPermaLink="false")
    add(item, "pubDate", format_datetime(datetime.now(timezone.utc)))
    add(item, f"{{{ITUNES}}}explicit", "false")
    return item


def build_channel_header(rss):
    channel = add(rss, "channel")
    add(channel, "title", TITLE)
    add(channel, "link", BASE_URL)
    add(channel, "description", DESCRIPTION)
    add(channel, "language", LANGUAGE)
    add(channel, f"{{{ATOM}}}link", href=BASE_URL + "feed.xml", rel="self", type="application/rss+xml")
    image = add(channel, "image")
    add(image, "url", COVER_URL)
    add(image, "title", TITLE)
    add(image, "link", BASE_URL)
    add(channel, f"{{{ITUNES}}}author", AUTHOR)
    add(channel, f"{{{ITUNES}}}summary", DESCRIPTION)
    add(channel, f"{{{ITUNES}}}image", href=COVER_URL)
    add(channel, f"{{{ITUNES}}}explicit", "false")
    news = add(channel, f"{{{ITUNES}}}category", text="News")
    add(news, f"{{{ITUNES}}}category", text="Tech News")
    return channel


def main():
    today = date.today()
    mp3 = EPISODES_DIR / f"{today.isoformat()}.mp3"
    for f in (mp3, SCRIPT_FILE, STORIES_FILE):
        if not f.exists():
            sys.exit(f"{f.name} not found, run the earlier pipeline steps first")
    script = SCRIPT_FILE.read_text(encoding="utf-8")
    stories = json.loads(STORIES_FILE.read_text(encoding="utf-8"))

    new_item = build_item(today, stories, script, mp3)
    new_guid = new_item.findtext("guid")
    old_items = []
    if FEED_FILE.exists():
        old_channel = ET.parse(FEED_FILE).getroot().find("channel")
        old_items = [i for i in old_channel.findall("item") if i.findtext("guid") != new_guid]

    rss = ET.Element("rss", version="2.0")
    channel = build_channel_header(rss)
    channel.extend([new_item, *old_items])  # newest first

    ET.indent(rss)
    ET.ElementTree(rss).write(FEED_FILE, encoding="utf-8", xml_declaration=True)
    print(f"Wrote {FEED_FILE.name}: {len(old_items) + 1} episodes, latest: {new_item.findtext('title')}")


if __name__ == "__main__":
    main()
