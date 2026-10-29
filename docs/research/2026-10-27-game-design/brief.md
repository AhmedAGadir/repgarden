# Collection brief: how plant, farm, creature and fitness games keep people coming back

Date of reading: 27 October 2026. Written for a research agent collecting evidence for the
RepGarden game-design stage. Read all of this before starting.

## What RepGarden is, in four lines

RepGarden is a gym app for a personal trainer (Benji) and his clients. The trainer sets
workouts on a website; clients follow them on a phone in the gym, log sets, film a set for
feedback, and check in. It is vegetable-themed: vegetables grow, and so does the client. We
are designing the game layer that sits on top of the training. It must cost the trainer no
extra work: every game event is derived from what the trainer already does (set the
programme, comment, set a challenge) and what the client already logs.

## The constraints the game is designed inside

- Players are the clients, not the trainer.
- Venue: the gym. One hand, a glance of a few seconds between sets, with a longer sit-down
  moment at the end of a workout and in the evening. Never a locked-in 20-minute session.
- The game can only see what the app records: sessions done against sessions planned, sets,
  check-ins, personal bests. It cannot see effort or form.
- Clients train two to five times a week with rest days the trainer prescribed. A daily
  streak would punish the rest days.
- Free app, no shop, no paid currency.
- Simple UI, full-width, one scene at a time.

## The questions to answer for EVERY app in your lane

Answer each with evidence: the app's own store listing, help pages, wiki, developer blog or
press; and reviews or Reddit threads for what people complain about or love. Give a URL for
each claim. Where you cannot confirm, say "not confirmed" rather than guessing.

1. **Unit of play.** What is the thing that grows, accumulates or is tended? A farm, a tree,
   a creature, a plant per task, a town? What does one real-world action map to in-game?
2. **Session shape.** How long is a typical session and how is it structured? Is there a
   quick "glance" screen and a longer "sit-down" screen? What can you do in ten seconds?
3. **Absence.** What happens when the player does not come back for a day, a week, a month?
   Decay, wither, death, weeds, nothing? How is it recovered? Is there a streak and what
   protects it (freezes, repair, forgiveness)? What do reviews say about this?
4. **Currency and endogenous value.** What do you earn, what can you spend it on, and does
   spending feed back into the thing you care about (seeds that grow the garden) or is it
   cosmetic only? Any real-money layer and how it is perceived.
5. **Stakes, risk and chance.** Can the player bet, risk a loss for a bigger reward, or take
   an opt-in challenge? Any randomness: rare drops, surprise visitors, weather?
6. **Progression.** Levels, seasons, chapters, harvests, evolutions. What marks a milestone?
7. **Social.** Friends, visiting, leaderboards, co-op, competition. Is it opt-in?
8. **Freedom and identity.** What can the player choose, name, decorate, customise?
9. **Signature interaction.** The one gesture or moment that is unmistakably this app
   (the Fruit Ninja swipe, the Forest tree planting, the Finch bird going on an adventure).
10. **UI type and art.** One of: isometric world, top-down world, side-on single scene,
    creature in a room, map, minimal stat/figure. Describe the art style in a sentence and
    whether the screen is dense or sparse. Note what is on the home screen.
11. **Sound and feel.** Any notable feedback: haptics, sounds, animations on completing a task.
12. **Scale and reception.** App Store (GB) rating and count on the day, Play install band,
    launch year, developer, business model. Three concrete complaints from reviews or
    Reddit, quoted or closely paraphrased with a URL, and three things people love.
13. **Lesson for RepGarden.** Two or three sentences: what transfers to a 3-times-a-week
    gym app with a vegetable theme, and what to avoid.

## Tools and rules

- WebSearch and WebFetch for store listings, help centres, wikis, developer blogs, press.
  Headless Chrome is blocked on apps.apple.com, play.google.com and reddit.com; use
  WebFetch for the first two (they render server-side) and the ScrapeCreators Reddit
  endpoints for Reddit.
- Reddit via `~/.codex/skills/scrapecreators-research/scripts/sc.sh`, for example:
  `sc.sh /v1/reddit/subreddit/search "subreddit=finch&query=streak&sort=relevance"` or
  `sc.sh /v1/reddit/search "query=plant%20nanny%20wither"`. One credit a call. Budget:
  at most 30 credits for your lane. Never print the API key. Stop on HTTP 402.
- App Store numbers: `https://itunes.apple.com/lookup?id=<id>&country=gb` gives
  averageUserRating and userRatingCount with no scraping.
- Do not download anything from Uppbeat. Do not write to any repository. Do not record
  any secret.
- Read sources; do not rely on memory for facts that can be checked. Mark anything from
  memory that you could not confirm as "not confirmed".

## Output

Write two files into your lane's folder (given in your prompt):

1. `findings.md`: one section per app with the thirteen answers as numbered headings, each
   claim followed by its source URL in parentheses. Quote reviews briefly. At the end, a
   short "Across the lane" section: patterns you saw across your apps, in five to ten
   bullets, each with the apps that show it.
2. `apps.json`: a JSON array, one object per app, with these keys, all strings unless
   noted: name, app_store_id, developer, launch_year, business_model, unit_of_play,
   session_shape, absence, streak_protection, currency (array of {name, earned_by,
   spent_on, feeds_back: bool}), stakes_risk_chance, progression, social, freedom_identity,
   signature_interaction, ui_type (one of the six above), art_style, home_screen,
   sound_feel, ios_gb_rating (number), ios_gb_rating_count (number), play_installs,
   complaints (array of {text, url}), praise (array of {text, url}), lesson, sources
   (array of urls).

Report back in chat with: the two file paths, the credits used, which apps had thin
evidence, and the five most useful findings in one line each.
