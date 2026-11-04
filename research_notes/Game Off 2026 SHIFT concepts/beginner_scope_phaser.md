# Beginner scope and Phaser practicalities for a 3-person Game Off 2026 team (26 evenings, ~60-75 coder-hours)

> **Research conditions (read first).** This session could not fetch itch.io, phaser.io, github.blog or sfxr.me directly (network allowlist: `getaddrinfo ENOTFOUND`), and the shared web-search budget ran out partway through. Facts about itch.io and Game Off rules therefore come from search-result excerpts of those pages, not full-page reads. Facts about Phaser come from the **official Phaser 4.2.1 npm package**, which I downloaded and read directly: its README, migration guide, source, and the official AI-agent `skills/` folder that ships inside it. Those facts are high-confidence. Sections 4, 5 and 9 (genre risk, postmortems, AI pitfalls) are thinner than planned and lean more on clearly labeled inference. The Gaps sections list what still needs checking.

## 1. Phaser 3 vs Phaser 4 in November 2026, and which starter template to use

### Takeaway
Phaser 4 is the current stable line: 4.0.0 shipped April 10, 2026, and 4.2.1 (July 9, 2026) was the latest release on npm as of Nov 4, 2026. Phaser 3's last release was 3.90.0, in May 2025. A new team should start on Phaser 4 with the official Vite template (`npm create @phaserjs/game@latest`). The one real catch is that most tutorials and most LLM training data are Phaser 3, so the team should point its AI tool at the official skills folder that ships inside the Phaser 4 npm package.

### Cited Findings
- npm `latest` dist-tag is **4.2.1**. Release dates: 4.0.0 on 2026-04-10, 4.1.0 on 2026-04-30, 4.2.0 on 2026-06-19, 4.2.1 on 2026-07-09. No later version was published as of 2026-11-04. — [npm registry: phaser](https://registry.npmjs.org/phaser) (queried directly), [npm package page](https://www.npmjs.com/package/phaser)
- The last Phaser 3 release on npm is **3.90.0 (2025-05-23)**. Earlier 3.x releases: 3.88.1 and 3.88.2 in Feb 2025. — [npm registry: phaser](https://registry.npmjs.org/phaser)
- The official changelog titles the release "Version 4.0.0 - Caladan - 10th April 2026" and calls it the biggest release in Phaser's history. — [CHANGELOG v4.0.0 (GitHub mirror, per search excerpt)](https://github.1485827954.workers.dev/phaserjs/phaser/blob/master/changelog/v4/4.0/CHANGELOG-v4.0.0.md); [GameDev.net: Phaser 4 released](https://gamedev.net/news/2759-phaser-4-released/); [GameDev.net: Phaser v4.2.1 released](https://gamedev.net/news/4825-phaser-v421-released/)
- Phaser's own comparison article says that if you are starting a new project, "there's no reason to start on Phaser 3". It also says the public-facing API was kept almost identical, so most code using standard sprites, text and tilemaps works with minimal changes. (From a search excerpt; I could not open the page.) — [phaser.io: Phaser 3 vs Phaser 4](https://phaser.io/news/2026/05/phaser-3-vs-phaser-4)
- README: "If you've built games with Phaser 3, the public API is mostly familiar - but under the hood, everything has changed." The entire v3 WebGL pipeline was replaced with a node-based renderer, and FX and masks were merged into one Filter system. — [Phaser 4.2.1 README (unpkg)](https://unpkg.com/phaser@4.2.1/README.md)
- Breaking changes most likely to trip a beginner or an AI trained on v3:
  - The Canvas renderer is deprecated, and WebGL is recommended for all new projects.
  - `preFX`/`postFX` and masks became **Filters**.
  - The tint system changed, with a new `setTintMode()`.
  - The `roundPixels` default flipped to **false** (it was true in v3).
  - `Point` was replaced by `Vector2`.
  - `Mesh` and `Plane` were removed.
  - The camera matrix was rewritten. This only matters if you touch matrices directly.

  — [Phaser v3 to v4 Migration Guide (unpkg)](https://unpkg.com/phaser@4.2.1/changelog/v4/4.0/MIGRATION-GUIDE.md)
- Official scaffolding is `npm create @phaserjs/game@latest`, a CLI with official templates. It supports Vue, React, Angular, Next.js, SolidJS, Svelte and Remix, and the bundlers Vite, Rollup, Parcel, Webpack, ESBuild, Import Map and Bun. Most templates come in JS and TS. It also offers 3 demo games: "Phaser's Revenge" (space shooter), "Coin Clicker" and "Memory Card Game". For first-time users it says: "we recommend selecting the options: `Web Bundler` and then `Vite`." Latest version is 1.3.2 (2026-04-21). — [@phaserjs/create-game on npm](https://www.npmjs.com/package/@phaserjs/create-game) (README read directly from the registry)
- The Phaser 4.2.1 npm package ships **28 official AI-agent skill files**, about 12.6k lines in total. Topics: actions-and-utilities, animations, audio-and-sound, cameras, curves-and-paths, data-manager, events-system, filters-and-postfx, game-object-components, game-setup-and-config, geometry-and-math, graphics-and-shapes, groups-and-containers, input-keyboard-mouse-touch, loading-assets, particles, physics-arcade, physics-matter, render-textures, scale-and-responsive, scenes, sprites-and-images, text-and-bitmaptext, tilemaps, time-and-timers, tweens, v3-to-v4-migration, and v4-new-features. The README says: "Point your AI coding agent at the `skills/` folder and it will understand Phaser 4's architecture, APIs, patterns, and gotchas in depth." — [Phaser 4.2.1 README (unpkg)](https://unpkg.com/phaser@4.2.1/README.md); [skills/v3-to-v4-migration/SKILL.md (unpkg)](https://unpkg.com/phaser@4.2.1/skills/v3-to-v4-migration/SKILL.md)
- The README also promotes a browser "Phaser Sandbox" online editor, "fully updated for Phaser 4", which needs a free Phaser account to save entries. — [Phaser 4.2.1 README (unpkg)](https://unpkg.com/phaser@4.2.1/README.md)
- One community starter-template repo, written before v4 shipped, still advises "if you're not sure what version to use, I would recommend starting with Phaser 3". This is outdated. — [JamesSkemp/phaser-starter-templates](https://github.com/JamesSkemp/phaser-starter-templates)
- An aggregator reported a "Phaser Editor v5 beta". I could not verify the details. — [pulse.bot (aggregator)](https://www.pulse.bot/gaming/news/phaser-editor-v5-beta-now-available-53cf5674-3a1b-40af-bb33-73b9f91f705f/)
- A search summary of phaser.io/phaser4 mentioned a "Phaser AE" AI-assisted product pitched for people helping someone make a game. I could not open the page to confirm what it is. — [phaser.io/phaser4](https://phaser.io/phaser4)
- Evidence that Phaser 4 learning material exists by mid-2026: a Zenva beginner course, GameDev Academy Phaser 4 tutorials, and Phaser 4 news posts on filters and lighting. — [GameDev Academy Phaser 4 tutorials](https://gamedevacademy.org/phaser-4-tutorial/); [phaser.io: Phaser 4 filter system](https://phaser.io/news/2026/05/phaser-4-filter-system); [phaser.io: dynamic lighting](https://phaser.io/news/2026/05/phaser-4-dynamic-lighting)

### Inferences
- **Recommendation (inference):** Use Phaser 4.2.x with the Vite + TypeScript template. Then copy `node_modules/phaser/skills/` into the repo, or reference it from CLAUDE.md or the AI tool's rules, so generated code uses v4 APIs. The coder knows TS and Node, so the Vite template's dev server, hot reload and `npm run build` will feel familiar.
- Don't pick the React template unless the UI is heavy. Bridging React state and the Phaser scene loop adds a second mental model, and the team gains little from it.
- Phaser 3 is still viable if the team leans on a specific v3 tutorial series. But it has had no release in about 18 months, and v4 removes some v3 pain points (for example, lighting no longer needs manual pipeline setup).

### Gaps
- I couldn't open phaser.io pages to confirm the exact wording of the "Phaser 3 vs 4" article, or what "Phaser AE" and Phaser Editor v5 offer and cost.
- I didn't verify whether the create-game templates default to Phaser 4. The CLI is version-agnostic in its README. Check `package.json` after scaffolding.

## 2. What Phaser makes easy vs hard (physics, tilemaps, tweens, particles, cameras, input, audio, scaling, loading)

### Takeaway
Phaser makes the "2D arcade toolkit" nearly free: Arcade physics with boxes and circles, tweens with named easings, particle emitters, camera follow, shake, flash and fade, unified mouse and touch pointers, auto-unlocking WebAudio, FIT scaling, and a loader with progress events. Hard or fiddly areas are Matter.js rigid-body physics, Tiled pipeline gotchas (embedded tilesets, exact names), slopes and precise platformer feel, and anything outside 2D.

### Cited Findings
- **Arcade physics** covers velocity, acceleration, gravity, collide vs overlap, world bounds, physics groups, static bodies and collision categories. Bodies are AABB rectangles or circles (`setCircle`). — [physics-arcade SKILL](https://unpkg.com/phaser@4.2.1/skills/physics-arcade/SKILL.md)
- Arcade gotchas (official):
  - `collide` separates bodies, while `overlap` only detects. Use overlap for pickups.
  - Static bodies need `refreshBody()` after you move or scale them.
  - World events need opt-in flags such as `onWorldBounds`.
  - Group `defaults` only apply when a member is created.
  - With `useDamping`, drag is a multiplier (for example 0.05).
  - Disable `debug: true` for release.

  — [physics-arcade SKILL](https://unpkg.com/phaser@4.2.1/skills/physics-arcade/SKILL.md)
- **Matter.js** offers rigid bodies, compound bodies, constraints and joints, sensors, collision filtering and pointer dragging. Gotcha: "Matter position is center of mass, not top-left (unlike Arcade Physics)." — [physics-matter SKILL](https://unpkg.com/phaser@4.2.1/skills/physics-matter/SKILL.md)
- **Tilemaps** use the flow: load Tiled JSON and image, create the map, `addTilesetImage`, `createLayer`, then set collision. Gotchas:
  - The tileset name must match Tiled exactly, or you get `null`.
  - The layer name must match exactly.
  - `setCollision` must be called before colliders work.
  - "Collection of Images" tilesets are not supported.
  - Embedded tilesets in the exported JSON are required.

  — [tilemaps SKILL](https://unpkg.com/phaser@4.2.1/skills/tilemaps/SKILL.md)
- **Tweens** support named easings ('Power2', 'Sine.easeInOut', 'Bounce.easeOut', 'Cubic.easeIn'), per-property config, yoyo, repeat, stagger, chains and lifecycle callbacks. — [tweens SKILL](https://unpkg.com/phaser@4.2.1/skills/tweens/SKILL.md)
- **Particles** have flow mode and burst mode (`emitter.explode(20)`), with `scale`/`alpha` start-to-end ranges, gravity, gravity wells, and emission and death zones. — [particles SKILL](https://unpkg.com/phaser@4.2.1/skills/particles/SKILL.md)
- **Cameras** offer `startFollow(target, roundPixels, lerpX, lerpY)`, zoom, bounds, multiple cameras or minimap, and effects: `shake`, `flash`, `fadeIn`/`fadeOut`, `pan`, `zoomTo` and `rotateTo`. — [cameras SKILL](https://unpkg.com/phaser@4.2.1/skills/cameras/SKILL.md)
- **Input** is unified under `this.input`: keyboard polling and events, pointer (mouse plus touch) with click, hover and drag, multi-touch (2 pointers by default, up to 10 via `addPointer`), wheel and gamepad. — [input SKILL](https://unpkg.com/phaser@4.2.1/skills/input-keyboard-mouse-touch/SKILL.md)
- **Audio:** The SoundManager prefers WebAudio and falls back to HTML5 Audio. It covers markers, audio sprites, panning and spatial audio. Always ship OGG + MP3 at minimum; the loader picks the first format the browser supports. — [audio-and-sound SKILL](https://unpkg.com/phaser@4.2.1/skills/audio-and-sound/SKILL.md); [loading-assets SKILL](https://unpkg.com/phaser@4.2.1/skills/loading-assets/SKILL.md)
- **Scaling:** The modes are NONE, FIT ("most commonly used"), ENVELOP (crops), RESIZE (no CSS scaling; "beware GPU fill-rate"), and EXPAND (a RESIZE/FIT hybrid, since v3.80). `autoCenter: CENTER_BOTH` centres the canvas. Fullscreen via `this.scale.startFullscreen()` "must be called from a pointerup gesture (not pointerdown)", and inside iframes "the `allowfullscreen` attribute is required." — [scale-and-responsive SKILL](https://unpkg.com/phaser@4.2.1/skills/scale-and-responsive/SKILL.md)
- **Pixel art:** `pixelArt: true` in config sets `antialias: false` and `roundPixels: true` automatically. — [game-setup-and-config SKILL](https://unpkg.com/phaser@4.2.1/skills/game-setup-and-config/SKILL.md)
- **Loading:** The `this.load.on('progress', v => …)` event drives a progress bar. The official example is about 15 lines using two Graphics rectangles. Gotchas:
  - Keys must be unique.
  - A spritesheet (grid of frames) is not an atlas (named frames).
  - Loading outside `preload()` needs `this.load.start()`.

  — [loading-assets SKILL](https://unpkg.com/phaser@4.2.1/skills/loading-assets/SKILL.md)
- **v4 Filters:** Glow, blur and similar effects take about 2 lines, e.g. `sprite.enableFilters(); sprite.filters.internal.addGlow(0xff00ff, 4, 0, 1);`. Cameras have filters enabled by default. — [filters-and-postfx SKILL](https://unpkg.com/phaser@4.2.1/skills/filters-and-postfx/SKILL.md)
- **Bundle size** (measured from the npm tarball): `phaser.min.js` is 1,375,976 bytes (about 355 KB gzipped). The Arcade-only `phaser-arcade-physics.min.js` is 1,266,396 bytes (about 322 KB gzipped). — [phaser-4.2.1.tgz (npm)](https://registry.npmjs.org/phaser/-/phaser-4.2.1.tgz)

### Inferences
- **Easy (inference):** Anything whose world is one screen or a scrolling camera over boxes and circles: top-down movers, shooters, dodge games, breakout or pong variants, simple jump-and-run. Arcade physics plus tweens plus camera effects covers about 90% of jam needs.
- **Medium:** Tiled tilemaps. They work well, but the name-matching and embedded-tileset gotchas reliably cost a beginner an evening. Do one end-to-end "hello tilemap" test in week 1, before the level designer builds content.
- **Hard:**
  - Matter.js: stacking stability, tuning, and centre-of-mass offsets confuse sprite alignment.
  - Slopes in Arcade, which has only AABB and circles.
  - Precise platformer feel (coyote time, jump buffering, variable jump) has to be coded by hand.
  - 3D is out of scope: v4 even removed the limited Mesh and Plane objects.
- Use Matter only if the game *is* a physics toy (stacking, ropes, ragdolls). In that case it's a good choice, because emergent physics creates the fun and very little content is needed.

### Gaps
- I couldn't verify a specific community source on Arcade vs Matter performance trade-offs or common Matter tuning problems. The official skill describes features, not difficulty.

## 3. Cheap game-feel ("juice") features in Phaser and how many lines they take

### Takeaway
Most juice in Phaser is 1 to 8 lines per effect: camera shake, flash and fade are one call each; a squash or pop tween is about 5 lines; a particle burst is about 6 to 8 lines; hit-stop is 2 to 3 lines. The one trap is that time scale is split across three separate systems (timers, tweens, physics), and Arcade's `timeScale` runs backwards.

### Cited Findings
- **Camera shake:** `cam.shake(100)` or `cam.shake(500, 0.02)`. Full signature `shake(duration?, intensity?, force?, callback?, context?)`. Per-axis intensity works via a `Vector2`. — [cameras SKILL](https://unpkg.com/phaser@4.2.1/skills/cameras/SKILL.md)
- **Screen flash:** `cam.flash(250)` or `cam.flash(500, 255, 0, 0)` for red. Signature `flash(duration?, r?, g?, b?, force?, callback?, context?)`. — [cameras SKILL](https://unpkg.com/phaser@4.2.1/skills/cameras/SKILL.md)
- **Fades for scene transitions:** `cam.fadeOut(1000, 0, 0, 0, callback)` and `cam.fadeIn(500)`. — [cameras SKILL](https://unpkg.com/phaser@4.2.1/skills/cameras/SKILL.md)
- **Smooth camera follow:** `cam.startFollow(player, false, 0.1, 0.1)` (lerp). — [cameras SKILL](https://unpkg.com/phaser@4.2.1/skills/cameras/SKILL.md)
- **Tween with easing:** a `this.tweens.add({ targets, x, duration, ease: 'Power2' })` config object. Named eases include Bounce, Sine, Cubic and Power, plus yoyo and repeat. — [tweens SKILL](https://unpkg.com/phaser@4.2.1/skills/tweens/SKILL.md)
- **Particle burst:** an `this.add.particles(x, y, key, {speed, lifespan, scale:{start,end}, alpha:{start,end}, gravityY})` config, then `emitter.explode(20)`. — [particles SKILL](https://unpkg.com/phaser@4.2.1/skills/particles/SKILL.md)
- **Timer time scale:** `this.time.timeScale` multiplies timer delta (0.5 is half speed, 0 freezes). `this.time.paused = true` freezes all timers. This affects the scene Clock's TimerEvents only. — [time-and-timers SKILL](https://unpkg.com/phaser@4.2.1/skills/time-and-timers/SKILL.md)
- **Tween time scale:** the TweenManager has its own `timeScale` (default 1). — [TweenManager.js source (unpkg)](https://unpkg.com/phaser@4.2.1/src/tweens/TweenManager.js)
- **Arcade physics time scale is inverted:** "1.0 = normal speed, 2.0 = half speed, 0.5 = double speed". `this.physics.pause()` / `resume()` stop and restart the simulation. — [Arcade World.js source (unpkg)](https://unpkg.com/phaser@4.2.1/src/physics/arcade/World.js); [physics-arcade SKILL](https://unpkg.com/phaser@4.2.1/skills/physics-arcade/SKILL.md)
- **Glow, blur and vignette-style post effects** take 1 to 2 lines with v4 Filters. — [filters-and-postfx SKILL](https://unpkg.com/phaser@4.2.1/skills/filters-and-postfx/SKILL.md)

### Inferences
These line counts are my estimates from the cited API signatures:

| Effect | Approx. lines | Sketch |
|---|---|---|
| Screen shake on hit | 1 | `this.cameras.main.shake(120, 0.008)` |
| Red damage flash | 1 | `this.cameras.main.flash(80, 255, 60, 60)` |
| Hit-stop (freeze 60 ms) | 2–3 | `this.physics.pause(); this.tweens.pauseAll(); this.time.delayedCall(60, () => { this.physics.resume(); this.tweens.resumeAll(); });` (the scene clock keeps running, so the delayed call still fires) |
| Slow-mo | 3 | `this.time.timeScale = 0.5; this.tweens.timeScale = 0.5; this.physics.world.timeScale = 2;` (Arcade is inverted) |
| Squash/stretch or "pop" on pickup | ~5 | tween `scaleX/scaleY` to 1.3/0.7 with `ease:'Back.easeOut', yoyo:true, duration:80` |
| Particle burst on death/pickup | ~6–8 | emitter config plus `explode(n)` |
| Sprite flash white on hit | ~3 | tint or tint mode set, then a delayed call to clear. Check v4 `setTintMode()` semantics, which changed from v3 |
| Scene fade transition | ~3 | `fadeOut` plus a callback to `scene.start` |
| Floating score text | ~6 | `add.text` plus a tween on `y` and `alpha`, `onComplete: destroy` |

- (Inference) A "juice pass" covering roughly 10 of these effects is about 1 to 2 evenings. That makes it the highest-value polish work for a jam: ratings get a strong boost for little code.

### Gaps
- I couldn't fetch or verify the classic game-feel talks: "Juice it or lose it" (Jonasson & Purho) and Vlambeer's "The Art of Screenshake" (Jan Willem Nijman). The search budget ran out. They are widely cited in jam communities, but I have no URL verified this session.
- I couldn't verify the exact v4 tint-flash idiom. The migration guide confirms the tint system changed but I didn't extract a code sample.

## 4. Low-risk vs high-risk genres for a beginner in Phaser, and best content-to-fun ratio

### Takeaway
Little external evidence was retrievable this session, so this section is mostly inference grounded in sections 2 and 5. The lowest-risk designs are single-screen or endless, systems-driven arcade games with one core verb plus a twist. For the SHIFT theme, that could be a toggle of gravity, palette, world, perspective or rules. Jammers' own reports point to multiplayer, procedural generation, many hand-made levels, narrative branching and precise platformers as the usual killers.

### Cited Findings
- A postmortem on a too-ambitious earlier idea describes "many interdependent pieces". The author then aimed for a playable first phase. This supports avoiding designs where nothing is fun until every system exists. — [devharts: LD43 postmortem](https://devharts.com/2019/01/game-jam-postmortem-ludum-dare-43/)
- One team scaled down to meet the deadline but never re-did the design for the smaller scope. The result was a cut-down big game rather than a complete small game. (Search-summary excerpt; the specific devlog wasn't confirmed among the results.) — [BeanBlock postmortem](https://yosephalex4nder.itch.io/bean-block/devlog/1040140/postmortem-lessons-learned) / [Forest foRTS postmortem](https://popoprizrak.itch.io/forest-forts/devlog/687329/post-jam-postmortem)
- Forest foRTS dev wished they had built critical features (cameras, room resizing) before filling out the character roster. This is the content-before-systems trap. — [Forest foRTS postmortem](https://popoprizrak.itch.io/forest-forts/devlog/687329/post-jam-postmortem)
- Phaser 4 removed even its limited 3D objects (Mesh, Plane). "Proper 3D support is planned for the future." — [Migration Guide](https://unpkg.com/phaser@4.2.1/changelog/v4/4.0/MIGRATION-GUIDE.md)

### Inferences
**Risk tiers.** These are opinions and inferences, built from the Phaser capabilities in sections 2 and 3 and the time-sink evidence in section 5.

| Tier | Genres / mechanics | Why |
|---|---|---|
| **Low risk** | Single-screen arcade / score-attack (dodger, twin-stick-lite, breakout variant); endless runner/flyer; top-down arena survival with waves; one-screen puzzle with a toggle mechanic; physics toy (only if the physics *is* the game); clicker/incremental; rhythm-lite with a few tracks | Content comes from spawn rules and difficulty ramps, not hand-built levels. Arcade physics covers it. A restart loop means no save system. The art set is small (player, 2–4 enemy types, pickups, background) |
| **Medium risk** | Short hand-made puzzle game (8–15 small single-screen levels in Tiled); simple platformer with ~5 short levels; top-down exploration with 1–3 rooms | Fine if the level designer starts in week 1 and levels stay one screen. Tiled gotchas and level iteration cost real time |
| **High risk** | Platformer whose fun depends on precise feel; online multiplayer/networking; 3D; procedural generation (dungeons, terrain); large hand-made level sets (20+); branching dialogue/narrative; pathfinding AI beyond "move toward player"; save/load systems; inventory/crafting; RTS/city builder | Each needs a subsystem that is new to a game-engine beginner and invisible to players until it works. Bugs live in the gaps between systems. Several also need a lot of content |

- **Best content-to-fun ratio (inference):** Games where one rule interacts with randomized or scaling spawns. Examples: "survive N waves", "how far can you get", or "chain combos for score". Here 1 mechanic, 1 arena and about 10 juice effects can carry a whole game. For SHIFT, a single "shift" verb with clear audiovisual feedback (palette swap, gravity flip, lane shift, time shift) on an arena or endless structure gets most of the theme score cheaply.
- A **local** two-player same-keyboard mode is cheap in Phaser, since it's just two key sets. *Online* multiplayer is not cheap.
- Avoid save systems entirely. A `localStorage` high score is about 2 lines and is enough.

### Gaps
- My planned searches on systemic and "content-to-fun" design guidance (GMTK, Brackeys, Pirate Software jam tips) and on genre breakdowns of Game Off winners were cut off by the search budget. I found no quantitative data (for example, ratings by genre).

## 5. Scope traps that kill jam games: evidence from postmortems and biggest time sinks

### Takeaway
First-jam postmortems keep reporting the same pattern. A long timer (a week or a month) feels like plenty of time, so features pile up. Content gets built before core systems. Teams cut scope late without re-designing. The web build and submission get tested too late. Team tooling causes friction. The evidence is anecdotal devlogs, not systematic data.

### Cited Findings
- A first-jam developer had a Trello board full of bigger ideas (enemies, coins, health) and had to cut them as the hours went by. — [Nathaniel Morihara: First Game Jam Post-mortem](https://nathanielmorihara.medium.com/game-dev-journal-entry-3-first-game-jam-post-mortem-1abdcdec9f79)
- The Door Loop dev (96-hour jam) found at submission time that the game hadn't been set up to run in the browser on itch.io. This is the web-build trap. — [Door Loop postmortem](https://gumovakachnicka.itch.io/door-loop/devlog/1028665/postmortem-what-i-learned-making-door-loop-in-96-hours)
- A remote team said you can't assume everyone has the same comfort or discipline with shared tools (git and similar). They recommended teams in similar time zones for short sprints. — [BeanBlock postmortem](https://yosephalex4nder.itch.io/bean-block/devlog/1040140/postmortem-lessons-learned)
- Forest foRTS: should have built critical systems (camera, room resizing) before the character roster. — [Forest foRTS postmortem](https://popoprizrak.itch.io/forest-forts/devlog/687329/post-jam-postmortem)
- LD43: the earlier concept was too ambitious, with many interdependent pieces. — [devharts LD43](https://devharts.com/2019/01/game-jam-postmortem-ludum-dare-43/)
- Search summaries of the same postmortem set reported two more points. I could not pin each to a specific devlog among the results above, so treat them as unattributed:
  - "a week felt like heaps of time", which made it easy to keep adding scope.
  - one dev kept adding features while telling themselves there was still plenty of time.
- A guide calls scope creep "the biggest jam killer". It says the core loop should be playable by the first third of the jam, or cut features immediately. (This is an AI-skill listing page, so low authority.) — [gamedev-skills: Game Jam](https://www.typingmind.com/skills/gamedev-skills-game-jam)
- A common regret in write-ups is too little playtesting and no schedule for when key pillars should be done. — [ushallplay: Game Design Tips for Game Jams](https://ushallplay.wordpress.com/2024/09/23/game-design-tips-for-game-jams/)
- A 2026 jam postmortem exists (Spooktober 2026, "How I kept my scholarship at a Monster University…"). Its content wasn't retrieved. — [valorzard postmortem](https://valorzard.itch.io/spooktober-2026/devlog/1687861/game-jam-postmortemretrospective)

### Inferences
**Likely time sinks for this team**, ranked. This is inference that combines the postmortems above with the Phaser gotchas in section 2.
1. **Scope creep from the long timer.** 30 days feels huge, but 26 evenings at 2.5 h is only about 1.5 weekends of full-time work.
2. **Art pipeline friction.** Mismatched sizes and resolutions, spritesheet frame sizes, transparent backgrounds, atlas vs spritesheet confusion, and file names that don't match code keys. Fix this with a one-page "asset spec" (canvas size, frame size, palette, naming) on day 1.
3. **Level design for a level-based game.** It needs a working tilemap and object pipeline before the designer can do anything useful.
4. **Menus and UI.** Title, pause, game over, restart, volume and mute. Each is small, but together they take about 2 to 4 evenings.
5. **Audio integration.** Formats (ship OGG + MP3), volume balancing, the autoplay unlock, and looping music seams.
6. **Web-build issues found late.** Base paths in Vite builds, case-sensitive file names on the server, iframe size and scaling, and keys scrolling the page.
7. **Debugging physics and collision edge cases**, especially with AI-written code (see section 9).

- (Inference) The most important protection is to **deploy a private itch.io build in week 1** and redeploy at least weekly.

### Gaps
- I found no systematic survey (for example, Ludum Dare or Game Off participant surveys) quantifying time sinks or completion rates. The search budget ran out before I could look at gamedeveloper.com postmortems or Game Off-specific postmortems.

## 6. Cheapest workable art and audio pipelines for non-artists, licenses, and whether the jam allows pre-made assets

### Takeaway
- **Free and safe sources:** Kenney (CC0), ChipTone output (CC0), BeepBox and Bosca Ceoil Blue (you own your songs), Freesound filtered to CC0 or CC BY, and the team's own recordings.
- **Free art tools:** Piskel (browser), Pixelorama (free, open source), LibreSprite (free but lagging), Aseprite (about $20, or compile it yourself). Inkscape for vectors.
- **Jam rules:** Game Off does not ban pre-made assets; past FAQs mention paid assets and third-party assets. But the repo must be public, assets you can't redistribute must be left out, and organizers have said that heavy reliance on pre-made content isn't really "in the spirit".

### Cited Findings
**Jam rules on assets**
- Game Off requires the game's source and redistributable assets in a public GitHub repo, but the code need not be open source; any license is allowed. Past FAQs say "taking a game you've been working on for months, or forking a game and changing some pixels is probably not in the spirit of the jam." — [Game Off 2020 FAQ](https://itch.io/jam/game-off-2020/topic/1043790/faq-frequently-asked-questions); [Game Off 2021 FAQ](https://itch.io/jam/game-off-2021/topic/1674910/faq-frequently-asked-questions)
- 2024 host replies:
  - For third-party assets you can't redistribute, don't include them in the repo.
  - Share as much as you're able to.
  - Note what's excluded in the README.
  - One reply appears to say pre-made assets "wouldn't really be in the spirit of the jam". The question was truncated in the excerpt, so this is uncertain.

  — [Game Off 2024 FAQ](https://itch.io/jam/game-off-2024/topic/4220573/frequently-asked-questions-faq)
- The 2026 community FAQ reportedly says paid assets are allowed. A user post there also offers a free CC0 jam effects and sound kit. — [Game Off 2026 community](https://itch.io/jam/game-off-2026/community)
- Older FAQs recommend attribution in the repo README. — [Game Off 2021 FAQ](https://itch.io/jam/game-off-2021/topic/1674910/faq-frequently-asked-questions)
- 2026 basics: the theme is **SHIFT**. Submissions are due **Dec 1, 2026 at 13:37 PST**. Voting runs until Jan 1, 2027 across Overall, Gameplay, Graphics, Audio, Innovation and Theme Interpretation. Any language or engine is allowed. — [GitHub Blog: Game Off 2026 – the theme is SHIFT](https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/); [itch.io Game Off 2026](https://itch.io/jam/game-off-2026)

**Art assets and tools**
- Kenney assets are CC0 1.0. They can be used in personal and commercial projects with no permission needed, and attribution is "not required, but greatly appreciated". — [Kenney mirror quoting license](https://github.com/ETdoFresh/kenney.nl); [Kenney Game Assets bundle on itch](https://kenney.itch.io/kenney-game-assets-1); [Construct forum (Kenney)](https://www.construct.net/en/forum/game-development/tools-and-resources-27/kenneys-free-assets-30000-70995)
- Aseprite pre-built installers cost about $19.99. The source can be compiled for free for personal or commercial use but not redistributed, and compiling (Visual Studio, CMake, Ninja) is non-trivial. — [aseprite community thread](https://community.aseprite.org/t/aseprite-is-a-pixel-art-program-make-it-free/7043); [Steam discussion](https://steamcommunity.com/app/431730/discussions/0/3954784199565300429)
- LibreSprite is free and forked from Aseprite's last GPLv2 commit. A March 2026 blog calls it hard to recommend in 2026 because it lacks newer Aseprite features (tilemaps, reference images). — [LibreSprite (best-of-web)](https://best-of-web.builder.io/library/LibreSprite/LibreSprite); [wikidocs blog (KR, 2026)](https://wikidocs.net/blog/@jaehong/8794/)
- Piskel is free in the browser with no install, simpler and with fewer options. Pixelorama is free, open source and actively maintained. (Source is a vendor comparison with a disclosed bias.) — [Piskel (best-of-web)](https://best-of-web.builder.io/library/piskelapp/piskel); [sprite-ai: Aseprite alternatives (biased)](https://www.sprite-ai.art/blog/aseprite-alternatives)

**Audio assets and tools**
- ChipTone (by SFB Games / Tom Vian) says: "All sounds created using ChipTone are FREE to use for any purpose, commercial or otherwise, under the CC0 licence." No credit is needed, and the tool is free with optional payment. — [ChipTone on itch](https://sfbgames.itch.io/chiptone); [ChipTone forum post](https://itch.io/t/1138063/chiptone-a-free-sound-effects-tool)
- **jsfxr:** The npm package lists no license. The chr15m fork is listed as Unlicense. A comparison listing reportedly puts "unrestricted commercial use" under a paid Pro tier on sfxr.me, which is unclear and unverified. jfxr explicitly states that sounds you create belong to you, including for commercial use. — [jsfxr on npm](https://www.npmjs.com/package/jsfxr); [jfxr GitHub](https://github.com/ttencate/jfxr); [sfxr.me](https://sfxr.me)
- BeepBox doesn't claim ownership of songs created with it. The MIT license covers the code, not your songs. — [beepbox.co](https://beepbox.co/)
- Bosca Ceoil Blue is a Godot port of Terry Cavanagh's Bosca Ceoil by Yuri Sizov. It is free under a permissive open-source license. 3.0 went stable in July 2024, then 3.1. — [GameFromScratch: Bosca Ceoil Blue](https://gamefromscratch.com/bosca-ceoil-blue/); [Bosca Ceoil Blue devlog](https://yurisizov.itch.io/boscaceoil-blue/devlog)
- Freesound licenses are per sound:
  - CC0: no credit needed.
  - CC BY: credit the author's username and link the sound.
  - CC BY-NC: avoid for anything commercial.

  Freesound's search can filter by license. (Third-party guides; Freesound's own page couldn't be fetched.) — [cinevva: free SFX & music guide](https://app.cinevva.com/guides/free-sound-effects-music); [SoundSpool licenses](https://www.soundspool.com/fr/licenses); [Freesound forum](https://freesound.org/forum/legal-help-and-attribution-questions/38292)
- itch.io requires asset creators to tag anything made with generative AI, even hand-edited. Untagged AI assets lose browse indexing (since late 2024). — [PC Gamer](https://www.pcgamer.com/software/platforms/indie-distribution-platform-itch-io-now-requires-asset-creators-to-disclose-the-use-of-generative-ai-in-their-work); [Game Developer](https://gamedeveloper.com/production/itch-wants-asset-creators-to-disclose-when-they-ve-used-generative-ai)

### Inferences
**Realistic art output for two non-artists in about 3 to 4 weeks of evenings** (opinion and inference):
- One player sprite with 2 to 4 animation states of about 2 to 4 frames each.
- 3 to 6 enemy or object sprites.
- One tileset of about 16 to 32 tiles, or 1 to 3 painted backgrounds.
- A title card and a UI font, with pixel or bitmap text through Phaser.

That's achievable if the style is chosen *to hide inexperience*.

**Styles that hide inexperience** (opinion, not sourced this session):
- **Strict limited palette** (2 to 4 colours, for example from Lospec). It forces cohesion, and palette swaps are a natural fit for "SHIFT".
- **Single-colour silhouettes on a gradient background.**
- **Geometric shapes.** Use Phaser `Graphics` and shapes or Inkscape vectors. Can be drawn in code with zero art time.
- **Low-res 16x16 pixel art with `pixelArt: true`.**
- **Hand-drawn, scanned or photographed paper art**, including deliberately crude MS Paint style. Charming if it's consistent.
- **Photo collage or cut-out style.**

The rule that matters is *consistency*: one palette, one resolution, one line weight. Mixing Kenney packs with original art usually looks worse than either alone.

**Audio:**
- About 10 to 20 SFX made in ChipTone or jsfxr in one evening.
- 1 to 2 looping tracks in BeepBox. A beginner composer should budget about 2 to 4 evenings.
- Foley: record real-world sounds on a phone (paper, keys, voice) and trim them in Audacity. That's a distinctive, zero-cost option.
- Export OGG + MP3.

**Licensing hygiene:** Keep `CREDITS.md` and a `/assets/LICENSES` folder from day 1. Prefer CC0 to avoid attribution bookkeeping. Never use NC-licensed sounds if you might later sell the game.

### Gaps
- I couldn't fetch kenney.nl's own license page, Freesound's license help, OpenGameArt's license list, Inkscape, or Lospec. Facts above are from mirrors and secondary guides.
- The sfxr.me free-tier license for generated sounds is unclear. Verify on the site, or use ChipTone or jfxr, whose terms are explicit.
- I found no sourced evidence (postmortems or ratings data) on which art styles score best for non-artists. Those bullets are opinion.
- I couldn't find the exact 2026 official wording on pre-made assets.

## 7. Deploying Phaser to itch.io (zip, limits, embed, fullscreen, mobile, audio unlock, key scrolling)

### Takeaway
- **Packaging:** Build with Vite and zip the *contents* of `dist/`, with `index.html` at the zip root. Stay well under itch's limits: about 500 MB extracted, 200 MB per file, and a file-count cap around 1,000 (older posts say 500).
- **Scaling and fullscreen:** Use Phaser `Scale.FIT` + `CENTER_BOTH` with a fixed design resolution. Trigger fullscreen from `pointerup`.
- **Input and audio:** Capture arrow and space keys so the page doesn't scroll. Phaser unlocks audio on first interaction automatically.
- **Hosting:** No SharedArrayBuffer is needed for Phaser.

### Cited Findings
- itch.io HTML5 limits (from forum excerpts; the official page couldn't be fetched):
  - The total extracted size must not exceed 500 MB.
  - Any single extracted file must not exceed 200 MB.
  - The file-count cap is reported as 1,000. Older threads show "805 > 500" errors, and leafo has said manual raises are possible.

  The 200 MB per-file check can fail only *after* upload processing. — [itch.io HTML5 docs](https://itch.io/docs/creators/html5); [itch.io forum: html5 files limit raise](https://itch.io/t/320785/html5-files-limit-raise); [itch.io post](https://itch.io/post/342834/view-in-topic); [Web Export Doctor (Godot tool page)](https://njeza.itch.io/web-export-doctor)
- **Audio unlock:** "Browsers block audio until user interaction. Phaser handles this automatically." WebAudio's `AudioContext` starts suspended. Phaser listens for touch, mouse and key events on `document.body` to resume it, and fires an `'unlocked'` event. "You do not need to handle unlocking manually." Pattern: `if (this.sound.locked) this.sound.once('unlocked', () => this.sound.play('bgm'))`. — [audio-and-sound SKILL](https://unpkg.com/phaser@4.2.1/skills/audio-and-sound/SKILL.md)
- **Prevent page scroll from game keys:** `this.input.keyboard.addCapture('SPACE,UP,DOWN,LEFT,RIGHT')` (or key codes `[32,37,38,39,40]`). "Captures are global across all Scenes." `addKey(key, enableCapture, emitOnRepeat)` also captures. — [input SKILL](https://unpkg.com/phaser@4.2.1/skills/input-keyboard-mouse-touch/SKILL.md)
- **Fullscreen:** `this.scale.startFullscreen()` / `toggleFullscreen()` must run in a `pointerup` handler. Iframes need `allowfullscreen`. — [scale-and-responsive SKILL](https://unpkg.com/phaser@4.2.1/skills/scale-and-responsive/SKILL.md)
- **Scaling:** `mode: Phaser.Scale.FIT, autoCenter: Phaser.Scale.CENTER_BOTH` is "the most common setup for responsive games". It letterboxes and keeps aspect ratio. Orientation can be read via `game.scale.orientation`. — [scale-and-responsive SKILL](https://unpkg.com/phaser@4.2.1/skills/scale-and-responsive/SKILL.md)
- **Touch:** Pointers unify mouse and touch. 2 pointers by default and up to 10 via `addPointer()`. — [input SKILL](https://unpkg.com/phaser@4.2.1/skills/input-keyboard-mouse-touch/SKILL.md)
- **Size budget:** The Phaser runtime is about 1.38 MB minified (about 355 KB gzipped). That is far below itch limits. — [phaser-4.2.1.tgz](https://registry.npmjs.org/phaser/-/phaser-4.2.1.tgz)
- **Renderer:** Canvas is deprecated in v4 ("WebGL support is effectively baseline today"). — [Migration Guide](https://unpkg.com/phaser@4.2.1/changelog/v4/4.0/MIGRATION-GUIDE.md)
- A postmortem cautionary tale: the game hadn't been set up to run in the browser on itch at submission time. — [Door Loop postmortem](https://gumovakachnicka.itch.io/door-loop/devlog/1028665/postmortem-what-i-learned-making-door-loop-in-96-hours)

### Inferences
**Deploy checklist** (inference; the itch-specific UI items are from prior knowledge, unverified this session):
1. In `vite.config`, set `base: './'` so asset URLs are relative inside itch's iframe. The official templates may already do this, so check.
2. Zip the contents of `dist/`, not the folder itself.
3. Upload as an HTML file, tick "This file will be played in the browser", and set the embed size to the game's design resolution or a multiple of it. 960×540 or 1280×720 for 16:9 is common.
4. Enable itch's fullscreen button and "mobile friendly" only if touch controls actually exist.
5. Leave SharedArrayBuffer off. Phaser doesn't need it; it matters for engines with threaded WASM such as Godot 4 or Unity.
6. Watch case-sensitive file names. `Player.png` vs `player.png` works locally on Windows and macOS but can 404 on the server.
7. Add an in-game "click to start" title screen. This gives the audio unlock and keyboard focus inside the iframe in one step.
8. Upload a private or draft build in week 1 and test it on a phone and a second browser.

**Phaser 3 vs 4 for deployment:** No difference in the itch.io process; both are a static `index.html` plus JS and assets.

### Gaps
- I couldn't read itch.io's official HTML5 docs to confirm:
  - the current file-count cap,
  - the embed/viewport options,
  - the "mobile friendly" and orientation settings,
  - the fullscreen-button wording,
  - SharedArrayBuffer support,
  - whether the 500 MB applies to the zip or the extracted content (forum posts conflict).

  The itch.io host was blocked in this session.
- Whether the official Vite template sets `base: './'` by default wasn't verified.

## 8. Recommended schedule for a 26-evening jam

### Takeaway
Jam guides converge on four rules:
- Make the core loop playable within the first third.
- Use placeholder art until the mechanic is fun.
- Freeze features before the last stretch, and polish and playtest after.
- Leave buffer for submission.

For 26 evenings, that means locking the core mechanic by about evening 6 to 8, freezing features by about evening 18 to 19, polishing for a week, and submitting a full day early (Nov 29 to 30, before the Dec 1 13:37 PST deadline).

### Cited Findings
- Core loop playable by the first third of the jam, or cut features immediately. Bug-fix freeze near hour 38–44 of a 48-hour jam, which is about the last 10–20%. (Low-authority AI-skill page.) — [gamedev-skills: Game Jam](https://www.typingmind.com/skills/gamedev-skills-game-jam)
- "50/50, core/polish": split the time into two halves; anything not done by halftime is cut. — [ushallplay: Game Design Tips for Game Jams](https://ushallplay.wordpress.com/2024/09/23/game-design-tips-for-game-jams/)
- Prototype with gray boxes and placeholder art; polish only after the core mechanic is fun. Final hours go to polish and submission materials, not new features. — [Into Games: Global Game Jam key tips](https://intogames.org/news/global-game-jam-key-tips); [SummerEngine jam guides](https://www.summerengine.com/jam/guides); [RPG Maker: 4 ways to make a jam game fast](https://rpgmakerweb.com/blog/4-ways-to-make-a-game-jam-game-fast)
- A small, polished, finished game beats a big, broken one. Lock the core plan. — [BeanBlock postmortem](https://yosephalex4nder.itch.io/bean-block/devlog/1040140/postmortem-lessons-learned)
- Deadline: Dec 1, 2026 at 13:37 PST, pushed to a public GitHub repo. — [GitHub Blog: Game Off 2026](https://github.blog/open-source/gaming/game-off-2026-the-theme-is-shift/); [itch.io Game Off 2026](https://itch.io/jam/game-off-2026)

### Inferences
Proposed 26-evening plan (inference; it adapts the cited ratios to this team):

| Evenings | Coder | Artist + audio + level designer | Gate |
|---|---|---|---|
| 1–2 | Scaffold Vite+TS Phaser 4 template; public GitHub repo; **deploy "hello world" to a private itch page**; input + scaling + keyboard capture | Pick ONE style + palette + resolution; write asset spec (sizes, frame counts, naming); make 3 throwaway test sprites and 3 ChipTone SFX to prove the pipeline | Build runs on itch on a phone |
| 3–7 | Gray-box core mechanic (the "SHIFT" verb) + fail/restart loop | Paper prototypes, mood board, first real player sprite; audio person makes SFX list and starts a music loop | **Evening ~7: core-mechanic lock.** If it isn't fun with boxes, change the mechanic now |
| 8–13 | Content systems: spawner/waves or level loader, scoring, difficulty ramp; first juice pass | Art production; level designer builds levels in Tiled or spawn tables in JSON; music loop v1 | Evening ~13: full game playable start to end with placeholders ("vertical slice") |
| 14–18 | Title, game-over, pause and mute UI; audio integration; second juice pass; fix blockers | Finish all required art and SFX; tune levels and difficulty; outside playtests with 3+ people | **Evening ~18: feature freeze.** New ideas go to a "post-jam" list |
| 19–24 | Bug fixes and polish only; performance check; mobile/touch if in scope | Polish art (title card, itch cover image 630×500, screenshots, GIF); final music mix; volume balance | Evening ~23: release candidate uploaded |
| 25–26 | Buffer; README with credits and AI disclosure; **submit on Nov 29–30** | itch page copy, controls text, credits | Submitted ≥1 day early |

- (Inference) Time budget: about 60–75 coder-hours, of which roughly 15 go to setup and deploy, 20 to core and systems, 10 to UI and audio integration, 10 to juice and polish, and 10 to bugs and buffer. Anything not in the core loop by evening 7 should be listed as optional.
- (Inference) With part-time evenings, missing 2 to 3 evenings to life is likely. Plan for 22 to 23 real evenings and treat 3 as slack.
- (Inference) The itch cover image is usually 630×500. That's from memory and unverified this session.

### Gaps
- I couldn't fetch or confirm specific schedules from well-known jammers (GMTK, Brackeys, Pirate Software) or month-long-jam schedules. The cited ratios come from 48-hour-jam guides and blogs and are being extrapolated.

## 9. How AI coding tools are used for jam games, their pitfalls, and Game Off's AI rules

### Takeaway
- **Rules:** Game Off has historically allowed AI tools: "Nope!" (no restrictions) in the 2025 FAQ, and "use of AI is allowed" in 2023. A 2026 community post says AI-assisted coding is allowed but should be disclosed at submission. itch.io separately requires AI-generated *assets* to be disclosed or tagged.
- **Pitfalls:** The main practical risks are v3/v4 API confusion (most training data is Phaser 3), invented APIs and config fields, and code that "works" but feels bad, which no AI fixes without human playtesting.

### Cited Findings
- Game Off 2025 FAQ. Q: "Any restrictions on AI code assistants or asset generation?" Lee Reilly: "Nope!" — [itch.io post (Game Off 2025 FAQ)](https://itch.io/post/14674865)
- Game Off 2023: Lee Reilly answered "The use of AI is allowed ✓". The 2023 theme post said participants can use any languages, engines, or AI tools to help generate code, assets, or anything in between. — [Game Off 2023: Can participants use AI generated assets?](https://itch.io/jam/game-off-2023/topic/3219500/can-participants-use-ai-generated-assets-in-their-games); [Game Off 2023 page](https://itch.io/jam/game-off-2023)
- Game Off 2026: a community-FAQ excerpt says AI-assisted coding is allowed this year, with disclosure at submission. This comes from a search excerpt of a community thread, not the official rules page. — [Game Off 2026 community](https://itch.io/jam/game-off-2026/community)
- An itch.io jam post (which jam is unconfirmed) says games with AI-generated assets must state which parts used AI in the description, or risk disqualification. — [itch.io post](https://itch.io/post/15118497)
- itch.io requires generative-AI asset disclosure and tagging for asset packs. Untagged AI assets are removed from browse indexing. — [PC Gamer](https://www.pcgamer.com/software/platforms/indie-distribution-platform-itch-io-now-requires-asset-creators-to-disclose-the-use-of-generative-ai-in-their-work); [Game Developer](https://gamedeveloper.com/production/itch-wants-asset-creators-to-disclose-when-they-ve-used-generative-ai)
- Phaser's README claims "Phaser's API is well understood by every major frontier LLM". It ships official agent skills for every subsystem, plus a v3-to-v4 migration skill that "understands every breaking change". — [Phaser 4.2.1 README](https://unpkg.com/phaser@4.2.1/README.md)
- A community Claude/Codex skill ("phaser-docs-engineer") makes the agent search a local copy of the Phaser docs before writing code. Its stated aim is to reduce invented APIs and config fields, which is evidence that hallucinated Phaser APIs are a recognized problem. — [phaser-docs-engineer](https://gh.r-mj.com/imfurman/phaser-docs-engineer)
- Several community "Phaser" skills target Phaser 3 rather than 4. — [ClaudSkills: phaser-gamedev](https://claudskills.com/skills/phaser-gamedev/)
- v4 changed defaults and APIs that v3-trained code relies on:
  - `roundPixels` default is now false.
  - FX and masks became Filters.
  - Tint semantics changed.
  - `Point` became `Vector2`.
  - `Mesh` was removed.

  — [Migration Guide](https://unpkg.com/phaser@4.2.1/changelog/v4/4.0/MIGRATION-GUIDE.md)
- A concrete trap that LLMs and humans both hit: Arcade `world.timeScale` is inverted (2.0 = half speed), unlike `time.timeScale` and `tweens.timeScale`. — [Arcade World.js](https://unpkg.com/phaser@4.2.1/src/physics/arcade/World.js)

### Inferences
**Usage pattern that should work** (inference and opinion):
- Let the AI write boilerplate: scene setup, a loader with progress bar, UI scenes, a tween/particle juice helper, a localStorage high score, deploy scripts.
- The human owns game-feel numbers: speeds, gravity, jump arcs, timings, spawn rates. Expose those as constants or a debug panel, for example a simple `lil-gui` or keyboard keys that nudge values, and tune them by playing.

**Pitfalls to expect:**
- **v3-style code in a v4 project.** `preFX`/`postFX`, old tint behaviour, `Phaser.Geom.Point`, assuming `roundPixels:true` and getting blurry pixel art. Mitigation: add `node_modules/phaser/skills/` to the agent context and pin "Phaser 4.2" in the rules file.
- **Physics debugging by trial and error.** The AI can't see the game. Turn on `arcade.debug: true` to see bodies, and describe the symptom precisely: "body offset 8px right of sprite when flipped".
- **Over-engineered architecture.** ECS, state machines and event buses for a 3-week game. Ask for the simplest single-scene implementation.
- **Code that works but feels bad.** Floaty movement, no acceleration curves, no feedback. Run a dedicated juice pass from section 3.
- **Large AI-generated diffs** break things silently. Commit often, so git bisect is available.
- **AI-generated art and audio.** Allowed historically for Game Off, but disclosure is expected (itch platform plus the 2026 community note), and some raters may mark down obvious AI art. Two human artists on the team make this moot. Recommendation: use AI for code; keep art and audio human-made or CC0; disclose AI coding in the README and the submission.

### Gaps
- I couldn't read the official 2026 Game Off rules page to confirm the exact AI wording, including whether disclosure is mandatory and whether AI-generated assets are treated differently from AI code. Check https://itch.io/jam/game-off-2026 before submitting.
- The search budget ran out before I could find 2025–2026 postmortems or articles specifically about using AI coding assistants (Claude Code, Cursor, Copilot) for jam games, or rater attitudes toward AI-assisted entries. No sourced claims on those are included.
