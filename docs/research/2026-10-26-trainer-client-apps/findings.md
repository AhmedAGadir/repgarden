# Trainer-to-client coaching platforms: market research

Research date: 26 October 2026. Every page cited was read on that date. Company marketing
figures are marked as such; anything that could not be confirmed from a page actually read says
"not verified".

## Summary

The market splits into three groups that look alike from outside and work differently
underneath. The largest group is trainer-side software: the coach pays, invites their own
clients, and the clients use the platform's app free — ABC Trainerize, TrueCoach, Everfit, My PT
Hub, PT Distinction, FITR, Hevy Coach, Kahunas, FitBudd, TrainerFu and CoachRx all work this
way, covering every price point from $9 to $700 a month. The second group sells distribution
rather than software: TrainHeroic and Playbook acquire consumers directly and take a cut when a
coach sells to them (30% on a TrainHeroic-sourced sale, 20% of everything on Playbook). The
third is gym and studio management software that includes coaching, where Exercise.com now sits
after Daxko bought it. Consolidation has been the story of the last two years: Garmin bought
TrainHeroic and TrainingPeaks on 22 July 2026, Daxko bought Exercise.com on 23 October 2025, My
PT Hub passed from EverCommerce to PYXiS Software Group (Jonas Software / Constellation) on
13 March 2024, ABC Fitness owns Trainerize, and Xplor owns TrueCoach. PT Distinction, FITR,
Hevy, Kahunas, FitBudd and CoachRx are the notable independents left.

Three findings bear most directly on RepGarden's scope decisions:

1. **Client video of working sets is not universal, and nobody has solved reviewing it.** It is
   a verified, named feature on TrueCoach (200MB per upload, attached to the exercise), Everfit
   (video comments tagged per exercise), PT Distinction (billed on every tier), TrainHeroic
   ("Video review") and FITR (500MB per file, attached to a training performance). **ABC
   Trainerize, the largest platform in the market, does not have it** — its own staff closed the
   feature request on 4 June 2020 saying video messages sufficed. My PT Hub, Kahunas, FitBudd,
   Hevy Coach and TrainerFu could not be verified as having it at all; all of them move video
   through chat. And on **no platform** could annotation, drawing or frame-by-frame review be
   verified. The upload is table stakes among strength-focused tools; the review experience is an
   open gap across the whole category.

2. **Nobody bills a trainer's own clients through Apple in-app purchase.** Every trainer-side
   platform collects on the web, almost always Stripe (Everfit, TrueCoach, Trainerize, My PT Hub,
   FITR, CoachRx, Kahunas via Stripe Connect) or the trainer's own PayPal/Stripe (PT
   Distinction). Apple in-app purchase appears in only three places: TrainHeroic's own Athlete
   Pro ($4.99/month), Playbook's consumer subscription ($14.99/month), and **FitBudd's Super Pro
   tier**, where Apple becomes merchant of record and pays the coach directly — quietly importing
   Apple's commission into the coach's margin, at a rate FitBudd never states. Platform rakes on
   top of the processor vary sharply: FITR 5.99%, TrueCoach a flat 5%, Everfit 3.15% + $0.30 (US
   domestic, Stripe included) plus $9/month. Hevy Coach and Kahunas take nothing; Hevy Coach has
   no client billing at all.

3. **Gamification is thin almost everywhere, so it is a differentiator rather than hygiene.**
   Only three platforms have a genuine layer: **Everfit** (eleven leaderboard types, an AI
   push-up challenge that counts reps by camera, streak insights — though challenges sit behind
   the paid Autoflow add-on), **ABC Trainerize** (streaks, badges, milestones, leaderboard *and*
   threshold challenges with points, groups, WOD, high-fives), and **TrainHeroic**
   (coach-programmed team leaderboards on any exercise/circuit/superset, a global StackUp
   percentile, weekly streaks, a one-million-pound lifting club). My PT Hub, PT Distinction,
   TrueCoach, CoachRx, Hevy Coach, Kahunas, Playbook and TrainerFu have essentially nothing.
   **No platform in the comparison has verified points, levels or avatars.** FITR sits in
   between: challenge leaderboards and habit progress bars, but no streaks, points or badges.

---

## 1. Who the top platforms are, ranked by evidence of scale

Ranking uses what can be observed — App Store rating counts in the GB and US storefronts (public
iTunes Search/Lookup API), Google Play install bands and review counts, Similarweb rank where
visible. Self-reported trainer counts are recorded but not used to set the order, because
several do not survive comparison with store data.

**1. ABC Trainerize** — clear leader on every observable measure. Client app 68,999 US and
15,651 GB ratings at 4.90/4.89; Play (`com.trainerize.Trainerize`) 1m+ installs, 4.7, 10,865
reviews; Similarweb 2.1m visits/3 months, global rank #16,538 (September 2026). Claims "400k+
personal trainers and coaches", "45k+ health and fitness businesses", "1.6M+ clients", and "over
5 million workouts, 1.6 million habits, and 23 million meals" monthly. Operating company TSR Gym
Technik Ltd, founded in Vancouver; **acquired by ABC Financial/ABC Fitness, announced
15 September 2020** (Thoma Bravo press release). Worth noting: the published trainer count has
been frozen at "400,000+" since the November 2022 NASM announcement.

**2. TrueCoach** — 35,746 US and 16,346 GB ratings at 4.86/4.85; Play (`co.truecoach.client`)
100k+ installs, 4.8, 5,798 reviews. Claims "16K+ Total Coaches", "250K+ Total Clients", "50M+
Workouts delivered" — the most plausible self-report in the set, being the only one proportionate
to its store footprint. Similarweb 815,900 visits/3 months with global rank **falling** from
#50,809 to #53,700. Owned by **Xplor**, confirmed on TrueCoach's own about page. Note the
published coach count has gone *down*: aggregators still repeat "more than 20,000" while the
company now says 16,000+.

**3. Everfit** — client app 2,710 US and 1,166 GB ratings at 4.72/4.76; Play (`com.everfit`)
100k+ installs, 4.4, 990 reviews; coach app 10k+. Similarweb ~1.2m visits/3 months, rank
#26,917, traffic down 3.57% month on month. The homepage claim of **"Trusted by over 380,000
coaches" should be treated as unsubstantiated marketing** — it is nearly level with Trainerize on
a fraction of the traffic and a twentieth of the ratings, and Everfit's own older copy says "over
200,000 … in 190+ countries". Ownership, HQ, founders and founding year are all unstated on the
site and **not verified**; App Store developer is Everfit Technologies Inc. A $1.1m seed dated
24 October 2019 appears on PitchBook. **Name-collision warning:** the $7m June 2022 seed led by
645 Ventures belongs to "EverFit Inc." trading as *kickoff*, a different company.

**4. My PT Hub** — 1,860 US and 1,733 GB ratings, but at a notably lower 4.14; Play
(`net.mypthub.kilo`, developer Fitii Ltd) 100k+ installs, 4.6, 2,315 reviews. Claims "200,000+
fitness coaches globally", "170+ Countries", "3m+ Clients onboarded" — though its own customers
page says "2 million+ clients", contradicting the homepage. Ownership chain: UK company Fitii Ltd
(Burgess Hill, West Sussex), founded 2015 by Phil Carr; **acquired by EverCommerce 18 November
2020 for $11.7m** (announced 3 December 2020, citing "over 83,000 trainers and their 1.3 million
clients"); then **acquired by PYXiS Software Group, a division of Jonas Software, ultimately
Constellation Software Inc., announced 13 March 2024**, in a bundle with ClubOS, ASF and ClubWise
(~10,000 customer locations, "less than 4% of EverCommerce's 2023 revenue"). **No "Kilo"
ownership link could be found despite the Play package name — not verified.**

**5. TrainHeroic** — 1,836 US and 113 GB ratings at 4.26/4.29; Play
(`com.TrainHeroic.TrainHeroic`) 500k+ installs, 688 reviews. **Acquired by Garmin on 22 July
2026** alongside TrainingPeaks, from Peaksware Holdings; terms not released; ~120 staff moved;
run as a separate business unit, staying "brand-agnostic for wearables and smart trainers"; Dirk
Friel stays as strategic adviser, Lee Gerakos remains. **The site had not been updated to reflect
this as of 26 October 2026** — the footer still reads "© 2026 TrainHeroic, Inc." and names
Denver, Colorado. Its own two pages disagree by 2× on scale: homepage "500000+ Athletes / 10000+
COACHES / 96 COUNTRIES" versus coach page "20k+ Coaches / 650k+ athletes / 96 countries".

**6. Playbook** — 37,040 US and 1,427 GB ratings at 4.92/4.88; Play
(`io.playbookapp.android`) 500k+ installs, 10,491 reviews. A different category: a
creator-subscription marketplace for fitness influencers, not a 1:1 coaching tool. Claims "$233M+
Paid to creators" since 2016, "2,500+ Earning creators", "300k+ Active subscribers", "80M+
workouts completed", "56,000+ workouts from 500+ instructors". Playbook Technologies Inc, founded
2016, CEO Jeff Krahel, "41 people across 30 cities globally"; **$9.3m Series A announced
14 October 2020** (E.ventures, Michael Ovitz, Abstract, Algae Ventures, Porsche Ventures, FJ
Labs), total $12.3m; no round since found.

**7. FITR** — the platform Benji currently uses. Play (`com.fitr_training.client`) 50k+ installs
but only 3.0 from 74 reviews; coach app 1k+. App Store footprint is negligible: **fewer than 25
ratings in total across both apps across the GB, US, AU, IE, CA, NZ, DE and SE storefronts.**
Both iOS apps shipped v2.0.2 on 7 October 2026 and the company has just rebranded its domain, so
a ratings reset is plausible but **not verified**. Claims "34,000+ programs run daily", "£53
million+ income generated through platform", "120,000+ clients". Full detail below.

**8. PT Distinction** — 121 US and 63 GB ratings at 4.16/4.08 for its own app, plus a shared
container app ("Online Personal Training", BH App Development Limited) with 471 US and 383 GB
ratings. **No current Google Play listing could be found** under any package id tried. Claims
"Used by over 60,000 training businesses" — awkward beside 121 US ratings, though client traffic
partly runs through trainers' branded apps and the web portal. PT Distinction Ltd, UK company
8413544, Pewsham, Wiltshire; founded 2010 by brothers Tim and Adam Saye; **independent, no
funding or acquisition ever announced**.

**9. TrainerFu** — 3,209 US and 302 GB ratings at 4.84/4.74, more iOS ratings than My PT Hub, but
barely developed: **iOS last updated 19 May 2025, Android 26 October 2025**, and marketing-site
`lastmod` dates stall in March–April 2024. Play 50k+ installs, 4.8, 692 reviews. Founded by
Manobal Jain; no funding, no team page, no published trainer count. An actively monetised but
near-static one-person operation with a blog live to 13 July 2026.

**10. Kahunas** — Play (`com.cofox.kahunas.Kahunas`) 100k+ installs but **2.5 stars from 257
reviews**, the worst rating in the set; iOS 77 US and 142 GB ratings at ~3.2, and the App Store
seller is an individual, **"Mark Covey-Fox"**, not a company. Founder Mark Fox. Claims "Trusted
by 750,000+ users" and "Over 14,000 coaches". **Stripe's own customer page (2023) gives harder
numbers**: "Over 6,000 trainers with 150,000 global customers", "$4 million in annual revenue",
"900% growth in 2023", "$1.2 million in monthly client payments processed", churn cut 16%→7% —
note the gap against today's claims. HQ not published anywhere; funding none found.

**11. Hevy Coach** — tiny as a coaching platform (Play 10k+, 3.7, 70 reviews; iOS 4 US and 6 GB
ratings) but attached to the largest consumer workout logger here. **Consumer Hevy: 5m+ Play
installs at 4.9 from ~255,000–283,000 reviews, and 100,098 US App Store ratings at 4.92**; the
company claims "17+ million users". Crucially, **the coach's clients use the ordinary consumer
Hevy app** and get Hevy Pro free. Hevy Studios S.L., Barcelona; founders Guillem Ros (CEO) and
Desmond McNamee (CTO); ~25 staff; launched October 2024; funding not verified. **No trainer count
is published.**

**12. CoachRx** — Play 10k+; iOS 81 US and 14 GB ratings at a poor 3.63/4.07. Claims "Trusted by
8,000+ coaches", hard to square with 81 US ratings. Owned by **OPEX Fitness** (App Store seller
OPEX Fitness LLC, Play developer OPEX Management Corporation), founder James Fitzgerald, CEO Carl
Hardwick, Scottsdale, Arizona, launched 2022. James Fitzgerald is not named anywhere on
coachrx.app itself.

**13. FitBudd** — smallest first-party footprint of the live products: Play
(`com.fitbudd.app`) 5k+ installs, coach app 1k+; iOS client app 6–109 US ratings depending on
read, coach app zero. But that understates it, because clients install the *trainer's* app: **the
FitBudd Play developer page lists 20 distinct apps, nearly all trainer-branded**. FitBudd, Inc.,
founded 2021 by Saumya Mittal (CEO), Pranav Chaturvedi and Naman Singhal (IIT Delhi); **$3.4m
seed announced 12 October 2022**, led by Accel India with Beenext, Sequoia Capital India and
Waveform Ventures, when it claimed "over 600 coaches across 20 countries". Now claims "10,000+ …
in 80+ countries". US entity, India engineering base; no address published and /about-us 404s.

**14. Exercise.com** — no meaningful consumer scale, by design. Its generic iOS app is now listed
as **"Daxko Exercise"** (seller Exercise.com LLC, copyright "© 2026 Daxko Exercise") with 22 US
and 4 GB ratings, last version 5.32.0 dated 14 October 2024. **Acquired by Daxko, announced
23 October 2025**, terms undisclosed, Vista Point Advisors as Exercise.com's exclusive adviser;
named in the release are Jeff VanDixhorn (CEO, Daxko), Joel Ohman (Founder and CEO, Exercise.com
— not named on Exercise.com's own about page) and Aldor H. Delp (President of Boutique Fitness).
Quote-only, demo-gated, sold to gyms and studios with per-customer branded apps. HQ now reads as
Daxko's Birmingham, Alabama address.

**15. Sidekick — no such product.** This needs stating plainly. `sidekick.fit` returns HTTP 302
to a listing on the Atom domain marketplace, and its nameservers are ns1.atom.com /
ns2.atom.com — parked and for sale. `trainwithsidekick.com` has no DNS A or NS records at all.
`sidekick.fitness` resolves but serves an empty client-rendered shell built with Create React App
v3 (~2019–2020 vintage), with no marketing site, pricing or about page. "Sidekick Fitness" on
Google Play is `com.trainerize.sidekickfitness` — a Trainerize white-label app for a gym of that
name. "Sidekick Platform" is Sidekick Health, digital therapeutics. `sidekicktraining.com` is
corporate workforce training. **No Sidekick entry belongs in a competitive comparison.** If the
brief meant "a small PT platform that died", **QuickCoach** is the real example — a genuine PT
coaching platform that has shut down and is being actively poached by competitors.

### White-label app volume, from bundle-id evidence

Bundle prefixes give a reliable read on who really publishes per-trainer listings. At least
**35 distinct `com.trainerize.*` Play listings** surfaced in three searches alone
(`com.trainerize.mygym`, `.fitribe`, `.burbankfitnessclub`, `.royalfit2`, `.myptstudio`,
`.peakfitness`, `.sidekickfitness`), so Trainerize publishes trainer-branded apps at volume.
**FitBudd's 20-app developer page** is the second-clearest case, and it was verified end to end:
**BossFitAmy** (`com.bossfitamy.app`) is published on iOS with **developer and seller "Amy
Hollings"** — the trainer's own Apple account — while the same bundle on Play is published by
**"FitBudd"**. So on iOS the trainer's store identity is genuinely theirs; on Android it is not.
Kahunas does the same (`com.kahunas.unlmtdcoaching` → "UNLMTD PERFORMANCE", developer "Kahunas",
**seller "The Trustee for THE SARANDIS TRUST"**). `com.trainerfu.*` per-trainer apps exist in
small numbers. PT Distinction instead routes clients through one shared container app,
`com.bhappdevelopment.containerapp`, consistent with icon-and-in-app branding rather than
separate listings — inference from the store, not a company statement, so **not verified**.

---

## 2. Which of them are gamified, and how

**Everfit — the strongest layer in the market, and genuinely built.** Leaderboards are documented
with **eleven types in four groups**: weight loss (absolute, percentage), strength (highest
volume lifted, cumulative volume lifted, total reps), activity (total steps, tasks completed,
workouts completed, push-up challenge), with "Other leaderboard types are in development".
Coaches set ranking criteria, rules and dates, and leaderboards render inside Community Forums,
so competitive and social layers share one surface. The **AI push-up challenge** counts reps in
real time on-device and syncs to the leaderboard — the only computer-vision game mechanic found
anywhere here. Streaks are real: habit Insights show "Current streak, Best streak, Daily average,
Completed days/weeks, and percentage", resetting on a setback. **Important caveat: challenges and
leaderboards sit behind the paid Autoflow add-on ($24–29/month), not the base plan.** Badges
appear in blog copy but **not verified** in the help centre. Points, levels, avatars: no evidence.

**ABC Trainerize — moderate and real.** Features page lists "Streaks and badges" under Habits;
"Groups", "Challenges", "Workout of the Day (WOD)" under Community; "Badges and milestones" and
"High-five and reactions in messages" under Motivation. The Challenges help article (403 to
direct fetch, read via search rendering) describes two types — **leaderboard** challenges with
three top winners, and **threshold** challenges where everyone passing a target wins — with
clients competing to "earn points by working out, achieving personal bests, completing habits"
across six trackable activities. So streaks, badges, challenges, leaderboards and points are all
present. Levels, avatars: not verified. A habit *score* as a single number: not verified.

**TrainHeroic — real, but narrower than its reputation.** Two kinds of leaderboard:
coach-programmed team leaderboards that attach to **any exercise, circuit or superset** (toggled
by a trophy icon, scored on Reps, Weight or Time, optional for the athlete to log, with "virtual
fist bumps"), and global **StackUp** leaderboards for Athlete Pro subscribers. Streaks verified
("Find consistency & Motivation with streaks" — consecutive weeks). One achievement tier
verified: "Join the TrainHeroic Millionaire's club by lifting over 1M lbs." **To be precise on
the brief: there is no product called a "strength score" and no levels system on any TrainHeroic
page read.** StackUp is a body-weight-scaled percentile ("what percent of people you perform
better than", a nonlinear formula "similar in concept to a Wilks score"), and that formula detail
comes from Cloudflare-blocked support docs, so **not directly verified**. Athletes can opt out.
**StackUp is paywalled behind Athlete Pro at $4.99/month.** Readiness Insights is a five-question
daily survey attributed to the Air Force Research Lab — a wellness score, not a game mechanic.
Points, levels, avatars, named challenges: not verified.

**FITR — partial.** Challenge leaderboards are real: Challenges are repeatable, "Every entry is
saved", and coaches can "Tag clients in Leaderboard entries or Community Chats". Habit tracking
exists with progress bars and completion counts ("completed 6 of 8 tasks") and a coach view of
"who's on track and who needs a nudge". But the habits page contains **no streaks, completion
scores, points or badges**, and none were found elsewhere. No levels, no avatars.

**Hevy — two real mechanics, but inherited from the consumer app, not built for coaching.** Hevy
Coach itself has **no game layer whatsoever** — nothing on its features index, product, pricing
or feature pages. The consumer Hevy app has a genuine **weekly streak** ("your active streak …
the number of consecutive weeks you've logged at least one session", with forgiving backfill that
extends rather than resets) and a **leaderboard** covering heaviest weight on **38 movements**,
but only among people you follow. Plus live PR notifications, monthly report, Year in Review. No
badges, points, levels, avatars, challenges or habit tracking anywhere in the Hevy feature index.

**Exercise.com — two mechanics.** "Leaderboards" and "On-Demand Challenges" are both named
platform features, alongside "Habit Tracking", Progress Photos and Rep Max Progressions. Streaks,
badges, points, levels, avatars: no evidence.

**Kahunas — thin engagement layer, not a game layer.** "Custom Habit Tracking" is a named feature
from Essentials up. A **login streak** (not a training streak) and a water tracker shipped in
v2.6.0 on 21 December 2024 per App Store release notes. "Health Score A.I" exists as a named
Growth-tier feature but is entirely undocumented — what it computes is **not verified**.
**Badges, points, leaderboards, challenges, levels, avatars: absent — none of those words appears
on kahunas.io.**

**FitBudd — one real layer, paywalled behind quote-only pricing.** "Challenges & Leaderboard" is
marked "*Exclusive For Elite Plan*": trainers create workout challenges and the leaderboard ranks
on "Total Workouts Completed", "Total Duration" or "Total Calories Burned Per Day", updating "in
real time as soon as there is any new log". Two documented challenge types: body transformation
and activity. **Points, badges, levels, avatars, streaks, habit scores: absent** — the 41-article
client-app help collection contains no article on any of them. Water intake and daily activity
targets are the only habit-adjacent features; there is no habit tracker.

**TrueCoach — almost nothing.** Badges genuinely exist: "Clients receive personal badges and are
notified when they hit certain workout milestones." Habit tracking exists. Streaks, points,
leaderboards, challenges, levels, avatars: **not verified**, absent from features page, pricing
page and help centre. Notably the official client-experience help article does not mention badges
at all, suggesting the layer is very light. TrueCoach's blog publishes on gamification, challenges
and leaderboards — **as coaching tactics for the trainer to run manually, not as product
features.**

**TrainerFu — two mechanics, on one page.** Challenges verified ("Run habit based challenges to
increase adherence, build community, and make your training more fun"); a leaderboard exists but
only on the habit-coaching page ("Award prizes in the end to spark that friendly competition").
The homepage mentions "streaks broken" as a *coach-facing alert*, not a client-facing counter, so
streaks are **not verified** as a client mechanic. Badges, points, levels, avatars: no evidence.

**CoachRx — one mechanic, unmarketed.** The shipped iOS app has a **streak** counting consecutive
completed workouts, visible in the listing and its reviews (including a complaint that it credits
the logging date rather than the completion date). **Nothing about it appears on the website.**
Everything else absent. Positioning is explicitly anti-gamification: "depth over volume",
"coaching as a relationship, not a transaction".

**My PT Hub — none.** The only game-layer language is "Personal best records — **Gamify
workouts** and motivate clients with personal best records", i.e. PB tracking labelled as
gamification. Communities is a private social feed (posts, images, videos, GIFs, comments,
reactions, pinned announcements, @tag-all). "Challenge groups" is described only as a naming
convention for a community space. Leaderboards, badges, points, levels, avatars, streaks, habit
scores: all **not verified**.

**PT Distinction — none at all.** Features and pricing pages read in full: no leaderboards,
badges, points, levels, avatars or streaks. Habit tracking is a flagship but carries no score.
Challenges exist as a **business-development product**, not a mechanic: "Online challenges are
great to build trust, bring in new clients and grow your business … **we'll cover the cost of the
challenge** … we'll pay for their accounts during the challenge."

**Playbook — none in the XP sense.** Community features are real (threaded replies, emoji
reactions, likes, comments, feed filters) and a post-workout star rating exists. "Challenges"
appears with two meanings: member-facing challenges with prize structures in the App Store
listing, and "Quarterly Challenges" which are business-growth challenges for *creators*. Streaks,
badges, points, leaderboards, levels, avatars: no evidence.

### Plain summary

Genuine game layer: **Everfit**, **ABC Trainerize**, **TrainHeroic**. Isolated mechanics:
**Exercise.com** (leaderboards, challenges), **FITR** (challenge leaderboards, habit progress),
**FitBudd** (Elite-only challenges and leaderboards), **Hevy** (consumer streak and follower
leaderboard), **Kahunas** (habits, login streak), **CoachRx** (unmarketed streak), **TrainerFu**
(habit leaderboard), **TrueCoach** (milestone badges). **My PT Hub, PT Distinction and Playbook
are plain tools with no game layer at all.** Nowhere are points, levels or avatars verified.

---

## 3. Core feature sets and what they charge

### Who pays

Every trainer-side platform charges the trainer and gives the client the app free, several saying
so explicitly. My PT Hub: "**Do my clients have to pay anything? No, absolutely not!**"
TrainerFu: "Trainerfu is completely FREE for clients to use, and will always be." Hevy Coach:
"No, your clients will not pay anything … their clients will get coached through Hevy completely
for free", plus free Hevy Pro. Trainerize: "There is no additional cost for your members/clients
to use the app other than what you decide to charge them." Only **TrainHeroic** and **Playbook**
earn from the end user.

### Prices

| Platform | Model | Prices as published | Free trial |
|---|---|---|---|
| ABC Trainerize | Trainer subscription, per client band | Basic free (1); Grow $9/mo (2); Pro from $23/mo (slider 5–200, higher steps **not verified**); Studio Plus $248/mo (500), custom at 1,000+. Studio FAQ gives a conflicting $250–350/mo or $2,700–3,780/yr. Add-ons: Advanced Nutrition $20–45/mo, Business $25/mo, Video Coaching $10/mo, Stripe Payments $10/mo, Custom Branded App $169 one-time. Annual saves 10% | **30 days**, unlimited clients, no card |
| TrueCoach | Trainer subscription, per client band | Starter $26.34/mo (5); Standard $57.99/mo (20); Pro $136.99/mo (50); custom above 250. **These are almost certainly annual-equivalent monthly figures** — the page carries a Monthly/Annual toggle with "1 MONTH FREE"/"2 MONTHS FREE", and $136.99 ≈ $164.98 × 10/12. Monthly list prices **not verified** | 14 days, no card |
| Everfit | Trainer subscription, per client band | Starter **forever free** (5); Pro $16–242/mo annual, $19–290/mo monthly (5–300); Studio $88–358/mo annual, $105–430/mo monthly (50–500); Enterprise custom (500+). Add-ons: Autoflow $24–29/mo, On-Demand Collections $21–25/mo, Payments & Packages $8–9/mo, Meal Plans $33–39/mo, Advanced Custom Branding $75 one-time. Annual saves 16% | Length **not verified**; no card |
| My PT Hub | Trainer subscription, unlimited clients above entry | Starter £20/mo (3); Premium £59/mo (unlimited); Ultimate £199/mo (all add-ons). Annual paid monthly £18/£52/£179. Add-ons: custom branded app £95 one-time, **white-label app with store listings £125/mo**, extra trainers £10/mo, Check-Ins AI £9/mo, Zapier £15/mo | 30 days, no card |
| PT Distinction | Trainer subscription + marginal per-client | Basic $19.90/mo (3, $6.00 extra each); Pro $59.90/mo (25, $2.40); Master $89.90/mo (50, $1.60). Extra clients free for 1 month. **Every feature on every plan** | 1 month |
| TrainHeroic | Per athlete band + marketplace cut + direct-to-athlete | $9.99 (1), $17.99 (5), $34.99 (15), $44.99 (25), $59.99 (35), $74.99 (50), $99.99 (100), $159.99 (250), $199.99 (500), $299.99 (750), $399.99 (1,000), contact above; assistant coaches $9.99/mo. **Athlete Pro $4.99/mo or $29.99/yr via Apple IAP.** Marketplace: **$1/client/month** on self-sourced sales, **70/30 split** on TrainHeroic-sourced "Matches", $1/transaction on affiliate-link sales (**not verified**), **2.9% + $0.30 bank fee on all sales**, PayPal payout on the 15th. **No 1:1 client billing at all** — outsourced to Pike13 | 14 days, no card |
| FITR | Trainer subscription, per active client | £14.99/mo at entry and £3.00 per client on the slider, plus an unlimited option; GBP/USD/EUR; annual saves 20%; prices include sales tax. **Business Automation fee 5.99%**, Stripe fees passed through with no markup. Custom App $199.99/mo or $119.92/mo annually | 14 days, no card |
| Hevy Coach | Trainer subscription, per client band | $25 (1–10), $50 (11–25), $90 (26–50), $160 (51–100), $250 (101–200), $360 (201–300), $460 (301–400), $550 (401–500), $700 (501–1,000). Coach subscription via **Paddle**. No client billing, so no transaction fees | **30 days**, no card |
| Kahunas | Trainer subscription | Essentials $35/mo ($315/yr, 25 clients); Growth $69/mo ($621/yr, 50); Ultimate $99/mo ($900/yr, unlimited). "We do not charge your clients directly or take any commission" | 14 days, plus a founder's personal 3-month same-day refund promise |
| FitBudd | Trainer subscription + marginal per-client | Starter $15/mo ($159/yr, 2 clients, +$4 each); Pro $79/mo ($799/yr, 20, +$2 each, no setup fee); Super Pro $149/mo ($1,499/yr) **+ $75 one-time setup**; Elite Studio and Elite Creator custom **+ $100 setup**. Add-ons: Appointments $50/mo, Team $50/mo, Explore $50/mo, Smart Flow $20/mo + $1/client over 20. White-label also needs a **D-U-N-S number, $99 Apple and $25 Google** | **30 days**, no card |
| TrainerFu | Trainer subscription, per client band | $29 (10), $49 (20), $79 (40), $99 (60), $119 (80), $139 (100), $189 (150), $250 (250), custom above. Branded app **+$75/mo**. Annual gives 2 months free. Figures extracted from the site's own `main.js`, since the page renders prices client-side | 14 days |
| CoachRx | Trainer subscription, per client band | $29/mo (1–5), $79/mo (6–50), **$199/mo (51–150)** — though the homepage FAQ still says $149/mo for that tier; annual $25/$67/$169; enterprise above 150 | 14 days, free migration |
| Playbook | Revenue share | No subscription, no setup fee. **Creator keeps 80%, Playbook takes 20% of Net Revenue** — defined as gross less payment processing, **app store fees**, refunds, chargebacks and taxes, so the creator absorbs Apple's cut *before* the split. Consumer pays $14.99/mo or $99.99/yr | 7 days for the consumer |
| Exercise.com | Quote only | **No prices published anywhere**; every CTA is "Book Demo"; **no free trial found**. Directories put entry around $239/mo — **not verified** | None |

### White-label: who really gets their own store listing

This separates sharply, and it matters because a separate listing pushes an Apple developer
account and Apple's legal-entity requirements onto the trainer.

**Genuine separate listings on both stores:** My PT Hub's white-label add-on at **£125/month**,
which spells out the requirements in its own comparison table — App Store Developer Account,
**DUNS number**, independent website and independent privacy policy hosted on it. FITR's Custom
App at **$199.99/month**: "A Custom App is your own standalone app on the App Store and Google
Play. Brand Kit adds your branding inside the Fitr app", ~4 weeks from kickoff once developer
accounts exist. **Trainerize Studio** (from $248/month, "Your own Apple Store listing", custom
iOS app name, 8–12 weeks setup, registered legal entity required). **Everfit Enterprise**, where
the help centre is unusually candid: "Android and Apple only allow for the app icon to be
switchable. If you are interested in having your own app listings, we have a white-label solution
available for our Enterprise plan, which requires a minimum of the Studio plan with 500 clients."
**Kahunas Ultimate** at $99/month: "In the Google Play & Apple App Store you have your own page
with your logo, name, description, it's 100% yours", live in under 30 days, coach supplies the $99
Apple account. **FitBudd Super Pro** at $149/month + $75 + $99 + $25, verified working end to end
via BossFitAmy. **TrainerFu** at $75/month, promised in "less than 3 weeks". **Exercise.com**
sells "Custom-Branded Apps" as a headline platform feature, price undisclosed.

**In-app branding only, despite the marketing:** TrueCoach — "Customize the TrueCoach app with
your logo and any color", Standard and Pro, with **no separate listing found at any tier**; the
client app listing says "A TrueCoach account is required". Trainerize **Pro** at $169 one-time is
a hybrid — a real Google Play listing but only an icon and theme inside the "ABC Trainerize shared
Apple Store listing". Everfit's Advanced Custom Branding at $75 one-time is icon, splash screen,
workout backgrounds, colour themes and welcome video. My PT Hub's £95 custom branded app likewise
has **no store listing**.

**None by design:** **Hevy Coach** — no white-label at any price, because the client uses the
consumer Hevy app and gets Pro free; this is the clearest structural difference in the set.
**TrainHeroic** — strongest claim is "Make TrainHeroic your own by adding your logo, custom
exercise demos, and personalized coaching content"; deliberate, since the shared app is what makes
the marketplace and global leaderboards work. **CoachRx** — none. **Playbook** — structurally
cannot, since its model depends on one consumer app where creators are discoverable together.

**Not verified:** PT Distinction's "custom-branded iOS and Android apps", free from $59.90. Its
copy emphasises the app icon and never mentions a store listing, developer account or DUNS
number, unlike My PT Hub which is explicit about both. A single App Store listing with 121 US
ratings plus a shared container app is consistent with icon branding, but the company does not
say either way.

### Client video upload of working sets

| Platform | Verified? | Detail |
|---|---|---|
| TrueCoach | **Yes** | "TrueCoach has a video limit size of 200mb which is normally about a :60 video taken on a smart phone", with guidance to trim or split sets across uploads and stay in the app while uploading. Media attaches to the exercise, not just chat. Voice Notes can be attached to workouts or logs. Slow-motion/annotation appears only in third-party reviews — **not verified** |
| Everfit | **Yes** | Clients comment during a workout in three types — Message, Image, Video, explicitly "a form check video to ensure they are doing their workout correctly". On save, comments collect in a unified per-workout thread, **each tagged to its exercise**; the coach replies in the same thread with video, image or GIF. Extended to the web app in 2026. No annotation |
| PT Distinction | **Yes** | A billed feature line on **every tier**: "Our apps allow clients to video their technique while training which goes straight to you for review". Annotation **not verified** |
| TrainHeroic | **Yes** | "Video review — Review athlete videos and deliver fast, actionable feedback" is a headline coach feature, alongside "technique videos". Annotation **not verified** |
| FITR | **Yes** | "Photos and videos up to **500 MB** per file", attachable to training performances ("ideal for form checks and workout videos"), Personal Records, Challenges and Body Metrics. "You can leave comments on any media your clients share - they will receive a push notification when you respond" |
| CoachRx | Coach→client only | Loom video messaging and screen share for the coach; **client upload of sets not verified** |
| ABC Trainerize | **No** | The request "Allow clients to upload video of their form" is marked **Closed** on ABC's own ideas portal, 5 votes, staff response from Trevor dated **4 June 2020**: "Closing out this idea as this can already be done in the app by sending video messages" |
| Hevy | Partial, not a coaching feature | A user may attach "three images or two images and one video before saving the session" — to the **session**, not a set, visible to followers or the public, not routed to a coach. Coach chat does exchange image and video files and is pitched to "monitor technique", but no annotation |
| My PT Hub | Not verified | Trainers upload demo videos (300MB, or YouTube/Vimeo); clients post photos and videos into the **Community feed**; check-ins auto-sync progress photos and measurements. No form-check submission or coach review found |
| Kahunas | Not verified | Messaging carries voice notes; Progress Overlay compares client *photos* |
| FitBudd | Not verified | Chat carries video messages with duration and size limits; check-ins carry progress photos. No form-check or annotation article exists in a 41-article client-app help collection |
| TrainerFu, Playbook, Exercise.com | Not verified | TrainerFu's only verified client upload is meal photos |

### Programme to workout to exercise structure

- **TrueCoach** is flattest: Program > Weeks > Workouts > Exercises. "A program is a series of
  workouts that you create and 'save-for-later'"; weeks can be added at any time.
- **ABC Trainerize** adds a phase: Program > **Training Phase** > Workout > Exercise, with two
  programme types ("Phased Training Programs", "On-Demand Programs"), plus Master Programs and
  Master Workouts as reusable templates.
- **Everfit** adds a level *inside* the workout: Program > weeks > Workout > **Section** >
  Exercise > Set, where sections are typed (regular, interval, AMRAP, timed) and an Arrangement
  panel reorders exercises and sections. The most expressive here for interval and conditioning
  work; the only one that models supersets and circuits as first-class objects.
- **TrainHeroic** is the most explicit about reuse: Programs > **Sessions** > Circuits/Exercises,
  with three separately reusable libraries — "TrainHeroic's **Exercise, Prescription, and
  Program** libraries are 100% reusable, shareable with your staff, and fully customizable." A
  **Prescription** as a first-class object (sets, reps and load schemes including %1RM) is
  distinctive and the single idea most worth borrowing. Athletes group into **Teams**.
- **FITR**: Program > **Training Day** > Sets & Reps table > Exercises, with "training blocks"
  combined into weeks and **Tracks** as variants inside one programme. Supersets link up to ten
  exercises; PR library of 2,500+ options.
- **FitBudd**: Workout Schedule > Workout (either "Structured Workout" or "Follow-Along Video
  Workout") > **Segment** (superset, triset, warm-up, circuit, AMRAP, Tabata, EMOM) > Exercise >
  reps or duration. "Segment" is its distinctive middle layer; alternate exercises and alternate
  workouts can be set per exercise and per schedule.
- **My PT Hub**: Workouts (sessions) > Programs (multi-week, automated progression) > Exercises,
  plus supersets, giant sets and circuits, tracking "1RM, Tempo, Rep range & more".
- **PT Distinction**: Program Builder > training programs > multiple workouts ("Build multiple
  workouts on one page") > exercises, with circuits, supersets, giant sets and 6-12-25.
  Scheduling is item-level, not block-level: "Every item has the ability to be scheduled",
  specific day or complex repeating, plus a workout progressions calculator.
- **Hevy Coach**: Program > Workout (also "routine") > Exercise > Set, assigned via "Assign
  Program" with a 1–52 week duration and start date. No periodisation vocabulary.
- **CoachRx** is deepest on periodisation: macro, micro and meso cycle planning, a unified
  programme calendar with an AI assistant (RxBot), 60+ OPEX-designed templates.
- **Kahunas**: "workout plans" with straight sets, supersets and circuits, plus nutrition and
  supplement plans. A named hierarchy is **not set out on the site — not verified**.

### Exercise video libraries

Several companies publish contradictory numbers for their own libraries, so treat all as
approximate. **Conflicting within one company:** TrueCoach says "3,500+ professionally recorded
exercise demonstrations" on one page and "3,000+" on two others; Everfit's pages say 3,500,
2,500, 1,000+ and "improved videos on 500+"; TrainHeroic says "over 1200 movements" (coach FAQ),
"1,300+ exercises and template programs" (/create/) and "1,500+ movements" (/athlete/); PT
Distinction says "over 1200" on its blog (Tim Saye, 14 February 2024) and "thousands" on its
features page; FITR says "hundreds" on the programming page and "1,000+ movement videos" on the
communication page. **Clearer single figures:** FitBudd "4000+ Dynamic Exercises", My PT Hub
"8,000+ HD", CoachRx "over 2,000 video demonstrations" (Vimeo-hosted), ABC Trainerize "2,400+"
(from a resources page, read via search rendering, so **not verified**), TrainerFu "over 1000+",
Kahunas "Over 1000", Hevy Coach "400+ exercises" with "step-by-step instructions and animations".
**Who filmed any of them is not verified anywhere.** All let the trainer add custom exercises by
upload or YouTube/Vimeo link; Trainerize caps uploads at 5 minutes, 500MB, .mov or .mp4.

### Calendar, dashboards, notifications, messaging

**Client calendar** is verified on ABC Trainerize (a Calendar tab showing workouts, cardio, habits
and appointments, default one week, plus "Things To Do Today"), TrueCoach (upcoming/past views,
clients can reschedule if allowed, controlled under Client Workout Visibility), PT Distinction
("Clients get a notification for every item in their schedule", optionally movable), TrainHeroic
("Control your calendar … move your training when something comes up"), FITR, My PT Hub
(bookings, classes, waiting lists, registers, external sync), Hevy Coach (a Calendar in the
client's profile with full history), FitBudd (previous/future week view, workout planner,
Appointments add-on, Google Calendar sync), Kahunas (events, goals, appointments with
notifications) and CoachRx (unified across exercise, nutrition and lifestyle). **Everfit does not
give the client a calendar**: the client surface is a **Today screen** with up to six adaptive
sections (Training, Tasks, Steps Tracking, Food Journal, Community Forums, Notifications); a
month or week view is **not verified**. Playbook's client calendar is **not verified**.

**Progress dashboards** exist everywhere. The distinctive ones: TrueCoach's compliance-and-risk
framing ("Automated Risk Assessment – Get alerted when clients start to lose compliance");
TrainHeroic's lifting-specific set (PRs, total volume lifted, total reps, hours trained, a
Training Load Calendar, readiness trends); Hevy Coach's strength depth (exercise performance
graphs, 1RM predictions, volume over time, sets per muscle group, with body measurements and
progress photos the trainer gets "instant access to"); My PT Hub's programme compliance tracking
with side-by-side check-in comparison; Everfit's habit Insights.

**Push notifications** verified on TrueCoach, Everfit, My PT Hub (check-in notifications, overdue
nudges, @-mention alerts), PT Distinction, FITR, FitBudd and Kahunas. **Not verified** on ABC
Trainerize (no page read states it), **TrainHeroic** (not marketed anywhere), CoachRx or Playbook.
Hevy Coach is thin — clients get a notification when a coach messages, coaches get email and
browser notifications. TrainerFu is verified for habit reminders only.

**Messaging:** ABC Trainerize is richest — 1:1 and group messages, voice messages, video calls
(group video on Studio Plus; Video Coaching add-on $10/month for 50 hours of calls and 100 hours
of streaming; Studio gets 500 live + 5,000 on-demand hours). **FitBudd** is next — 1:1 (toggleable
per client), group chat, broadcast, scheduled group messages, automated drips, audio notes, video
messages, reply-privately-in-group, document sharing, **1:1 video calling** on Pro, Zoom for group
classes. TrueCoach: 1:1 with pictures, videos and GIFs, group messaging, Voice Notes — **no
verified calling**. Everfit: 1:1, scheduled, saved responses, AI smart response, group chat and
broadcast on Studio, Community Forums — no verified calling; Zoom links attach to tasks instead.
My PT Hub: "Individual, group or broadcast" instant and scheduled — no verified calling. PT
Distinction: Messenger, group forum, pre-scheduled messages, email from the trainer's own address,
scheduled SMS; its "Video Coaching" means recorded content, not live calls. TrainHeroic: real-time
chat with GIFs and reactions, 1:1 and team-wide. Kahunas: 1:1 with **voice notes** on every tier,
group messaging from Growth. **Hevy Coach: 1:1 only** — group chat, voice notes and calling all
**not verified**. FITR: 1-2-1, community chat, bulk messaging to segments (trial users, active,
unsubscribed), comments on workouts/exercises/PRs, @-mentions, media from a Media Library — no
voice notes, no WhatsApp or SMS integration.

**Nutrition**, briefly, since it varies more than expected: Kahunas and FitBudd are deepest
(Kahunas 1.6m verified foods "approved by a team of nutritionists", 800k barcodes, 2,400+
restaurant items, micronutrients, and the coach can hide macros/micros selectively; FitBudd adds
BMR meal plans, recipe library, barcode scanning, grocery list, supplement plans). My PT Hub has
650,000 food items with barcode scanning and Nutrition AI. Everfit has MacroSnap AI photo meal
logging. PT Distinction leans on "the only complete integration of MyFitnessPal in the industry".
TrueCoach is weakest of the majors (MyFitnessPal plus meal plans as documents). **Hevy Coach has
none at all**, and TrainHeroic's Nutrition Sync sits behind the athlete's own paid tier.

---

## 4. How they market themselves to trainers

### Homepage headlines, as published

| Platform | Headline |
|---|---|
| ABC Trainerize | "The #1 coaching app to better engage your clients" |
| TrueCoach | "Train Your Clients Online With The #1 Platform Built For Personal Trainers" |
| Everfit | "The all-in-one platform for [Fitness Coaches / Gyms & Studios / Nutrition Coaches / Sport Coaches] to level up your business" (animated rotator), sub-headline "Unlock your full potential with the #1 platform to coach, scale, and win." |
| My PT Hub | "The all-in-one personal training software and app" / "Unlimited clients. Unlimited growth. One coaching app." |
| PT Distinction | "Personal Trainer Software" (a bare keyword H1) / "Train more clients in less time, with better results" (H2) |
| TrainHeroic | "The Premier Platform For Strength Coaches" / "Deliver a premium athlete experience, manage remote and in-person clients in one place, and scale without losing your personal touch." |
| FITR | "where your business works out" / "You're already a great coach. This is where you build the systems you need to run a great coaching business too." |
| Hevy Coach | "Simple Personal Trainer Software for Professional Coaches" / "…Built by the Hevy team." |
| Kahunas | "When it comes to coaching, who has time for clunky platforms and dull spreadsheets?" |
| FitBudd | H1 is the small kicker "#1 Personal Training Software for Fitness Coaches & Gyms"; the dominant hero line is an H2: "Launch your **Branded Fitness App in minutes**" |
| TrainerFu | "Simple Personal Trainer Software for In-Person and Online Training." |
| CoachRx | "Build a Coaching Practice That Values Depth Over Volume" |
| Playbook | "Turn your audience into recurring income" |
| Exercise.com | "The #1 Software for Fitness Businesses" / "Ditch the generic salon tools." |

Four claim "#1" and two claim "all-in-one". The differentiated ones are the interesting ones:
TrainHeroic names a single vertical, CoachRx sells restraint, Playbook sells audience
monetisation rather than software, FitBudd leads with the branded app rather than the platform,
and Kahunas opens with a complaint about the competition.

### Channels

**Long-form SEO is universal and is the primary channel for almost everyone — but the intensity
differs by an order of magnitude.** Measured from their own sitemaps: **FitBudd ~4,341 URLs**
(592 blog posts, 136 insights, 125 academy, 23 coach stories, 420 tag pages, 34 niche landing
pages, **60 competitor/"best alternative to X" pages** naming Trainerize, TrueCoach, MyPTHub,
Everfit, **Fitr**, **Kahunas**, CoachRx, PT Distinction, TrainerFu, Mindbody, Glofox and more).
**Hevy Coach ~216 URLs** (54 blog posts, 100 glossary entries, **12 "Hevy Coach vs X" pages**, 20
sport pages). **Kahunas is a single marketing page** plus 75 blog posts and no comparison estate
at all. ABC Trainerize has the largest footprint among the majors (blog, Academy, a separate
resources subdomain). Exercise.com bakes competitor names into site navigation (Mindbody,
Trainerize, ZenPlanner, Pike13) across 15+ business-type landing pages, on top of owning the
exact-match domain.

Head-to-head comparison content is written in several directions at once: Everfit publishes
"Everfit vs Trainerize vs TrueCoach", PT Distinction publishes "PT Distinction vs Trainerize,
Everfit & TrueCoach" and a dedicated TrueCoach comparison, FITR publishes a "how we compare" page
against Everfit, ABC Trainerize, My PT Hub and TrueCoach plus a "fitr-switch" page, CoachRx runs
"Vs The Rest" and an explicit "we know TrueCoach inside-out" migration offer, TrainerFu runs a
Trainerize-alternative page, and FitBudd runs 60 of them.

**Two platforms are now optimising for language models, not just search.** Everfit publishes a
`/llms.txt` file. FitBudd goes further: its pricing-page footer reads "Still wondering if FitBudd
is right for you? **Get an unbiased answer from AI**", with buttons for ChatGPT, Claude,
Perplexity and Gemini.

**Free trials are the universal CTA, at very different lengths** — and the trial length, not a
price or a feature, is what the paid ads put in the headline (section 6): ABC Trainerize 30 days with
unlimited clients, My PT Hub 30 days, Hevy Coach 30 days, FitBudd 30 days, PT Distinction 1
month, TrueCoach 14 days, TrainHeroic 14 days, FITR 14 days, TrainerFu 14 days, CoachRx 14 days
(30 if referred), Kahunas 14 days. Everfit's trial length is unpublished on its own site but its live
Meta ads state **30 days**, and it has the only permanent free tier with meaningful functionality
(5 clients); Trainerize's free Basic allows one
client. **Exercise.com has no trial at all** — demo-gated and sales-led, as are FitBudd's Super
Pro and Elite tiers.

**YouTube, where measurable:** TrainHeroic 25.1K subscribers, My PT Hub 12.4K, PT Distinction
2.9K, Hevy consumer 3.41K, FitBudd 1.84K, Kahunas 1.81K, FITR 408 (28 videos), **Hevy Coach 56
subscribers and 2 videos**. Instagram, TikTok and X counts could not be read for any platform
(Instagram serves a login wall to automated requests) and are **not verified** throughout; search
snippets suggested ~23K Instagram for Trainerize and ~28K for Everfit, neither confirmed.

**Certification-body partnerships** are used by five platforms and are a real gap for the rest.
**ABC Trainerize** publishes an education-partners page naming **NASM** (multiple courses),
**The PTDC**, **NPE**, **IPTA** and **Precision Nutrition**, plus Axelsons PT Education in
Sweden; the NASM deal was announced November 2022 and press-released as reaching "400,000+
Personal Trainers and Coaches". **TrueCoach** embeds a discounted NASM CEU library at "up to 33%
savings". **My PT Hub** carries a UK-specific band headed "**Endorsed by industry-leading
education providers**" with logos for **CIMSPA, Create PT, FutureFit, Strength & Conditioning
Education and The Fitness Group** (dates not published). **CoachRx** goes furthest by making
certification the funnel: the **OPEX Coaching Certificate Program at $5,995** includes CoachRx
itself — "16 weeks included, plus LearnRx for 12 months". **TrainHeroic** appears under NSCA
member "Pro Deals" — a discount, not a partnership, and **not verified** directly. Everfit (NPE
Fitness is a business-coaching firm, not a certifier), PT Distinction, FITR, Hevy Coach, Kahunas,
FitBudd, TrainerFu, Playbook and Exercise.com: **not verified**. FitBudd publishes a lot of
NASM/ISSA comparison content, but that is keyword capture, not partnership.

**Gym, event and equipment partnerships** are rarer. **FITR** is the clearest: **PureGym** across
"370+ locations nationwide" with a "90 Day FREE Trial" and "10% OFF Annual Plan" for verified
PureGym trainers, and **HYROX** ("HYROX affiliated coaches get a free 90-day trial of the Fitr
Unlimited plan"), plus MyProtein, Hyperice, Eleiko, Built For Athletes and Compete for a Cure
under #FITRTOGETHER. **Kahunas** shows a single **PureGym** logo under "Recommended by" with no
wording, date or scope — **nature of the relationship not verified**. **TrainHeroic** runs a
**P2P Network** of athlete perks with published offers: Bells of Steel (free collars over $200,
code THCLIPS), Strong Coffee (10%, code trainheroic), BioSteel US and CA (30%, TRAINHEROIC30),
Vibram (15%), LMNT (free gift), O2 (20%/50%), Designs For Sport (10%, TH10) — athlete retention,
not coach acquisition — plus a software partnership with **Pike13** for the scheduling and billing
it deliberately does not build. Exercise.com shows Gold's Gym and APEC Sports Performance as
customers, not partners.

**Review-site authority** is PT Distinction's core proof strategy, to an unusual degree — its
homepage is built around "We're the highest-rated personal training software across all major
review sites", "Rated 4.9 stars on Capterra / Getapp / G2" and "number 1 … on Trustpilot,
Capterra, Software Advice, Get App". My PT Hub does the same with volume: "10,000+ 5-star
reviews", "the world's most-reviewed app for personal trainers". CoachRx and Exercise.com link
Capterra, G2 and GetApp from their footers.

**Paid advertising and podcast sponsorship** could not be observed from the pages and are **not
verified** for any platform, with two exceptions: **CoachRx** runs its own **CoachRx Podcast
Network**, and TrainHeroic publishes webinars and a media kit. Everfit runs **Everfit Academy**
with weekly live sessions and guest webinars; FitBudd runs webinars, an Academy, ebooks,
templates, free calculators (body fat, army body fat, lean body mass, TDEE) and a Facebook group;
My PT Hub runs a Facebook trainer community group and gated lead magnets on a separate
`pages.mypthub.net` domain. ABC Trainerize also runs a dedicated influencer segment page:
"Influence your fitness followers for the better — Keep your audience accountable, grow your
following, promote your brand, and earn money while you workout."

---

## 5. How they grow (distribution)

### Referral and affiliate schemes

| Platform | Scheme | Terms as published |
|---|---|---|
| ABC Trainerize | Public affiliate + credit referral | "earn a **15% recurring commission** on the price of their subscription", monthly and annual plans plus recurring add-ons, no caps, run on **PartnerStack**, approval in 2–3 business days; explicitly open to "influencers, personal trainers, fitness or nutrition professionals, celebrity trainers". Separate "Refer for Credit" gives account credit equal to the referee's first month |
| Everfit | Public affiliate | **10% of the referred coach's revenue for the first two years**, no caps, 30-day cookie, monthly PayPal payout above a threshold, covering Pro/Studio plus add-ons (Custom Branding, On-Demand Collection, Payments, Autoflow base), with extra commission on upgrades |
| My PT Hub | Public affiliate, open to anyone | Affiliates page: "**earn up to 25% per sale**", "Absolutely anyone can be an affiliate", "We don't cap referrals", run on Referral Rock, with segments named for "Webmaster / Fitness Personality ('Publish a video about My PT Hub on your YouTube or Vimeo Channel') / Social Publisher". Their blog breaks it down as **10% monthly, 25% annual**, paid by PayPal, referred trainer gets 30% off. Their own blog headlines conflict ("up to $100", "up to 100%") — treat the affiliates page's 25% as authoritative |
| TrueCoach | Credit referral + a near-hidden cash affiliate | "**up to $1000 of bonus credit** for every coach that becomes a TrueCoach customer", awarded by a spin-the-wheel mechanic, **credit only** — "No cash alternative to the referral credit" — expiring on cancellation, W-9 above $600/year. A separate cash affiliate programme runs on ReferralRock at **tsgfitness.referralrock.com** and is **not linked from truecoach.co anywhere found**, so effectively unpublished; third-party sources say $75 per customer after 90 days — **not verified** |
| FitBudd | Public partner programme, fully published | "Earn **up to $50 bonus** (on first successful customer) **+ 15% monthly recurring commission for 12 months**", 90-day tracking cookie, "No minimum payout", with separate Refer a Coach and Refer a Gym paths |
| Kahunas | Two, both real | Referral: "**$49 for each coach you refer**", paid once the referred coach is "active on Kahunas for 60 days", via PayPal. Separate **Rewardful** affiliate programme whose terms page is **Cloudflare-403 — rates not verified from the page**; reported elsewhere as 35% standard, 45% at 100 subscribers, 50% at 500+, with 20K Instagram / 10K YouTube eligibility |
| Exercise.com | Public affiliate | Run on **Refersion**: **10.00% commission**, 7-day attribution window, "Payout is net 60 days", open sign-up. Distinct from two in-product features sold *to* customers: "Trainer Commissions" for staff and a Refer-a-Friend tool for a gym's own members |
| CoachRx | Public referral | "CoachRx Referral Program (New April 2026)", dated 21 April: "**Earn $50 per referred signup.** Plus your referred coach gets their first 30 days free" — double the standard trial — paid as cash, link in the settings menu |
| TrainHeroic | Finder's fee + a delegated affiliate layer | A **$100 finder's fee** for referring a coach who subscribes within 90 days, credited to the next invoice, requiring TrainHeroic be copied on an intro email (search-surfaced from Cloudflare-403 docs, **not verified**). No public percentage affiliate programme. More interesting: **affiliate links are delegated to coaches** — coaches create links for "athletes or influencers on their team", pay **$1/transaction plus bank fees**, and TrainHeroic offers "no built-in rewards program for those affiliates — coaches can reward their affiliates however they see fit". A live example runs in the marketplace as "MFLH Affiliate Program" |
| PT Distinction | Invite-only, unpublished | A refer-a-friend scheme paying the referrer the equivalent of the referred trainer's first monthly payment (so up to $89.90), after the trial completes and a first payment clears, with the link inside the trainer's account. Search-surfaced from a press release; **not verified on ptdistinction.com**, which has no affiliate page |
| Hevy | Consumer app only | The Hevy app runs **25% commission "on every new subscription and renewal"**, 5K+ follower eligibility, monthly payouts via Everflow. **No Hevy Coach affiliate or ambassador programme is published — not verified** |
| FITR | **None** | Their own help article, dated **28 August 2026**: "There is no formal coach referral scheme on Fitr at the moment", with support willing to help paying coaches refer informally. Older third-party copy describing £10/£30/£50 credits by plan refers to a retired scheme |
| Playbook | None, and none needed | The relationship *is* a revenue share, so there is nothing to affiliate. In its place: a Creator Management Team, a private creator community, live coaching calls, a done-for-you Services arm, and Quarterly Challenges for creators with "the potential to win cash prizes" |
| TrainerFu | **None** | No affiliate, referral or partner page exists; `/affiliate.html`, `/referral.html`, `/refer.html` and `/partners.html` all return 404 |

### Named faces who front the platform

**Playbook is entirely creator-fronted, and this is its distribution strategy.** It publishes
creators by name with follower counts and revenue figures, all company-stated: **Mackenzie
Wells** ("30,000+ Paid subscribers", "200%+ Subscriber growth"), **Alicia Erickson** ("$100K+
Average/month", "12,000+ Paid Subscribers"), **Judd Lienhard** ("6,000+ Paid subscribers", "85%+
On annual billing"), **Melania Antuchas** ("~3,000 Paid subscribers", "80%+ Trial-to-paid
conversion", "788K followers"), plus **Aubri & Liv** ("15K+ Sales"), **Quinton Pulliam**, **Dana
Linn Bailey** ("7-figure"), **Amy Williams / Abs by Amy** ("209K followers") and **Andi Di
Battista** ("44.7K followers"). Even its staff are influencers: Creator Managers **Morgan Tyler**
(@findingmorgantyler, 500k followers), **Courtney Worthington** (@worth.fit, 100k) and **Brooke
Bohning** (@brookeworksout, 70k).

**Kahunas is creator-fronted by design** — 18 named coaches with Instagram handles on its
homepage wall: **Adam Ballinger** (@adamballingerfitness), **Lucy Anjuna**
(@lucyanjuna_the_coach), **Shane Parsons** (@shane_skulpt), **Callum Siddall**
(@cscoachingcallum), **Louise Harwood** (@lou_harwood_lpc), **Excel Coaching**
(@excelcoaching_), **Bryce Bahm** (@brycebahm), **Meftah Dagali** (@meftahdagali), **Louis
Barril** (@theprepdad), plus Sean Barber, Haider Medhi, Robert Laing, Sadie Moes, Ryan Lee, Angas
Wright, Clare Windsor, Martin Rowlands and Yonah Duniam — alongside 11 long-form videos and 7
Shorts embedded from @kahunasio and a signed personal letter from founder Mark.

**TrainHeroic fronts named strength coaches through its marketplace catalogue, and the economics
are published:** **Matt Chan** ("Titan Games winner"), **Matt Wenning** ("world record setter in
RAW AND EQUIPPED Power Lifting"), **Christian Harris** (Move Fast Lift Heavy), **Maddy Forberg**
(POWER Built, $16/month), **Catalyst Athletics** (Greg Everett), **MBSC / Mike Boyle Strength &
Conditioning**, **California Strength**, **Lift-Run-Bang** (Paul Carter), **Power Athlete**, plus
Johnnie WOD, Garage Gym Gladiators, The EMOM Co., Elite Physique and others. **These people are
revenue-shared, not sponsored** — they keep everything but $1/client/month on self-driven sales,
or 70% on TrainHeroic-sourced sales. No flat sponsorship or paid ambassadorship found. This is
the sharpest distribution difference in the set: TrainHeroic's marketing surface grows as its
coaches sell.

**FITR borrows athlete credibility through its cap table and its content.** **Mat Fraser**,
five-time CrossFit Games champion, is an investor and board member alongside **Matt O'Keefe** of
HWPO; elite CrossFit athlete **Reggie Fasa** also invested. Maven's write-up calls FITR "trusted
by standout industry names such as HWPO and five-time CrossFit Games champion Mat Fraser". A
"Coach Spotlight" series names ~19 coaches; the real-results page names 12 with their tenure,
including **Emma Mcquaid** (Daily Grind, 8 years) and **Gus Vaz Tostes** (HYROX coach).

**FitBudd is case-study-fronted** — 23 `/coach-stories/` pages naming **Derek Noble** (Noble
Nutrition, flagged as "SWITCHED FROM PT DISTINCTION"), **Amy Hollings** (BossFitAmy, "from 0 to
1,000 personal training clients"), **Ben Corliss**, **Mike Lacombe**, **Meha Jivan**, **Shruthi
Reddy**, **Justin Perkins**, **Chef Yadiyah**, plus homepage testimonials from **Pelegrina Dora**
(Amazon Girls Training) and **Jeremy Sry** (Pursuit by SRY); its YouTube lists a collaborator,
@drmarcmorris (15K subscribers).

**My PT Hub names case studies, not ambassadors** (the word does not appear): **Lane Bunch**
("built a $100K/year fitness business"), **Emma Storey-Gordon & Chloe Madeley** of **The EC
Method** ("grew from 100 to 9,000 clients"; Madeley is a UK media figure, making this the closest
to influencer fronting), **Jeremy Boisseau** (Custom Physique), **Emily DeLuzy** (FitQueen).
Whether any are paid is **not verified**.

**PT Distinction borrows authority through interviews**: **Jon Goodman** (Online Trainer
Academy), **AJ Mihrzad**, **Paul Mort**, **Joey Percia**, **Sukh Sidhu**, **Linh Trinh**, **Dan
Salcumbe**, **Tim Drummond**, **Janak Patel**. Paid or sponsored: **not verified**.

**CoachRx fronts working practitioners, not influencers**: **Kyle Krancher** (Train & Able),
**Bruno Miguel Ferreira Rocha** (Get.The.Coach), **Dr Austin Schoen** (Warrior Sports Wellness),
**Sam Smith** (Proof3 Coaching), **Brandon Wilton** (CrossFit South Bend), **Dr Frank Tardi**,
**Chad Johnson** (Chamber Fitness). The authority figures — James Fitzgerald and Carl Hardwick —
are not named on coachrx.app at all.

**ABC Trainerize has no ambassador page** but runs a named customer-story library (**Michelle
Roots**, **Brian Silva**, **Michelle Riley**, **Ange Drake** of 23W, **Amber Coates-Reid** of
Cobalt Club, **Johnny Loreti** of Anthrofit, **Mike Monti**). Note its *editorial* influencer
round-ups naming Stefi Cohen and Kaisa Keranen are SEO content with no stated relationship — not
ambassadorship. **TrueCoach** runs a case-study series including **Margaux Alverez**, a known
CrossFit Games athlete — the closest it comes to an athlete face — plus **Taylor M**, **Kyle** of
Blacklisted HQ, **Joshua Davis** and **Simeon Brombach**. **Everfit** is the most coach-led of the
majors, with a dated "End-of-Year Coach Spotlight 2025" (Matthew Hebert, Riane Anjuanew Payne,
Joshua Alston, Celeste Harrington, Leanne Dilnot) and named Academy webinars (Josh Clay, 1% Better
Academy, the Brian Keane Story, Despina Staikos), plus a homepage testimonial from **Brandon Woo**
of Winning Mentality Fitness.

**Hevy Coach has almost no named faces** — three testimonials (**Scott Slaman** @themechanic,
**Fit With Rashid** @fitwithrashid, **Gilian Reichert** @om_giigo); the faces that matter are the
founders'. It does have an audience landing page for health and wellness influencers, so they are
a target segment, not yet a channel. **TrainerFu has none at all** — social proof is anonymous
App Store snippets ("by MiniJazMarie", "by jlgraham"); the only named person is its founder.
**Exercise.com** uses institutional logos plus one named customer quote (**Brandon Stro**).
**Sponsored YouTube videos and podcast ad buys: not verified for any platform.**

### Which side is acquired first

**The trainer is acquired first on eleven of the live platforms**, and the evidence is
consistent: the trainer pays, the client pays nothing, and the client cannot get in without an
invitation or a purchase. ABC Trainerize's client listing states "Clients can only access the app
after being invited by their trainer, coach, gym, or fitness studio" and "Coaches create accounts
and invite clients to join"; the flow is coach-initiated ("ADD AND SEND INVITE"). TrueCoach's is
blunter: "If you are downloading this app, you are a client of a trainer who has chosen to level
up and subscribe." PT Distinction: "Clients can only use the app if they are working with a
trainer who uses PT Distinction. If you're a client, ask your trainer for your account details."
FITR: "Sign up to a program with your coach first, then download the Fitr Client app." My PT Hub,
CoachRx, TrainerFu, Kahunas and FitBudd all work the same way. **Exercise.com is the extreme
case**: consumers never meet the brand, because each gym ships its own branded app. PT
Distinction pushes hardest in this direction by design — "Sell your packages on **your own
website**, meaning you control the sales process" — and goes further than anyone in subsidising
its trainers' funnels: **PT Distinction pays for the prospect's account** during challenges,
automated free trials and sample programmes ("we'll even cover the cost for you").

**Hevy is the one genuinely consumer-first case, and it declines to broker.** The consumer app
launched November 2019, claims 17m+ users, and has 5m+ Play installs and ~100,000 US App Store
ratings. Hevy Coach was layered on top, the coached client uses **the ordinary consumer app**, and
the consumer app actively routes users toward coaching ("Do you work with a coach? Click here to
learn how getting coached through the Hevy app makes everything easier"). Hevy Coach then borrows
the consumer app's "4.9/5 · 630,000+ ratings" as its own proof. So Hevy owns consumer demand at
scale and monetises coaches on top of it — but it does not sell coaches *to* consumers.

**Two platforms acquire the consumer first and transact with them.** **Playbook** is fully open:
the App Store free trial unlocks "access to the entire platform, including all instructors,
workouts, programs, and videos" across "over 56,000 workouts and more than 500 instructors", at
$14.99/month or $99.99/year after 7 days, billed by Apple — "Your iTunes account will be charged
when the purchase is confirmed." A stranger can subscribe to a creator they have never met.
**TrainHeroic** runs both sides on one asset: marketplace.trainheroic.com is a public,
unauthenticated, browsable, priced storefront (22 programmes on the front page, $16–$49/month
subscriptions and ~$50 one-offs, each with "Start My 7-Day Free Trial"), and TrainHeroic recruits
coaches with that demand — "over 1 million unique visitors per year", "Reach athletes anywhere in
the world". It also monetises the athlete independently via Athlete Pro. The flywheel runs both
ways.

**In-product discovery — where a client finds a trainer they do not already know — is rarer than
the marketing implies.** It genuinely exists in three places. **ABC Trainerize's trainerize.me**
is the most mature: an open consumer marketplace, "Browse thousands of fitness professionals
around the world", browsable without an account, with filters for training type (Private Personal
Training, Online Personal Training, Group Bootcamp, Yoga, Pilates, CrossFit) and specialty
(Weight Loss, Muscle and Strength Gain, Pre and Post Natal Training, Nutrition and Meal Plans)
and city pages for New York, Los Angeles, London, Sydney and 20+ others; a profile is a Grow-tier
feature. Whether checkout completes on the marketplace or hands off to the coach is **not
verified**. **TrainHeroic's Marketplace** is a full discovery surface with category browsing,
search, public pricing and free trials, plus a **Matching** service where TrainHeroic introduces
athletes to coaches and takes 30%. **Everfit's Marketplace** is the third, at everfit.io/explore
("Find your perfect coach"), a survey-then-browse flow, in **public beta limited to coaches in
the USA, UK, Australia, New Zealand and Canada**, with profiles built by the coach with AI help or
by Everfit's design team "in 2 to 3 days" — though /explore is a client-rendered SPA that
returned no static content, so **what a signed-out consumer actually sees, and whether they can
transact, is not verified**, and the marketplace commission is **not verified** either.

**Everything else has no discovery surface at all.** TrueCoach's Public Coach Profiles (Standard
and up) are "a fully customizable, professional-looking profile … an online business card" with a
lead form that the coach shares themselves — there is no browsable TrueCoach directory. My PT
Hub's page labelled "Marketplace" is a **template library** for trainers ("Choose from 1,000s of
free, pre-made coaching templates"), not a coach directory. Kahunas has per-coach public package
pages that are search-indexed but no cross-coach browsing. FitBudd's `/personal-trainers-near-me`
reads like consumer intent but serves a **trainer-acquisition** landing page. FITR, PT
Distinction, CoachRx, TrainerFu, Exercise.com, Hevy Coach and FitBudd all route discovery to the
trainer's own channels. Everfit is the only one of the trainer-first group that lets a client
self-serve onto a roster without a manual gate, via its **Public Client Invite Link** ("Share the
link on your social media … Clients can just sign up with the invite link without you manually
adding them!"), with overflow going to a waiting list.

### Funding, acquisitions and growth events, dated

- **Garmin acquired TrainHeroic and TrainingPeaks from Peaksware Holdings, announced 22 July
  2026.** Terms undisclosed; ~120 staff became Garmin associates; separate business unit;
  "brand-agnostic for wearables and smart trainers"; Dirk Friel strategic adviser, Lee Gerakos
  remains; Peaksware kept MakeMusic and Alfred Music. Nothing on trainheroic.com mentioned Garmin
  as at 26 October 2026.
- **Daxko acquired Exercise.com, announced 23 October 2025.** Terms undisclosed; Vista Point
  Advisors was Exercise.com's exclusive financial adviser. Named: Jeff VanDixhorn (CEO, Daxko),
  Joel Ohman (Founder and CEO, Exercise.com), Aldor H. Delp (President of Boutique Fitness).
- **PYXiS Software Group (Jonas Software / Constellation Software) acquired EverCommerce's
  fitness solutions, announced 13 March 2024**, including **My PT Hub** with ClubOS, ASF and
  ClubWise; ~10,000 customer locations; "less than 4% of EverCommerce's 2023 revenue";
  international businesses expected to close Q3 2024.
- **EverCommerce acquired My PT Hub 18 November 2020 for $11.7m** (announced 3 December 2020),
  when it had "over 83,000 trainers and their 1.3 million clients". Own-reported trainer count has
  since gone 83,000 to 200,000+.
- **ABC Financial / ABC Fitness acquired Trainerize, announced 15 September 2020** (Thoma Bravo
  press release). ABC also bought GymSales in July 2020 and Glofox in 2022. Note the two
  companies' own pages disagree on ABC's scale: Trainerize's about page says ABC "serves
  approximately 30,000 clubs and studios and over 40 million members globally, processing
  approximately 12 billion dollars in payments annually", while ABC Fitness's own page says
  ~40,000 clients, 30+ million active members, $1B+ in annual payment volume and 2 billion
  workouts tracked.
- **Xplor owns TrueCoach**, confirmed on TrueCoach's own about page; the TSG (April 2020) to
  Xplor (1 July 2021) path is third-party and **not verified**, though the affiliate programme
  running on tsgfitness.referralrock.com is consistent with it.
- **FitBudd raised a $3.4m seed announced 12 October 2022**, led by Accel India with Beenext,
  Sequoia Capital India and Waveform Ventures; founded 2021; "over 600 coaches across 20
  countries" at the time. A $3.9m lifetime total is reported by Tracxn — **not verified**.
- **Playbook raised a $9.3m Series A announced 14 October 2020** (E.ventures, Michael Ovitz,
  Abstract, Algae Ventures, Porsche Ventures, FJ Labs), total $12.3m including a June 2020 seed;
  TechCrunch reported the same 80% creator cut then. No round since found.
- **FITR raised $1.2m in April 2022** (Maven Capital Partners, Mat Fraser), then **£1.5m from
  Maven VCTs published 2 December 2025**, with Maven stating FITR is "already profitable, which is
  unusual for a young fast growing technology business".
- **Everfit**: a $1.1m seed dated 24 October 2019 (PitchBook). Getlatka estimates $8.4m ARR and a
  $25.1m valuation — **not verified**.
- **Kahunas**: no funding found. Stripe's own 2023 customer page reports $4m annual revenue, 900%
  2023 growth and $1.2m monthly client payments processed, on Stripe Payments, Billing,
  **Connect** and Checkout.
- **Hevy Studios S.L., PT Distinction, TrainerFu, CoachRx/OPEX**: funding **not verified / none
  found**. PT Distinction and TrainerFu describe themselves as independent and unfunded;
  CoachRx/OPEX is privately held with no disclosed raise. A reported "$2M in annual revenue" for
  Hevy (Ottawa Business Journal) is **not verified**.

---

## 6. Social reach and paid advertising

Read through the ScrapeCreators API on 26 October 2026, which reaches the public profile data and
the Meta, Google and LinkedIn ad libraries that ordinary web requests could not. Endpoints are
listed in the sources. Counts are live figures on that date; a blank means no account was found
under any handle published on the company's own site.

### Followers and subscribers, 26 October 2026

| Platform | YouTube | Instagram | X | TikTok | Facebook page likes |
|---|---|---|---|---|---|
| ABC Trainerize | @TrainerizeYoutube **10,700** (491 videos, 663,591 views, joined Oct 2017) | @trainerize **24,247** (2,237 posts) | @trainerize **3,002** (4,600 posts, since Feb 2011) | none — @trainerize is a dormant account with 0 followers and 1 video | 18,247 |
| TrueCoach | none published | @truecoach.co **33,065** (4,181 posts) | @truecoachco **1,519** | @therealtruecoach is linked in the footer but returned no profile data | 23,089 |
| Everfit | 4,310 (174 videos, **59.2m views** — by far the most views in the set) | @everfit **32,628**; @everfitpros 2,940 | @geteverfit **710** | @everfit.io **10** | 9,849 |
| My PT Hub | @MyPTHub **12,400** (2,028 videos, 23.0m views, joined Apr 2015) | @mypthub **7,511** (1,445 posts) | @mypthub **1,083** | @mypthub **27** | 11,509 |
| PT Distinction | 2,900 (306 videos) | @pt_distinction **3,769** (3,139 posts) | @PTDistinction **474** | not retrievable | 7,505 |
| TrainHeroic | @TrainHeroic **25,100** (369 videos, 9.8m views, joined Oct 2011) | @trainheroic **66,344** — the largest Instagram in the set | @trainheroic **3,704** | @trainheroic **389** | 30,013 |
| Hevy (consumer) | @HevyApp 3,410 (48 videos) | @hevyapp **60,085** | @hevyapp **5,424** | @hevyapp **25,600** (715,600 likes, 222 videos) — the only real TikTok presence in the set | 12,157 |
| Hevy Coach | @hevycoach **56** (2 videos) | @hevycoach **1,221** (16 posts) | none | none | — |
| Kahunas | @kahunasio 1,810 (**814 videos**) | @kahunasio **20,185** (1,379 posts) | @kahunasio **9**, account created 14 Sep 2026 | none | 2,567 |
| FitBudd | @fitbudd. 1,840 (526 videos) | @fitbudd.app **13,689** (1,050 posts) | none | @fitbudd **20** | — |
| TrainerFu | @trainerfu **314** (26 videos) | @trainerfuapp **138** (14 posts) | @trainerfu **49** | none | — |
| Playbook | @join.playbook **145**, channel joined Jun 2025 | @joinplaybook **8,073** | none | none | — |
| CoachRx | no channel — the footer links a playlist | @coachrx.app **15,201** (2,464 posts) | none | none | 1,911 |
| Exercise.com | @exercise, now "Daxko Exercise", **682** (313 videos) | not retrievable (@exercisecom returns 404) | @exercise **7,814** (3,606 posts, since Jul 2010) | @exercisecom **28** | — |
| FITR | @PERSONALTRAINERSOFTWARE **408** (28 videos) | @fitr.app **11,990** (490 posts) | none | @fitr.app **81** | — |

Three things stand out. **Instagram is the only social channel any of them has built**, and the
order there is not the store order: TrainHeroic (66,344) and Hevy (60,085) lead, TrueCoach
(33,065) and Everfit (32,628) are ahead of ABC Trainerize (24,247) despite Trainerize having
nearly twice TrueCoach's App Store ratings and twenty-five times Everfit's. **TikTok is empty**
for twelve of the fourteen: the only account with a real audience is consumer Hevy, and the
trainer-side platforms sit between 0 and 389 followers. **X is close to abandoned** — the largest
is Daxko Exercise at 7,814, inherited from a 2010 account, and Kahunas only opened an X account
six weeks ago.

### Who is buying growth, and what the ad promises

Meta figures are active ads on 26 October 2026 from the Meta Ad Library; Google figures are the
ad-count estimate from the Google Ad Transparency Center for ads pointing at the company's own
domain, with the advertiser's legal name as Google publishes it.

| Platform | Meta, active now | Google | LinkedIn | What the ad leads with |
|---|---|---|---|---|
| Everfit | **141** — the heaviest Meta buyer in the set, from 12 Sep 2026 | ~200 est., Everfit Technologies Inc., running since 19 Jul 2022 | none | "Everfit \| Start Your 30 Day Free Trial" / "Run your entire coaching business on your couch. Let Everfit manage your business so you can focus on actually coaching." A second flight sells one feature: "Macro-Tracking for Clients" |
| Kahunas | **58**, oldest active 23 Jul 2026 | 11 est., 4 of them Kahunas FZC, since 11 Oct 2024 | none | Every single ad is titled "14 Day Free Trial"; the body always opens on a coach's problem — "Still asking clients, 'What did you lift last week?'", "How many times have you lost a client just because a check-in slipped through the cracks?" |
| ABC Trainerize | **29**, from 1 Sep 2026 | 66 est., 27 of them TSR GYM TECHNIK LTD., since 15 Nov 2023 | 2 | "Explore powerful Trainerize features to build and scale your fitness businesses." / "See why coaches are loving ABC Trainerize"; a second line reads "Scale Your Fitness Business — All-in-one platform to manage clients, workouts, nutrition, and payments in one place." |
| My PT Hub | **28**, oldest active 8 Jul 2026 | ~200 est., Fitii Ltd, since 7 Dec 2021 | **11** — the only platform with a real LinkedIn buy | "Start Your 30-Day Free Trial" and "The #1 App for Personal Trainers", over a body that opens "Too much admin, not enough coaching? 😫" and promises "Save up to 80% of your admin time" |
| TrainHeroic | **35**, a new flight started 21–22 Oct 2026 | 43 est., 24 of them TrainHeroic, since 8 May 2025 | **10** | "Start Your Free Trial" / "Your coaching is premium. Your athletes' experience should be too." |
| CoachRx | **15**, all from 7 Oct 2026 | 20 est., 18 of them OPTIMUM PERFORMANCE TRAINING LLC, since 30 Jul 2024 | none | A switching ad, not an acquisition ad: "Upgrade Your Coaching Software Now … Don't settle, demand more and start your free trial now. We offer free transition…" |
| PT Distinction | **12**, running continuously since **29 Aug 2025** — the longest unbroken flight in the set | 27, PT Distinction, since 7 Nov 2023 | none | "Unlock the Future of Fitness Training!" landing on `/ai-coaching`, closing "Sign up for a 1-Month Free Trial and elevate your PT game!" |
| Exercise.com | none | **~200 est., Exercise.com LLC, last shown 26 Oct 2026** — the heaviest Google buyer, across text, image and video | none | Google only; no Meta page in the ad library |
| FITR | none | **~200 est. on coachwithfitr.com** and 18 of 25 on fitr.training, Fitr Holdings Limited, since 3 Jun 2025 | none | Google only; no Meta ad-library page under its own name |
| FitBudd | none found under the company name | 67 est., 35 of them Fitbudd Inc, since 11 Jan 2024 | none | Google only |
| TrueCoach | page exists, **0 active** | 47 est., all **AI Sky US Bidco Inc** (Xplor's entity), since 25 Oct 2021, 37 of 40 text ads | none | Google search only |
| Playbook | page exists, **0 active** | 20, of which only **5** are Playbook Technologies Inc.; the other 14 are creators buying their own ads to Playbook pages (Latitude Wellness, Kaitlynn Jones) | none | Paid acquisition is delegated to the creators |
| Hevy / Hevy Coach | page exists, **0 active** | **zero company ads** — hevyapp.com shows only two unrelated third-party advertisers, hevycoach.com none | none | Buys nothing anywhere |
| TrainerFu | none | **zero** | none | Buys nothing anywhere |

Four observations worth carrying forward.

**Every ad read is aimed at the trainer, not the client.** Not one platform runs a consumer-facing
ad for its own brand. The only paid consumer acquisition in the whole market is *delegated*:
Playbook's creators buy ads to their own Playbook subscription pages, and TrainHeroic's
marketplace coaches run their own Google ads pointing at trainheroic.com — California Strength
LLC, Matt Wenning, Atlas Training Solutions and GBRS Group all appear as advertisers on
TrainHeroic's own domain. The marketplace model shows up in the ad library as other people's
money.

**The free trial is the offer, and the trial length is the headline.** Everfit, My PT Hub,
Kahunas, TrainHeroic, CoachRx and PT Distinction all put the trial in the ad title rather than a
benefit or a price. This also settles a gap from earlier in the report: **Everfit's unpublished
trial length is 30 days**, stated in its own live ads.

**Google search is where the quiet ones spend.** Exercise.com and FITR, the two platforms with
almost no observable app-store or social footprint, are the heaviest Google buyers in the set and
run nothing on Meta. TrueCoach does the same in a smaller way — 47 Google ads, 37 of them plain
text, and zero on Meta. A platform can look dormant from the outside and still be buying demand.

**Advertiser legal names fill in gaps the websites leave.** Google publishes the paying entity:
TrueCoach's ads are paid for by **AI Sky US Bidco Inc** (consistent with Xplor ownership),
CoachRx's by **OPTIMUM PERFORMANCE TRAINING LLC** (OPEX), FITR's by **Fitr Holdings Limited**,
Everfit's by **Everfit Technologies Inc.**, My PT Hub's by **Fitii Ltd**, and Kahunas's by
**Kahunas FZC** — an FZC being a United Arab Emirates free-zone company, the first signal anywhere
of where Kahunas is registered, though it is an advertiser name and not a stated head office.

---

## Ranking table

| # | Platform | Who it is for | Scale signal (observed) | Social reach, 26 Oct 2026 | Running paid ads? | Gamified? | Client video upload of sets? | Billing route for the trainer's clients | Price (trainer pays unless stated) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC Trainerize | Trainers, gyms, studios, enterprise | iOS 68,999 US / 15,651 GB; Play 1m+; Similarweb 2.1m visits/3mo; claims 400k+ coaches | IG 24,247; YT 10,700; X 3,002; TikTok none | **Yes** — Meta 29 active, Google 66 est., LinkedIn 2. "Scale Your Fitness Business" | **Yes** — streaks, badges, milestones, leaderboard + threshold challenges with points, groups, WOD | **No** — request closed by staff, 4 Jun 2020; video via chat | Stripe on the web, $10/mo add-on; platform % not verified | Free (1) to $248/mo (500); Pro from $23/mo |
| 2 | TrueCoach | Solo online personal trainers | iOS 35,746 US / 16,346 GB; Play 100k+; claims 16k coaches, 250k clients; Similarweb rank falling | IG 33,065; YT none; X 1,519; TikTok none | Google only — 47 est. (AI Sky US Bidco Inc), 37 text ads; **Meta 0** | Barely — milestone badges and habits only | **Yes** — 200MB/~60s, attached to the exercise | Stripe on the web, **flat 5%**, US/UK/AU/CA only | $26.34–$136.99/mo (5–50 clients); monthly list prices not verified |
| 3 | Everfit | Fitness, nutrition and sport coaches, gyms | iOS 2,710 US / 1,166 GB; Play 100k+; Similarweb 1.2m visits/3mo; claims 380k coaches (unsubstantiated) | IG 32,628; YT 4,310 (59.2m views); X 710; TikTok 10 | **Yes, heaviest on Meta** — 141 active, Google ~200 est. "Start Your 30 Day Free Trial" | **Yes, strongest** — 11 leaderboard types, AI push-up challenge, streaks (challenges behind paid add-on) | **Yes** — video comments tagged per exercise | Stripe on the web, $9/mo + 3.15% + $0.30 US domestic | Free (5) to $430/mo; Enterprise custom |
| 4 | My PT Hub | Trainers and nutritionists, UK-rooted | iOS 1,860 US / 1,733 GB at 4.14; Play 100k+, 2,315 reviews; claims 200k+ coaches | IG 7,511; YT 12,400; X 1,083; TikTok 27 | **Yes** — Meta 28, Google ~200 est., **LinkedIn 11**. "Too much admin, not enough coaching?" | **No** — personal bests and a social feed only | Not verified | Stripe on the web (Apple Pay as a card method) | £20/mo (3); £59/mo unlimited; £199/mo all-in |
| 5 | TrainHeroic | Strength coaches and teams | iOS 1,836 US; Play 500k+; **Garmin-owned since 22 Jul 2026**; own pages disagree 10k vs 20k coaches | **IG 66,344** (largest); YT 25,100; X 3,704; TikTok 389 | **Yes** — Meta 35 (new flight 21 Oct), Google 43 est., LinkedIn 10; **its marketplace coaches buy their own Google ads to trainheroic.com** | **Yes** — team leaderboards on any exercise, StackUp percentile, streaks, 1M-lb club | **Yes** — "Video review" is a headline coach feature | Marketplace: card at 2.9% + $0.30, PayPal payout. Athlete Pro via **Apple IAP**. **No 1:1 client billing** — Pike13 | $9.99–$399.99/mo by athlete band; 30% or $1/client/mo on marketplace; Athlete Pro $4.99/mo |
| 6 | Playbook | Fitness creators and influencers, not 1:1 trainers | iOS 37,040 US at 4.92; Play 500k+; claims $233m paid to creators, 300k subscribers | IG 8,073; YT 145; X none; TikTok none | **No own buy** — Meta 0; of 20 Google ads only 5 are Playbook, 14 are creators advertising their own pages | No game layer — community features only | Not verified, structurally unlikely | **Apple IAP**, Google Play Billing and Stripe | No subscription; **20% of net revenue**. Consumer pays $14.99/mo or $99.99/yr |
| 7 | FITR | Coaches and gyms, functional-fitness lean, UK | Play 50k+ at 3.0/74 reviews; **iOS under 25 ratings worldwide**; claims £53m income, 120k clients | IG 11,990; YT 408; X none; TikTok 81 | Google only — **~200 est.** (Fitr Holdings Limited); Meta none | Partly — challenge leaderboards, habit progress; no streaks, points or badges | **Yes** — 500MB/file, attached to a training performance | Stripe via FITR, **5.99%** Business Automation fee | £14.99/mo entry + £3.00/client, unlimited option; Custom App $199.99/mo |
| 8 | PT Distinction | Online personal trainers, independent | iOS 121 US + 471 on its container app; **no Play listing found**; claims 60k businesses | IG 3,769; YT 2,900; X 474 | **Yes** — Meta 12, running since **29 Aug 2025**, the longest flight; Google 27 | **No** — none at all | **Yes** — billed on every tier | The trainer's own PayPal or Stripe, sold from the trainer's own site | $19.90 / $59.90 / $89.90 per month + per-client fees |
| 9 | TrainerFu | Solo trainers and small studios | iOS 3,209 US; Play 50k+; **iOS not updated since 19 May 2025** | IG 138; YT 314; X 49; TikTok none | **None anywhere** | Thin — habit challenges and one leaderboard | Not verified (meal photos only) | Payment processing offered; processor not named | $29–$250/mo by band; branded app +$75/mo |
| 10 | Kahunas | Online coaches wanting a branded app | Play 100k+ but **2.5 stars / 257 reviews**; iOS ~3.2; claims 14k coaches, 750k users; Stripe reported $4m ARR (2023) | IG 20,185; YT 1,810; X 9; TikTok none | **Yes** — Meta 58, every ad titled "14 Day Free Trial"; Google 11 est. (Kahunas FZC) | **No** — habits, a login streak, a water tracker | Not verified | Stripe or PayPal direct (Stripe **Connect**), **no commission** | $35 / $69 / $99 per month |
| 11 | Hevy Coach | Strength coaches with small rosters | Coach app tiny (Play 10k+, 70 reviews); **consumer Hevy 5m+ Play installs, ~100k US iOS ratings, 17m+ claimed users** | Coach IG 1,221 / YT 56. **Consumer Hevy IG 60,085; TikTok 25,600; X 5,424; YT 3,410** | **None anywhere** — zero Meta, zero Google, zero LinkedIn | **No** on its own surface; consumer app has a weekly streak + 38-exercise follower leaderboard | Partial, session-level and social, not coach-routed | **None** — no client billing at all; coach pays via Paddle | $25/mo (1–10) to $700/mo (501–1,000) |
| 12 | CoachRx | Coaches wanting depth, OPEX-trained | Play 10k+; iOS 81 US at 3.63; claims 8,000+ coaches | IG 15,201; YT none; X none; TikTok none | **Yes** — Meta 15 (all 7 Oct 2026), a switching ad; Google 20 est. (OPEX) | One unmarketed streak counter in the app | Coach→client video only (Loom) | Stripe on the web | $29 / $79 / $199 per month |
| 13 | FitBudd | Coaches wanting their own store listing | Play 5k+ first-party, but **20 trainer-branded apps** on its Play developer page; claims 10,000+ coaches; $3.4m seed | IG 13,689; YT 1,840; X none; TikTok 20 | Google only — 67 est. (Fitbudd Inc); no Meta page found | Challenges + leaderboards, **Elite (quote-only) tier only** | Not verified | Stripe/PayPal on web, **plus Apple IAP on Super Pro** (Apple pays the coach) | $15 / $79 / $149 per month + setup fees; Elite custom |
| 14 | Exercise.com (Daxko) | Gyms, studios, multi-location | No consumer scale by design; iOS now "Daxko Exercise", 22 US ratings, last shipped 14 Oct 2024 | IG n/a; YT 682; X 7,814; TikTok 28 | Google only — **~200 est.** (Exercise.com LLC), the heaviest Google buyer; Meta none | Leaderboards and challenges; nothing else | Not verified | Web merchant processing, ECommerce and POS | **Quote only**; no published price, no free trial |
| — | Sidekick | — | **No such product** — sidekick.fit parked and for sale; trainwithsidekick.com does not resolve | — | — | — | — | — | — |

---

## FITR in detail

### What it is and who runs it

`fitr.training` now redirects permanently to **coachwithfitr.com**; the old domain resolves only
as a redirect, and so does `fitr.app`. Homepage H1: **"where your business works out"**,
sub-headline "You're already a great coach. This is where you build the systems you need to run a
great coaching business too." The about page calls FITR "the business builder for coaches that
turns real work into real results", adding that it is "built with a level of care that doesn't
change depending on whether anyone's looking" and positioning itself against inflated industry
claims — coaches who "measure success in lives changed, not likes".

The legal entity on both App Store listings is **Fitr. Holdings Limited**, Companies House number
**09759426**, incorporated **2 September 2015**, registered office **Richmond House, Walkern Road,
Stevenage, Hertfordshire SG1 3QP**, status Active, SIC codes 62012 (business and domestic software
development) and 63110 (data processing, hosting and related activities). It was previously
**Libertatum Applications Limited** until 18 July 2019. A second company, **Fitr. Training
Limited (12112152)**, also exists. Maven describes FITR as London-based; the registered office is
in Hertfordshire; the about page gives no location at all.

Leadership, from the about page: **Leon Cassidy**, Founder & CEO (a KPMG-trained chartered
accountant per third-party profiles); **Katrina Southey**, COO; **Tom Livings**, Chief Product
Officer; **Ryan Singh**, Chief Customer Officer; **Clive Baker**, CTO; **Keith Boyd**, board
member, "both an investor and advisor".

Funding: a **$1.2m seed in April 2022**, investors including Maven Capital Partners and **Mat
Fraser**, who joined the board with **Matt O'Keefe**, CEO of HWPO. A further **£1.5m from Maven
VCTs** was published **2 December 2025**, with Maven stating the company is "already profitable",
and the funds earmarked for sales and marketing, headcount and technology development. Elite
CrossFit athlete **Reggie Fasa** has also invested, per FITR's own blog.

### Scale

All company claims, from the real-results page: **"34,000+ programs run daily"**, **"£53 million+
income generated through platform"**, **"120,000+ clients achieving training goals"**. A figure of
"over 30,000 programs and 8 million workouts" circulates in software directories, sourced from
FITR's own copy; directories also describe it as serving businesses "with 1 to 15,000 clients".

Store reality is more modest. Google Play: **Fitr Client, 50k+ installs, 3.0 from 74 reviews**;
**Fitr Coach, 1k+ installs**. The App Store footprint is negligible — **fewer than 25 ratings in
total across both apps across the GB, US, AU, IE, CA, NZ, DE and SE storefronts** (GB: 4 for the
client app, 12 for the coach app; US: 3 and 1). Both apps shipped v2.0.2 on 7 October 2026 and
the company has just rebranded its domain, so a ratings reset is plausible but **not verified**.
The FITR YouTube channel (@PERSONALTRAINERSOFTWARE, "Fitr") has **408 subscribers and 28 videos**.

### Pricing

Per active client. The pricing page as served shows **£14.99/month** at the entry point with
**£3.00 per client** on the slider, and an unlimited-clients option headed "Your business. No
limit." Because the slider is interactive, the exact figures at each client step are **not
verified**. Currency switches GBP/USD/EUR; annual saves 20%; "Prices shown include all sales tax.
No contracts. Change plan anytime."

An active client is defined precisely: "any client who is currently subscribed to one of your
ongoing programs. **Clients who download your fixed length programs won't count** towards your
active client subscription count." Coaches invited to join another coach's account pay no
subscription fee.

On payments: **"Payments are processed through Fitr, supported by Stripe, with a 5.99% fee for
full automation."** Stripe's own fees are passed through "directly, with no markup". FITR frames
the 5.99% as covering "invoicing, tax automation, financial dashboards, dispute handling,
reporting, and client access control", with "no hidden add-ons, no module upgrades, and no premium
tiers". Prices can be set in the coach's currency and displayed in the client's, across the 135+
currencies Stripe supports. Programmes can be set to free.

Free trial: **14 days, full access, no credit card**. A full migration service is offered
(support@fitr.training). Legacy plan names — **Starter, Pro and Unlimited** — still appear in help
articles, so the tiering changed recently.

The **Custom App** add-on is **$199.99/month, or $119.92/month billed annually** (40% saving). It
is a genuine separate app: "A Custom App is your own standalone app on the App Store and Google
Play. Brand Kit adds your branding inside the Fitr app." It includes "Your own App Store & Google
Play listing", full branding (colours, splash screens, logo, wallpaper), and a dedicated build
lead; "We'll handle publishing, maintenance, and future updates". The coach must register
developer accounts with both Apple and Google at kickoff, and the build takes about four weeks.

### Can a prospective client download the app and look round without an invite?

**No. Access is purchase-first, and there is no public marketplace.**

- The client-app page: "**Sign up to a program with your coach first**, then download the Fitr
  Client app from the App Store or Google Play and log in to get started."
- The App Store description says the same: "Sign up to a program with your coach, then download
  the Fitr app to train."
- Each coach gets their own **Storefront** and **Program Pages**, headed "Showcase your offer.
  Make the sale.", at a custom URL of the form `brand-name.fitr.app/t/branded-storefront`, which
  the coach shares across their own marketing channels. Storefronts now resolve under
  `coachwithfitr.com/t/<slug>`. There is **no FITR-wide directory** of coaches or programmes, and
  the storefront page makes no mention of discoverability, SEO or cross-coach browsing.
- No `/marketplace`, `/explore` or `/find-a-coach` page exists on coachwithfitr.com — all return
  404. `fitr.training/marketplace` has **no Wayback Machine snapshot at all**, so there is no
  evidence a public marketplace ever existed.

So a prospective client can read a coach's storefront page on the open web, but cannot browse
FITR, cannot find a coach through FITR, and cannot use the app until they have bought a programme
from a specific coach. FITR does run "Example Programs - Try FITR as a Client" for coaches
evaluating the product, which is the only route into the client app without a real purchase.

### Features

- **Programme structure**: Program > Training Day > Sets & Reps table > Exercises, with "training
  blocks" combined to structure weeks, and **Tracks** as variants within one programme for a
  multi-track experience. Supersets link up to ten exercises. Personal Records library of 2,500+
  options.
- **Exercise library**: "preloaded exercise library" with "hundreds" of exercises on the
  programming page, and "our 1,000+ movement videos" on the communication page — FITR's own two
  figures disagree.
- **Client video of working sets**: yes. "Photos and videos up to **500 MB** per file",
  attachable to training performances ("ideal for form checks and workout videos"), Personal
  Records, Challenges and Body Metrics. "You can leave comments on any media your clients share -
  they will receive a push notification when you respond." Coaches can also "attach photos, videos
  or files and leave feedback right in the scheduling view".
- **Calendar**: client-side — "Open your calendar and see exactly what's on, wherever you are."
- **Progress**: Personal Records tracked over time, body metrics logged in the client app, workout
  history review, charts, repeatable Challenges where "Every entry is saved". "Review and comment.
  See every entry as it comes in. Comment directly to encourage."
- **Push notifications**: yes — "Push notifications keep you on track, so nothing slips through."
- **Messaging**: 1-2-1 chat; community chat for subscription-based programmes; bulk messaging to
  segments (trial users, active clients, unsubscribed); comments on past workouts, exercises and
  Personal Records; @-mentions in leaderboard entries and community chats; media and video
  attachments from a Media Library or the 1,000+ movement videos; automated welcome messages;
  private coach notes. **No voice notes, no WhatsApp or SMS integration found.**
- **Nutrition**: macros set by the coach and followed in the client app.
- **Habits**: recurring lifestyle goals (sleep, hydration, cold exposure, custom), target values
  and frequencies from daily up to a year, logged through the client's calendar, automated push
  reminders, and a coach dashboard showing completion rates — "Track how clients are getting on,
  who's on track and who needs a nudge", with progress bars showing "completed 6 of 8 tasks".
- **Wearables**: "Connect your wearable and track your Readiness, Strain and more."
- **Fitr AI**: programming built from the coach's chosen sports, goals and approach, "adjusted
  daily" from client wearable data and responses — marked **coming soon**, so not shipped.
- **Business**: Brand Kit (branding inside the FITR app), Packages, Promotions, Business
  Automation, integrations.

### Gamification

Challenge leaderboards are real, and clients can be tagged in leaderboard entries. Challenges are
repeatable with every entry saved. Habit tracking has progress bars and completion counts and a
coach view of who needs a nudge. But the habits page contains **no streaks, completion scores,
points or badges**, and none were found elsewhere. No levels, no avatars.

### Distribution

- **No formal referral scheme.** FITR's own help article, dated **28 August 2026**: "There is no
  formal coach referral scheme on Fitr at the moment", with support willing to help paying coaches
  refer informally.
- **Gym chain**: **PureGym**, across "370+ locations nationwide", with new PureGym trainers
  offered a "**90 Day FREE Trial**" and "10% OFF Annual Plan" on verifying their trainer status.
- **Event series**: **HYROX** — "HYROX affiliated coaches get a free **90-day trial** of the Fitr
  Unlimited plan", with full access and no upfront payment.
- **Other named partners**: MyProtein, Hyperice, Eleiko, Built For Athletes and Compete for a
  Cure, under **#FITRTOGETHER**.
- **Athlete-investor credibility**: Mat Fraser and HWPO's Matt O'Keefe on the board; Reggie Fasa
  an investor.
- **Content**: a Coach Spotlight blog series naming ~19 coaches; a real-results page naming 12
  coaches and businesses with their tenure; a "how we compare" page against Everfit, ABC
  Trainerize, My PT Hub and TrueCoach (claiming built-in payments, nutrition, Packages and habits
  where rivals show "Add-On" or "Partial", and "Save 20% when you commit annually" against "~16%"
  or "Varies"); a "fitr-switch" page; webinars (The Spring Surge, Built to Coach, Predictable
  Income Blueprint); and five free calculators (macros, 1RM, percentage, pace, coaching price) as
  lead magnets.
- **Which side first**: the coach. The coach pays, the client cannot enter without buying a
  programme, and there is **no client-side discovery and no in-app marketplace**.

### App Store and Play listings

| Listing | Store | Id / package | Rating and count | Released | Last updated |
|---|---|---|---|---|---|
| Fitr Client | App Store | 1548478229 | GB 5.00 / 4; US 2.33 / 3 | 19 Jan 2021 | 7 Oct 2026 (v2.0.2) |
| Fitr Coach | App Store | 1576833196 | GB 5.00 / 12; US 2.00 / 1 | 9 Sep 2021 | 7 Oct 2026 (v2.0.2) |
| Fitr Client | Google Play | com.fitr_training.client | 3.0 from 74 reviews, 50k+ installs | — | — |
| Fitr Coach | Google Play | com.fitr_training.coach | not extracted, 1k+ installs | — | — |

Seller on both App Store listings: **Fitr. Holdings Limited**. Both apps are free with no in-app
purchases listed. Client app description: "The Fitr Client app is where you achieve your training
and wellbeing goals. Follow the program your coach built for you, log your effort, and stay in
touch between sessions."

---

## What could not be verified

Gathered in one place so the gaps are visible.

- **Three social accounts out of fifty-six.** Follower counts for every platform on YouTube,
  Instagram, X and TikTok were read through the ScrapeCreators API and are in section 6. Three
  remain open: **Exercise.com's Instagram** (@exercisecom, the handle in its own footer, returns
  404), **PT Distinction's TikTok** (the request failed twice and no handle is published), and
  **TrueCoach's TikTok** (@therealtruecoach is linked in its footer but returned no profile data).
  A blank elsewhere in section 6 means no account was found under any published handle, which is
  weaker than confirmed absence.
- **Capterra, GetApp, G2 and Trustpilot review counts** — all Cloudflare-blocked. This matters
  most for PT Distinction, whose "4.9 on Capterra / GetApp / G2" and "#1 on Trustpilot" claims are
  therefore unchecked marketing, and for My PT Hub's "10,000+ 5-star reviews".
- **ABC Trainerize**: the platform percentage on client payments (the Stripe Integrated Payments
  help article returns HTTP 403; third parties say 3.5% on Pro and 10% on Free, unconfirmed); the
  exercise-library size as read from a page rather than a search rendering; push notifications as
  an explicitly stated feature; the Challenges help-article body; ABC Fitness's HQ and
  private-equity ownership beyond the Thoma Bravo press release.
- **TrueCoach**: the monthly-billing list prices; HQ and founding date (nothing on the site states
  either); the chargeback fee; whether coaches get slow-motion or annotated video review; the
  contents of the "Partner Perks" programme (the page 404s); and whether a separate app listing is
  offered at any tier.
- **Everfit**: HQ, founders, founding year and funding — none stated on the site (its Google
  advertiser name is Everfit Technologies Inc., matching the App Store developer); the
  exercise-library size (its own pages give four different numbers);
  whether badges exist as a shipped feature; a client-facing calendar view; the Enterprise
  white-label requirements; the marketplace commission; what a signed-out consumer sees on
  everfit.io/explore; and the affiliate terms as read from the live page rather than a search
  rendering.
- **My PT Hub**: client video upload of working sets, and any coach video review — no evidence
  found either way; the EverCommerce press release itself (403 and 502 to direct fetches); the
  dates of its education-provider endorsements; and whether any Play listing uses a Trainerize
  bundle id, which could not be reproduced.
- **PT Distinction**: whether its custom-branded app is a genuine separate store listing or icon
  and in-app branding; the referral terms as published by the company; any platform transaction
  fee; and any certification-body or gym-chain partnership.
- **TrainHeroic**: the entire support centre sits behind Cloudflare and returned 403 to every
  method, so the leaderboard mechanics, the StackUp body-weight-scaling formula, the $100 finder's
  fee and the $1-per-transaction affiliate fee are search-surfaced rather than directly read.
  Also unverified: push notifications, wearable integrations (notable given the Garmin
  acquisition), the marketplace payment processor, the total marketplace catalogue size, and the
  "2.1 million athletes visited the Marketplace" figure.
- **FITR**: the exact price at each step of the client slider; whether the near-zero App Store
  rating counts reflect a reset at version 2.0.2 or genuinely low volume; and the company's stated
  location, which differs between Maven (London) and the registered office (Hertfordshire).
- **Kahunas**: HQ and founding year — nothing on the site states either, and the only signal
  found is its Google advertiser name, **Kahunas FZC**, a United Arab Emirates free-zone company,
  which is where it pays for ads from and not necessarily where it is based; funding; the Rewardful
  affiliate commission rates (the terms page is Cloudflare-403); what "Health Score A.I" actually
  computes; the nature of the PureGym relationship behind the "Recommended by" logo; the named
  programme hierarchy; and whether its "in app payments" route through Apple in-app purchase.
- **FitBudd**: the HQ city (no address published, /about-us 404s); Apple's commission rate on
  Super Pro in-app purchases, which FitBudd never states; Razorpay support; client video upload of
  sets; and the $3.9m lifetime funding total.
- **Hevy**: funding; a trainer or coach count, which is published nowhere; whether the consumer
  app's streak and leaderboard amount to a game layer in the coached context; Apple Health and
  Health Connect integration; and the reported "$2M in annual revenue".
- **CoachRx**: the 2022 launch press release (HTTP 502); push notifications; client video upload
  of sets; funding; and which of its two conflicting prices for the 51–150 client tier ($149 on
  the homepage FAQ, $199 on the pricing page) is current.
- **Exercise.com**: any published price or trial; the payment processor; client video upload;
  in-app 1:1 chat; a client-facing training calendar; and whether Gold's Gym and APEC are
  partners rather than customers.
- **Playbook**: 1:1 direct messaging; push notifications; a client calendar; two of its three
  reported co-founders (its own about page names only Jeff Krahel); and any funding since 2020.
- **TrainerFu**: the payment processor; client video upload of sets; any coach video review.
- **Sidekick**: the asking price for sidekick.fit, behind a Cloudflare interstitial on the Atom
  marketplace.
- **Paid advertising on TikTok**, for every platform. The ScrapeCreators API has no TikTok
  ad-library endpoint, so that network could not be checked at all. Meta, Google and LinkedIn are
  covered in section 6. Three further limits there: Meta ad counts are **active ads on
  26 October 2026 only**, so a platform showing zero may have advertised earlier in the year;
  Google's figure is an *estimate* capped in the response at 200; and **no spend figure is public
  on any network**, so ad counts measure activity, not budget. Whether FitBudd, FITR,
  Exercise.com or TrainerFu run Meta ads under a page name other than their own could not be
  ruled out — no ad-library page was found under the company name, which is weaker than confirmed
  absence.
- **Certification-body partnerships for nine of the fourteen platforms** — searched for and not
  found, which is weaker than confirmed absence.

A browser session with real cookies would close most of the Cloudflare and 403 gaps above,
particularly the Trainerize, TrainHeroic and My PT Hub help centres and the review aggregators.

---

## Sources

All read 26 October 2026.

### Store data

- Public iTunes Search API: `https://itunes.apple.com/search?term=...&entity=software&country=gb|us`
- Public iTunes Lookup API: `https://itunes.apple.com/lookup?id=...&country=gb|us`
- Google Play store pages, GB and US storefronts, for every package id named in this report
- `https://play.google.com/store/apps/developer?id=FitBudd`
- `https://play.google.com/store/apps/developer?id=TrainHeroic+LLC`

### Social counts and ad libraries

Every call below went to the ScrapeCreators API at `https://api.scrapecreators.com`, authenticated
with an `x-api-key` header, on 26 October 2026. One credit per call; 126 credits were spent in
total. Endpoint documentation: `https://docs.scrapecreators.com/llms.txt`.

- `GET /v1/account/credit-balance` — balance before and after the run
- `GET /v1/youtube/channel?handle=|channelId=` — name, `subscriberCount`, video and view counts,
  join date, and the Twitter and Instagram links the channel publishes. Called for
  TrainerizeYoutube, truecoach (404), UC9WcVndJYeRe1Muha1oM98w (Everfit), MyPTHub,
  UC2Q2UcCtid-OkVn9-afG0Ew (PT Distinction), TrainHeroic, HevyApp, hevycoach, kahunasio,
  "fitbudd.", trainerfu, join.playbook, coachrx, exercise, PERSONALTRAINERSOFTWARE
- `GET /v1/instagram/profile?handle=` — follower and post counts under
  `data.user.edge_followed_by.count`. Called for trainerize, truecoach.co, everfit, everfitpros,
  mypthub, pt_distinction, trainheroic, hevyapp, hevycoach, kahunasio, fitbudd.app, trainerfuapp,
  joinplaybook, coachrx.app, exercisecom (404), fitr.app
- `GET /v1/twitter/profile?handle=` — counts under `legacy.followers_count`, not at the top level.
  Called for trainerize, truecoachco, geteverfit, mypthub, PTDistinction, trainheroic, hevyapp,
  kahunasio, fitbudd, trainerfu, joinplaybook, coachrx, exercise, fitrtraining
- `GET /v1/tiktok/profile?handle=` — `stats.followerCount`, `heartCount`, `videoCount`. Called for
  trainerize, therealtruecoach, everfit.io, mypthub, ptdistinction, trainheroic, hevyapp,
  kahunasio, fitbudd, trainerfu, joinplaybook, coachrx.app, exercisecom, fitr.app
- `GET /v1/facebook/adLibrary/search/companies?query=` — Meta ad-library `page_id`, Facebook page
  `likes`, and `ig_username` with `ig_followers`. Called for Trainerize, TrueCoach, Everfit,
  My PT Hub, PT Distinction, TrainHeroic, Hevy, Kahunas, FitBudd, TrainerFu, Playbook, CoachRx,
  Exercise.com, Fitr, coachwithfitr, "FitBudd Personal Trainer Software", "Fitr Training",
  "Playbook App", "Hevy Coach"
- `GET /v1/facebook/adLibrary/company/ads?pageId=|companyName=&status=ACTIVE` — `searchResultsCount`
  (total active ads), and per ad `ad_archive_id`, `is_active`, `start_date_string`,
  `publisher_platform` and a `snapshot` carrying `title`, `body.text`, `cta_text` and `link_url`.
  Called for page ids 179570012091994 (ABC Trainerize), 825464357519848 (TrueCoach by Xplor),
  1792380510832178 (Everfit), 324873511052146 (My PT Hub), 153736141492401 (PT Distinction),
  144952055597057 (TrainHeroic), 453778398520668 (Hevy), 108609668169335 (Kahunas),
  102775272355941 (CoachRx), 111907537611003 (Playbook App), and by name for FitBudd, TrainerFu,
  Exercise.com and Fitr
- `GET /v1/facebook/adLibrary/search/ads?query=&status=ACTIVE` — keyword cross-check for Fitr
- `GET /v1/google/company/ads?domain=&topic=all` — `number_of_ads_estimate` and per ad
  `advertiserName`, `advertiserId`, `format`, `firstShown`, `lastShown`. Called for trainerize.com,
  truecoach.co, everfit.io, mypthub.net, ptdistinction.com, trainheroic.com, hevyapp.com,
  hevycoach.com, kahunas.io, fitbudd.com, trainerfu.com, playbookapp.io, coachrx.app,
  exercise.com, fitr.training, coachwithfitr.com. `get_ad_details` was never passed — it costs 25
  credits a call
- `GET /v1/linkedin/ads/search?company=` — `totalAds` and per ad `advertiser`,
  `advertiserLinkedinPage`, `headline`, `description`. Called for ABC Trainerize, TrueCoach,
  Everfit, My PT Hub, PT Distinction, TrainHeroic, Hevy, Kahunas, FitBudd, TrainerFu,
  Playbook Technologies, CoachRx, Exercise.com, Fitr

Handles not in the report's earlier sources were taken from each company's own site footer:
fitbudd.com, coachwithfitr.com, playbookapp.io, exercise.com, trainerfu.com, trainerize.com,
truecoach.co, everfit.io, mypthub.net, ptdistinction.com, trainheroic.com, hevyapp.com,
kahunas.io, coachrx.app.

### FITR

fitr.training (301 to coachwithfitr.com); coachwithfitr.com — `/`, `/pricing`, `/about`,
`/client-app`, `/coach-app`, `/real-results`, `/real-results/testimonials`, `/partners`,
`/how-we-compare`, `/fitr-switch`, `/features`, `/features/programming`, `/features/communication`,
`/features/habits`, `/features/macros`, `/features/tracks`, `/features/progress-tracking`,
`/features/custom-app`, `/features/brand-kit`, `/features/storefront-program-pages`,
`/features/business-automation`, `/features/packages`, `/features/promotions`,
`/features/ai-programming`, `/features/integrations`, `/blog`,
`/blog/fitr-x-puregym-partnership`, `/blog/fitr-expansion-fundraising-concluded`,
`/blog/elite-crossfit-athlete-reggie-fasa-invests-into-fitr-training`, `/sitemap.xml`,
`/robots.txt`; support.coachwithfitr.com articles 6388938 (client photo and video upload), 9245685
(coach referral scheme), 11992016 (HYROX affiliate trial), 5050475 (download the client app),
10125580 (example programs), 6344978 (body metrics);
apps.apple.com/gb/app/fitr-client/id1548478229; apps.apple.com/gb/app/fitr-coach/id1576833196;
play.google.com/store/apps/details?id=com.fitr_training.client and `.coach`;
find-and-update.company-information.service.gov.uk/company/09759426;
mavencp.com/latest-news/maven-vcts-invest-in-fitr-healthtech-business;
thesaasnews.com/news/fitr-training-raises-1-2-million-in-funding/;
archive.org/wayback/available?url=fitr.training/marketplace (no snapshots);
youtube.com/@PERSONALTRAINERSOFTWARE.

### ABC Trainerize

trainerize.com `/`, `/about/`, `/pricing/`, `/features/`,
`/features/custom-branded-fitness-apps/`, `/education-partners/`, `/creators-influencers/`,
`/affiliate-program/`, `/blog/trainerize-affiliate-program/`, `/blog/trainerize-nasm-partnership/`,
`/blog/23w-case-study/`, `/blog/fitness-influencers/`, `/blog/tag/trainerize-partnerships/`;
trainerize.me `/` and `/find-a-trainer/`; resources.trainerize.com `/studio-faq`,
`/abc-trainerize-collections`, `/customer-success-stories`, `/tz-cobalt-customer-success-story`,
`/loreti-success-story`, `/mike-monti-success-story`; help.trainerize.com articles
17302175826196, 115004404763, 360001208803, 208689136, 360060751552, 208689066, 211162663,
26392590876692, 214738683, 6147809498004, 9140932737428, 42797720796564 (all HTTP 403 to direct
fetch, read via search rendering);
ideas.abcfitness.com/forums/167887-coach-trainer-abc-trainerize/suggestions/38395417;
abcfitness.com/about-us/; thomabravo.com press release, 15 September 2020; prnewswire.com NASM
release 301684442; similarweb.com/website/trainerize.com/;
apps.apple.com/us/app/fitness-app-abc-trainerize/id516851502;
play.google.com/store/apps/details?id=com.trainerize.Trainerize.

### TrueCoach

truecoach.co `/`, `/about/`, `/pricing/`, `/features/`, `/features/dashboard/`,
`/features/public-profiles/`, `/case-studies/`, `/case-studies/margaux-alvarez/`,
`/case-studies/taylor-m/`, `/case-studies/blacklisted-hq-case-study/`,
`/blog/introducing-voice-notes-for-personal-trainers-in-truecoach/`,
`/blog/how-to-gamify-workouts-for-better-motivation-with-ai/`, `/partner-perks/` (HTTP 404);
help.truecoach.co articles 3491685 (processing fees), 3363353 (client video uploading), 3047401
(programs), 2403707 (client experience), 9099548 (client changing schedule), 6384679 (referral
programme), 10827765 (public profile); tsgfitness.referralrock.com/v2/9/terms and `/register`;
uppromote.com/affiliate-directory/truecoach/; apps.apple.com/us/app/truecoach/id1439127794;
play.google.com/store/apps/details?id=co.truecoach.client;
similarweb.com/website/truecoach.co/; mergr.com/company/truecoach;
pitchbook.com/profiles/company/168580-72.

### Everfit

everfit.io `/`, `/pricing`, `/features`, `/about-us/`, `/affiliates/`, `/explore` (SPA, no static
content), `/webinar/`, `/webinar/programming-that-transfers/`,
`/webinar/everfit-academy-x-1-better-academy/`, `/llms.txt`; academy.everfit.io `/webinars`,
`/course/lead-generation-tool-for-coaches/course-detail`; help.everfit.io articles 4854106
(leaderboards), 11469293 (AI push-up challenge), 6866473 and 6866635 (habit coaching), 4346734
(comments for completed workouts), 4620515 and 4620472 (workout builder), 5829094 (client app
track a workout), 5635436 (Today screen), 5684968 (processing fees), 5754312 (advanced custom
branding), 9711702 (smartwatch app), 4604646 (health app integration), 5161301 (steps tracking),
4701854 (own demo video), 6323554 (logged activities), 4436288 (referral programme), 5369004
(public client invite link), 2951524 (assign tasks), 3661707 (Autoflow overview);
help-marketplace.everfit.io articles 12601836 and 9234618; blog.everfit.io
`/everfit-vs-trainerize-vs-truecoach`, `/everfit-may-2026-new-features`,
`/end-of-year-coach-spotlight-2025-holistic-coaching-in-practice`,
`/how-to-make-the-most-of-everfit-exercise-library-upgrades`,
`/3-exciting-upgrades-for-exercise-library`;
apps.apple.com/us/app/everfit-train-smart/id1438926364;
play.google.com/store/apps/details?id=com.everfit and `.coach`;
similarweb.com/website/everfit.io/; pitchbook.com/profiles/company/507212-74;
getlatka.com/companies/everfit.io; npefitness.com/partners/everfit/.

### My PT Hub

mypthub.net `/`, `/pricing/`, `/customers/`, `/features/`, `/features/workout-features/`,
`/features/client-management-features/`, `/features/communities-feature/`,
`/features/marketplace-features/`, `/features/automated-client-check-ins/`, `/all-updates/`,
`/affiliates/`, `/blog/evercommerce-acquires-my-pt-hub/`, `/blog/refer-a-friend-earn-cash/`,
`/blog/top-tips-to-make-our-affiliate-scheme-work-for-you/`,
`/blog/earn-up-to-100-with-the-my-pt-hub-affiliate-program/`;
pages.mypthub.net/get-a-free-program-template/; mypthub.referralrock.com/v2/1/register;
youtube.com/c/MyPTHub; facebook.com/groups/834245170774560;
apps.apple.com/us/app/my-pt-hub/id1473947709;
play.google.com/store/apps/details?id=net.mypthub.kilo;
pyxissoftware.com/post/pyxis-software-group-acquires-evercommerces-fitness-solutions;
investors.evercommerce.com news release (HTTP 403); prnewswire.com 301185240 (HTTP 502);
marketscreener.com EverCommerce / My PT Hub $11.7m; crunchbase.com/organization/my-pt-hub;
strengthandconditioningeducation.com/my-pt-hub/.

### PT Distinction

ptdistinction.com `/`, `/pricing`, `/features`, `/our-story`, `/custom-branded-fitness-app`,
`/compare-pt-distinction-truecoach`,
`/pt-distinction-trainerize-everyfit-truecoach-comparison`,
`/blog/how-to-build-your-personalized-exercise-library-in-pt-distinction`;
youtube.com/channel/UC2Q2UcCtid-OkVn9-afG0Ew;
apps.apple.com/us/app/pt-distinction/id973466681;
apps.apple.com/us/app/online-personal-training/id1249635424;
news.marketersmedia.com/pt-distinction-launches-refer-a-friend-scheme/89081580;
appbrain.com/app/pt-distinction/com.ptdistinction; ptpioneer.com/personal-training/tools/pt-distinction-review/.

### TrainHeroic

trainheroic.com `/`, `/coach/`, `/athlete/`, `/pricing/`, `/create/`, `/grow/`,
`/become-a-seller/`, `/athlete-pro-tools/`, `/coach-faq/`, `/p2p-network/`;
marketplace.trainheroic.com `/` and the team pages `/workout-plan/team/ftw-thrive`,
`/patreon-4x-a-week-program`, `/mflh`, `/mflh-affiliate-program`, `/built-like-a-mf`,
`/catalyst-athletics-club`, `/the-barbell-wod`, `/lift-run-bang-all-access-bundle`;
support.trainheroic.com articles 18170915515917 (programming leaderboards), 18156555844237
(Athlete Pro StackUp), 18156511371917 (hiding scores), 18156549307277 (marketplace matching,
attributions and affiliate links), 39620825088141 (Athlete Pro nutrition) — all Cloudflare 403,
read via search rendering;
peaksware.com/garmin-acquires-trainingpeaks-and-trainheroic-leading-endurance-and-strength-training-platforms-for-athletes-and-coaches/;
dcrainmaker.com/2026/07/garmin-acquires-training-trainheroic.html;
slowtwitch.com/industry/garmin-buys-trainingpeaks-and-trainheroic/;
escapecollective.com/garmin-buys-trainingpeaks-and-trainheroic/;
apps.apple.com/us/app/trainheroic-strength-training/id955074569;
play.google.com/store/apps/details?id=com.TrainHeroic.TrainHeroic; youtube.com/c/TrainHeroic;
nsca.com/membership/pro-deals/.

### Hevy and Hevy Coach

hevycoach.com `/`, `/pricing`, `/about-us/`, `/features/client-chat/`,
`/features/workout-program-builder/`, `/features/video-exercise-library/`,
`/features/client-app/`, `/features/invite-link/`, `/compare/`, `/online-fitness-coach/`,
`/personal-trainer/`, `/gym-fitness-studio/`, `/school-university/`,
`/health-and-wellness-influencers/`, `/sitemap_index.xml`; hevyapp.com `/about-us/`, `/press/`,
`/features/`, `/features/trainer-platform/`, `/features/strength-coach/`,
`/features/gym-consistency/`, `/features/gym-leaderboard/`, `/features/gym-selfie-footage/`,
`/affiliate/`; apps.apple.com/us/app/hevy-coach-for-coaches-pt/id6502961756;
apps.apple.com/us/app/hevy-workout-tracker-gym-log/id1458862350;
play.google.com/store/apps/details?id=com.hevy and `com.hevycoach.app`;
youtube.com/@hevycoach and youtube.com/@HevyApp.

### Kahunas

kahunas.io `/` (single-page site; `#features-section`, `#plan-section` anchors);
help.kahunas.io/en/articles/236-kahunas-referral-program;
kahunas.getrewardful.com/terms (Cloudflare 403); stripe.com/customers/kahunas;
apps.apple.com/gb/app/kahunas/id1638377758 (including version history);
apps.apple.com/us/app/unlmtd-performance/ (bundle com.kahunas.unlmtdcoaching);
play.google.com/store/apps/details?id=com.cofox.kahunas.Kahunas; youtube.com/@kahunasio;
blog.kahunas.io/sitemap-1.xml.

### FitBudd

fitbudd.com `/`, `/pricing`, `/feature-workouts`, `/your-brand-your-app`,
`/fitbudd-partner-program`, `/personal-trainers-near-me`, `/coach-stories/`,
`/coach-stories/how-amy-hollings-went-from-0-to-1-000-personal-training-clients-without-burning-out`,
`/post/best-online-personal-training-platforms-for-coaches`, `/sitemap.xml`; help.fitbudd.com
articles 5804360 (how clients gain access), 4086565 (types of workouts), 5804383 (segments),
10113898 (challenges and leaderboard), 16818745 (body transformation challenge), 16839298
(activity challenge), 4086628 (billing clients), 4152399 (iOS app payments), 6491639 (video
message limits), and collection 3252413 (client app);
apps.apple.com/us/app/fitbudd-client/id1588719496;
apps.apple.com/us/app/fitbudd-coach/id6748600009;
apps.apple.com/us/app/bossfitamy/id6479200038;
play.google.com/store/apps/details?id=com.fitbudd.app and `com.fitbudd.coach` and
`com.bossfitamy.app`; youtube.com/@fitbudd.;
inc42.com/buzz/fitbudd-raises-funding-to-help-fitness-coaches-engage-better-with-customers/;
facebook.com/groups/fitbudd.

### TrainerFu

trainerfu.com `/`, `/about.html`, `/pricing.html`, `/features.html`,
`/habit-coaching-software.html`, `/white-label-fitness-app.html`, `/trainerize-alternative.html`,
`/blog/`, `/blog/best-app-for-personal-trainers/`, `/js/main.js` (price table),
`/sitemap.xml`, and the 404 probes `/affiliate.html`, `/affiliate-program.html`,
`/referral.html`, `/refer.html`, `/partners.html`; help.trainerfu.com/en/;
apps.apple.com/us/app/trainerfu-for-personal-trainer/id807834256;
play.google.com/store/apps/details?id=com.trainerfu.android.

### Playbook

playbookapp.io `/`, `/about`, `/billing-details`, `/creator-agreement`, `/download`,
`/updates/members`, `/case-studies/mackenzie-wells`, `/case-studies/alicia-erickson`,
`/case-studies/judd-lienhard`, `/case-studies/melania-antuchas`, `/sitemap-0.xml`, plus the
homepage JSON-LD;
techcrunch.com/2020/10/14/playbook-a-fitness-platform-that-puts-creators-first-raises-9-3-million/;
finsmes.com/2020/10/playbook-raises-9-3m-in-series-a-funding.html;
apps.apple.com/us/app/playbook-trainers-workouts/id1107266414;
apps.apple.com/us/app/playbook-creator/id1166632935;
play.google.com/store/apps/details?id=io.playbookapp.android.

### CoachRx and OPEX

coachrx.app `/`, `/pricing`, `/features`, `/podcast-network`,
`/articles/coachrx-referral-program`, `/sitemap.xml`; opexfit.com `/`, `/opex-method`,
`/ccp-level-1`; learnrx.app/courses/coaching-certificate-program;
apps.apple.com/us/app/coachrx-by-opex-fitness/id1544150077;
play.google.com/store/apps/details?id=app.coachrx.android; PR Newswire release 301525109 (HTTP
502).

### Exercise.com and Daxko

exercise.com `/`, `/about/`, `/features/`, `/platform/pricing/`,
`/support/topics/affilliate-sales-commissions/`, `/support/affiliate-program-refersion/`;
exercise.refersion.com/;
daxko.com/news/daxko-broadens-boutique-fitness-market-offering-with-acquisition-of-exercise-com;
vistapointadvisors.com/news/exercisecom-announces-acquisition-by-daxko;
athletechnews.com/daxko-acquires-exercise-com-boutique-fitness-tech/;
apps.apple.com/us/app/daxko-exercise/id559019054; capterra.com/p/152284/exercise-com/.

### Sidekick (no product found)

sidekick.fit (HTTP 302 to domains.atom.com; `dig sidekick.fit NS` returns ns1.atom.com and
ns2.atom.com); trainwithsidekick.com (`dig A` and `dig NS` both empty);
sidekick.fitness (empty client-rendered shell; `manifest.json` reads "Sidekick Fitness"; assets
are Create React App v3-era builds); sidekicktraining.com (corporate workforce training, "Powered
by Enable Education"); play.google.com/store/apps/details?id=com.trainerize.sidekickfitness;
apps.apple.com/us/app/sidekick-platform/id6504539500; betalist.com/startups/sidekickco.

---

## What this changes

The new data does not overturn the summary, but it corrects the scale order and settles the
question the report could not answer: how these companies grow.

**Store size and audience size are different orders.** TrainHeroic sits fifth on store evidence
and first on Instagram, with 66,344 followers and 25,100 YouTube subscribers against ABC
Trainerize's 24,247 and 10,700 — and Trainerize has roughly thirty-eight times TrainHeroic's iOS
rating count. Trainerize's frozen "400,000+ personal trainers" claim looks thinner still beside a
24k Instagram and a 3k X account. **Everfit is smaller than it says and bigger than it looks**:
its "380,000 coaches" remains unsubstantiated marketing, but 141 active Meta ads and four years of
unbroken Google buying make it the most aggressive paid acquirer in the market, which is a more
honest reading of its traffic than any coach count. **Exercise.com and FITR are larger than their
store numbers suggest** — both run around 200 Google ads and nothing else visible, so FITR's
near-empty App Store footprint is not a failing product but a product whose whole funnel is Google
search plus the PureGym and HYROX partnerships.

**Who is buying growth, and with what promise.** Eight platforms run Meta ads: Everfit (141),
Kahunas (58), TrainHeroic (35), ABC Trainerize (29), My PT Hub (28), CoachRx (15) and PT
Distinction (12, continuously since August 2025). Four more buy Google only — Exercise.com, FITR,
FitBudd and TrueCoach. The promise is remarkably uniform: a free trial in the headline, and admin
relief in the body. My PT Hub sells "Save up to 80% of your admin time"; Kahunas sells never
missing a check-in; Everfit sells running the business "on your couch". CoachRx is the one
different pitch, and it is a poaching pitch — "Upgrade Your Coaching Software Now … We offer free
transition" — which, with FitBudd's sixty competitor pages, confirms an active market in moving
trainers off incumbents.

**Two platforms buy nothing at all, and the difference matters.** TrainerFu's zero ads on every
network confirm the near-static read. **Hevy's zero ads are the real finding**: no Meta, no Google,
no LinkedIn, and it still holds the largest consumer following in the set — 60,085 Instagram,
25,600 TikTok, 5,424 X. It is the only organic growth story here, and the only one not paid for.
Its coaching product is tiny by comparison (Hevy Coach: 1,221 Instagram followers, 56 YouTube
subscribers), which is what it looks like to build the consumer side first and let coaches arrive.
TrueCoach is the mirror image: zero Meta ads, a falling Similarweb rank, a published coach count
that has gone *down*, and Google ads paid for by a holding entity, **AI Sky US Bidco Inc**, rather
than the brand. That is a product being run for cash.

**What bears on RepGarden's scope.** Three points, and one of them is the useful one.

*Invite-only, trainer-first gives up nothing.* Not one platform in the set buys consumer demand
for its own brand. Every ad read is aimed at the trainer. The only paid consumer acquisition
anywhere is delegated — Playbook's creators and TrainHeroic's marketplace coaches buying their own
ads — so being invite-only forgoes a channel nobody is actually using.

*No payments in the app costs nothing in positioning.* Across 318 active Meta ads from eight
platforms, payments never appear as the promise. They sit inside feature lists, behind admin
relief, check-in reliability and nutrition. Nobody is winning trainers on billing.

*Video of a set with trainer feedback is unclaimed in paid messaging too.* This is the strongest
new signal. In every ad read across Meta, Google and LinkedIn, **not one leads with form review,
video feedback or technique**. TrainHeroic, which has "Video review" as a headline site feature,
advertises it only inside a generic list — "programming, feedback, tracking, and communication in
one place". Kahunas's nearest ad is about reading back logged sets and reps, not watching them.
So the gap the report found in the products is also a gap in the market's messaging: the upload
exists on five platforms and none of them thinks it is worth buying attention for. That is either
a mispriced opportunity or a sign that trainers do not ask for it — and the honest answer is that
the ad libraries cannot tell us which.

One caution against over-reading all of this. Ad counts are activity, not budget; no network
publishes spend. Meta figures are active ads on 26 October 2026 only, so a platform at zero today
may have run a flight in the spring. And competing on paid trainer acquisition against Everfit's
141 ads was never the plan — the data mainly says that the crowded ground is bought, and the one
company that grew without buying did it by owning the consumer side first.
