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

- The vegetable's visual stages and the plot's look: **decided 2 November 2026, flat vector.** From the concept sheets of 1 November (`GadirLabs - RepGarden UI concepts - 1 Nov 2026` on Ahmed's Desktop), Ahmed chose the flat vector style: bold rounded shapes, thick dark outlines, a cream screen, the carrot with muscles as the character. The screen is animated by moving still illustrations (a hop, a scale-up per stage, a glow behind a personal best) with a sound and a haptic, not by frame animation. The share grid: hue is the vegetable, lightness is how the session went, gold is a personal best with nothing inside it, bare soil a missed session, slate a rest day. Pixel art and sprite animation go to the later pool, to revisit once people have used the flat version. Next: the carrot's states as separate still illustrations from one reference (sprout, growing, full, gold with muscles), then the pot, the plot squares and the other vegetables in the same style.
- Whether the lookback's photo is the same upload as the filmed set, or separate.
- The name of the currency.

## Ahmed's mechanics, 1 November 2026 (ideation, not yet a decision)

Told to Claude on 1 November 2026, before Benji's second call; recorded as said, with where each idea meets the box above. Nothing here changes the proposed answers until Ahmed decides.

- **A character to feed.** Mrs Babushka, a frail old woman in a cottage by the plot, drawn in a cartoon or pixel style (art styles to be chosen from concept sheets). The client is a farmer. Each week's harvest is delivered to her and she gets better; at the start of every week she is unwell again. The weekly reset is the loop.
- **Seeds and sprouting.** Seeds arrive each week, delivered by someone. They sprout on the training days the coach has set. Kinds of seed map to kinds of training: fruit for cardio, vegetables for lifting, as a first idea.
- **Growth per set.** A vegetable grows as the client trains, set by set. Regular training makes it strong; a personal best makes it visibly muscular, perhaps golden; missed sessions leave it feeble and weak, possibly with flies on it.
- **The weekly harvest view.** A Forest-style isometric view of each week's plot showing that week's harvest, kept as a memory.
- **Sharing.** A Wordle-style export: a plain coloured grid with no borders, gold for a personal best, vivid orange for a good session, pale orange or brown for a poor one.
- **A wager on feeling.** At the start of a session the client says how they feel. Feeling great and training great earns the expected reward; feeling bad and training well anyway earns more. Selling the harvest may bring in money or a bonus to growth.

Where it meets the box: the loop is weekly and rest days are untouched (the box's "never daily"); the growth-per-set and the personal best are what the app records (the box's "only what the app records"); the feeling check is the lookback's "how it felt in one tap" moved to the start of the session, where it is also the readiness note a trainer can use. Where it departs from the proposed answers: a character whose health is a weekly verdict sits close to "nothing is a verdict on the client" (decision 1) and to "stall, droop, never die" (decision 3); feeble vegetables with flies are a visible punishment the research asked to keep recoverable; the isometric week sits against decision 5's "no isometric world and no map", though a seven-square row is far smaller than a world; seeds delivered weekly rather than earned by logging changes the economy in decision 4; cardio as fruit depends on the programme having cardio at all. The share grid and the lookback are compatible as they stand.

