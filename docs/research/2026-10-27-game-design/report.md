*Research · 27 October 2026*

# What the best growing games do, and what a gym app can borrow

Markdown twin of `report.pdf`, generated from the same source by `report/gen.py` and `report/tomd.py` on 27 October 2026. Charts are tables here; the data behind every figure is in `apps.json` and `report/store-meta.json`, and every claim's source is in `findings.md`.

Twenty-two growing, tending and walking games read on one day: what grows, what happens when you stop, what you earn and spend, how much is on the screen, and what their players complain about. Written for the RepGarden game-design stage, where the vegetable garden gets its rules.

Prepared by gadirlabs**.** Ahmed Gadir · gadirlabs.io · Store figures are the GB App Store on 27 October 2026; mechanics are from each game's own pages, help centre or wiki; complaints are quoted from reviews and Reddit with a source for each. Anything that could not be confirmed is marked.

*Why this report*

## The questions the garden has to answer.

RepGarden's research found that none of the fourteen trainer platforms has a character, a world, or anything that grows: their game layers are streaks, badges and leaderboards bolted on with no theme. RepGarden's theme is decided, vegetables and growth, and this stage turns it into rules. Before inventing them, we read the games that already make millions of people tend something, and the habit apps that grow a plant or a creature out of real-life behaviour.

### The box the game is designed inside

| Constraint | What it means for the design |
|---|---|
| **The client plays, not the trainer** | Every game event is derived from what the trainer already does and what the client already logs. The trainer gets no new work. |
| **The venue is the gym** | One hand, a glance of a few seconds between sets; a longer sit-down after the workout and in the evening. Never a locked-in session. |
| **The game only sees what the app records** | Sessions done against sessions planned, sets logged, check-ins, personal bests. Not effort, not form. |
| **Rest days are prescribed** | Clients train two to five times a week. Anything daily punishes the rest the trainer asked for. |
| **Free, no shop** | No paid currency, so the economy can be honest: everything earned is earned by training. |
| **One simple scene** | Full-width controls, no drill-down menus, tasteful rather than busy. |

### What we needed to learn

For every game, the same thirteen questions: what is the unit of play; what does a session look like; what happens when you stop coming and how you recover; what you earn, what it buys and whether that feeds back; stakes, risk and chance; progression; social; freedom and identity; the one signature interaction; the UI type and how dense the screen is; sound and feel; how big it is and what players say; and what transfers to a gym app.

### The decisions this report feeds, in order

| # | Decision | Page |
|---|---|---|
| 1 | The story: is the client the plant, or the gardener? | 4 |
| 2 | The unit of play: what in the training grows what in the garden | 5 |
| 3 | Absence: what withers, how fast, and how it is recovered | 6 |
| 4 | The economy: what you earn and what it buys | 7 |
| 5 | The screen: which UI type fits a glance between sets | 8 |
| 6 | Surprise, risk, social and freedom: which mechanics, and when | 9 |
| 7 | The MVP cut, and what to avoid | 10 |

> Page 11 is the theming argument, written for the video. Pages 12 onwards are the evidence: the games one by one, their size, and what their players say. The decisions themselves are recorded in the RepGarden repository, not here.

*Summary*

## Three things the growing games tell us.

- 1of 22**takes back what you built when you stop** Habitica, with hit points lost for every missed day. It is the lowest-rated app in the set at 4.04. The two famous punishers, 2009 FarmVille and the 1996 Tamagotchi, are closed or had the death removed. In every surviving garden, a missed day **stalls** growth or leaves a gap; nothing withers to nothing.

- 5of 22**have a daily streak** Duolingo, Finch, Pokémon GO, Sweatcoin and Habitica. Three of those are among the four lowest-rated apps here. The two that score well let you switch the streak off or freeze it, and Duolingo's own numbers say forgiveness lifts retention. A 1,031-upvote thread calls the daily streak the thing people quit over.

- 1=1**unit of effort, one unit of growth** Gardenscapes gives exactly one star per level and will not sell stars at any price; Finch's stones cannot be bought; Stardew has no shop at all. Where money reaches the thing you care about, it is the loudest complaint in the app.

The games split into three kinds. **Gardens you tend**, from Stardew Valley to the 36-billion-visit Grow a Garden, retain for a decade or more with no punishment for absence; their pressure is a barn that fills up, a season that ends, a plot that grows while you are away. **Habit apps that grow something**, Finch, Forest, Flora and Plant Nanny, are each bigger in Britain than any trainer platform in the market report, and the best of them count what you did, not the days you did not. **Activity games**, Pikmin Bloom above all, show what it looks like when a real-world action grows a world in the background, with a nightly lookback that makes the player feel seen rather than scored.

Two mechanics appear in every lane and are worth naming. The **two-speed session**: a glance that takes one tap, and one sit-down a day where the game happens. And the **chosen stake**: Forest's tree, Flora's self-reported price, Duolingo's streak wager and Zombies, Run!'s chase all work because the player set the terms and the loss is capped. Nothing in the set imposes an involuntary loss and keeps its rating.

> **What it means for RepGarden.** The garden grows when a planned session is done and stalls when one is missed; it never dies. Progress is counted in sessions done against the trainer's plan, never in calendar days, so a rest day is a zero and not a minus. One session is one unit of growth, and nothing in the garden can be bought. Two screens: one plant between sets, the garden after. A lookback after every workout. Stakes only when the client sets them. Pages 4 to 10 take each decision in turn.

*Decision 1 · the story*

## Is the client the plant, or the gardener?

Every game here puts one of three things on the screen: something that is **you**, something that is **yours**, or a **place** you tend. Which one it is decides how a loss feels, what there is to choose, and what there is to spend on.

| The figure is… | Games | What a loss feels like | Freedom and spending | GB rating |
|---|---|---|---|---|
| **You** | **Habitica** avatar with hit points · **Brainrot** your brain · **Duolingo** your streak | Personal. “Emotionally it lands like real failure… I avoid the app for a month.” Brainrot's reviewers call it “guilt with no credit for good behaviour”. | Little to choose, little to spend on; Habitica's gear is the exception and the clutter. | 4.04 · 4.37 · 4.70 |
| **Yours** | **Finch** a bird · **Focus Friend** a bean · **Tamagotchi** a creature · **Plant Nanny** a plant in a pot | Sympathy, not shame. The bird is sad, the bean drops its stitches, the plant wilts and perks up. You can let it down; it never lets you down. | Name it, dress it, decorate its room. Finch's identity layer is the deepest in the set and it is all earned. | **4.93** · 4.75 · 4.44 · 4.70 |
| **A place** | **Stardew Valley** **Grow a Garden** **Hay Day** **Gardenscapes** **Forest** **Flora** | Partial. One bed stalls, one tree dies, the row has a gap. The rest of the place is untouched and still yours. | The most: what to plant, where, which design; Gardenscapes' choices are free and reversible forever. | 4.80 · 4.67 · 4.79 · 4.76 |

### The pattern

Where the figure is **you**, every miss is a verdict on you, and those are the apps people describe avoiding. Where it is **yours**, the same miss is something to make up to a creature that is glad to see you, and those are the apps rated highest. A place adds what a single creature lacks: things to choose and things to spend on. Finch and Focus Friend already combine the two, a creature that is the reason you care and a room that is the record.

### And the physiology agrees

Vegetables do most of their growing when nobody is watching them. So do muscles: the session is the stimulus, the growth happens in the rest after it. Grow a Garden puts “your garden literally grows while you are offline” in its one-line store description, and Stardew's crops only stall when unwatered. A garden is the one metaphor where a rest day is part of the story rather than a gap in it.

> **Recommendation: the client is the gardener. The vegetables are theirs, not them.** Each client has a plot. The trainer's programme is, without the trainer doing anything, the season's planting plan. A planned session done is a watering; the growth comes on the rest day; a missed session stalls the plant, and nothing dies. One hero vegetable per programme block carries the identity, named and chosen by the client as Finch's bird is, so the client can feel for it without being it. What this rules out: a plant that is the client's body, an avatar with health, and any screen that shows the client a verdict on themselves.
Yours, not you: Finch's bird, Plant Nanny's plant, Grow a Garden's plot.

*Decision 2 · the unit of play*

## What in the training grows what in the garden.

The game can only see sessions done against sessions planned, sets logged, check-ins and personal bests. Each of the games maps one real thing to one growing thing, and the mapping decides everything downstream. Four mappings are in use.

| One grows per… | Who does it | What it gives | What it costs | Fit |
|---|---|---|---|---|
| **Session** | **Forest** one tree per focus session into a grid · **Flora** one plant per session in a row · **Gardenscapes** one star per level | The simplest honest ledger: every session is visible, forever. Gaps show without anyone being punished. | At three sessions a week the garden fills slowly and reads as a log. Forest's and Flora's rows are records, not places. | yes |
| **Week** | **Finch** the bird grows on adventures completed, energy resets daily · **Pikmin Bloom** weekly challenges with a shared goal | Matches how the trainer plans: sessions per week. A rest day is a zero, never a minus. Fair across two-a-week and five-a-week clients. | Needs the plan to be known, which it is: the trainer wrote it. | yes |
| **Programme block** | **Plant Nanny** grow one plant to max, harvest it to the greenhouse, plant the next · **Stardew Valley** 28-day seasons ending in a harvest · **Pokémon GO** three-month seasons | A beginning and an end. The harvest is the milestone, and the harvested vegetable goes into a permanent collection that a long absence cannot touch. | Blocks vary in length; the plant's growth stages must scale to the block. | yes |
| **Exercise or lift** | **Pokémon GO** candy per species · **Stardew Valley** crops by type · **Habitica** a task per habit | Ties growth to real progress on a real lift: the squat plant, the deadlift plant, a personal best as a bloom. | Many plants, a data model per exercise, and clutter. The trainer's programme changes exercises between blocks. | later |

### Recommendation: nest the first three

**The session is the watering.** One planned session logged is one unit of growth, exactly one, as Gardenscapes' star is, and nothing else produces it. **The week is a bed.** Each week shows its planned sessions as cans to fill; the bed is full when the plan is met, whatever the plan was. **The programme block is the season.** One vegetable is planted when the trainer's block starts and grows a stage per session; when the block ends it is harvested into the client's permanent collection, their larder, and the next block plants the next one. Per-lift plants wait for a later phase, when the garden has earned a second row.

The stages scale to the block: twelve waterings or thirty-six, the vegetable has the same five visible stages, so the client always sees the next one within a few sessions. That is Duolingo's finding about early motivation: the gain is largest in the first days.

### What the harvest protects

Pokémon GO's returning player after ten years still had “a couple hundred original 2016 Pokémon sitting safely in my storage” and got hooked again; Plant Nanny's greenhouse and Forest's grid do the same job. A larder of harvested vegetables is the bank that makes a long absence recoverable in a way a streak never is. Every vegetable the client ever grew stays theirs.
Plant Nanny's greenhouse of finished plants; Forest's grid of sessions; Flora's row with its gaps.

*Decision 3 · absence*

## What happens when the client stops coming.

The same question put to all twenty-two games. The answer is almost unanimous, and the exceptions are the lowest-rated apps in the set.

| When you stop… | Games | What the players say |
|---|---|---|
| **Nothing happens**, and often you are paid to come back | **Hay Day** re-engagement rewards after 31 days away · **Neko Atsume** cats visited while you were out · **Grow a Garden** grew while offline · **Walkr** planets kept producing · **Gardenscapes** lives refilled · **Finch** **Pikmin Bloom** **Focus Friend** and five more | Hay Day players discuss lapsing on purpose to collect the rewards. Grow a Garden puts “grows while you are offline” in its store blurb. |
| **Growth pauses**, and one action resumes it | **Stardew Valley** “unwatered crops do not die, but they will not grow either” · **Pocket Camp** a wilted flower pauses its timer; one watering resumes it · **Plant Nanny** the plant wilts, cannot die, and one glass revives it | Plant Nanny's recovery costs exactly the action that would have prevented the wilt. No repair item, no apology. |
| **A gap shows**, and stays | **Flora** the row shifts left and leaves a space · **Forest** a dead tree stays in the grid | Accepted, because the player set the timer and knows what they did. Flora's rating is dragged down only by false kills. |
| **A counter resets** | **Duolingo** one missed day ends the streak; two freezes, paid repair · **Pokémon GO** first-catch streak resets, no freeze · **Sweatcoin** sells “Restore your longest streak” for £0.99 · **Finch** opt-in, can be switched off or paused | “Lost my 595 day streak because of a funeral”, 2,900 upvotes. “Woke up Monday to a zero. Closed the app and never went back.” |
| **You are punished** | **Habitica** hit points lost per missed daily, escalating with neglect; death wipes gold and a level | “Missing 1 day makes me feel so bad about the character that I avoid the app for a month.” Rated 4.04, the lowest here. |

### The one decay worth copying

Pikmin Bloom's only withering punishes over-harvesting one Pikmin, not absence, and it heals when you walk: the decay targets gaming the game and the cure is the real behaviour. The gym version: junk sets logged in a row grow nothing, and a day counts once.

### Duolingo's own numbers

Two freezes instead of one lifted daily actives; a weekend amulet made people 4% likelier to return and 5% less likely to break; binge sessions predicted abandonment. The company built on the streak publishes the case for slack.

> **Recommendation: stall, droop, never die. Count sessions, not days.** **A missed planned session** stalls the vegetable: no growth, nothing lost. **A week with nothing logged** makes it droop, and the next logged set perks it up, as Plant Nanny's glass does. **It never dies**, and the larder is permanent. **No daily streak.** The count is weeks in which the plan was met, shown as a percentage of planned sessions done: “so much less shaming to see 99% than a reset to zero”. **A pause** the client switches on, as in Finch, for holidays and injuries. **A return is paid**, Hay Day style: something has happened in the garden while you were away. The workout is the watering; the growth comes on the rest day.

*Decision 4 · the economy*

## What you earn, and what it buys.

Ahmed's rule from ArabyBuddy was that a reward has to be spendable on something that matters inside the app. The games agree, and they add a second rule: the currency that buys the thing you care about must not be for sale.

| Game | Earned by | Spent on | Feeds back | Buyable | What happened |
|---|---|---|---|---|---|
| **Stars** | one per level won | garden tasks | yes | no | Stars never for sale; coins, which are, reach only boosters. The complaint is stars that buy “a bench”. |
| **Rainbow stones** | goals ticked, quests | clothes, furniture, travel | yes | no | “Can't be bought.” No complaint about the economy at all. |
| **Gold** | shipping crops | seeds, tools, buildings | yes | no | No shop of any kind. “IT IS SO WORTH THE MONEY.” |
| **Clovers** | achievements, logins | plants, pots, decor | yes | yes | A daily seed system was removed with the one strategic choice; users left over it. |
| **Petals, nectar** | blooming Pikmin, fruit | flowers on the map, feeding Pikmin | yes | no | The loop closes on itself. Coins, bought, reach only storage. |
| **Coins** | sessions completed | species, real trees | yes | ~ | A bought Crystal and daily logins arrived in December 2025; a petition followed. |
| **Coins, diamonds** | orders; purchase | seeds, buildings; speed | yes | yes | The pretty path priced in diamonds: “higher than my will to live”. |
| **Coins, T-Cash** | orders; purchase | buildings; skipping timers | yes | yes | “The game reaches a level where paying is the only way to progress.” |
| **Energy, coins, cubes** | steps; idle yield; purchase | travel; planets; boosts | yes | yes | Three currencies across five systems: “simply too complicated”. |
| **Supplies** | picked up while running | base buildings | no | no | Its own fans call the base “pointless”: upgrades “produce no tangible effects”. |
| **XP, gems** | lessons | league rank; freezes, repairs | yes | yes | Gems buy forgiveness; the streak wager stakes them and lifted day-7 retention 14%. |
| **Sweatcoins** | verified outdoor steps | discounts, prize draws | no | no | Valued at pennies by users; the app backfills meaning with lotteries and a £0.99 streak restore. |

### Three rules the table gives

**One currency, earned only by training.** Walkr and Hay Day show what sprawl costs; Finch and Gardenscapes show one clean loop. RepGarden is free with no shop, so the wall is free: nothing in the garden is ever for sale, and the report can say so. **Every spend changes something you can see.** Zombies, Run!'s base is the warning: a reward that changes nothing is called pointless within weeks. Gardenscapes' bench is the subtler version: the change must be worth an evening. **Plan the catalogue for months.** Focus Friend's shop empties in days and that is its top complaint; Finch solved it with seasons and a long tail of things to collect.

> **Recommendation: seeds, earned by sessions, spent on the garden.** A planned session logged earns **seeds** (the name can change). Seeds buy the next vegetable to plant, a second bed, pots and garden furniture, and the choice of design for each, free to change afterwards as Gardenscapes allows. A harvest pays a bonus. A trainer's comment on a filmed set, which already exists as a feature, is **sunshine**: it costs nothing to earn and arrives when the trainer chooses, which makes it the surprise. Nothing is purchasable, and the trainer sets none of it.

*Decision 5 · the screen*

## Six ways to draw a world, side by side.

Every game in the set uses one of six screen types. The question for RepGarden is which one survives a glance between sets, and which has enough in it to last a twelve-week programme. The screenshots are each game's own store listing.
**Isometric world** Township, Hay Day, Gardenscapes, Forest's forest view A tilted 3D-looking town or farm you pan around. Everything is on screen at once: buildings, timers, orders, coins, events. does not fit Dense. Needs a lot of art, and the home screen is a shop window. Between sets it is noise. **Top-down world** Stardew Valley, Pocket Camp's garden, Grow a Garden's plots A plot seen from above, tended square by square. Reads as 'my garden' at a glance; each bed can mean something. fits a glance Works at any size, from one bed to a field. Can grow with the client. The strongest fit for a garden that reflects a programme. **Side-on single scene** Plant Nanny, Forest's tree, Flora, Neko Atsume's yard One plant, one pot, one window. The whole state of play is visible in a second with nothing to pan or tap. fits a glance The best glance screen in the set. Weak on freedom and economy: there is little to choose or spend on. **Creature in a room** Finch, Tamagotchi, Focus Friend A character who is you, or yours, in a room you decorate. Tasks are a list under the character. fits a glance Strongest identification; the room gives freedom and spending. Risk: a sad creature is a mirror, and that cuts both ways. **Map** Pokémon GO, Pikmin Bloom, Zombies, Run!, Flora's Grand Tour The real world or a route as the board; the activity itself is the input. does not fit Right for walking games, wrong for a gym: the client is standing still, and the map would be the gym. **Minimal figure** Brainrot, Duolingo's streak screen, Focus Friend's timer One figure and one number. Nothing to explore; the figure's state is the whole message. fits a glance Zero load, instantly read. Too thin on its own for a game that has to last months, but it is the right between-sets layer.

> **Recommendation: two screens, not one.** Between sets, a single plant in a single scene, the side-on or minimal type, with one tap. After the workout and in the evening, the garden seen from above, one bed per thing that is growing. The two are the same garden at two distances. Isometric worlds and maps are out: the first is a shop window and the second is for walking.

*Decision 6 · mechanics*

## Surprise, risk, time, social, freedom: which, and when.

The rest of Ahmed's list, each taken against the best example in the set, with a verdict on whether it fits a client in a gym three times a week.

| Mechanic | Best examples | The RepGarden version | When |
|---|---|---|---|
| **Focus** clear goal, feedback, challenge | **Stardew Valley** the farm as the readout · **Township** a thought-bubble over a building saying what it wants | The goal is today's session, already set by the trainer. Every logged set visibly does something to the plant. The challenge is progressive overload, which the trainer supplies; the game only has to show it. | MVP |
| **The lookback** | **Pikmin Bloom** at 9pm, the day's steps replayed, one photo, a face · **Stardew Valley** the bedtime tally · **Pokémon GO** weekly report | After every workout: what grew, the sets, one photo from the gym, how it felt in one tap, unscored. Rolled up on Sunday with the week's bed. The cheapest retention mechanic in the set. | MVP |
| **Surprise** | **Neko Atsume** who visited while you were out · **Grow a Garden** weather that mutates a crop · **Finch** a discovery on every return | The trainer's comment is sunshine; a push notification already carries it. Rare seeds on a harvest. Something in the garden has changed when you return after a gap. Randomness only ever adds. | MVP |
| **Time** | **Stardew Valley** 28-day seasons · **Pikmin Bloom** the month as a season · **Pokémon GO** a three-hour surge with nothing lost by skipping it | The programme block is the season and the harvest ends it. No stopwatch anywhere: rewarding speed fights rest periods and form. Event quotas in short windows are the mechanic Pikmin's and Pokémon's players quit over. | MVP |
| **Freedom, identity** | **Finch** name, pronouns, dress, decorate · **Gardenscapes** three designs, changeable free forever · **Stardew Valley** name everything | Choose and name the vegetable for the block, choose the pot and bed design, change it free. Identity costs nothing to run and is where people say they attach. | MVP |
| **Stakes, risk** | **Forest** the tree you planted · **Flora** a price you set and report yourself · **Duolingo** the streak wager, +14% day-7 · **Zombies, Run!** the chase, optional, tunable, capped loss | Opt-in only: “I'll do every session this week” for a bigger harvest, with the loss capped at that week's bonus. The client reports the outcome; the app never asserts a failure it cannot prove. Benji can mark a push set; opting in and missing costs one seed, never the session. | later |
| **Social** | **Finch** no leaderboard; vibes, hugs, goal buddies · **Pikmin Bloom** weekly group goals with participation prizes · **Hay Day** the opt-in Derby · against **Habitica** misses that damage friends and **Township** teams that kick you | Benji's clients as an allotment: a row of plots you can walk past and cheer. Leaderboards rank adherence to each person's own plan, never volume, so two-a-week can beat five-a-week. Challenges the trainer sets are co-operative and opt-in; the game attaches the reward. | later |
| **Chance, fairness** | **Neko Atsume** rare cats on better food · **Gardenscapes** “it feels rigged” when difficulty sells boosters | Chance sits on top of progress and never gates it. Fairness is adherence: the only inputs are things every client can do equally. | MVP |
| **The gesture** | **Plant Nanny** press and hold to pour · **Hay Day** drag to harvest · **Fruit Ninja** swipe to slice | One signature: logging a set is a hold that waters, with the pour and a haptic. Everything else is a tap. No new way of using a phone. | MVP |

*Decision 7 · the MVP cut*

## What to build first, and what to avoid.

### Build in the MVP
One plot, one vegetable per programme block, five growth stages, harvest to a permanent larder.Session logged = one watering = one seed. Missed = stall. A blank week = droop, revived by the next set. Never dies.The week as a bed: planned sessions as cans; percentage met, never a day count.Two screens: the plant and today between sets; the garden after.The lookback after every workout; a Sunday roll-up.Seeds spent on the next vegetable, a bed, a pot, a design; nothing purchasable.Sunshine when the trainer comments; a surprise on return after a gap.Choose and name the vegetable; the hold-to-water gesture.A pause the client switches on.

### Second phase
The allotment: Benji's clients' plots side by side, adherence-ranked, opt-in.Trainer-set challenges, co-operative, with a participation reward when the group falls short.Opt-in weekly commitment stakes, self-reported, loss capped at the bonus.Per-lift plants and a personal best as a bloom.Seasonal vegetables and a long catalogue, so the shop never empties.Sound design beyond the pour and the harvest.

### NeverA daily streak. Anything that dies. A verdict on the client.Rewards for speed or for volume beyond the plan.Anything the trainer has to set up for the game.A currency for sale, or a second currency.

### Things to watch out for

| Trap | Seen in |
|---|---|
| **Adding taps to a one-press loop.** “It is no longer a focus app, it's part of the problem.” Between sets, every tap is multiplied. | **Forest** **Flora** |
| **The event treadmill.** Weekly events the developer admitted were burning players out; a stack of popups before the garden. | **Grow a Garden** **Gardenscapes** |
| **Asserting a failure the app cannot prove.** False kills are Flora's whole rating problem. A set done but not logged must never wither anything. | **Flora** **Habitica** |
| **The shop that empties in a week.** Content exhaustion is the retention cliff in the habit lane. | **Focus Friend** **Plant Nanny** |
| **The game displacing the goal.** “Better at protecting a streak than learning the language.” | **Duolingo** |
| **Blame that transfers.** Your miss damages your friends; teams that kick you. | **Habitica** **Township** |
| **Density.** Seven currencies and five systems; the home screen as a shop window. | **Township** **Walkr** |

> **Is the garden worth building at all?** A growing thing retains where points do not: Finch has 78,000 GB ratings at 4.93, Plant Nanny and Forest are a decade old and each larger in Britain than any trainer platform, Gardenscapes is a two-billion-dollar business built on a garden as the receipt for an unrelated task, and Grow a Garden took thirty-six billion visits in a year on the promise that it grows while you are away. None of the fourteen trainer platforms has anything of the kind. The risk is not that a garden will not hold people; it is that a garden laid over a utility becomes the utility's problem, and the cure is in the first column: one tap between sets, everything else after the workout.

*Why a theme at all*

## Shapes with a story win.

- **Space Invaders, 1978** Mechanically it is a row of shapes descending on a shape that shoots. Taito drew the shapes as aliens, called the shooter a laser cannon and the shields bunkers, and the same mechanics became an invasion you are holding back. The occasional saucer across the top is the risk: leave your lane to shoot it and the rows get closer.

- **Chess** A grid, six movement rules. The medieval theme, kings, knights, castles and a church, gives every piece a reason for how it moves and makes a trade feel like a sacrifice. People have cared about the outcome of a board of shapes for a thousand years because the shapes have names.

- **Fruit Ninja, 2010** Swipe to cut moving targets, avoid some of them. The theme chose the gesture: a blade through fruit, with the juice splash and the slash mark as the feedback. The mechanic and the theme are the same thing, which is why it is still on phones fifteen years later.

The trainer platforms RepGarden competes with have the mechanics, points, streaks, leaderboards, and no theme, so a streak is a number and a badge is a shape. The games in this report are the other way round: in every one, the thing on the screen is something you would recognise from life, a farm, a tree, a bird, a brain, and the mechanics are explained by it. Nobody reads a manual for Plant Nanny. You drink water, the plant drinks water.

### What a theme does for the mechanics

**It explains the rules.** A plant that wilts when it is not watered needs no tutorial; a "streak at risk" banner does. **It sets the emotion.** Growth, tending, harvest, seasons: the garden says what the app wants the client to feel without a line of copy. **It picks the gesture.** Fruit gets sliced, a plant gets watered, a set gets logged: the theme should decide what the one tap between sets looks like. **It makes a loss bearable.** A wilted bed is sad and fixable; a streak reset to zero is a verdict.

### Why vegetables fit the gym

Vegetables grow slowly, visibly and on their own schedule, and they grow most when you are not looking. So do muscles: the work is the session, the growth happens in the rest between. That is one true sentence that is both a story and a training principle, and it is the sentence the whole garden can be built on: **the workout is the watering; the growth comes on the rest day.**

> The name already carries it. Rep, garden: the thing you do, the thing that grows.

*Evidence · farm and garden games*

## Farms and gardens, one by one.

Nine games where a plot is the thing you tend. Read from each game's own pages and wiki, its GB store listing and its players' threads on 27 October 2026. Screenshots are each game's own listing.

**Grow a Garden**Roblox · 2025 · free, Robux for shortcutsisometric

What grows One square plot. Buy seeds with Sheckles, plant, wait, harvest, sell, buy rarer seeds. Crops grow in real time while you are logged out.
When you stop Nothing withers, ever; the store blurb is “your garden literally grows while you are offline”. Absence costs only the global weather events you were not there for.
Earn → spend Sheckles from selling crops → seeds, gear, pet eggs. Weather mutations multiply a crop's value by tens or hundreds.
Signature Plant, log out, trust the plot. Then stand in your garden during a live weather event with the right gear placed.
For RepGarden Copy the asymmetry: away time grows, presence multiplies. Avoid the weekly event treadmill its own developer admitted was burning players out.

**Stardew Valley**ConcernedApe · 2016, iOS 2018 · £4.99, no purchasestop-down

What grows A farm, tile by tile, and the farmer: five skills, twelve villagers, four 28-day seasons.
When you stop Unwatered crops do not die, they stop growing. Loss comes only from the season boundary you were warned about, lightning, or crows. Close the app for six months and nothing has changed.
Earn → spend Gold from shipping → seeds, tools, buildings. The best reward is the sprinkler, which removes the daily chore you have been doing by hand.
Signature Going to bed: the overnight tally, the level-up jingle, a clean morning. And the watering-can sweep along a row.
For RepGarden Stall, never kill. And reward the client who has done the work by hand with less to do, not more.

**Hay Day**Supercell · 2012 · free, diamonds for speedisometric

What grows An isometric farm: fields, animals, bakery, dairy, orders by truck and boat.
When you stop “It never rains here, but the crops never die.” After 31 days away the game pays you to come back: free barn and silo upgrades, animals fed. Players lapse on purpose to collect it.
Earn → spend Coins → seeds, animals, buildings. The squeeze is the barn: full storage, not dead crops, is the urgency.
Signature One finger dragged across a ripe field cuts the whole row; dragged back, it sows again.
For RepGarden Capacity beats decay as a pressure. The Derby, an opt-in weekly team challenge with a cooldown, is the shape for a trainer's challenge.

**FarmVille 2**Zynga · 2014 · free, keys for speedisometric

What grows A coastal farm with workshops and farm hands you send out to forage.
When you stop No withering. The original FarmVille (2009–2020) withered crops and sold a $42 Unwither Ring to switch the punishment off; the mobile successor dropped decay entirely.
Earn → spend Coins → seeds and buildings; keys, mostly bought, skip timers. Keys “essential for expanding” is the top complaint.
Signature Sending a farm hand down the coast road and getting back a bag of rarities you could not have grown.
For RepGarden The FarmVille arc is the case against decay: the punishment that made it famous is the thing it had to sell a cure for.

**Township**Playrix · 2012 · free, T-Cash for speedisometric

What grows A town and a farm: crops → factories → helicopter, train and plane orders → more town.
When you stop No decay and no streak. The barn fills up instead, and refills within hours of every upgrade; it is the top complaint and the top conversion mechanic at once.
Earn → spend Coins → buildings and territory; T-Cash skips timers. Three currencies plus building materials.
Signature A sickle dragged across a ripe field. Buildings float a thought-bubble of what they want.
For RepGarden Copy the thought-bubble: the whole screen becomes one glanceable instruction. Avoid the density and the team Regatta that kicks people for not keeping up.

*Evidence · farm and garden games*

## Farms and gardens, continued.

**Gardenscapes**Playrix · 2016 · free, coins for boosterssingle scene

What grows A derelict estate garden restored task by task. The game is match-3; the garden is the receipt for having played it.
When you stop Nothing decays; lives refill while you are away. The only cost of absence is missed timed events, which players call “a stack of popups” to dismiss.
Earn → spend One level won is exactly one star, and stars cannot be bought at any price. Coins, which can, reach only boosters. Bank stars and spend them in one go with Complete the Day.
Signature Spending a star and watching one corner of the garden change, before and after.
For RepGarden RepGarden's exact architecture: unrelated effort buys garden progress. Keep one unit of effort to one star, keep money out. Avoid the conveyor belt where an evening's grind buys “a bench”.

**Pocket Camp**Nintendo · 2017, Complete 2024 · one-off purchaseisometric

What grows A campsite to decorate, villagers to befriend, a twenty-plot flower garden.
When you stop Nothing dies. A neglected flower wilts, which pauses its timer, and one watering resumes it. Seven years of events now repeat on a four-year cycle, so nothing is missed for good.
Earn → spend Bells → crafting and furniture; leaf tokens, no longer purchasable, → fortune cookies.
Signature Handing a villager the exact thing they asked for, every three hours.
For RepGarden Copy the wilt that pauses rather than kills, and events that come round again rather than expire.

**Neko Atsume**Hit-Point · 2014 · free, gold fish optionalsingle scene

What grows A yard that cats visit on their own. What accumulates is the catbook and the mementos they leave.
When you stop No decay, no streak, no fail state. You can only make the cats happier. The reward is for returning: who showed up while you were out.
Earn → spend Fish left by cats → food and goodies that attract rarer cats. Touching a cat reduces what it leaves.
Signature Opening the app to find cats you did not choose, and tapping the camera.
For RepGarden Retention without stakes: pay for coming back, not for never missing. A trainer's comment on a filmed set is exactly “who showed up while you were out”.

**Tamagotchi**Bandai Namco · 2018 · free, ads and gemscreature

What grows One creature in a room, evolving by how it is cared for: sleep, hunger, play, bathroom.
When you stop It cannot die. The 1996 toy died in half a day without care, got banned from schools and buried in toy graveyards; the 2018 app removed death, and a creature ignored for ten days is a healthy adult that “waited patiently”.
Earn → spend Coins from minigames → food, toys, costumes, decorations. Gems skip the sleep timer.
Signature Tapping the toilet to clean up after it. Tickling it.
For RepGarden A care loop still works when the creature can only look sad. Copy the screen: seven elements, the creature uncontested in the centre.

*Evidence · habit apps*

## When a habit grows a plant or a creature.

Seven apps where a real-life behaviour, from drinking water to not touching your phone, grows something on the screen. These are the closest relatives of a garden that grows when you train.

**Finch**Finch Care · 2021 · free, no ads, Plus optionalcreature

What grows One bird, yours, hatched from an egg you chose and named. Ticking a goal fills an energy bar; a full bar sends the bird on an adventure, and it comes home at night with a story.
When you stop No decay anywhere. Energy resets daily, so a day off is a zero, not a minus. Growth counts adventures completed, not days. Only the opt-in check-in streak can hurt, and it can be switched off or paused.
Earn → spend Rainbow stones from goals → clothes, furniture, dyes, travel. Stones cannot be bought. The complaints are about the subscription price, never the economy.
Signature The bird leaving on its own because your ticks filled the bar, and the two-option conversation when it returns.
For RepGarden Copy the whole absence architecture: nothing decays, progress counts sessions done, a pause the client switches on. Leave the daily streak out; it is the subject of Finch's most upvoted complaint.

**Forest**Seekrtech · 2014 · free, Plus subscriptionsingle scene

What grows One tree per focus session, planted permanently into a forest grid by day, week and month.
When you stop Nothing rots between sessions and there is no streak. The penalty is inside the session: leave the app before the timer ends and the tree withers, and the dead tree stays in the grid as a record.
Earn → spend Coins per session → species and decorations, and real trees planted. A December 2025 rebuild added daily logins and claim animations, and five-year users left: “it is no longer a focus app, it's part of the problem.”
Signature Pressing Plant and putting the phone face down. The stakes are live the moment the sapling appears.
For RepGarden A stake the client chose beats a penalty the app imposed. And every tap added to a one-press loop is noticed; in a gym it is multiplied.

**Flora**AppFinca · 2018 · freesingle scene

What grows One plant per session into a garden that is a single row, newest on the right. Over time the row shifts left and leaves a visible gap where you did not plant.
When you stop Nothing dies from absence; the gap is the record. In a session, leaving kills the plant, and the loudest complaint is false kills.
Earn → spend Focus time → new species at Grand Tour stops. The Price is a cash stake you set on yourself, charged only if you press “Honor My Price” after a kill; setting it removes your own pause button.
Signature Setting a price and watching the pause button disappear. Joining a friend's live room and growing in parallel.
For RepGarden If RepGarden ever takes a stake, the client reports the failure themselves. And never assert a failure the app cannot prove: a set done but not logged must not wither anything.

**Plant Nanny**Sparkful · 2013, v2 2019 · free, clovers optionalcreature

What grows One plant in a pot, grown by drinking water. At max level it is moved to the greenhouse and a new one is planted; three in a tree hole attract creatures.
When you stop The plant wilts but cannot die. One logged glass revives it, with no repair item or apology. Recovery costs exactly the action that would have prevented it.
Earn → spend Clovers → new plants, pots, decoration. An update removed the daily seed system and the one strategic choice with it; users noticed.
Signature Press and hold the water button and watch it pour. Logging feels like watering.
For RepGarden The closest model to copy: grow one vegetable, harvest it into a permanent collection, plant the next. The wilt that cannot kill, revived by one logged set, is the absence rule.

*Evidence · habit apps*

## Habit apps, continued, and the baseline.

Duolingo is included here because every streak, league and freeze in the set descends from it.

**Habitica**HabitRPG · 2015 · free, gems optionalminimal

What grows A role-playing avatar with HP, XP and gear. Tick a Daily, earn gold; miss one and take damage. Death costs a level and all gold.
When you stop The only app in the set that punishes absence, with damage that escalates the longer you stay away. “Missing 1 day makes me feel so bad about the character that I avoid the app for a month.”
Earn → spend Gold → equipment and potions; gems, bought, → quests and pets.
Signature The red damage notification the next morning for what you did not do.
For RepGarden The design RepGarden must not be. Its scheduler cannot express a real routine: “How about if I want to visit the gym twice a week?”

**Focus Friend**Hank Green · 2025 · free, no ads, Pro optionalcreature

What grows A bean that knits socks while you focus. The bean is not what grows; the room is, bought with the socks.
When you stop No decay, no streak, no penalty between sessions. Stop a timer early and the bean is “really really sad” and drops its stitches. That is the whole punishment, and it reached number one in five countries.
Earn → spend Socks → hundreds of decorations across rooms. The top complaint is content exhaustion: the shop is emptied in days.
Signature Starting a timer and watching a bean knit on the lock screen; the needles stopping is the failure signal.
For RepGarden A sad companion is enough. Plan the catalogue for months, not days: seasonal vegetables, not a shop that empties in a week.

**Brainrot**Smolworks · 2025 · subscriptionminimal

What grows A brain with a health percentage that decays as you use your phone and heals as you stop. One character, one number, one screen.
When you stop Inverted: absence from your phone is the win. No streak, no shop, no progression ladder. The complaints are about the hard paywall and unreliable blocking, never about the game.
Earn → spend No currency at all.
Signature The brain getting visibly sicker on the home-screen widget as the day goes on, and the “chat with my brain” gate before a blocked app opens.
For RepGarden The example of restraint: a reactive figure on a continuous dial needs no economy to work. Too thin to last a twelve-week programme on its own, but the right between-sets layer.

**Duolingo**Duolingo · 2012 · free, ads, Super subscriptionminimal

What grows A number: the streak, a flame on the home screen, and a path of lesson nodes. Nothing is tended, which is why losing the counter is catastrophic.
When you stop One missed day ends the streak. Its own research argues for slack: two equippable freezes lifted daily actives; a weekend amulet made people 4% likelier to return and 5% less likely to break; binge sessions predicted abandonment.
Earn → spend XP ranks you in a weekly league of thirty; gems → freezes and repairs (500 gems). The Streak Wager, an opt-in bet on holding seven days, lifted day-7 retention by 14%.
Signature The flame ticking to the next number with its milestone animation, and the owl's notifications.
For RepGarden Copy the forgiveness research and reject the “daily” in daily streak. Celebrate early: motivation gain is 50% from day two to three and 0.5% from day 200 to 201.

*Evidence · activity games*

## When moving your body is the input.

Five apps where walking or running drives a game world, read the same way as the farms, on the same day.

**Pikmin Bloom**Niantic, now Scopely · 2021 · free, coins optionalmap

What grows Three things at once: seedlings mature into Pikmin after a set number of steps, flowers are planted along the real streets you walk, and fed Pikmin bloom petals you harvest.
When you stop No streak, no death, no loss. Only the world expires: planted flowers clear after five days. The one decay punishes over-harvesting a Pikmin, not absence, and the cure is walking.
Earn → spend Petals from Pikmin → flowers planted on the map; nectar from fruit → feeding Pikmin. The loop closes on itself. Coins, bought, reach only storage and event items.
Signature A squad of Pikmin trailing your avatar, and at 9pm the lookback: the day's steps replayed, one photo, a happy or sad face, unscored.
For RepGarden The closest model to “train and something grows”. Copy the nightly lookback almost literally, and the weekly challenge that pays a participation prize when the group falls short.

**Pokémon GO**Niantic, now Scopely · 2016 · free, coins for storage and passesmap

What grows Nothing is tended; a permanent collection accumulates. Walking feeds eggs, buddy candy and weekly distance goals with the app closed.
When you stop The collection is a bank: a player back after ten years still had “a couple hundred original 2016 Pokémon sitting safely in my storage”. The daily streaks, by contrast, reset to day one with no freeze.
Earn → spend Stardust and candy → powering up and evolving. Coins, bought, → bag space, incubators, raid passes.
Signature The swipe-flick of a ball at a creature standing on the pavement in front of you.
For RepGarden Take the background accrual, so a logged session grows something even if the app is closed, and the bank: a permanent collection makes a long absence recoverable in a way a streak never is.

**Zombies, Run!**Six to Start · 2012 · subscriptionminimal

What grows A story in your headphones as you run, and underneath it a base, Abel Township, built from supplies collected while moving.
When you stop No streak, no decay. Free users unlock one mission a week, so an absent player returns to a backlog of missions, not a penalty.
Earn → spend Supplies picked up automatically → buildings. Its own fans call the base “pointless” because upgrades “produce no tangible effects”.
Signature “Zombies detected.” The voice cutting into your playlist and the sprint that follows: 20% faster for 100 seconds, optional, tunable, can be switched off.
For RepGarden The opt-in intensity spike with a capped loss is the shape for a trainer's push set. The base is the warning: a reward that changes nothing is noticed within weeks.

**Walkr**Sparkful, was Fourdesire · 2014 · free, cubes optionalsingle scene

What grows A galaxy: steps become fuel for a spaceship, fuel discovers planets, planets are levelled and decorated and produce coins while you are away.
When you stop An idle game: planets keep producing in your absence and you harvest on return. Absence costs uncollected yield, never loss.
Earn → spend Energy from steps → travel; coins from planets → planet upgrades, satellites, wonders. Three currencies across five systems, and “too complicated” is the top complaint.
Signature Tapping Boost and watching the ship surge: the day's walking spent as fuel in one gesture.
For RepGarden An idle harvest is a better absence model than a streak: returning is a reward, not a reckoning. The sprawl of its economy is the thing to avoid.

**Sweatcoin**Sweatco · 2016 · free, ads, premiumminimal

What grows Nothing grows; a wallet fills. Roughly one coin per thousand GPS-verified outdoor steps. Gym steps do not count.
When you stop Earning stops, the balance stays. The daily streak's repair is a purchase: “Restore your longest streak, £0.99” is in its in-app list.
Earn → spend Sweatcoins → brand discounts, trials, prize draws. Valued at one to five cents each by its users, and the draws, scratch cards and a spin wheel do the retaining.
Signature The step-to-coin counter ticking over, and the verification that silently discards steps it does not trust.
For RepGarden The counter-example that justifies the brief: when the reward is external to the activity its value gets measured in pounds, found wanting, and replaced with lotteries and ads.

*Scale*

## How big each one is.

Ratings on the GB App Store on 27 October 2026, which only accumulate when real people use an app. Grow a Garden is not an app of its own: it runs inside Roblox, where its page showed thirty-six billion visits and eleven million favourites on the day.

### GB App Store ratings, 27 October 2026

| Game | GB ratings | Average |
|---|---|---|
| Duolingo | 993,193 | 4.70 |
| Township | 263,895 | 4.72 |
| Gardenscapes | 249,729 | 4.67 |
| Pokémon GO | 96,457 | 4.10 |
| Flora | 84,985 | 4.76 |
| Finch | 78,607 | 4.93 |
| Hay Day | 73,814 | 4.67 |
| Sweatcoin | 71,224 | 4.49 |
| FarmVille 2 | 27,054 | 4.61 |
| Forest | 20,506 | 4.79 |
| Plant Nanny | 10,392 | 4.70 |
| Stardew Valley | 6,206 | 4.80 |
| Pikmin Bloom | 5,821 | 4.75 |
| Zombies, Run! | 4,725 | 4.76 |
| Tamagotchi | 3,336 | 4.44 |
| Neko Atsume | 2,965 | 4.74 |
| Brainrot | 2,573 | 4.37 |
| Pocket Camp | 1,134 | 4.74 |
| Focus Friend | 733 | 4.75 |
| Walkr | 630 | 4.59 |
| Habitica | 378 | 4.04 |

### Read it this way

Duolingo is the scale everyone else is measured against, and the two habit apps that grow something, Finch and Flora, are each larger in Britain than any trainer platform in the market report. Finch has the highest rating in the set, 4.93 from 78,000 people, for an app whose whole mechanic is a bird that grows when you look after yourself. Forest and Plant Nanny are a decade old and still updated. Habitica, the role-playing habit app with the most mechanics, has 378 ratings.

### Launch year Zombies, Run! 2012Hay Day 2012Duolingo 2012Township 2013FarmVille 2 2014Forest 2014Walkr 2014Neko Atsume 2014Habitica 2015Sweatcoin 2016Pokémon GO 2016Gardenscapes 2016Tamagotchi 2018Flora 2018Stardew Valley 2018Plant Nanny 2019Finch 2021Pikmin Bloom 2021Pocket Camp 2024Grow a Garden 2025Brainrot 2025Focus Friend 2025

*What people say about streaks*

## The daily streak is the mechanic people quit over.

A thread titled “Tired of the daily streak punishment/reward system on apps” had 1,031 upvotes on the day it was read. Its top comments are below, with others from a thread on why habit trackers make people quit. They are one community's view, but the shape repeats across the games in this report: the streak keeps people going until the first miss, and the first miss is where they leave.
“on finch you can turn the streak feature off. It removed a lot of guilt for me using that app. But yeah I hate that feature it's really disheartening”r/adhdwomen · 414 points “Everybody recommended Duolingo so I started using it and the constant reminders to keep the streak, and the pressure to not lose it put me completely off”r/adhdwomen · 139 points “the faux urgency of the streak is key to how these apps work, but also the biggest hurdle to getting back on the wagon when you break it. Once a streak is broken, my brain ... sees restarting as committing to sticking with it for however long the previous streak was”r/adhdwomen · 83 points “I wish tracking “% of days completed” and similar was more of a thing than streaks. It's so much less shaming to see 99% of days vs a reset to zero days”r/adhdwomen · 49 points “i had a 34-day run in one app and missed a sunday because i was camping. woke up monday to a zero. closed the app and never went back”r/getdisciplined “If something doesn't truly need to happen every single day, then a “daily streak” is probably the wrong metric. A goal like “3 times per week” feels more humane and still keeps you accountable”r/getdisciplined

> **What it means for RepGarden.** The client's week is set by the trainer: three sessions, say, with rest days between. The streak the garden counts is weeks with every planned session done, and a missed session costs one bed's growth, not the whole garden. Finch lets people switch the streak off, and that comment has more upvotes than any other in the thread; RepGarden can go one better by never having a daily one.

*Method*

## Where this comes from.

**What was read.** Twenty-two games and apps, in three groups: nine farm, garden and creature games; seven habit apps that grow a plant or a creature; six apps where walking or running drives a game, with Duolingo as the baseline everyone copies. For each, the GB App Store listing, the developer's own pages, help centre, blog or wiki, press coverage, and reviews and Reddit threads, all on 27 October 2026, by three agents working from one written brief with thirteen fixed questions, every claim recorded against a source.

**What counts as verified.** A mechanic is stated as present only where the game's own pages or an established wiki describe it. “Not confirmed” means it could not be found on the day. Review quotes are reproduced closely and attributed to the thread, not the person.

**Scale.** App Store figures are the GB storefront's rating count and average on the day; Roblox figures are its own game page. Google Play gives install bands only.

**Images.** Icons and screenshots are each game's own store listing, reproduced for comparison and commentary.

**Limits.** One day's reading; live-service games change their events monthly. Nothing here comes from playing every game to the end; where a mechanic's late-game shape mattered, the wiki was used. The Reddit threads are self-selected communities and are read as signals, not measurements.

**Games read.** Grow a Garden, Stardew Valley, Hay Day, FarmVille 2, Township, Gardenscapes, Pocket Camp, Neko Atsume, Tamagotchi, Finch, Forest, Flora, Plant Nanny, Habitica, Focus Friend, Brainrot, Pikmin Bloom, Pokémon GO, Zombies, Run!, Walkr, Sweatcoin, Duolingo. Also used as examples of theming: Space Invaders, chess and Fruit Ninja.

**The full record.** A findings document with a source for every claim, a structured file of all twenty-two games, the store metadata, and the Reddit threads as read, in the RepGarden repository at docs/research/2026-10-27-game-design/. This report is a reading of that record; where the two disagree, the record wins.

**Decisions this report feeds.** The game-design decisions are recorded in docs/game-design.md in the same repository, the one place they are kept current.

> **Prepared by** Ahmed Gadir, GadirLabs, for the RepGarden build. gadirlabs.io
