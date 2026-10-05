"""Brar Bytes: pick today's episode stories.

Pulls recent items from RSS feeds and Hacker News, classifies them into beats,
skips anything already in history.json, writes stories.json, updates history.json.
"""

import json
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import requests

HERE = Path(__file__).parent
HISTORY_FILE = HERE / "history.json"
STORIES_FILE = HERE / "stories.json"

MAX_AGE_DAYS = 3
MAX_STORIES = 4
HN_TOP_N = 60
HEADERS = {"User-Agent": "BrarBytes/1.0 (podcast story fetcher)"}

# (source name, feed url, needs_ai_filter, weight)
# General tech feeds are filtered to AI stories; weight favors primary sources.
FEEDS = [
    ("OpenAI", "https://openai.com/news/rss.xml", False, 3),
    ("Anthropic", "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml", False, 3),
    ("Google DeepMind", "https://deepmind.google/blog/rss.xml", False, 3),
    ("TechCrunch", "https://techcrunch.com/category/artificial-intelligence/feed/", False, 2),
    ("The Verge", "https://www.theverge.com/rss/index.xml", True, 2),
    ("Ars Technica", "https://feeds.arstechnica.com/arstechnica/index", True, 2),
    ("VentureBeat", "https://venturebeat.com/category/ai/feed/", False, 2),
]

AI_RE = re.compile(
    r"\b(ai|a\.i\.|llm|llms|gpt|chatgpt|openai|anthropic|claude|gemini|deepmind|"
    r"machine learning|neural|model|models|agent|agents|copilot|generative|nvidia)\b",
    re.I,
)

# Checked in order; first match wins.
BEAT_PATTERNS = [
    ("funding", re.compile(
        r"\b(raises?|raised|funding|series [a-e]|seed round|valuation|acquires?|acquired|"
        r"acquisition|buys|invests?|investment|investors?|ipo|unicorn)\b", re.I)),
    ("safety_governance", re.compile(
        r"\b(safety|safe|alignment|regulat\w*|polic(y|ies)|law|laws|lawsuit|sues?|"
        r"senate|congress|eu ai act|ban|bans|governance|copyright|privacy|"
        r"misuse|risks?|guardrails?|red.?team\w*|preparedness|executive order)\b", re.I)),
    ("model_release", re.compile(
        r"\b(launch\w*|releas\w*|introduc\w*|unveil\w*|announc\w*|debuts?|rolls? out|"
        r"new model|gpt-?\d\S*|claude \S+|gemini \S+|llama|mistral|api|available|"
        r"now live|open.?weights?)\b", re.I)),
]
BUILD_RE = re.compile(r"^show hn|github\.com|\bopen.?source", re.I)


def load_history():
    if HISTORY_FILE.exists():
        return set(json.loads(HISTORY_FILE.read_text(encoding="utf-8")))
    return set()


def entry_date(entry):
    parsed = entry.get("published_parsed") or entry.get("updated_parsed")
    if not parsed:
        return None
    return datetime(*parsed[:6], tzinfo=timezone.utc)


def fetch_feed(feed):
    source, url, needs_filter, weight = feed
    try:
        # Fetch with requests for a timeout and UA, then hand the bytes to feedparser.
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        parsed = feedparser.parse(resp.content)
    except requests.RequestException as e:
        print(f"[warn] {source}: {e}")
        return []
    items = []
    for e in parsed.entries:
        title, link, date = e.get("title", "").strip(), e.get("link", ""), entry_date(e)
        if not (title and link and date):
            continue
        if needs_filter and not AI_RE.search(title):
            continue
        items.append({"title": title, "source": source, "url": link, "date": date, "weight": weight})
    return items


def fetch_hn():
    try:
        ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=15).json()[:HN_TOP_N]
    except requests.RequestException as e:
        print(f"[warn] Hacker News: {e}")
        return []

    def get_item(i):
        try:
            return requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json", timeout=15).json()
        except requests.RequestException:
            return None

    with ThreadPoolExecutor(max_workers=16) as pool:
        raw = list(pool.map(get_item, ids))

    items = []
    for it in raw:
        if not it or it.get("type") != "story" or not it.get("title"):
            continue
        url = it.get("url") or f"https://news.ycombinator.com/item?id={it['id']}"
        items.append({
            "title": it["title"],
            "source": "Hacker News",
            "url": url,
            "date": datetime.fromtimestamp(it["time"], tz=timezone.utc),
            "weight": 1,
            "hn_score": it.get("score", 0),
        })
    return items


def classify(item):
    title, url = item["title"], item["url"]
    is_ai = bool(AI_RE.search(title))
    # Open-source projects: prefer HN / GitHub items.
    if item["source"] == "Hacker News" and BUILD_RE.search(f"{title} {url}"):
        return "build_spotlight"
    if "github.com" in url:
        return "build_spotlight"
    # HN items outside build_spotlight only count if they're about AI.
    if item["source"] == "Hacker News" and not is_ai:
        return None
    for beat, pattern in BEAT_PATTERNS:
        if pattern.search(title):
            return beat
    # Unmatched lab-blog posts are most often product/research launches.
    if item["weight"] == 3:
        return "model_release"
    return None


def score(item, now):
    age_hours = (now - item["date"]).total_seconds() / 3600
    recency = max(0.0, 1 - age_hours / (MAX_AGE_DAYS * 24)) * 5
    hn = min(item.get("hn_score", 0) / 200, 3)
    return recency + item["weight"] + hn


def main():
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=MAX_AGE_DAYS)
    history = load_history()

    with ThreadPoolExecutor(max_workers=8) as pool:
        batches = list(pool.map(fetch_feed, FEEDS))
    items = [i for batch in batches for i in batch] + fetch_hn()

    seen, candidates = set(), []
    for item in items:
        if item["url"] in history or item["url"] in seen or item["date"] < cutoff:
            continue
        seen.add(item["url"])
        beat = classify(item)
        if beat:
            item["beat"] = beat
            item["score"] = score(item, now)
            candidates.append(item)
    candidates.sort(key=lambda i: i["score"], reverse=True)

    # One per beat first, then fill remaining slots with the best leftovers.
    selected = {}
    for item in candidates:
        selected.setdefault(item["beat"], item)
    picks = list(selected.values())[:MAX_STORIES]
    for item in candidates:
        if len(picks) >= MAX_STORIES:
            break
        if item not in picks:
            picks.append(item)

    order = ["model_release", "safety_governance", "funding", "build_spotlight"]
    picks.sort(key=lambda i: order.index(i["beat"]))

    stories = [
        {
            "beat": i["beat"],
            "title": i["title"],
            "source": i["source"],
            "url": i["url"],
            "published_date": i["date"].isoformat(),
        }
        for i in picks
    ]
    STORIES_FILE.write_text(json.dumps(stories, indent=2), encoding="utf-8")
    HISTORY_FILE.write_text(json.dumps(sorted(history | {s["url"] for s in stories}), indent=2), encoding="utf-8")

    print(f"Selected {len(stories)} stories from {len(candidates)} candidates:")
    for s in stories:
        print(f"  [{s['beat']}] {s['title']} ({s['source']})")
    missing = set(order) - {s["beat"] for s in stories}
    if missing:
        print(f"No fresh story for: {', '.join(sorted(missing))}")


if __name__ == "__main__":
    main()
