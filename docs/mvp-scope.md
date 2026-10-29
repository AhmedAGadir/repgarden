# MVP scope

What the first version of RepGarden does, what it leaves out and why, and the decisions behind both. Agreed by Ahmed on 26 October 2026 from the first discovery call with Benji (24 October) and his own scoping; it replaces the wider "agreed build scope" the [project brief](project-brief.md) carried before. Everything here is subject to the market and compliance research still in progress; a decision changed by that research is changed here, not appended.

**Status: scoping. Nothing in this document is built.**

## The product in one paragraph

A trainer runs their clients from a web app: invites them, builds programmes out of workouts and exercises, assigns them to a calendar, and sees how each client is getting on. Clients use a phone app: they open it to a calendar, do today's workout, log their sets, film a working set for the trainer to look at, and watch their own progress. Benji is the first trainer. Messaging stays on WhatsApp.

## In the MVP

| Area | Trainer, on the web | Client, on the phone |
|---|---|---|
| Accounts | Invite or create clients; trainer and client roles; a trainer sees only their own clients. **Invite-only:** a client gets in only through their trainer; there is no self-serve sign-up in the client app | Sign in to an account the trainer set up; profile and goals |
| Programmes | Exercise → workout → programme; assign a programme to a client with dates | — |
| Exercise library | A stock library of exercises with demonstration clips, the trainer's own clips on top, and a fallback image for any exercise without a clip. Where the stock library comes from is being researched (see below) | Watch the demonstration from inside the workout |
| Doing the work | — | Calendar on opening; today's workout; log each set (weight, reps, a note); mark the workout complete; rest days and empty days designed, not blank |
| Video of a set | Watch a client's clip; reply with a short note pinned to a moment in the clip (a timestamp the client can tap to), or a mark of approval; an inbox of clips waiting for a reply, oldest first | Record or upload a short clip against a set, with a note; a push notification when the trainer replies |
| Progress | Per-client dashboard: adherence, loads over time, personal bests | The same, for the client's own training |
| Check-ins | See a client's check-in photos, weight and measurements over time | Check in with photos, weight and measurements if they want to. Agreed 26 October 2026; the detail is still to be scoped |
| Goals | Set goals with a client | See their goals and progress towards them |
| Reminders | See who missed a workout | Push notification for a scheduled workout; a nudge after a missed one; a word when one is done. When and how often to remind is being researched (see below); it must not be noisy |
| Accessibility | Built in from the first screen on both: labels, contrast, text scaling, screen-reader order | |

The reply on a set is not messaging. It is a comment attached to one piece of work, the way a reviewer comments on a line. Without it the upload has no audience and the feature decays.

**Where the differentiator actually is**, from the [market research](research/2026-10-26-trainer-client-apps/findings.md) (26 October 2026): uploading a video of a set is a named feature on five platforms — TrueCoach, Everfit, PT Distinction, TrainHeroic and FITR itself (up to 500 MB, attached to a training performance, with coach comments). Benji's complaint about Fitr is that it is clunky, not that the upload is missing. What no platform has, verified, is a good review experience: annotation, drawing, frame-by-frame, or a reply pinned to a moment in the clip. The upload is table stakes among strength-focused tools; the review is the open gap, and that is where RepGarden's "watch a set, reply" should be designed to be better than a chat thread. Separately, the market leader (ABC Trainerize) has no client video upload at all.

## Out of the MVP, and why

| Left out | Why, in one line |
|---|---|
| Payments | Clients already pay Benji, and the app is free to trainers initially. Adding payments later is routine (Stripe with RevenueCat has been done before); what it would add now is Apple's in-app-purchase rules and store commission on the critical path. Decided 26 October 2026. |
| Messaging and chat | WhatsApp exists and his clients are on it. RepGarden will not rebuild it. |
| Gamification | The next phase, designed on top of a working core; the garden and the mascots come after people can log a workout. Its base is leaderboards, streaks and XP, which is basic but already more than the market has, plus challenges; whether challenges are set by the trainer or run app-wide for everyone is open. Decided 26 October 2026. |
| AI video analysis | A different product. The trainer's eye is the feature. |
| Meals, nutrition, calorie counting | Not what Benji coaches through the app. |
| Localisation | Setting it up "from the start" costs on every string and screen for an app with one trainer's clients in one city. Accessibility is the opposite case and is in. |
| Bookings and session scheduling | Removed from the earlier brief with payments; sessions are arranged off the app for now. |
| Public trainer discovery, marketplace | Trainers invite their own clients. |
| Wearables, offline sync, external calendars | Later, if ever. |

The point for the build series: a few features that work beat an everything-soup, and leaving things out is a decision to show, not an apology.

## Required by the stores

From the [store compliance research](research/2026-10-26-store-compliance/findings.md), 26 October 2026. These are in the MVP because Apple and Google will not approve the app without them.

| Requirement | Why | Where |
|---|---|---|
| A demo trainer and a demo client login in the review notes | An invite-only app is allowed on both stores; reviewers must be able to get in (Apple 2.1(a), Google's sign-in details form) | Submission |
| No price, paywall or payment link anywhere in the client app | Pre-recorded programmes and videos count as digital content; in-app they would carry 15–30% commission. When payments return, they return on the web, as every competitor does | Both apps |
| One listing, multi-trainer, published by Gadir Tech Ltd | Apple 4.2.6 rejects one-app-per-trainer templates; RepGarden is one app that many trainers use | Store listing |
| Report and block controls on uploaded video, terms accepted before the first upload, published contact details | Both stores treat a client's upload as user-generated content even when only the trainer can see it (Apple 1.2; Google's UGC policy) | Mobile app |
| Account deletion in the app and on the web | Required by both stores | Mobile app, website |
| Google's Health apps declaration; a "not a medical device" line; the regulated-device question answered no | It is a fitness app, not a medical one, and must say so | Submission, website |
| Adults only at launch | The UK Children's code covers general fitness and wellbeing apps; under-18 clients would bring it into scope. Ask Benji whether he has any | Accounts |

## Stack and repository layout

Decided 26 October 2026. One language across all three apps and the backend, tools Ahmed has shipped with before, and the fewest moving parts for a two-app product with a shared database.

- **Client app:** Expo (React Native), iOS and Android from one codebase. Expo Notifications for push.
- **Trainer web app:** Next.js.
- **Backend:** Supabase — auth, Postgres, storage, row-level security. RLS is how "a trainer sees their clients' data and a client sees only their own" is enforced in the database rather than in app code.
- **Video:** compress on the device before upload, resumable uploads to Supabase Storage, clips kept short by design (a set, not a session). If transcoding or playback becomes a problem, Cloudflare Stream or Mux is the step up.

Everything RepGarden lives in this one repository:

```
repgarden/
  docs/              brief, scope, epics, progress (this folder)
  apps/mobile/       the client app (Expo)
  apps/trainer/      the trainer web app (Next.js)
  apps/website/      the public site: landing, support, privacy, account deletion
  packages/shared/   types, validation and anything both apps use
  supabase/          schema, migrations, policies, edge functions
```

The `apps/` and `packages/` folders do not exist yet; they are created when the scaffolding epic is requested.

## Proposed: how long a video is kept

Proposed by Ahmed on 26 October 2026, not yet decided. Storage is the one cost that grows with use, and a clip of a set is only useful for a short time.

- A clip is deleted **seven days after the trainer has viewed it**, unless the trainer marks it to keep.
- A clip the trainer never opens is deleted after **30 days** regardless, so storage cannot grow unbounded on an inactive trainer.
- The set's logged data (weight, reps, note, the trainer's reply) is kept forever; only the media goes. A poster frame of the clip is kept so the history still shows that a video was there.
- The client is told the rule when they upload, in one line.

This also serves data minimisation under UK GDPR, which the compliance research will say more about.

## Still to decide, and what decides it

| Question | Decided by |
|---|---|
| The video retention rule above | Ahmed, after the compliance research |
| Brand direction and the mascots | The branding work, after Benji's second call. The colours are decided: see [colours](brand/colours.md) (28 October 2026) |
| Which stock exercise library to use, and what it costs | Ahmed, from the [exercise library research](research/2026-10-26-exercise-library/findings.md) (26 October 2026). It recommends RepDB's free tier plus wger for nothing, or GymVisual direct at about £205 for 300 GIFs; it rules out free-exercise-db's images, the ExerciseDB GIF mirrors and every streaming-only API |
| How the reminder engine decides when to ping, and how to congratulate | Ahmed, from the [reminder timing research](research/2026-10-26-reminder-timing/findings.md) (26 October 2026). It proposes a fixed rule set, one push a day and four a week, quiet hours, back-off, spendable skips, and no learning in the first version; spaced repetition does not transfer |
| What a check-in contains | Scoping with Benji |
| The rules of the game layer: the story, what grows, what happens when a client stops, the economy, the screen | Ahmed, from the [game design research](research/2026-10-27-game-design/report.md) (27 October 2026, twenty-two growing games). Its proposals are recorded in [game design](game-design.md), marked proposed until decided: the client is the gardener, one vegetable per programme block, growth stalls and never dies, sessions counted against the plan rather than days, one unbuyable currency, two screens |
| Benji's avatars and what sells to each | The second discovery call |

## Decisions recorded here

- 26 October 2026 — market research in: video upload is common, video review is not; gamification is thin (3 of 14 have a real layer, none have points, levels or avatars); nobody bills clients through Apple; growth is trainer-first on eleven of fourteen platforms.
- 26 October 2026 — the app is free to trainers initially; the client gets a push when the trainer replies on a set; gamification's base is leaderboards, streaks and XP plus challenges. Ahmed, after reading the market report.
- 26 October 2026 — invite-only confirmed: the client app has no self-serve sign-up; clients come through a trainer, as on FITR, TrueCoach and Trainerize. Both stores allow it with a demo login for review. Growth in this category is trainer-first (the market research), so the marketing website sells to trainers and the store listing is secondary.
- 26 October 2026 — the store requirements above added from the compliance research. Ahmed to decide on under-18 clients.
- 26 October 2026 — payments out of the MVP; messaging out; gamification to the next phase; localisation out, accessibility in; stack chosen; monorepo layout agreed. Ahmed.
- 24 October 2026 — client video upload against a set is in; messaging is not rebuilt; branding is open. From the first call with Benji.
