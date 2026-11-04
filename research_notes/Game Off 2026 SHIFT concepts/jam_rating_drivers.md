# What Drives Ratings Count and Scores in itch.io / Ludum Dare-Style Rated Jams

Researched 2026-11-04 for a 3-person beginner team entering GitHub Game Off 2026 (theme "SHIFT", Phaser 3 browser game on itch.io).

**Labels used throughout:**
- **[DATA]**: quantitative analysis of real jam results. Formal or informal; each one says which.
- **[STUDY]**: peer-reviewed or academic research.
- **[PLATFORM/HOST]**: statements by itch.io staff, official jam rules or pages, or jam organizers.
- **[OPINION/ANECDOTE]**: experienced jammers, postmortems, forum advice, third-party guides.
- **Inferences** sections hold my own reasoning, not sourced facts.

**Method caveat:** In this session, WebFetch could not reach itch.io, ldjam.com, leafo.net, arxiv.org, rumorgames.com or the University of Alberta lab site (DNS blocked by the network policy). Findings from those domains come from search-engine result summaries that quote the pages. The quoted numbers were consistent across queries. Still, nothing was checked against the full primary page, and items most worth re-checking are marked **[VERIFY]**.

---

## 1. Data: what correlates with rating counts and scores (web vs download, ratings given, team size, description, etc.)

### Takeaway
The strongest quantitative signals are informal but consistent:
- **Browser-playable entries get about 2x the ratings of download-only entries.**
- **Makers who rate other games get about 1.85x the ratings of makers who rate none.** Reciprocity is roughly one rating back for each rating given.
- **Team entries get more ratings than solo entries** in most jams.

The only peer-reviewed itch.io study links high ranking to description quality, more developers, and multi-platform/multi-genre support. None of these results is causal, because better teams may simply do all of these things.

### Cited Findings
**Browser vs download**
- **[DATA, informal, single author, 10 itch.io jams]** Across the 9 jams that had both kinds of entry, the median browser entry had more ratings than the median download-only entry in **all 9**. The median ratio was **2.1** (range **1.2** in Bezi Jam 8 to **5.5** in Bezi Jam 12). — [jamshell devlog, "Browser builds get about twice the ratings: data from 10 itch.io jams" (MV2 of Munim, Inc.)](https://munimv2.itch.io/jamshell/devlog/1713443/browser-builds-get-about-twice-the-ratings-data-from-10-itchio-jams)
- **[DATA, same source]** In random same-jam pairs, the browser entry had more ratings **83%–96%** of the time. The gap held within the same raw-score band (median ratios **2.0, 2.0, 2.2**), which suggests it is not only "better games ship web builds." Browser entries had higher *raw scores* in only 4 of 9 jams, with no clear difference in the other 5. Entries with no playable files at all usually got the fewest ratings. — [same devlog](https://munimv2.itch.io/jamshell/devlog/1713443/browser-builds-get-about-twice-the-ratings-data-from-10-itchio-jams)
- **[DATA, same source]** **307 of 392 (78%) download-only entries** were penalised by itch's rating-count adjustment, compared with **216 of 813 (27%) browser entries**. — [same devlog](https://munimv2.itch.io/jamshell/devlog/1713443/browser-builds-get-about-twice-the-ratings-data-from-10-itchio-jams)
- **[PLATFORM/HOST]** The same author reports that when itch.io was asked for real numbers in 2021, its founder said no formal analysis had been done. — [same devlog](https://munimv2.itch.io/jamshell/devlog/1713443/browser-builds-get-about-twice-the-ratings-data-from-10-itchio-jams) **[VERIFY]**
- **[PLATFORM/HOST]** A jam organizer page says browser play gets more attention. Another jam page says games with web builds tend to get more votes. — [The Demo Jam](https://itch.io/jam/the-demo); [Browser Game Jam](https://itch.io/jam/browser-game-jam)
- **[PLATFORM/HOST]** Ludum Dare's 2017 rules: "the ideal Ludum Dare game can be played right in the browser, in a few minutes, alone." — [Ludum Dare Rules (from 2017)](https://ludumdare.com/resources/archive/rules-2017/)

**Rating others (karma / "coolness")**
- **[DATA, informal, 14 itch.io jams]** In **13 of 14** jams, entries whose makers rated more games received more ratings. Median rank correlation was **0.58**, with pooled p < 0.001. In 13 jams with enough data, entries from heavy raters got a median of **1.85x** the ratings of entries whose makers rated none (range 0.93–7.0). An exploratory estimate is about **one rating back per rating given**. **11%–46%** of entries came from makers who rated nobody. The author warns this may not be causal, since heavy raters may also promote more, ship browser builds and finish better games. — [jamshell devlog, "Makers who rate other jam games get more ratings: data from 14 itch.io jams"](https://munimv2.itch.io/jamshell/devlog/1713956/makers-who-rate-other-jam-games-get-more-ratings-data-from-14-itchio-jams)
- **[PLATFORM/HOST]** Ludum Dare's 2017 rules: "more players will find (and likely) rate your game if you have a high Coolness." Coolness is LD's measure of how many games you have rated. — [Ludum Dare Rules (from 2017)](https://ludumdare.com/resources/archive/rules-2017/)
- **[OPINION/ANECDOTE]** An LD43 guide says **one-third of LD42 entrants failed to reach 20 ratings**. It treats submission as "just the beginning" and says you must then market (rate, comment, promote). — [Rumor Games, "An honest guide to getting your Ludum Dare game rated"](https://rumorgames.com/ludum-dare-honest-guide/); [ldjam.com mirror](https://ldjam.com/events/ludum-dare/43/space-battle-zero/an-honest-guide-to-getting-your-ludum-dare-game-rated) **[VERIFY]**
- **[OPINION/ANECDOTE]** An itch.io commenter says rate-for-rate posts were the biggest contributor to a jam's ratings gap. — [itch.io post](https://itch.io/post/767867) **[VERIFY attribution]**

**Team size**
- **[DATA, informal]** Team entries received more ratings than solo entries in **9 of 12** jams that had both. — [jamshell 14-jam devlog](https://munimv2.itch.io/jamshell/devlog/1713956/makers-who-rate-other-jam-games-get-more-ratings-data-from-14-itchio-jams)
- **[STUDY]** Vu & Bezemer (FDG 2020), **1,290 itch.io jams and 3,752 submissions**: "more manpower ... developing a game increases ... a game's high-ranking likelihood." However, both high- and low-ranking games had a **median of one developer**. — [Semantic Scholar record](https://www.semanticscholar.org/paper/An-Empirical-Study-of-the-Characteristics-of-Game-Vu-Bezemer/3744d4167e86b084bc6cba7690439974e20b0ed5); [ACM full text](https://dl.acm.org/doi/fullHtml/10.1145/3402942.3402981); [Vu MSc thesis (U. Alberta)](https://asgaard.ece.ualberta.ca/papers/MSc_Thesis/MSc_Thesis_2020_Vu_Leveraging_Data_From_the_Itchio_Online_Distribution_Platform_to_Help_Indie_Game_Developers.pdf)

**Description, platforms and genre**
- **[STUDY]** Vu & Bezemer found that a quality description contributes positively to a game's ranking. Games "with a better quality description, multi-platform and multi-genre support are more likely to be high-ranking." High-ranking games tended to be on Windows or macOS and in the Puzzle, Platformer, Interactive Fiction or Action genres. The search summaries mention no screenshot-count or description-length variable. — [ACM full text](https://dl.acm.org/doi/fullHtml/10.1145/3402942.3402981); [ResearchGate](https://www.researchgate.net/publication/340634103_An_Empirical_Study_of_the_Characteristics_of_Popular_Game_Jams_and_Their_High-ranking_Submissions_on_itchio)
  - *Possible tension:* "Windows or macOS" in Vu & Bezemer versus the browser advantage in jamshell. The study used roughly 2019 data and measured ranking rather than rating counts; jamshell measured rating counts.

**Rating counts and noise**
- **[OPINION/ANECDOTE]** A Ludum Dare entrant's LD50 analysis found that the winners did not have more raters. They had a smaller subset of raters who scored them higher. — [gbgames, LD50 "Disaster City" results](https://www.gbgames.com/2022/04/25/ld50-how-my-entry-disaster-city-did-ldjam-ld50/) **[VERIFY attribution; came from a search summary]**
- **[OPINION/ANECDOTE]** A jammer notes that 35 ratings, or even 100, is not statistically significant, so scores are noisy. — [gbgames](https://www.gbgames.com/?p=5858) **[VERIFY attribution]**

### Inferences
- The two cheapest, best-evidenced levers are **ship a browser build** (already planned) and **rate many other games early, with comments**. Neither needs any game-dev skill.
- With about 1:1 reciprocity, the team should collectively rate at least as many games as the number of ratings it wants to receive, roughly 20–30. That number comes from the Game Off median in Section 2.
- A team of 3 is above the median team size of 1, which the data mildly favors. The edge only shows up if the team actually finishes and polishes the game.

### Gaps
- No analysis was found that correlates **game length, screenshot count, thumbnail quality or description length** with ratings or scores in jams.
- There is no peer-reviewed replication of the browser and reciprocity findings; jamshell is one self-published author.
- It is unclear whether, on itch.io, ratings given by *each* team member count toward an entry's karma, or only those from the submitting account.

---

## 2. How itch.io ranks entries and decides what raters see; Game Off specifics

### Takeaway
- **Ranking:** itch.io multiplies each entry's raw average by **sqrt(min(median, ratings)/median)**. Entries below the jam's median rating count are penalised, and entries at or above it are not. In Game Off 2025 the **median was 16 ratings**.
- **What raters see:** Exposure comes from a **random rating queue** plus browse sorts (Random, Popular, Most/Fewest ratings, Karma). The Popular sort can snowball early-liked entries.

### Cited Findings
**The adjustment formula**
- **[PLATFORM/HOST, staff post quoted by others]** adjustment = **sqrt(min(median, votes_received) / median)**. Worked example: 19 votes with a median of 20 gives a factor of 0.97467, about a 2.5% reduction. Entries at or above the median keep their raw average. — [leafo post, "Calculated ratings for jams vs raw scores?"](https://itch.io/post/8993133); [thread](https://itch.io/t/644401/calculated-ratings-for-jams-vs-raw-scores); formula restated in [jamshell browser devlog](https://munimv2.itch.io/jamshell/devlog/1713443/browser-builds-get-about-twice-the-ratings-data-from-10-itchio-jams) **[VERIFY exact wording]**
- **[PLATFORM/HOST]** The median is used rather than the mean, so a few prolific raters don't distort it. Staff describe the number of ratings as a confidence value applied to the average. Very low rating counts produce unreliable averages, so itch.io may not show a ranking for them. — [itch.io forum post](https://itch.io/post/3955382); [itch.io post](https://itch.io/post/3860950); [itch.io post](https://itch.io/post/3863718) **[VERIFY]**
- **[PLATFORM/HOST]** Rate pages state: "Score is adjusted from raw score by the median number of ratings per game in the jam." — [Game Off 2025 rate page example](https://itch.io/jam/game-off-2025/rate/4067350)

**Game Off 2025 numbers**
- **[DATA, official results page]** **10,414 ratings** went to **699 entries (98.6%)**. Voting ran 2025-12-01 to 2026-01-08. The **average was 14.7 ratings per game and the median was 16**. — [Game Off 2025 results](https://itch.io/jam/game-off-2025/results)
- **[DATA]** Top 3 overall:

  | Rank | Game | Team | Ratings | Score |
  |---|---|---|---|---|
  | 1 | Evaw | Wafflenaut Games | 34 | 4.294 |
  | 2 | Where The Water Flows | Nademtis, sara_strm | 35 | 4.200 |
  | 3 | BEACON | ICD, sashhahah | 20 | 4.150 |

  Winners sit at only about 1.3–2x the median, so enormous rating counts are not required. — [Game Off 2025 results](https://itch.io/jam/game-off-2025/results)

**Medians in comparison jams**
- **[DATA]** GameDev.tv Jam 2025: average 14.0, median 9. Bevy Jam 2: average 31.8, median 32. GMTK 2026: 223,337 ratings to 10,382 entries, average 21.2. — [GameDev.tv Jam 2025 results](https://itch.io/jam/gamedevtv-jam-2025/results?page=10); [Bevy Jam 2 results](https://itch.io/jam/bevy-jam-2/results); [GMTK 2026 audio results](https://itch.io/jam/gmtk-jam-2026/results/audio)

**Game Off 2026 rules**
- **[PLATFORM/HOST]** Submissions are open 2026-11-01 21:37 to 2026-12-01 21:37. Voting ends **January 1, 2027, 13:37 PST**. Categories are Overall, Gameplay, Graphics, Audio, Innovation, Theme Interpretation. — [Game Off 2026 jam page](https://itch.io/jam/game-off-2026)
- **[PLATFORM/HOST]** "Once you've submitted on itch.io, you'll be able to play other entries and cast your votes." Participants rate each other. — [GitHub Blog, Game Off 2025 theme announcement](https://github.blog/company/github-game-off-2025-theme-announcement/); [Game Off 2025 FAQ](https://itch.io/jam/game-off-2025/topic/5489423/frequently-asked-questions-faq)
- **[PLATFORM/HOST]** No Game Off-specific minimum rating threshold was found. The standard itch.io median adjustment applies, per the rate-page note above.

**Rating queue and browse sorts**
- **[PLATFORM/HOST]** **Rating queue:** voters get a random set of entries (default 5). Each rated entry is swapped for another random one, which prevents targeting specific projects and spreads ratings. Voters can set a preferred platform and shuffle the queue. — [itch.io docs: Game jams](https://itch.io/docs/creators/game-jams); [leafo forum posts](https://itch.io/post/900883), [2](https://itch.io/post/872545)
  - *Inference:* the preferred-platform filter means raters who choose "web" never see download-only games.
- **[PLATFORM/HOST]** **Popular and Random sorts:** leafo described "Popular" as letting newcomers see entries "vetted in some way by the community," while questioning whether "Most ratings"/"Popular" make good defaults. He said "random sort by default is the most fair to distribute ratings." A "least rated" sort also exists. — [itch.io post (leafo)](https://itch.io/post/900883); [itch.io post](https://itch.io/post/9245332)
- **[OPINION/ANECDOTE]** A user observed that the default Popular filter "tends to create a snowball effect on good entries." — [itch.io thread](https://itch.io/t/3451166/game-jam-filters-how-does-the-popular-filter-work-where-is-most-karma-set-random-to-default)
- **[PLATFORM/HOST]** **Karma sort:** leafo added it in August 2019 as an experiment and said he personally thinks such a system is flawed. It sorts entries by how many ratings their makers have given. — [itch.io thread on karma sort](https://itch.io/t/3451166/game-jam-filters-how-does-the-popular-filter-work-where-is-most-karma-set-random-to-default); [Karma system thread](https://itch.io/t/527869/karma-system-for-the-game-jams); [GitHub issue #964](https://github.com/itchio/itch.io/issues/964)
- **[PLATFORM/HOST]** A "coolest" sort reportedly existed once and "got lost in some code updates." — [itch.io post](https://itch.io/post/6472629) **[VERIFY attribution]**

**Ludum Dare comparison**
- **[PLATFORM/HOST]** LD requires about 20 ratings for a game to receive a score; this comes from community posts, not an official page. ldjam.com filters are Smart (default), Classic, Danger, Feedback, Grade and Zero. "Smart" boosts makers whose comments get thumbs-up. "Classic" rewarded rating many games. "Zero" surfaces unrated games. — [itch.io post re: LD 20-vote minimum](https://itch.io/post/8970561); [ldjam LD50 metrics thread](https://ldjam.com/events/ludum-dare/50/dlays-buffet/can-some-explain-the-metrics); [Rumor Games guide](https://rumorgames.com/ludum-dare-honest-guide/); [JamBrain issue #1972](https://github.com/JamBrain/JamBrain/issues/1972)

### Inferences (my calculations)
With a median of 16, as in 2025, a game with a 4.0 raw score would land at:

| Ratings received | Adjustment factor | Final score |
|---|---|---|
| 12 | 0.866 | 3.46 |
| 8 | 0.707 | 2.83 |
| 4 | 0.5 | 2.0 |

- **Reaching the median matters more than nearly any polish item**, and ratings beyond the median do not raise the score.
- **Target at least 20 ratings received** as a safety margin, since the 2026 median is unknown until results.
- Ratings come mainly from the random queue plus reciprocity. A strong thumbnail and title matter for conversion from the browse grid; with the Popular snowball, early ratings may compound.
- Submitting early in the window, not at the deadline, plausibly gives more time on the board. This is untested.

### Gaps
- There is no official itch.io documentation page with the formula in the search results; it comes from staff forum posts. The algorithm behind "Popular" is undocumented.
- It was not confirmed whether the Game Off 2026 host enabled a rating-queue requirement or the Karma sort.

---

## 3. Academic research on game jams and success factors

### Takeaway
Academic evidence on *what wins* is thin:
- Vu & Bezemer (2020) is the only rigorous itch.io ranking study found. It points to description quality, more manpower, and multi-platform/multi-genre support.
- The Global Game Jam survey (Borg et al.) finds time pressure pushes teams to ad hoc processes. Scope management and an MVP are the top reported practices.
- No paper titled "What makes a successful game jam game" by Borg et al. was found.

### Cited Findings
- **[STUDY]** Vu & Bezemer, "An Empirical Study of the Characteristics of Popular Game Jams and Their High-ranking Submissions on itch.io," FDG 2020. It covers 1,290 jams and 3,752 submissions. Quality description, more developers, and multi-platform and multi-genre support predict high ranking. Common high-ranking genres: Puzzle, Platformer, Interactive Fiction, Action. — [ACM DL](https://dl.acm.org/doi/fullHtml/10.1145/3402942.3402981); [DBLP](https://dblp.dagstuhl.de/rec/conf/fdg/VuB20.html); [Semantic Scholar](https://www.semanticscholar.org/paper/An-Empirical-Study-of-the-Characteristics-of-Game-Vu-Bezemer/3744d4167e86b084bc6cba7690439974e20b0ed5)
- **[STUDY]** Borg, Garousi, Mahmoud, Olsson & Stålberg, "Video Game Development in a Rush: A Survey of the Global Game Jam Participants," IEEE Transactions on Games 12(3), 2020 (arXiv 2019).
  - 198 responses from GGJ 2017.
  - Time pressure pushes teams toward ad hoc development.
  - Most-reported practices: continuous integration, **minimum viable product, scope management**.
  - Requirements were set through iterative brainstorming.
  - QA was regular communication, **internal playtesting**, and dynamic planning.
  - Agile familiarity had only a weak correlation with *perceived* success.

  — [arXiv 1904.00462](https://arxiv.org/abs/1904.00462); [QUB PDF](https://pureadmin.qub.ac.uk/ws/files/199651559/GameJamSurvey_MajorRev_Mar31.pdf); [author page](https://mrksbrg.com/tog19-borg/)
- **[STUDY]** Lai, Kultima et al., "Two Decades of Game Jams" (ICGJ 2021): a literature survey with history and taxonomies. The abstract reports no success-factor findings. — [arXiv 2110.13569](https://arxiv.org/abs/2110.13569); [Goldsmiths](https://research.gold.ac.uk/id/eprint/26837)
- **[STUDY, contrast]** Ullmann & Politowski, "What Makes a Game High-rated?" studies commercial games, not jams. "None of the aspects of this study have a strong relationship with the game's success." — [arXiv 2105.14137](https://arxiv.org/abs/2105.14137)
- **[STUDY]** Kao (2020), "The effects of juiciness in an action RPG," Entertainment Computing vol. 34, **N = 3,018**. Four versions were tested (none/medium/high/extreme juice). **The lowest and the highest juiciness both reduced play time, performance, player experience and intrinsic motivation; moderate levels did best.** — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1875952118300879); [ResearchGate](https://www.researchgate.net/publication/339467686_The_Effects_of_Juiciness_in_an_Action_RPG)
- **[STUDY]** Juul & Begy (2016), "Good feedback for bad players?" (FDG/DiGRA). An exploratory study found **null results** comparing juicy and non-juicy tile-matching games. — cited via [ResearchGate (Kao)](https://www.researchgate.net/publication/339467686_The_Effects_of_Juiciness_in_an_Action_RPG)

### Inferences
- The academic evidence supports **scope management, an early MVP, and internal playtesting** as practices.
- Ranking correlates with *presentation* (description) and *team capacity*.
- Puzzle is a common high-ranking genre, so the team's earlier failure was likely about the fun arriving late, not the puzzle genre itself.

### Gaps
- No study was found by Fowler on jam success factors, and no "Game Jam Success Factors" paper was found under those names.
- No study measured the effect of game length or tutorial length on jam ratings.

---

## 4. The first 30–60 seconds: immediate playability and rater attention spans

### Takeaway
Hosts and veterans agree on several points:
- Raters play back-to-back for "a few minutes."
- A jam game should be understandable in under a minute, fun within about 30 seconds, playable without a tutorial, and easy at the start.
- No rigorous measurement of rater session length was found.

### Cited Findings
- **[PLATFORM/HOST]** Ludum Dare: the ideal game is playable "in the browser, in a few minutes, alone." — [LD Rules 2017](https://ludumdare.com/resources/archive/rules-2017/)
- **[OPINION/ANECDOTE]** A jam veteran's tips say a game should be understandable in under one minute, because judges rate many games. Put mechanics and controls up front; players who don't get it in the first minute stop. A 100+-jam veteran advises an "Oh, now I get it!" moment within the first minute. — [Manasoup "10 Tips from a Game Jam Veteran"](https://itch.io/jam/manasoup/topic/1754557/10-tips-from-a-game-jam-veteran); [Very Serious Jam Tips](https://itch.io/jam/theveryseriousjuniperdevgamejam/topic/6363232/very-serious-jam-tips) **[VERIFY which tip is from which thread]**
- **[OPINION/ANECDOTE]** A checklist asks: "Is the core loop fun in 30 seconds? Judges play hundreds of games. Can someone understand it without a tutorial?" — [StraySpark, Game Jam Survival Guide](https://www.strayspark.studio/blog/game-jam-survival-guide-tools-templates)
- **[OPINION/ANECDOTE]** Judges "look at what is right in front of them, interact for a few minutes, and then leave," so presentation often matters more than substance. — [Trichotome Design, Game Jam Survival Guide](http://www.trichotome-design.com/blog/2021/12/27/kuriushacks-ce-presentation-game-jam-survival-guide)
- **[OPINION/ANECDOTE]** Make the first part easy so everyone forms a good impression without frustration. Aim for about 5–10 minutes of total content. — [Game Developer, "Game Jam beginner Tips for Success"](https://www.gamedeveloper.com/game-platforms/game-jam-beginner-tips-for-success); [Manasoup tips](https://itch.io/jam/manasoup/topic/1754557/10-tips-from-a-game-jam-veteran)
- **[OPINION/ANECDOTE, postmortem]** "During game jam voting, people play games back to back, very quickly ... your concept must fit this constraint or people will quit the game before seeing what is interesting." — one of these postmortems, from a search summary: [Gargoyle Landing postmortem (LD)](https://boopsgames.itch.io/the-gargoyle-landing-post-ld/devlog/47399/postmortem-of-game-jam); [7 Seconds to Live postmortem](https://zachu.itch.io/7-seconds-to-live/devlog/1617009/7-seconds-to-live-post-jam-postmortem) **[VERIFY attribution]**
- **[OPINION/ANECDOTE]** Brackeys Jam 13, "my game failed, here's what I learned": with thousands of games, if a game loses momentum, players say "Okay, quick rating, next game." — [itch.io thread](https://itch.io/jam/brackeys-13/topic/4626778/my-game-failed-heres-what-i-learned)
- **[OPINION/ANECDOTE]** A developer whose jam players found the game "too complex to enjoy" cut scope and shortened it for jam players. — [itch.io post](https://itch.io/post/16249087) **[VERIFY attribution]**

### Inferences
- The team's failed prototype, a dry puzzle whose fun appeared after several minutes, is exactly the pattern these sources warn against.
- Design so the **core "shift" verb is used within about 10 seconds of clicking Play**, and the first "aha" lands within about 60 seconds.
- Use a one-click title screen. Avoid multi-screen story intros.
- Teach controls through the first level, or with on-screen key prompts, rather than a text tutorial.

### Gaps
- No telemetry or study was found measuring how long jam raters actually play (median session length) or how drop-off relates to score.

---

## 5. Controls: simplicity, on-screen prompts, and browser and OS keyboard pitfalls

### Takeaway
Several browser and OS pitfalls are well documented:
- Ctrl+W (and other Ctrl+key browser shortcuts) cannot reliably be overridden, so avoid Ctrl bindings.
- Arrow keys and Space scroll the itch.io page unless the canvas has focus and the game calls `preventDefault`.
- Pressing **Shift 5 times opens Windows Sticky Keys**, which is especially relevant for a theme literally named SHIFT.

### Cited Findings
**Ctrl shortcuts**
- **[OPINION/ANECDOTE, developer forums]** Chrome reserves Ctrl+W for closing the tab and it can't be stopped. The only workaround is an `onbeforeunload` confirmation prompt. `preventDefault` didn't stop it in Babylon.js tests. — [HTML5GameDevs thread](https://www.html5gamedevs.com/topic/24499-overwrite-button-combinations-like-ctrls/); [Babylon.js forum](https://forum.babylonjs.com/t/how-prevent-default-of-c-w-t-n/44117)
- **[PLATFORM/HOST]** Firefox marks close-tab as a reserved key. — [Mozilla Support](https://support.mozilla.org/questions/1318792)
- **[OPINION/ANECDOTE]** An itch.io commenter advised "avoid using CTRL for web games, because CTRL+W will close the tab," and the developer changed the controls. — [itch.io comments (Overhealted)](https://keb1t.itch.io/overhealted/comments); [itch.io post](https://itch.io/post/5618746)
- **[OPINION/ANECDOTE]** GDevelop can't override Ctrl+W, which is treated as a system command. — [GDevelop forum](https://forum.gdevelop.io/t/gdevelop-ignoring-shortcut-preferences/73610)

**Arrow keys and Space in the itch.io iframe**
- **[PLATFORM/HOST]** Arrow keys and Space scroll the host page until the canvas has focus. itch.io's admin said they don't plan to change default keyboard behavior, for accessibility reasons. — [bugnet: arrow keys scroll the page](https://bugnet.io/blog/how-to-fix-web-game-arrow-keys-scroll-the-page); [bugnet: losing input focus in iframe](https://bugnet.io/blog/how-to-fix-web-game-losing-input-focus-inside-an-iframe) **[VERIFY admin quote location]**
- **[OPINION/ANECDOTE]** Fixes developers report:
  - give the canvas `tabindex="0"` and focus it on load and on pointerdown;
  - call `preventDefault` only for the keys the game uses (arrows, Space; one patch also blocked PgUp/PgDn/Home/End);
  - call `window.focus()` on load.

  Firefox may behave differently. — [bugnet](https://bugnet.io/blog/how-to-fix-web-keyboard-events-stolen-by-iframe); [Voltdrop web patch devlog](https://itch.io/devlog/1605028/voltdrop-web-patch-keyboard-input-fix.amp); [Arrow-key scrolling fix devlog](https://itch.io/devlog/1125211/-update-arrow-key-scrolling-bug-fixed.amp); [Construct forum](https://www.construct.net/en/forum/construct-3/how-do-i-8/prevent-arrow-keys-scrolling-166558); [Lexaloffle BBS](https://lexaloffle.com/bbs/?tid=4080)
- **[OPINION/ANECDOTE]** Jam players report "HTML keyboard controls not working sometimes," a typical focus problem. — [itch.io thread](https://itch.io/jam/amaze-me-game-jam/topic/1490586/html-keyboard-controls-not-working-sometimes)

**Sticky Keys and Filter Keys**
- **[PLATFORM/HOST, OS behavior]** Pressing Shift 5 times in a row opens a Sticky Keys dialog. In games, Windows can minimize the game to show it. Pressing another key between Shift presses avoids triggering it. Holding right Shift for 8 seconds triggers Filter Keys. — [Panda3D forum test](https://discourse.panda3d.org/t/shift-press-more-then-5-times/7452); [How-To Geek](https://www.howtogeek.com/1498/disable-the-irritating-sticky-filter-keys-popup-dialogs/); [Digital Citizen](https://www.digitalcitizen.life/problem-sticky-keys-takes-me-out-of-games/)

### Inferences
- **Do not make tapping or holding Shift the core mechanic**, even though "SHIFT" invites the pun. If Shift is used, also bind an alternative key (e.g. Space, E or right-click) and show both on screen. Repeated Shift taps by Windows players can pop up Sticky Keys and steal focus. (The Sticky Keys behavior is sourced; applying it to browsers is my inference, since browsers run under the same OS shortcut handling.)
- Avoid Ctrl, Alt, Tab, F-keys and Backspace bindings.
- Prefer WASD/arrows + Space, or mouse-only.
- Show control prompts on the first screen.
- Add a "click to play" overlay. It solves iframe focus and audio unlock in one step (see Section 9).
- No source was found on mobile; making it mouse/touch-compatible is cheap extra reach in Phaser (inference).

### Gaps
- No quantitative evidence was found linking control complexity or keybinding choice to jam scores.
- No source was found on mobile share of jam raters.

---

## 6. Juice and game feel: biggest impact for least effort

### Takeaway
The canonical talks show that cheap layered feedback transforms a plain game:
- **"Juice it or lose it"** adds tweening/easing, particles, screenshake, sound, color and flashes.
- **"The Art of Screenshake"** adds animation, faster and bigger bullets, muzzle flash, more fire and shake.

The largest controlled study (Kao 2020, N = 3,018) found **moderate juice beats both none and extreme**, so add it, but don't overdo it.

### Cited Findings
- **[OPINION/EXPERT TALK]** Jonasson & Purho, "Juice It or Lose It" (GDC 2012). They live-upgrade a "boring old" block-breaker using tweening/easing, particles, screenshake, sound, animation, color and screen flashes. Purho: if a game is juicy "it's way more fun to interact with it and it feels more professional." — [GDC Vault session](https://gdcvault.com/play/1016487/contactUs); [Game Developer, "Has your game got juice?"](https://www.gamedeveloper.com/business/has-your-game-got-juice-more-); [summary](https://gamejuice.pages.dev/articles/juice-it-or-lose-it-lessons)
- **[OPINION/EXPERT TALK]** Jan Willem Nijman (Vlambeer), "The Art of Screenshake" (INDIGO 2013). He progressively upgrades a top-down shooter. A community recreation lists: animation, lower time-to-kill, higher fire rate, bigger bullets, muzzle flash, faster bullets, lower accuracy, plus screenshake and recoil. — [DK Liao recreation breakdown](https://dkliao.itch.io/the-art-of-screenshake-recreation/devlog/451576/quick-breakdown-of-all-the-effects); [Game Developer coverage](https://gamedeveloper.com/design/vlambeer-co-founder-shares-advice-on-building-better-action-games); [Kenney's must-see videos list](https://kenney.nl/learn/must-see-videos-for-indie-developers)
- **[STUDY]** Kao 2020 (N = 3,018): no juice and extreme juice both reduced play time, performance, experience and intrinsic motivation; medium and high did best. — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1875952118300879)
- **[STUDY]** Juul & Begy 2016: null results for juicy vs non-juicy tile-matching. Juice may matter less in slow puzzle games. — [via ResearchGate](https://www.researchgate.net/publication/339467686_The_Effects_of_Juiciness_in_an_Action_RPG)
- **[OPINION/EXPERT]** Steve Swink, *Game Feel* (2008): game feel is "real-time control of virtual objects in a simulated space, with interactions emphasised by polish." Response must have no noticeable lag. — [Wikipedia: Game feel](https://en.wikipedia.org/wiki/Game_feel); [Liz England review](https://lizengland.com/blog/review-game-feel-by-steve-swink/)
- **[OPINION/EXPERT]** GMTK video "Secrets of Game Feel and Juice." — [Amara transcript page](https://amara.org/v/C3BGA)
- **[OPINION]** Critique: Folmer Kelly argued juice can cost immersion. — [Game Developer](https://www.gamedeveloper.com/business/has-your-game-got-juice-more-) **[VERIFY]**

### Inferences
Highest return for a Phaser 3 team, all built-in or one-liners:
1. Tweened squash/scale "pop" on every interaction (`this.tweens.add`).
2. A short camera shake (`cameras.main.shake`) and flash (`cameras.main.flash`) on key events.
3. A particle burst on success or destruction.
4. A sound for **every** player action.
5. Eased (not linear) UI and screen transitions.

For a "shift" mechanic, the moment of shifting should get the strongest feedback: sound, flash or shake, and a tween. Keep it moderate, per Kao.

### Gaps
- The hit-pause/hit-stop, permanence and camera-lerp items commonly attributed to Nijman's talk could not be confirmed from accessible sources.
- No study links juice directly to jam ratings.

---

## 7. Audio: score lag, cheap tools, mute/volume control, autoplay

### Takeaway
- No dataset was found proving that the audio category lags. That claim stays an assumption.
- Browsers block audio until a user gesture, so Phaser games need a click/tap to unlock.
- Free, fast tools (ChipTone, jsfxr, BeepBox, Kenney, Freesound) make basic audio cheap.

### Cited Findings
- **[PLATFORM/HOST, Phaser docs]** Browsers, especially Chrome and mobile, require a user gesture before audio plays. Phaser's `sound.locked` reports this. Phaser tries to resume the AudioContext after the first click or tap, and the Chrome warning at boot is normal. — [Phaser docs: BaseSoundManager.locked](https://newdocs.phaser.io/docs/3.85.2/focus/Phaser.Sound.BaseSoundManager-locked); [Phaser docs: unlock](https://newdocs.phaser.io/docs/3.80.0/focus/Phaser.Sound.BaseSoundManager-unlock); [phaser3-faq: Sound](https://github.com/samme/phaser3-faq/wiki/Sound)
- **[OPINION/ANECDOTE]** A Phaser user fixed missing music by adding a "click to start" scene. — [Phaser Discourse, "Starting audio"](https://phaser.discourse.group/t/starting-audio/577)
- **[PLATFORM/HOST]** Tools:
  - **ChipTone**: browser SFX generator; sounds are CC0, free for any use.
  - **jsfxr**: browser port of sfxr with presets.
  - **BeepBox**: music sketching that needs no music knowledge.
  - **Kenney**: free CC0 audio packs.
  - **Freesound**: licenses vary per sound.

  — [itch.io ChipTone listing / similar tools](https://itch.io/games-like/684257/chiptone.amp); [Defold "Tools and resources for Game Jammers"](https://forum.defold.com/t/tools-and-resources-for-game-jammers/2707); [GoedWare free resources thread](https://itch.io/jam/goedware-game-jam-3/topic/1786789/free-gamedev-resources-art-music-sfx-vfx-models-etc); [gtstu guide](https://gtstu.com/free-sound-effects-indie-game/)
- **[DATA]** Audio-category results pages show wide spreads (e.g. GMTK 2025 audio scores down to about 1.37 deep in the rankings). This does not isolate silent games. — [GMTK 2025 audio results p.424](https://itch.io/jam/gmtk-2025/results/audio?page=424)

### Inferences
- Because Audio is one of the six Game Off categories, a silent game takes a near-guaranteed low score on one-sixth of the criteria, and probably drags down Overall too.
- Minimum viable audio:
  - one looping BeepBox track;
  - 5–10 ChipTone/jsfxr SFX, one per player action;
  - a distinct "shift" sound;
  - a mute/volume toggle (M key plus an on-screen icon).
- Start audio from the "click to play" screen so the unlock always succeeds.
- The mute-control recommendation is my inference; no source was found measuring its effect.

### Gaps
- No quantitative evidence was found that audio scores lag other categories, or that silent games score worst.
- No source was found on volume or mute controls and ratings.
- "That Sound's Juicy! Exploring Juicy Audio Effects" (ICEC 2021) exists, but its findings were not retrieved. — [Springer](https://link.springer.com/chapter/10.1007/978-3-030-89394-1_24)

---

## 8. Theme clarity: making the interpretation obvious fast

### Takeaway
Raters score "Theme Interpretation" on whether they *see and agree with* the reading. Community advice:
- State the interpretation explicitly in the title, cover and description.
- Make it visible in the first minutes of play.
- Be wary of subtle puns.

### Cited Findings
- **[PLATFORM/HOST]** Jam pages say entrants choose the interpretation and voters judge whether it is good. — [ELAN 2024 jam page](https://itch.io/jam/elan-2024-game-jam); [itch.io post](https://itch.io/post/10456098) **[VERIFY attribution]**
- **[OPINION/ANECDOTE]** Unusual readings are fine "so long as you can explain how it relates to the theme." One developer admitted "maybe it wasn't clear how the mechanic works, so it's confusing how it fits the theme" and added an explanation post-jam. A punning entry was defensible "but just not so obvious at first." — [itch.io posts](https://itch.io/post/10228735), [2](https://itch.io/post/6495764), [3](https://itch.io/post/12883791) **[VERIFY which quote is in which post]**
- **[OPINION/ANECDOTE]** Use an attention-grabbing cover with screenshots and a solid description. A more readable title on the cover would have helped. — [itch.io post](https://itch.io/post/14847343) **[VERIFY]**
- **[OPINION/ANECDOTE]** Don't take the theme too literally; twisting its meaning is fine. — [Tuts+, "How to deal with a bad game jam theme"](https://code.tutsplus.com/how-to-deal-with-a-bad-game-jam-theme--cms-21234a)
- **[STUDY]** Description quality predicts ranking. — [Vu & Bezemer, ACM](https://dl.acm.org/doi/fullHtml/10.1145/3402942.3402981)

### Inferences
- For SHIFT, make the shift **the core verb** and name it in the title or tagline.
- Write the first line of the description as "In [Title], you shift ___ to ___."
- Show the shift happening in the cover image or GIF, plus in the first 10 seconds of play.
- A double meaning (e.g. mechanical shift plus narrative or emotional shift) can earn Innovation, but only if the primary meaning is obvious.

### Gaps
- No data was found on how Theme Interpretation scores relate to the explicitness of the interpretation.

---

## 9. Web playability: ratings advantage and common web-build failures

### Takeaway
- Web builds roughly double rating counts and sharply cut exposure to the median penalty (Section 1).
- The usual web failures are iframe focus, keys scrolling the page, audio not starting before a click, fullscreen and aspect issues, and file size.
- SharedArrayBuffer is opt-in on itch.io and unnecessary for single-threaded Phaser.

### Cited Findings
- **[DATA]** Browser entries got about 2.1x the ratings, and 78% of download-only entries were penalised by the adjustment versus 27% of browser entries. — [jamshell](https://munimv2.itch.io/jamshell/devlog/1713443/browser-builds-get-about-twice-the-ratings-data-from-10-itchio-jams)
- **[OPINION/ANECDOTE, third-party guide]** itch.io HTML5 limits are reportedly 500 MB extracted, 200 MB per file, 1,000 files, as a ZIP with `index.html`. SharedArrayBuffer is an optional switch, and threaded builds need cross-origin headers, so single-threaded exports are recommended for portal iframes. The mobile option launches fullscreen on click. — [Summer Engine, "Where to publish HTML5 games"](https://www.summerengine.com/make-great-games/publish-an-html5-game) **[VERIFY against itch.io docs]**
- **[PLATFORM/HOST]** Phaser audio is locked until a gesture, and a click-to-start scene is the common fix. — [phaser3-faq Sound](https://github.com/samme/phaser3-faq/wiki/Sound); [Phaser Discourse](https://phaser.discourse.group/t/starting-audio/577)
- **[OPINION/ANECDOTE]** Iframe focus and arrow/space scrolling fixes are covered in Section 5. — [bugnet](https://bugnet.io/blog/how-to-fix-web-game-losing-input-focus-inside-an-iframe)
- **[OPINION/ANECDOTE]** LD guides recommend keeping file size down and targeting HTML5, and making the game "as simple as possible to play." — [Rumor Games guide](https://rumorgames.com/ludum-dare-honest-guide/); [arimia First Ludum Dare Tips](https://arimiadev.com/first-ludum-dare-tips/)

### Inferences
Phaser 3 web checklist:
- Use the Phaser Scale Manager (`FIT` + `autoCenter`) at a fixed 16:9 base resolution. Set the itch embed size to match, and enable the itch fullscreen button.
- Show a "Click to Play" overlay that focuses the canvas and unlocks audio.
- `preventDefault` only the arrow keys and Space.
- Avoid Ctrl and Shift-only bindings.
- Keep the total download small (compressed audio such as OGG plus MP3 fallback, texture atlases) for fast load.
- Test the uploaded build on itch.io itself, not just localhost, in Chrome, Firefox and Safari, on day one of building. Upload a "hello world" build early.

### Gaps
- No itch.io official doc was retrieved confirming current HTML5 size and file limits or SharedArrayBuffer wording.
- No data was found on how load time relates to ratings.

---

## 10. Common reasons jam games get low scores or few ratings

### Takeaway
Evidence-backed causes:
- **No browser build** or no playable files.
- **Not rating others.**
- **Falling below the median rating count** (median adjustment).

Anecdotal causes repeated across postmortems:
- Unclear goal or ending.
- Difficulty spikes.
- The interesting part comes too late.
- Too complex.
- Missing feedback or animation.
- Overscoped and unfinished.

### Cited Findings
- **[DATA]** Entries with no playable files got the fewest ratings. Download-only entries were penalised 78% of the time. — [jamshell](https://munimv2.itch.io/jamshell/devlog/1713443/browser-builds-get-about-twice-the-ratings-data-from-10-itchio-jams)
- **[DATA]** 11–46% of entries come from makers who rate no one, and those entries get far fewer ratings. — [jamshell 14-jam](https://munimv2.itch.io/jamshell/devlog/1713956/makers-who-rate-other-jam-games-get-more-ratings-data-from-14-itchio-jams)
- **[OPINION/ANECDOTE]** One-third of LD42 entries didn't reach 20 ratings. — [Rumor Games](https://rumorgames.com/ludum-dare-honest-guide/)
- **[OPINION/ANECDOTE, postmortems]** Recurring problems:
  - difficulty feedback split between "far too difficult" and "no skill needed";
  - "the goal and direction was hard to find and understand," and the ending confused players;
  - players quit before seeing what is interesting;
  - "stop the player before they feel like they need to quit out of frustration";
  - missing animation "made the game hard to understand";
  - plan to finish in 3/4 of the time.

  — [Gargoyle Landing postmortem](https://boopsgames.itch.io/the-gargoyle-landing-post-ld/devlog/47399/postmortem-of-game-jam); [7 Seconds to Live postmortem](https://zachu.itch.io/7-seconds-to-live/devlog/1617009/7-seconds-to-live-post-jam-postmortem); [The Cycle postmortem](https://phoenixphil.itch.io/the-cycle/devlog/995899/game-jam-postmortem); [Obedience GMTK25 postmortem](https://salty-gamedev.itch.io/obedience-gmtk25/devlog/1003875/gmtk-jam-25-postmortem-or-how-not-to-come-back-in-the-jam-development-after-7-years-of-not-doing-it); [devindetails, "Avoid these pitfalls"](https://devindetails.com/avoid-these-pitfalls-during-your-next-game-jam-as-i-wish-i-did/) **[VERIFY which quote belongs to which postmortem]**
- **[OPINION/ANECDOTE]** Thumbnail advice: turn off the UI, screenshot an interesting moment, and overlay the title. — [Rumor Games guide](https://rumorgames.com/ludum-dare-honest-guide/)
- **[STUDY]** Teams report scope management and MVP as top practices under jam time pressure. — [Borg et al.](https://arxiv.org/abs/1904.00462)
- **[OPINION/ANECDOTE]** Short voting windows mean the voting period is the only time many games get played. — [itch.io post](https://itch.io/post/16253707) **[VERIFY]**

### Inferences
Prioritised actions for this team, based on evidence strength and cost:
1. **Ship a working web build early and test it on itch.io.** [DATA]
2. **Rate and comment on many games from day one of voting**, all three members. Target at least 20 ratings received to clear an assumed ~16 median. [DATA + formula]
3. **Make the core "shift" verb fun in the first 30 seconds, with no text tutorial.** [OPINION, consistent across sources]
4. Use an easy start, a clear goal and a clear end state, about 5–10 minutes long. [OPINION]
5. Add moderate juice on the core verb. [STUDY + talks]
6. Add basic audio, unlocked on click, plus mute. [inference]
7. Make the title, cover and description state the SHIFT interpretation. [STUDY on description + OPINION]
8. Avoid Shift-only and Ctrl bindings, and fix arrow/space scrolling. [PLATFORM/ANECDOTE]

### Gaps
- No systematic analysis of jam-game comments or feedback categories was found (e.g. a frequency count of "too hard" or "unclear" complaints).
- No evidence was found on the effect of late submission or update policy on Game Off ratings.
