*Research · 26 October 2026*

# The apps personal trainers use to coach their clients

Markdown twin of `report.pdf`, generated from the same source by `report/gen.py` and `report/tomd.py` on 26 October 2026. The charts in the PDF are tables here; the data behind every figure is in `platforms.json`, and every claim's source is in `findings.md`.

Fourteen platforms, read from their own pages and store listings on one day: who is big, what they charge, which ones are games, how a client films a set, and how each one finds its trainers. Written for the RepGarden build, and for Benji.

Prepared by gadirlabs**.** Ahmed Gadir · gadirlabs.io · Every figure is from a page read on 26 October 2026; company marketing figures are marked as such; anything that could not be confirmed is marked not verified.

*Why this report*

## What we wanted to know, and what we found.

RepGarden is being built for Benji, a personal trainer, and his clients. Before the first screen is drawn, this report answers six questions about the apps trainers already use, so that the feature list, the second-phase game design and the way RepGarden finds trainers rest on what the market does rather than on guesses.

| The question | The short answer |
|---|---|
| **Who are the platforms, and how big are they really?** | Fourteen that matter, in three kinds of business. Company trainer counts are inflated; store ratings are the honest signal. Pages 7–8. |
| **What do they charge, and whom?** | The trainer, per client band, from $9 to $700 a month; clients pay nothing; nobody bills clients through Apple. Page 9. |
| **Which features are standard, and which are rare?** | Programmes, libraries, calendars, push and chat are universal. A client filming a set is on five of fourteen. A trainer marking that video up is on none. Pages 10 and 12. |
| **How do they gamify, if at all?** | Thinly. Three have a real layer, built from habit lists, leaderboards, streaks and badges. Nobody has levels, a character or a world. Pages 6 and 11. |
| **How do they find trainers and clients?** | The trainer first, on eleven of fourteen. Referral schemes, certification bodies, gyms, search, named faces, and paid ads that all sell a free trial. Pages 13–14. |
| **Is this a business anyone pays for?** | Yes: four acquisitions in six years, one profitable UK independent, and a crowded, cheap middle. Page 5. |

### What the report changes

- **The feature list holds, with one sharpening** Everything in the MVP is either standard or the gap. The sharpening: the reply to a client's video must land on a moment in the clip, because that is the one thing nobody has. Page 3.

- **The website sells to trainers** Clients never find these apps on their own. The marketing site, Benji as its first face, and later a referral scheme are the growth plan; the store listing is for approval. Page 4.

- **The second phase has no one to copy** The market's gamification stops at streaks and leaderboards. A garden that grows with a client's training is a different kind of thing, and the evidence says it is unoccupied. Page 6.

Pages 2–6 are the outcomes. Pages 7–15 are the evidence, platform by platform. Page 16 is the method. Every figure was read on 26 October 2026 from the platform's own pages or store listing; marketing claims are marked as such.

*Outcome 1 · The app*

## Are our features the right ones?

The MVP list was written from Benji's call before the research. Set against fourteen platforms, it holds.

| In the MVP | What the market does | Verdict |
|---|---|---|
| **Invite-only accounts; trainer and client roles** | Eleven of fourteen work exactly this way; TrueCoach's listing tells clients they are there because their trainer subscribed | Keep |
| **Exercise → workout → programme, assigned to dates** | Universal. Everfit and TrainHeroic add a block or section level inside the workout; Trainerize sells reusable templates | Keep. Copying a programme is expected |
| **A stock exercise library, the trainer's own clips on top, a fallback image** | Every platform ships a library of 1,000+ stock clips and lets the trainer add their own. The same shape; where the stock library comes from is being researched | Keep |
| **Calendar first; today's workout; log sets; mark complete** | Universal. Rest days and empty days are blank on most apps | Keep |
| **Film a set, with a note; trainer replies on that set** | Upload on five of fourteen, FITR included (500 MB). The reply is a comment under the clip everywhere; no drawing, scrubbing or pinned moment anywhere | Keep, sharpen. See below |
| **Per-client progress: adherence, loads, personal bests** | Standard. PB tracking is what My PT Hub calls gamification; Hevy sends a live PR notification | Keep. The PR moment deserves a screen |
| **Push for a scheduled workout; a nudge after a miss** | Standard, and TrainerFu's coach-side 'streaks broken' alert shows the trainer wants to know too | Keep. Add the trainer's view of who missed |
| **Accessibility from the first screen** | Not marketed by any platform, and ratings of 2.5–3.0 on two of them say app quality is uneven | Keep. A quiet advantage |

### Add, or bring forward

**The reply lands on a moment.** A timestamp on the trainer's note, a tap that jumps there, and a mark of approval. This is the whole difference between RepGarden's video and FITR's, and it is cheap. Design it now, not in phase two.

**A habit checklist.** Nine of fourteen have one; it is the cheapest mechanic in the market and the natural first thing a garden grows from. Not for the MVP, but the data model should expect it.

**Check-ins: photos and body metrics.** On six or more platforms. Agreed in; the detail is scoped with Benji.

**The trainer's inbox of sets.** A list of clips waiting for a reply, oldest first. Nobody shows this well, and it is what makes the review feature survive.

### Leave out, confirmed

**Messaging.** Every platform has it, and Benji's clients still use WhatsApp. Everfit's per-exercise comment threads are the one idea worth noting, and the reply-on-a-set covers it.

**Payments.** Nobody bills clients through the app; everyone collects on the web via Stripe. Out now, web-only later.

**Nutrition, AI form analysis, localisation, bookings, a marketplace.** Nothing in the research argues for any of them in a first version. Everfit's camera-counted push-up challenge is the only AI feature with any novelty, and it is a stunt.

**Remove: nothing.** The list was already short; the research argues for keeping it that way and spending the saved effort on the reply and on the calendar's empty days.

*Outcome 2 · Growth*

## How RepGarden finds its trainers.

The trainer is the customer and the client is a guest. Eleven of fourteen platforms acquire the trainer first; the client pays nothing and arrives by invitation. That settles where the effort goes.

### What this means now

**The marketing website is the product's front door,** and it speaks to trainers. Its job is to make a trainer want to move their clients onto RepGarden; the store listing exists to get approved and to be the thing the invited client taps.

**Benji is the first face.** Kahunas puts eighteen coaches with their Instagram handles on its homepage; Playbook fronts named creators with their earnings; TrainHeroic sells named strength coaches. The honest version of that is one real trainer whose clients use the app, saying what changed.

**Lead with the two things nobody else has,** in this order: the reply that lands on the moment in a client's set, then the garden. Across 318 active Meta ads from eight platforms, not one leads with form review, video feedback or technique; every one sells a free trial and less admin. Everything else on the feature page is a tick in a column every competitor can also tick.

### Channels, when there are trainers to send

| Channel | Precedent | For RepGarden |
|---|---|---|
| **Referral** | 10–25% recurring is the norm; FITR has none | An opening against FITR; set up once a second trainer exists |
| **Gyms** | FITR gives PureGym's trainers a 90-day trial; Kahunas shows the same logo | Benji's own gym first; the chain later |
| **Certification bodies** | NASM, Precision Nutrition, CIMSPA deals on five platforms | CIMSPA is the UK route |
| **Search** | FitBudd runs 60 'alternative to X' pages; Everfit publishes an llms.txt | 'RepGarden vs FITR' and one page per competitor, written honestly |
| **Events** | FITR and HYROX | Benji's sport, if he has one |
| **Social and ads** | Eight platforms run 318 Meta ads between them, all at trainers, every one selling a free trial; Hevy buys nothing and has the biggest following | Not yet. When there is a trainer to sell to, lead with the thing no ad mentions: the video reply |

> **One warning.** Hevy has 17 million consumer users and a coach product bolted on. If Benji's clients already log workouts in Hevy or Strong, RepGarden is competing with a free logger they like, and the trainer loop — the reply, the programme, the garden — has to be visibly better than what they lose.

*Outcome 3 · Risks, and the business*

## Things to watch out for.

**Fitr already has the upload.** Benji's complaint on the first call was that Fitr is clunky to use, and Fitr's own pages confirm the feature exists: 500 MB per file, coach comments, a push on reply. So the contest is on the review experience, not the upload. Filming a set and getting a reply has to feel light, and the reply has to land on the moment.

**Video storage is the one cost that grows.** FITR allows 500 MB per file. The proposed rule — delete seven days after the trainer has viewed it, thirty days regardless, keep the data and a poster frame — needs deciding before the first upload, and the client needs one line telling them.

**User-generated content rules.** Both stores treat a client's clip as UGC even when only the trainer sees it: report and block, terms before the first upload, published contact details. These are in the scope already; they must not slip.

**Price is not a moat.** Trainerize starts at $9, Everfit is free for five clients, and every platform runs a 14–30 day trial. A trainer can leave for almost nothing. The reason to stay has to be the clients liking the app.

**App quality is uneven and noticed.** Kahunas is at 2.5 stars on Play from 257 reviews, FITR at 3.0, and TrainerFu's iOS app has not shipped since May 2025. Clients rate the app they are made to use. A client app that is simply pleasant is itself a selling point to trainers.

**Some trainers distrust game mechanics.** CoachRx sells "depth over volume, a relationship not a transaction" and hides its own streak counter. The garden must read as coaching made visible, not a toy bolted onto a logger.

### Is this a business?

Not the main point, since the decision to build is made, but the research says something about it.

Money has moved in this category for six years: EverCommerce paid $11.7m for My PT Hub in 2020 and Jonas bought it in 2024; ABC bought Trainerize in 2020; Daxko bought Exercise.com in October 2025; Garmin bought TrainHeroic in July 2026. FITR, the UK independent nearest to RepGarden, raised £1.5m in December 2025 and is profitable. Everfit funds a free tier and an engineering team from per-client subscriptions. The model — a trainer paying $15–30 a month at entry, rising with clients, no cut on their payments — is proven on eleven platforms.

It is also crowded and cheap in the middle, where a UK trainer choosing between FITR, My PT Hub and Trainerize is choosing on feel. A new entrant does not win there on features. It wins with one reason to switch that can be said in a sentence, and with trainers who bring other trainers. The research gives RepGarden the sentence; Benji and the build series are the first trainers.

> **The viability test for later** is not revenue. It is whether a second trainer, one Benji did not bring, moves their clients onto RepGarden and keeps them there past the first month. Until then it is a product for one trainer, which is what it was scoped to be.

*Outcome 4 · The second phase*

## What the market calls gamification.

Fourteen platforms were checked for nine mechanics, from the simplest to the kind that makes an app a game. The count falls off a cliff after the fourth rung.

### Platforms with each mechanic, of 14

| Mechanic | Platforms |
|---|---|
| Habit checklist | 9 |
| Leaderboards | 5 |
| Challenges | 5 |
| Streaks | 4 |
| Badges | 2 |
| Points | 1 |
| Levels or XP | 0 |
| Avatars, a character | 0 |
| A world that grows | 0 |

Hevy's consumer app, which Hevy Coach's clients use, has a weekly streak and a follower leaderboard of its own; it is not counted above. "Challenges" on My PT Hub and PT Distinction are names for marketing programmes, not mechanics, and are not counted.

### What each one actually is

| Mechanic | In plain words |
|---|---|
| **Habit checklist** | a list of daily things to tick |
| **Leaderboards** | ranked lists of clients |
| **Challenges** | a time-boxed contest, usually with a leaderboard |
| **Streaks** | consecutive days or weeks, reset on a miss |
| **Badges** | a milestone sticker |
| **Points** | a score for doing things |
| **Levels or XP** | progression that unlocks something |
| **Avatars, a character** | someone to be |
| **A world that grows** | somewhere to be |

### What the three "real" layers are made of

**Trainerize**: streaks and badges on habits, leaderboard and threshold challenges where clients "earn points by working out, achieving personal bests, completing habits", groups, high-fives in messages. **Everfit**: eleven leaderboard types, streak insights on habits (current, best, daily average), challenges behind a paid add-on, and a push-up challenge counted by the phone camera. **TrainHeroic**: team leaderboards on any exercise, a global percentile called StackUp, weekly streaks, virtual fist bumps, and a badge for lifting a million pounds in total.

> **The finding, in one sentence:** the whole market's idea of a game is a scoreboard: a number that goes up, a list that ranks you, a chain you must not break. Nothing has a character, a place, or anything that grows and can be tended. Those are the mechanics that make people open an app when nobody is making them, and in this market they are untouched.

*Who's who*

## Fourteen platforms, three kinds of business.

### Trainer-side software — the coach pays, the client is invited
**ABC Trainerize** · Trainers, gyms, studios, enterprise The biggest. Owned by ABC Fitness since 2020. Every feature as a paid add-on; no client video upload. **TrueCoach** · Solo online personal trainers Solo online trainers. Owned by Xplor. Video upload attached to the exercise; flat 5% on client billing. **Everfit** · Fitness, nutrition and sport coaches, gyms and studios The strongest game layer and a free tier for five clients. Video comments tagged per exercise. **My PT Hub** · Personal trainers, fitness coaches and nutritionists UK-rooted, unlimited clients for £59. No game layer. Owned by Jonas Software since 2024. **FITR** · Coaches and gyms, functional-fitness lean; UK-rooted Benji's tool. UK, CrossFit and HYROX lean, profitable, small store footprint. See page 15. **PT Distinction** · Online personal trainers Independent, every feature on every tier, video upload included. Sells from the trainer's own site. **Hevy Coach** · Strength coaches with small rosters Built on the 17m-user Hevy consumer app. No client billing, no game layer of its own. **Kahunas** · Online coaches wanting their own branded app Branded-app play, creator-fronted, no commission. 2.5 stars on Play from 257 reviews. **FitBudd** · Coaches, influencers, gyms and studios wanting their own store listing Sells the trainer their own store listing. 60 'alternative to X' pages. $3.4m seed. **TrainerFu** · Solo trainers and small studios Simple and cheap. iOS app not updated since May 2025. **CoachRx** · Coaches wanting depth over volume; OPEX-trained By OPEX; sells depth over volume; a $5,995 certificate includes the software.

### Distribution businesses — the consumer comes first
**TrainHeroic** Strength coaches and teams; a marketplace that takes 30% on sales it sources. Bought by Garmin, 22 July 2026. **Playbook** Creators with audiences, not 1:1 trainers; keeps 20% of everything. Consumer pays $14.99 a month.

### Gym software with coaching in it
**Exercise.com** Gyms and studios, each shipping its own branded app. Quote-only, no trial. Bought by Daxko, October 2025.

Also checked: **Sidekick** does not exist as a product; its domain is parked and for sale.

*Scale*

## How big each one really is.

Companies' own trainer counts are not reliable — Everfit claims 380,000 coaches on 2,700 App Store ratings, Trainerize's "400,000+" has not changed since 2022, and TrueCoach's count has gone down. The honest signal is how many people have rated the client app, which only happens when a real client uses it.

### US App Store ratings on the client app, 26 October 2026

| Platform | US ratings |
|---|---|
| Hevy (consumer app) | 100,098 |
| ABC Trainerize | 34,300 |
| TrueCoach | 7,100 |
| Everfit | 2,700 |
| My PT Hub | 2,300 |
| TrainHeroic | 1,836 |
| Playbook | 1,100 |
| Kahunas | 600 |
| PT Distinction | 450 |
| TrainerFu | 300 |
| CoachRx | 100 |
| FitBudd | 60 |
| FITR | 25 |
| Hevy Coach | 4 |

Hevy's consumer app is shown because Hevy Coach's clients use it; Hevy Coach's own app has 4 ratings. PT Distinction has no Play listing; Exercise.com has no consumer scale by design. Social following tells a different story: TrainHeroic has the largest Instagram in the set and TrueCoach and Everfit both beat Trainerize (page 14).

### Google Play install bands
Trainerize **1m+** TrueCoach **100k+** Everfit **100k+** My PT Hub **100k+** TrainHeroic **500k+** Playbook **500k+** FITR **50k+** PT Distinction **—** TrainerFu **50k+** Kahunas **100k+** Hevy Coach **10k+** CoachRx **10k+** FitBudd **5k+** Exercise.com **—**

> Two platforms are a different size from what their numbers suggest. **TrainHeroic** has 500k+ Play installs on 1,836 iOS ratings because athletes come in through its marketplace, not through coaches. **FITR** claims 120,000 clients and £53m processed, but has 50k+ Play installs at 3.0 stars and fewer than 25 iOS ratings worldwide — its scale, if real, is not visible in the stores.

*Prices*

## What a trainer pays.

Almost everyone charges the trainer a monthly subscription that rises with the number of clients, and gives the client the app free. Sterling prices are shown in dollars at $1.30 for comparison; the originals are on the next table. Free trials are universal — 14 or 30 days — and Everfit's free tier is the only permanent one with real function.

### Cheapest paid tier, per month

### At around 50 clients, per month Dotted bars are estimates where the price at that step is not published.

| Platform | Model | Published prices | Trial | Cut on client payments |
|---|---|---|---|---|
| **ABC Trainerize** | Per client band | Free (1) · $9 (2) · Pro from $23 · $248 (500). Add-ons $10–45/mo each | 30 d | Stripe add-on $10/mo; % not verified |
| **TrueCoach** | Per client band | $26 (5) · $58 (20) · $137 (50), annual rates | 14 d | Flat 5% |
| **Everfit** | Per client band | Free (5) · Pro $16–242 · Studio $88–358 | 30 d | 3.15% + $0.30, plus $9/mo |
| **My PT Hub** | Flat above entry | £20 (3) · £59 unlimited · £199 all add-ons | 30 d | Stripe; % not stated |
| **PT Distinction** | Base + per client | $19.90 (3) · $59.90 (25) · $89.90 (50) | 1 mo | None — trainer's own Stripe or PayPal |
| **TrainHeroic** | Per athlete band | $9.99 (1) → $399.99 (1,000) | 14 d | No 1:1 billing; marketplace 30% or $1/client |
| **FITR** | Per active client | £14.99 + £3.00 per client; unlimited option | 14 d | 5.99% plus Stripe's fees |
| **Hevy Coach** | Per client band | $25 (1–10) → $700 (501–1,000) | 30 d | No client billing |
| **Kahunas** | Three tiers | $35 (25) · $69 (50) · $99 unlimited | 14 d | None |
| **FitBudd** | Base + per client | $15 (2) · $79 (20) · $149 + setup fees | 30 d | Web, or Apple IAP on Super Pro |
| **TrainerFu** | Per client band | $29 (10) → $250 (250); branded app +$75 | 14 d | Not named |

Playbook charges the trainer nothing and keeps 20% of what their followers pay ($14.99 a month each, 7-day trial). Exercise.com publishes no prices and offers no trial.

*Features*

## What they do, side by side.

Read from each platform's own feature pages and help centres. A question mark means it could not be confirmed either way on 26 October 2026, which for several smaller platforms is itself informative.

| Platform | Client films a set | Trainer marks the video up | Programme → workout → exercise | Client calendar | Progress dashboards | Push | Messaging | Client payments |
|---|---|---|---|---|---|---|---|---|
| **ABC Trainerize** | no | ? | yes | yes | yes | ? | 1:1, group, video messages | web, Stripe add-on |
| **TrueCoach** | yes | ? | yes | yes | yes | yes | 1:1 in-app | web, Stripe, 5% |
| **Everfit** | yes | ? | yes | no | yes | yes | 1:1, per-exercise threads | web, Stripe, 3.15%+$0.30 |
| **My PT Hub** | ? | ? | yes | yes | yes | yes | 1:1, community feed | web, Stripe |
| **TrainHeroic** | yes | ? | yes | yes | yes | ? | team chat | marketplace, 30% |
| **Playbook** | ? | ? | yes | ? | ? | ? | community threads | platform keeps 20% |
| **FITR** | yes | ? | yes | yes | yes | yes | 1:1, community, bulk | web, FITR's Stripe, 5.99% |
| **PT Distinction** | yes | ? | yes | yes | yes | yes | 1:1 and group | trainer's own Stripe/PayPal |
| **TrainerFu** | ? | ? | yes | yes | yes | ? | 1:1 | web, not named |
| **Kahunas** | ? | ? | no | yes | yes | yes | 1:1, video messages | web, no commission |
| **Hevy Coach** | ? | ? | yes | yes | yes | ? | 1:1 | none |
| **CoachRx** | ? | ? | yes | yes | yes | ? | 1:1 with video | web, Stripe |
| **FitBudd** | ? | ? | yes | yes | yes | yes | 1:1 with video | web; Apple IAP on top tier |
| **Exercise.com** | ? | ? | yes | ? | yes | yes | 1:1, group | own processing |

> **The column that matters is the third one.** Nobody has a verified way for a trainer to annotate a client's video — draw on it, scrub it frame by frame, or pin a note to a moment. Where video review exists it is a comment thread under the clip. That is the feature RepGarden can own.

*Gamification*

## Who has turned training into a game.

Three have a genuine layer, several have one mechanic sitting unused, and eight have essentially nothing. Trainerize is the only one with points; nowhere in the market are levels, XP or avatars confirmed to exist.

| Platform | Game layer | Streaks | Badges | Points | Leader- boards | Challenges | Levels | Avatars | What it actually looks like |
|---|---|---|---|---|---|---|---|---|---|
| **ABC Trainerize** | yes | yes | yes | yes | yes | yes | ? | ? | Streaks, badges, milestones, leaderboard and threshold challenges with points, groups, high-fives |
| **TrueCoach** | no | ? | yes | ? | ? | ? | ? | ? | Milestone badges and habits only |
| **Everfit** | yes | yes | ? | ? | yes | yes | ? | ? | Eleven leaderboard types, an AI push-up challenge that counts reps by camera, streak insights — challenges behind the paid Autoflow add-on |
| **My PT Hub** | no | ? | ? | ? | ? | ? | ? | ? | Personal bests and a social feed |
| **TrainHeroic** | yes | yes | ? | ? | yes | ? | no | ? | Team leaderboards on any exercise, a global StackUp percentile, weekly streaks, a million-pound club |
| **Playbook** | no | ? | ? | ? | ? | ? | ? | ? | Community features only |
| **FITR** | ? | no | no | no | yes | yes | no | no | Challenge leaderboards, habit progress bars; no streaks, points or badges |
| **PT Distinction** | no | no | no | no | no | ? | no | no | None |
| **TrainerFu** | ? | ? | ? | ? | ? | yes | ? | ? | Habit challenges, one leaderboard |
| **Kahunas** | no | ? | no | no | no | no | no | no | Habits, a login streak, a water tracker |
| **Hevy Coach** | ? | ? | no | no | ? | no | no | no | Nothing of its own; the consumer app has a weekly streak and a follower leaderboard |
| **CoachRx** | no | yes | no | no | no | no | no | no | One unmarketed streak counter |
| **FitBudd** | ? | no | no | no | ? | ? | no | no | Challenges and leaderboards, Elite tier only |
| **Exercise.com** | ? | no | no | no | yes | yes | no | no | Leaderboards and challenges |

> Everfit is the one to study: eleven leaderboard types and a camera-counted challenge show what a well-funded team thought was worth building. Notice what none of them built — a character, a world, a sense of growing something. That is the vegetable garden's opening.

*The video of a set*

## Where the gap is.

### Five let a client film a set and send it
**TrueCoach** 200 MB, about a minute of phone video, attached to the exercise, not to chat **Everfit** Video comments during a workout, each tagged to its exercise; the coach replies in the same thread **PT Distinction** Billed on every tier: clients video their technique and it goes straight to the trainer **TrainHeroic** 'Video review' is a headline coach feature **FITR** 500 MB per file, attached to a training performance; coach comments trigger a push notification

### And then it stops

On every one of the five, the trainer's reply is a comment under the clip. None has a verified way to draw on the video, step through it frame by frame, slow it down, or pin a note to the second where the knee caves in. Third-party reviews mention slow-motion on TrueCoach; TrueCoach's own pages do not.

The market leader does not have the upload at all. ABC Trainerize's ideas portal shows the request "Allow clients to upload video of their form" marked **Closed** by staff on 4 June 2020: "this can already be done in the app by sending video messages."

Six more platforms — My PT Hub, Kahunas, FitBudd, Hevy Coach, TrainerFu, CoachRx — could not be confirmed as having it. All of them move video through chat.

> **So the upload is table stakes, and the review is the product.** If a client films a set, the thing that keeps them filming is what comes back. A reply that lands on the moment, not under the clip, is a feature nobody in this market has shipped.

*How they grow*

## The trainer first, always.

On eleven of the fourteen the trainer is acquired first: the trainer pays, the client pays nothing, and the client cannot get in without an invitation or a purchase. TrueCoach's App Store listing puts it bluntly — "If you are downloading this app, you are a client of a trainer who has chosen to level up and subscribe." Hevy is the one consumer-first case with 17 million users, and it deliberately declines to sell coaches to them. Playbook and TrainHeroic are the two that transact with consumers and take a cut.

### Referral and affiliate schemes

| Platform | What they pay |
|---|---|
| ABC Trainerize | 15% recurring, no cap, via PartnerStack; open to influencers |
| Everfit | 10% of the referred coach's revenue for two years |
| My PT Hub | Up to 25% per sale; 10% monthly, 25% annual |
| TrueCoach | Up to $1,000 in credit, never cash; a hidden cash affiliate elsewhere |
| FitBudd | $50 bonus + 15% recurring for 12 months |
| Kahunas | $49 per coach after 60 days, plus a separate affiliate tier |
| CoachRx | $50 per signup, since April 2026 |
| TrainHeroic | $100 finder's fee; coaches run their own affiliate links |
| Exercise.com | 10%, net 60 |
| FITR | None — 'no formal coach referral scheme at the moment' |
| TrainerFu | None |

### Faces, partnerships, channels

**Creators front the platform** at Playbook (named creators with revenue figures, staff who are themselves influencers), Kahunas (18 coaches with Instagram handles on the homepage) and TrainHeroic (named strength coaches in its marketplace — revenue-shared, not sponsored). FITR borrows athlete credibility through its investors: Mat Fraser and HWPO on the board.

**Certification bodies** are a real channel for five: Trainerize with NASM and Precision Nutrition, TrueCoach with NASM, My PT Hub with CIMSPA and UK providers, CoachRx by selling its own certificate, TrainHeroic through NSCA pro deals.

**Gyms and events**: FITR has PureGym (370+ sites, 90-day free trial for its trainers) and HYROX. Kahunas shows a PureGym logo too.

**Search** is the universal channel, and FitBudd takes it furthest with 4,300 pages, sixty of them "alternative to X". Two platforms now optimise for AI assistants — Everfit publishes an llms.txt and FitBudd's pricing page offers "get an unbiased answer from ChatGPT".

**Money**: Garmin bought TrainHeroic (22 Jul 2026); Daxko bought Exercise.com (23 Oct 2025); Jonas bought My PT Hub (Mar 2024, after EverCommerce paid $11.7m in 2020); ABC bought Trainerize (2020). FITR raised $1.2m (2022) and £1.5m (Dec 2025) and is profitable. Playbook raised $12.3m by 2020; FitBudd $3.4m in 2022.

*Social and paid reach*

## Who has a following, and who buys one.

Read on 26 October 2026 through the ScrapeCreators API. Google figures are the library's estimate of ads shown in the last year; Meta is ads live on the day. There is no TikTok ad library.

| Platform | Instagram | TikTok | YouTube subs | Meta ads live | Google ads, est. | What the ads say |
|---|---|---|---|---|---|---|
| **ABC Trainerize** | 24,247 | 0 | 10,700 | **29** | 66 | Explore powerful Trainerize features to build and scale your fitness business |
| **TrueCoach** | 33,065 | — | — | **0** | 47 | Search text ads, paid by the Xplor holding company |
| **Everfit** | 32,628 | 10 | 4,310 | **141** | 200 | Start your 30 day free trial · Run your entire coaching business on your couch |
| **My PT Hub** | 7,511 | 27 | 12,400 | **28** | 200 | Start your 30-day free trial · Too much admin, not enough coaching? |
| **TrainHeroic** | 66,344 | 389 | 25,100 | **35** | 43 | Your coaching is premium. Your athletes' experience should be too. |
| **Playbook** | 8,073 | — | 145 | **0** | 20 | 14 of its 20 Google ads are bought by its creators, not Playbook |
| **FITR** | 11,990 | 81 | 408 | **0** | 200 | Google only, on coachwithfitr.com; nothing on Meta |
| **PT Distinction** | 3,769 | — | 2,900 | **12** | 27 | Unlock the future of fitness training · a 1-month free trial, landing on /ai-coaching |
| **TrainerFu** | 138 | — | 314 | **0** | 0 | Buys nothing on any network |
| **Kahunas** | 20,185 | — | 1,810 | **58** | 11 | 14 Day Free Trial, on all 58 ads; paid by Kahunas FZC, a UAE company |
| **Hevy Coach** | 60,085 | 25,600 | 3,410 | **0** | 0 | Buys nothing; the consumer app's following is shown |
| **CoachRx** | 15,201 | — | — | **15** | 20 | Upgrade your coaching software now · free transition: a switching ad |
| **FitBudd** | 13,689 | 20 | 1,840 | **0** | 67 | Google only; search ads since January 2024 |
| **Exercise.com** | — | 28 | 682 | **0** | 200 | Google only, heaviest buyer with FITR; text, image and video |

### Three things the ads show

**Everyone sells the same ad.** Across 318 active Meta ads from eight platforms, the offer is a free trial and less admin; not one leads with form review, video feedback or technique. TrainHeroic, which lists "video review" as a feature, mentions it only inside a generic list.

**Nobody advertises to the client.** No platform runs a consumer-facing ad for its own brand. The only paid consumer acquisition is delegated: Playbook's creators and TrainHeroic's marketplace coaches buy their own.

**The biggest following bought nothing.** Hevy runs no ads anywhere and has the largest consumer audience in the set. Everfit's size, by contrast, is explicable as bought: 141 live Meta ads and about 200 on Google.

### What the ad libraries filled in

Everfit's trial, unpublished on its site, is 30 days, stated in its own ads. Kahunas's ads are paid by Kahunas FZC, a UAE free-zone company, the first sign of where it is registered. Exercise.com and FITR, the two with almost no store or social footprint, are the heaviest Google buyers and run nothing on Meta.

> **For RepGarden:** nothing here changes the scope. The video reply is unclaimed in paid messaging as well as in product; when there is a trainer to sell to, the ad everyone else is not running is the one to run.

*Benji's current tool*

## FITR, in detail.

**What it is.** A UK platform (Fitr. Holdings Limited, incorporated 2015, Stevenage registered office), now at coachwithfitr.com under the line "where your business works out". Founder Leon Cassidy. Investors include Maven and the five-time CrossFit Games champion Mat Fraser; a £1.5m round in December 2025 came with the note that it is already profitable.

**Size.** Claims 120,000 clients and £53m processed. The stores say less: 50k+ Play installs at 3.0 stars from 74 reviews, and fewer than 25 App Store ratings across eight countries. 408 YouTube subscribers.

**Price.** £14.99 a month plus £3 per active client, or an unlimited plan; 14-day trial; annual saves 20%. Client payments run through FITR's Stripe at **5.99%**. A custom app with its own store listing is $199.99 a month.

**Getting in.** Invite-only and purchase-first: "Sign up to a program with your coach first, then download the Fitr Client app." There is no public marketplace and never was — the only way to see the client app without buying is Benji's invite.

### What it does

| Feature | FITR |
|---|---|
| Programmes | Program → training day → sets & reps → exercise; tracks within a programme; supersets of up to ten |
| Exercise videos | Preloaded library; 'hundreds' on one page, '1,000+' on another |
| Client films a set | **Yes** — up to 500 MB, attached to a performance, with coach comments and a push on reply |
| Calendar | Yes |
| Progress | Personal records over time, body metrics, charts, challenge history |
| Push | Yes |
| Messaging | 1:1, community, bulk; no voice notes, no WhatsApp |
| Habits | Lifestyle goals with reminders and a coach view of who needs a nudge |
| Nutrition | Macros set by the coach |
| Game layer | Challenge leaderboards and habit bars only — no streaks, points, badges, levels or avatars |
| Growth | No referral scheme; PureGym and HYROX partnerships; athlete investors |

> Benji's complaint on the first call was that Fitr is clunky, not that it lacks features: the set upload exists, with coach comments and a push on reply. That sets the bar for RepGarden: the same loop, made light, with the reply landing on the moment.

*Method*

## Where the numbers come from.

**What was read.** Fourteen platforms' own websites, pricing pages, help centres and blogs; their App Store and Google Play listings; Companies House and press releases for ownership and funding; the Internet Archive where a page had changed. All on 26 October 2026, by an agent working from a written brief, with every claim recorded against its source URL.

**What counts as verified.** A feature is marked present only where the platform's own pages or help centre describe it. "Not verified" means it could not be found on 26 October, not that it does not exist; for the smaller platforms the absence of a help article is itself a finding. Third-party review sites were read but are not used as evidence of a feature.

**Scale.** App Store rating counts are the US storefront on the day. Google Play gives install bands, not counts. Company figures for trainers and clients are reported as the company's own claims and are not relied on.

**Prices.** As published on the day, monthly, in the platform's own currency. Where a chart compares them, sterling is converted at $1.30. Estimated points are drawn dotted.

**Limits.** Nothing here comes from using the client apps; three are invite-only and could not be entered. Social follower counts and ad-library figures were read through the ScrapeCreators API on the same day; there is no TikTok ad library, so paid activity covers Meta, Google and LinkedIn only. A single day's reading of pricing pages will date; the platforms change their tiers often.

**Platforms checked.** ABC Trainerize, TrueCoach, Everfit, My PT Hub, TrainHeroic, Playbook, FITR, PT Distinction, TrainerFu, Kahunas, Hevy Coach, CoachRx, FitBudd, Exercise.com. Also checked and excluded: Sidekick, whose domain is parked.

**The full record.** A 1,300-line findings document with a source for every claim, and a structured data file of all fourteen platforms, in the RepGarden repository at docs/research/2026-10-26-trainer-client-apps/. This report is a reading of that record; where the two disagree, the record wins.

**Decisions this report fed.** The MVP scope, the invite-only decision, the no-payments decision and the second-phase gamification direction are recorded in docs/mvp-scope.md in the same repository, which is the one place they are kept current.

> **Prepared by** Ahmed Gadir, GadirLabs, for the RepGarden build. gadirlabs.io
