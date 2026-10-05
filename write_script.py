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
MAX_WORDS = 500
MAX_ATTEMPTS = 2

INTRO = "Hey, it's Brar Bytes, here's what matters in AI and tech today."

SYSTEM = """You write the spoken script for Brar Bytes, a short daily AI and tech podcast brief.

Voice: a person explaining why something matters, not an article being read aloud. Use contractions, \
vary sentence length, and take an actual point of view. No headlines-style phrasing, no "in a move that", \
no bullet points, no emojis, no stage directions.

You only get a headline and a source for each story. Write original commentary on what it means and why \
it matters. Do not paraphrase the headline, and do not invent specifics (numbers, names, quotes, dates) \
that the headline doesn't give you. If you're speculating, say so in your own voice.

Output only JSON, no code fences, in this shape:
{"stories": ["commentary for story 1", "commentary for story 2", ...], "outro": "..."}
"stories" must have exactly one entry per story, in the order given. Each entry is 2 to 4 sentences. \
The outro is one or two short sentences signing off."""


def build_prompt(stories, word_limit):
    lines = [f"{i}. [{s['beat']}] {s['title']} (source: {s['source']})" for i, s in enumerate(stories, 1)]
    return (
        f"Today's stories:\n" + "\n".join(lines) + "\n\n"
        f"Keep the commentary and outro combined to about {word_limit} words so the whole episode, "
        f"including the intro, stays under {MAX_WORDS} words."
    )


def generate(client, stories, word_limit):
    msg = client.messages.create(
        model=MODEL,
        max_tokens=1500,
        system=SYSTEM,
        messages=[{"role": "user", "content": build_prompt(stories, word_limit)}],
    )
    data = json.loads(msg.content[0].text)
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
    word_limit = MAX_WORDS - len(INTRO.split()) - 20
    script = None
    for attempt in range(MAX_ATTEMPTS):
        try:
            commentary, outro = generate(client, stories, word_limit)
        except (anthropic.APIError, json.JSONDecodeError, KeyError, ValueError) as e:
            sys.exit(f"Script generation failed: {e}")
        script = "\n\n".join([INTRO, *[c.strip() for c in commentary], outro])
        if len(script.split()) < MAX_WORDS:
            break
        print(f"[warn] attempt {attempt + 1} ran {len(script.split())} words, retrying shorter")
        word_limit = int(word_limit * 0.75)
    else:
        sys.exit(f"Script still over {MAX_WORDS} words after {MAX_ATTEMPTS} attempts, not writing script.txt")

    SCRIPT_FILE.write_text(script + "\n", encoding="utf-8")
    print(f"Wrote {SCRIPT_FILE.name}: {len(script.split())} words, {len(stories)} stories")


if __name__ == "__main__":
    main()
