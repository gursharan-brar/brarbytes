"""Brar Bytes: turn stories.json into a spoken episode script (script.txt).

Asks Claude for original spoken commentary on each story, based only on the
headline and source, then stitches intro + stories + outro together.
"""

import json
import sys
from pathlib import Path

import anthropic

HERE = Path(__file__).parent
STORIES_FILE = HERE / "stories.json"
SCRIPT_FILE = HERE / "script.txt"

MODEL = "claude-haiku-4-5-20251001"
TARGET_WORDS = 1100  # about 8 minutes spoken
MAX_WORDS = 1400  # hard ceiling, about 10 minutes
MAX_STORY_WORDS = 300
MAX_ATTEMPTS = 3

INTRO = "Hey, it's Brar Bytes, here's what matters in AI and tech today."

SYSTEM = """You write the spoken script for Brar Bytes, a daily AI and tech podcast of about eight minutes.

Voice: a person explaining why something matters, not an article being read aloud. Use contractions, \
vary sentence length, and take an actual point of view. No headlines-style phrasing, no "in a move that", \
no bullet points, no emojis, no stage directions.

You only get a headline and a source for each story. Write original commentary on what it means and why \
it matters: the context around it, who it affects, what's overhyped or underrated, and what to watch next. \
Do not paraphrase the headline, and do not invent specifics (numbers, names, quotes, dates) \
that the headline doesn't give you. If you're speculating, say so in your own voice. Give each story a \
natural arc, with a point of view up front and a closing thought, not a list of observations.

Output only JSON, no code fences, in this shape:
{"stories": ["commentary for story 1", "commentary for story 2", ...], "outro": "..."}
"stories" must have exactly one entry per story, in the order given. Each entry is one continuous spoken segment \
of roughly the word count you're given, with no paragraph breaks. The outro is two or three sentences \
signing off."""


def build_prompt(stories, word_limit):
    per_story = min(word_limit // len(stories), MAX_STORY_WORDS)
    lines = [f"{i}. [{s['beat']}] {s['title']} (source: {s['source']})" for i, s in enumerate(stories, 1)]
    return (
        f"Today's stories:\n" + "\n".join(lines) + "\n\n"
        f"Write about {per_story} words per story. Keep all commentary plus the outro to about "
        f"{word_limit} words so the whole episode, including the intro, stays under {MAX_WORDS} words."
    )


def generate(client, stories, word_limit):
    msg = client.messages.create(
        model=MODEL,
        max_tokens=4000,
        system=SYSTEM,
        messages=[{"role": "user", "content": build_prompt(stories, word_limit)}],
    )
    text = msg.content[0].text
    # Models sometimes wrap JSON in code fences or add a lead-in sentence; keep just the object.
    start, end = text.find("{"), text.rfind("}")
    try:
        data = json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        raise ValueError(f"reply was not valid JSON (stop_reason={msg.stop_reason}): {text[:300]!r}")
    if len(data["stories"]) != len(stories):
        raise ValueError(f"expected {len(stories)} commentaries, got {len(data['stories'])}")
    return data["stories"], data["outro"].strip()


def main():
    if not STORIES_FILE.exists():
        sys.exit(f"{STORIES_FILE.name} not found, run fetch_stories.py first")
    stories = json.loads(STORIES_FILE.read_text(encoding="utf-8"))
    if not stories:
        sys.exit("stories.json is empty, nothing to write")

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
    word_limit = TARGET_WORDS - len(INTRO.split()) - 60
    script = None
    for attempt in range(MAX_ATTEMPTS):
        try:
            commentary, outro = generate(client, stories, word_limit)
        except anthropic.APIError as e:
            sys.exit(f"Script generation failed: {e}")
        except (ValueError, KeyError) as e:
            print(f"[warn] attempt {attempt + 1} gave an unusable reply: {e}")
            continue
        script = "\n\n".join([INTRO, *[c.strip() for c in commentary], outro])
        if len(script.split()) < MAX_WORDS:
            break
        print(f"[warn] attempt {attempt + 1} ran {len(script.split())} words, retrying shorter")
        word_limit = int(word_limit * 0.75)
    else:
        sys.exit(f"No valid script under {MAX_WORDS} words after {MAX_ATTEMPTS} attempts, not writing script.txt")

    SCRIPT_FILE.write_text(script + "\n", encoding="utf-8")
    print(f"Wrote {SCRIPT_FILE.name}: {len(script.split())} words, {len(stories)} stories")


if __name__ == "__main__":
    main()
