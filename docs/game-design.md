# RepGarden game design

The rules of the vegetable garden that sits on top of the training. This page holds the decisions for the game layer; the [MVP scope](mvp-scope.md) owns what is in the first release, and the [game design research](research/2026-10-27-game-design/report.md) (27 October 2026, twenty-two growing, tending and walking games) is the evidence behind each line here. Everything below is **proposed**, from that research, until Ahmed decides; the status line of each decision says so.

## The box the game is designed inside

Settled with Ahmed on 27 October 2026, before the research:

- The client plays, not the trainer. Every game event is derived from what the trainer already does (set the programme, comment on a set, set a challenge) and what the client already logs. The trainer gets no new work.
- The venue is the gym: one hand, a glance of a few seconds between sets, a longer sit-down after the workout and in the evening. Never a locked-in session.
- The game only sees what the app records: sessions done against sessions planned, sets logged, check-ins, personal bests. Not effort, not form.
- Rest days are prescribed. Anything daily punishes the rest the trainer asked for.
- The app is free with no shop, so nothing in the garden is for sale.
- One simple scene at a time; full-width controls; no drill-down menus.
- The theme is vegetables and growth. The name carries it: rep, garden.

Tests every mechanic has to pass: zero trainer cost; glanceable; endogenous value (every reward is spendable on something that matters inside the garden); recoverable punishment; true to training (never rewards worse training); fair (only inputs every client can do equally); themed.

## The decisions

| # | Decision | Proposed answer | Status |
|---|---|---|---|
| 1 | The story: is the client the plant or the gardener? | The client is the gardener; the vegetables are theirs, not them. Each client has a plot. The trainer's programme is, without the trainer doing anything, the season's planting plan. One hero vegetable per programme block, named and chosen by the client, carries the identity. Nothing on screen is a verdict on the client. | Proposed, 27 October 2026 |
| 2 | The unit of play | Nested. The session is the watering: one planned session logged is exactly one unit of growth and one seed, and nothing else produces either. The week is a bed: planned sessions shown as cans to fill, full when the plan is met whatever the plan was. The programme block is the season: one vegetable planted when the block starts, a growth stage per session (five visible stages, scaled to the block's length), harvested at the end into the client's permanent larder. Per-lift plants wait for a later phase. | Proposed, 27 October 2026 |
| 3 | Absence | Stall, droop, never die; count sessions, not days. A missed planned session stalls the vegetable. A week with nothing logged makes it droop, and the next logged set revives it. Nothing dies and the larder is permanent. No daily streak: the count is weeks in which the plan was met, shown as a percentage of planned sessions done. A pause the client switches on for holidays and injuries. A return after a gap is rewarded, never shown a broken counter. The one decay that exists targets gaming the game: junk sets logged in a row grow nothing, and a day counts once. | Proposed, 27 October 2026 |
| 4 | The economy | One currency, seeds, earned only by logging planned sessions, with a bonus on harvest. Seeds buy the next vegetable, a second bed, pots and garden furniture, and the choice of design for each, free to change afterwards. Nothing is purchasable and there is no second currency. A trainer's comment on a filmed set is sunshine: it arrives when the trainer chooses, which makes it the surprise. The catalogue is planned for months (seasonal vegetables), not days. | Proposed, 27 October 2026 |
| 5 | The screen | Two screens, the same garden at two distances. Between sets: a single plant in a single scene, one tap. After the workout and in the evening: the plot seen from above, one bed per week, the larder. No isometric world and no map. | Proposed, 27 October 2026 |
| 6 | Mechanics | In the MVP: focus (the trainer's session is the goal, every logged set visibly does something, progressive overload is the challenge and the trainer supplies it); the lookback after every workout (what grew, the sets, one photo, how it felt in one tap, unscored; rolled up on Sunday); surprise that only adds (sunshine, rare seeds, something changed on return); time as seasons, never a stopwatch; freedom (choose and name the vegetable, the pot, the bed design); the hold-to-water gesture for logging a set. Later: opt-in stakes (a weekly commitment for a bigger harvest, self-reported, loss capped at the bonus); the allotment (clients' plots side by side, ranked by adherence to each person's own plan, never by volume); trainer-set challenges, co-operative, opt-in, with a participation reward. Never: speed bonuses, anything the trainer must set up for the game, blame that transfers between clients. | Proposed, 27 October 2026 |
| 7 | The MVP cut | Build first: one plot, one vegetable per block, five stages, harvest to the larder; session = watering = seed; stall, droop, never die; the week as a bed with a percentage; two screens; the lookback; seeds spent on the garden; sunshine on a trainer comment; choose and name the vegetable; the hold-to-water gesture; the pause. Second phase: the allotment, trainer challenges, opt-in stakes, per-lift plants, seasonal catalogue, fuller sound. Never: a daily streak, anything that dies, a verdict on the client, rewards for speed or volume beyond the plan, a currency for sale. | Proposed, 27 October 2026 |

## Things to watch out for

From the games' own players, in the research:

- Adding taps to a one-press loop. Forest's December 2025 rebuild added daily logins and claim animations and lost five-year users. Between sets, every tap is multiplied.
- The event treadmill. Grow a Garden's developer admitted weekly events were burning players out; Gardenscapes players dismiss "a stack of popups" before they reach the garden.
- Asserting a failure the app cannot prove. Flora's rating problem is false kills. A set done but not logged must never wither anything.
- The shop that empties in a week. Content exhaustion is the retention cliff in the habit apps.
- The game displacing the goal. Duolingo users "better at protecting a streak than learning the language".
- Blame that transfers. Habitica's misses damage friends; Township teams kick members who fall behind.
- Density. Walkr's three currencies across five systems; Township's home screen as a shop window.

## Open questions

- The vegetable's visual stages and the plot's look: the branding work, after Benji's second call.
- Whether the lookback's photo is the same upload as the filmed set, or separate.
- The name of the currency.
