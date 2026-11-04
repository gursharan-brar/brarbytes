# /brag plan: Brar Bytes

**What it is:** a daily AI & tech news podcast that produces itself. A GitHub Action pulls stories from 8 sources (OpenAI, Anthropic, DeepMind, TechCrunch, The Verge, Ars Technica, VentureBeat, Hacker News), picks four, has Claude write a spoken take, voices it with Kokoro, and publishes it to an RSS feed.

**For:** people who want to keep up with AI without spending an hour on it every morning.

**What sets it apart:** it cuts the flood down to four stories and gives a take on each instead of reading headlines out ("told straight, with an actual take").

**Hook:** the flood. A wall of 116 real headlines from the feed, then "Too much AI news."

**Highlights:** (1) four picks out of the flood, (2) the actual episode voice saying its own intro, (3) a finished episode in a player, 29 episodes deep.

**Punchline / outro:** the real cover art, "AI & tech news, daily", and the feed URL.

**Tone:** `default`: punchy, playful, clean. Borrows the cover's terminal feel (`BYTES_` cursor).

**Visual identity (from cover.png):** background `#070707`, white `#f4f4ef`, lime `#b5fa3f`, olive `#85ab59`. Inter Black for display type, JetBrains Mono for labels.

**Real material used:** 116 headlines from `feed.xml`, the 2026-11-03 picks and episode title, the intro line audio from `episodes/2026-11-03.mp3` (0.34–3.82s), a waveform built from that episode's real loudness, `cover.png`, the feed URL from `update_feed.py`. No invented numbers. No personal data: the only name shown is the show's.

## Music

120 BPM (0.5s beats, 2s bars), A minor, Am–F–C–G. Every scene cut lands on a beat.

## Storyboard (20.0s)

| # | Time | Scene | On screen | Sound |
|---|---|---|---|---|
| 1 | 0.0–3.0 | Hook | Dim columns of real headlines scrolling; counter climbs to 116; big "Too much AI news." | Filtered pad and hats, riser into 3.0 |
| 2 | 3.0–7.0 | Pick | Wall drops away; four 11-03 headlines land one per beat as numbered cards; "Four that matter." | Full beat kicks in; soft tuned blips as cards land |
| 3 | 7.0–11.0 | Take | Script card types the intro line in mono, synced to the real voice; "With an actual take." | Music ducks under the real episode voice |
| 4 | 11.0–15.0 | Ship | Podcast player: cover, episode title, real waveform playing; episode count flips 1 → 29 | Beat back in |
| 5 | 15.0–20.0 | Outro | Cover-art logo, blinking cursor, feed URL | Impact on 15.0, resolve on Am, tail out |
