"""Brar Bytes: turn script.txt into a dated, volume-leveled MP3 (episodes/YYYY-MM-DD.mp3).

Each paragraph of the script is synthesized with Kokoro, leveled to a common
loudness, joined with short pauses, then peak-normalized as a whole episode.
"""

import io
import sys
from datetime import date
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro import KPipeline
from pydub import AudioSegment

HERE = Path(__file__).parent
SCRIPT_FILE = HERE / "script.txt"
EPISODES_DIR = HERE / "episodes"

VOICE = "af_heart"
LANG_CODE = "a"
SAMPLE_RATE = 24000  # Kokoro's output rate
PAUSE_MS = 450  # silence between paragraphs
TARGET_DBFS = -20.0  # per-paragraph loudness before the final peak normalize
PEAK_DBFS = -1.0
BITRATE = "128k"


def synthesize(pipeline, text):
    """Kokoro splits long text into sentence-sized pieces itself; join them into one clip."""
    pieces = [np.asarray(audio, dtype=np.float32) for _, _, audio in pipeline(text, voice=VOICE) if audio is not None]
    if not pieces:
        raise RuntimeError(f"Kokoro returned no audio for: {text[:60]!r}")
    buf = io.BytesIO()
    sf.write(buf, np.concatenate(pieces), SAMPLE_RATE, format="WAV")
    buf.seek(0)
    return AudioSegment.from_wav(buf)


def main():
    if not SCRIPT_FILE.exists():
        sys.exit(f"{SCRIPT_FILE.name} not found, run write_script.py first")
    paragraphs = [p.strip() for p in SCRIPT_FILE.read_text(encoding="utf-8").split("\n\n") if p.strip()]
    if not paragraphs:
        sys.exit("script.txt is empty, nothing to voice")

    pipeline = KPipeline(lang_code=LANG_CODE)
    pause = AudioSegment.silent(duration=PAUSE_MS, frame_rate=SAMPLE_RATE)

    episode = AudioSegment.empty()
    for i, text in enumerate(paragraphs, 1):
        print(f"[{i}/{len(paragraphs)}] {text[:60]}...")
        clip = synthesize(pipeline, text)
        clip = clip.apply_gain(TARGET_DBFS - clip.dBFS)  # match loudness chunk to chunk
        episode += clip + pause if i < len(paragraphs) else clip

    episode = episode.apply_gain(PEAK_DBFS - episode.max_dBFS)  # final peak normalize

    EPISODES_DIR.mkdir(exist_ok=True)
    out = EPISODES_DIR / f"{date.today().isoformat()}.mp3"
    episode.export(out, format="mp3", bitrate=BITRATE)
    print(f"Wrote {out.relative_to(HERE)}: {len(episode) / 1000:.1f}s")


if __name__ == "__main__":
    main()
