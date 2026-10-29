# How growing games keep people coming back: findings

Read on 27 October 2026 for the RepGarden game-design stage. Three collection agents worked from one written brief (`brief.md` in this folder) with thirteen fixed questions per game; every claim below carries its source URL. This file is the record; `report.pdf` and `report.md` are a reading of it, and where they differ, this file wins. `apps.json` holds the same material as structured data, one object per game, with the GB App Store metadata from `report/store-meta.json` attached. Icons and screenshots are in `report/icons/` and `report/shots/`, taken from each game's own store listing.

Three groups, twenty-two games:

- **Farm, garden and creature games** (nine): Grow a Garden, Stardew Valley, Hay Day, FarmVille 2: Country Escape, Township, Gardenscapes, Animal Crossing: Pocket Camp Complete, Neko Atsume, My Tamagotchi Forever.
- **Habit apps that grow a plant or a creature** (seven): Finch, Forest, Flora, Plant Nanny, Habitica, Focus Friend, Brainrot.
- **Activity games and the baseline** (six): Pikmin Bloom, Pokémon GO, Zombies, Run!, Walkr, Sweatcoin, Duolingo.

Cross-cutting Reddit threads read directly (JSON in `evidence/reddit/`): "Tired of the daily streak punishment/reward system on apps" (r/adhdwomen, 1,031 upvotes), "what made people quit habitica" (r/habitica), "I think most habit trackers accidentally make people quit" (r/getdisciplined), "Why is gamified gyms not a thing" (r/NoStupidQuestions), "I keep quitting every habit app after 2 weeks" (r/ProductivityApps), and the Grow a Garden quitting threads.

Credits: 98 ScrapeCreators credits across the three lanes (27, 15 and 56; the Reddit search endpoints charge per post returned, now recorded in the skill). Thin evidence is marked "not confirmed" in place; the lanes' own notes on thin spots are at the end of each part.

---

# Part 1 · Farm, garden and creature games

## Farm and plant games: how they keep people coming back

Lane: FARM AND PLANT GAMES. Collected 27 October 2026 for the RepGarden game-design stage,
against the thirteen questions in the collection brief. Nine apps: eight from the App Store
plus Grow a Garden, which lives inside Roblox and has no listing of its own. App Store (GB)
ratings and counts are from `itunes.apple.com/lookup` on the day; Google Play install bands
are from the GB Play listing on the day. Claims carry their source URL; anything that could
not be sourced is marked "not confirmed".

Three corrections to the assumptions in the brief are recorded in the sections below:
Stardew Valley's crops do **not** die if you fail to water them (they stall); no public Zynga
statement explains why FarmVille 2: Country Escape dropped withering; and Township's live
simultaneous-badge count could not be confirmed, because its wiki is unfetchable and its
store screenshots are simplified marketing art.

---

### Stardew Valley

**1. Unit of play.** The farm, as individual tiles, plus the farmer as a character. You till a tile, water it, plant a seed, and each of those is one tool use that costs energy (https://stardewvalleywiki.com/Crops). "Crops are plants that are grown from seeds to be harvested for the purpose of profit, food, or gifting. Generally, each crop is seasonal" (https://stardewvalleywiki.com/Crops). Around that sits a whole second unit of play that matters more than the farm to many players: the farmer's own skills, relationships with 12 marriage candidates, the mines, fishing and the Community Center bundles (https://apps.apple.com/gb/app/stardew-valley/id1406710800). One real-world action maps to one tool swing on one tile — the game is deliberately granular and manual, and the reward for progressing is machinery that removes the manual work (see 5).

**2. Session shape.** The session unit is **the in-game day**, and you end it by choosing to go to bed. The day is bounded by two things: the clock (going to bed at or before 12:00AM "normally restores energy to its maximum"; later bedtimes restore less) and your energy bar (https://stardewvalleywiki.com/Energy). There is no quick-glance screen and no ten-second move — the mobile port's answer to that is auto-save plus control aids rather than a shorter loop: the listing advertises "new Mobile-specific features, such as auto-save and multiple controls options", and tapping an object auto-selects the right tool, "Tapping on stones, wood, stumps, boulders, rocks etc will auto-select the correct tool for the job" (https://apps.apple.com/gb/app/stardew-valley/id1406710800, https://stardewvalleywiki.com/Mobile_Controls). This is the one app in the lane whose session shape is flatly wrong for a gym: it wants a sit-down, not a glance.

**3. Absence.** **The headline claim needs correcting: crops do not die if you fail to water them.** The wiki is explicit: "Crops must be watered every day for maximum growth. If unwatered for a day, a crop will not grow. **Unwatered crops do not die, but they will not grow either.**" (https://stardewvalleywiki.com/Crops). Neglect stalls progress; it does not destroy it. Loss comes from three other places, none of them simple absence:
- **A deadline.** "On the 1st of each season, all crops that are no longer in season will wither and die, leaving behind a dead crop… Fully grown crops that are ready to harvest will wither and die when moving to a new season, however." (https://stardewvalleywiki.com/Crops)
- **Randomness.** "Lightning during thunderstorms can randomly strike crops, causing them to wither and die." (https://stardewvalleywiki.com/Crops)
- **A missing defence.** "Crops can be eaten by Crows when there are over 15 crops growing and there is no Scarecrow within range." (https://stardewvalleywiki.com/Crops)

And crucially: **real-world absence costs nothing at all.** The clock is in-game only; close the app for six months and the farm is exactly where you left it. There is no streak, nothing to protect, and no catch-up mechanic, because none is needed. The dead crop left behind is even useful — it "will keep the soil it was planted on tilled, which can reduce the amount of manual tilling and watering that needs to be done at the start of a season" (https://stardewvalleywiki.com/Crops).

**4. Currency and endogenous value.** One currency, gold (g), earned by shipping crops, fish, foraged goods and artisan products, and spent on seeds, tools, buildings, farm upgrades and gifts — so every pound of it feeds back into the farm or the relationships (https://apps.apple.com/gb/app/stardew-valley/id1406710800). There is **no real-money layer whatsoever**: ConcernedApe's own announcement set the price as "£7.99 / $7.99 / 8,99 € with no in-app purchases" and promised "It's the full game, not a cut down version" (https://www.stardewvalley.net/stardew-valley-coming-to-mobile/). The GB price is now £4.99 with no in-app purchases listed (https://apps.apple.com/gb/app/stardew-valley/id1406710800, https://itunes.apple.com/lookup?id=1406710800&country=gb). Players read the absence of a shop as the game's defining virtue: "If you are thinking of buying this app, IT IS SO WORTH THE MONEY." (https://apps.apple.com/gb/app/stardew-valley/id1406710800)

**5. Stakes, risk and chance.** The real stake is **energy, and it bites hard**. "The player becomes exhausted upon reaching 0 energy… At -15 energy, the player passes out, ending the day. If the player passes out anywhere outside the house, the player will lose 10% of their money, up to 1,000g." And the punishment reaches into tomorrow: "Exhaustion results in a 50% reduction in that night's energy restoration", a penalty you can cure by eating a Muscle Remedy or, if married, "kissing the player's spouse for the first time in the day" (https://stardewvalleywiki.com/Energy). Seasonal deadlines turn planting into a bet: plant an expensive long-growing seed too late in a season and it withers worthless on day 1 of the next (https://stardewvalleywiki.com/Crops). Chance is everywhere and mostly upside: giant crops have a "1% chance" per 3×3 grid per day and drop 15–21 items (https://stardewvalleywiki.com/Crops), there is a casino, a Night Market and random Challenge-style events. The progression reward that matters most is **risk removal**: the Sprinkler "waters 4 tiles (above, below, and to the right and left of it) every morning", unlocked at Farming level 2, and the better tiers water far more — the game lets you engineer the daily chore away entirely (https://stardewvalleywiki.com/Sprinkler).

**6. Progression.** Time is the frame: four 28-day seasons make a year, each with its own festivals, birthdays and crops, shown on a calendar you can buy and hang on your wall (https://stardewvalleywiki.com/Calendar). Milestones come from five skill trees levelled 1–10 with a profession choice at 5 and again at 10, tool upgrades, farm buildings, Community Center bundles, marriage, and a judged verdict from Grandpa at year 3 (https://apps.apple.com/gb/app/stardew-valley/id1406710800). The mobile port carries PC content up to 1.6.15 (https://stardewvalleywiki.com/Mobile_Version_History).

**7. Social.** Thin on iOS and rich inside the fiction. The launch announcement said mobile "Includes 1.3 single player content, such as the Night Market, but not Multiplayer" (https://www.stardewvalley.net/stardew-valley-coming-to-mobile/); the wiki notes Android now has "multiplayer support as an experimental feature" and that the 1.6.9 port included everything "except non-LAN multiplayer" (https://stardewvalleywiki.com/Mobile_Version_History). The real social layer is single-player: gift-giving, heart levels and 12 romanceable villagers. The March 2026 iOS update added Game Center leaderboards for Junimo Kart endless mode and deepest Skull Cavern floor — competitive, opt-in, and about side activities rather than the farm (https://apps.apple.com/gb/app/stardew-valley/id1406710800).

**8. Freedom and identity.** Very high. You name the farmer, the farm, the pet and every animal; you choose a farm layout type at the start; you lay out crops, buildings, paths and furniture freely; and you decide what each day is for (https://apps.apple.com/gb/app/stardew-valley/id1406710800). The 1.6.15.1 mobile notes refer to a tailoring menu and equipped clothes, so cosmetic self-expression is a real system (https://apps.apple.com/gb/app/stardew-valley/id1406710800).

**9. Signature interaction.** Going to bed to end the day, and the overnight tally: the shipping bin is totted up, money lands, skills level up with a jingle, and the next morning starts clean. The second signature gesture is the watering can sweep — dragging across a row of tilled tiles, which on mobile is done by "continuously holding on to the right-click or left-click control and moving the cursor" (https://stardewvalleywiki.com/Crops).

**10. UI type and art.** **Top-down world.** A hand-made 16-bit-style pixel-art farm viewed from a slightly angled top-down perspective, warm and seasonal, with hand-drawn character portraits for dialogue. The screen is **sparse**: a clock-and-date box and an energy bar at the edges, a small item toolbar, and nothing else over the world (https://apps.apple.com/gb/app/stardew-valley/id1406710800). The home screen is simply the farm with the farmer standing on it.

**11. Sound and feel.** Per-tool sound effects, seasonal music that changes with the calendar, animal noises, and the end-of-day level-up jingle. The mobile port's feel is dominated by its control schemes — tap-to-move plus auto-attack by default, with an on-screen joystick alternative, and auto-tool selection so the correct tool fires on a tap (https://stardewvalleywiki.com/Mobile_Controls). Game Center support and leaderboards arrived in 1.6.15.1 (https://apps.apple.com/gb/app/stardew-valley/id1406710800).

**12. Scale and reception.** App Store GB on 27 October 2026: **4.80 from 6,206 ratings**, £4.99, no in-app purchases (https://itunes.apple.com/lookup?id=1406710800&country=gb). Google Play: **5m+ downloads**, 4.58 from 156,785 reviews (https://play.google.com/store/apps/details?id=com.chucklefish.stardewvalley). PC release 26 February 2016; iOS 24 October 2018; Android 13 March 2019; by **ConcernedApe** (Eric Barone), with the mobile port built by London studio The Secret Police; premium one-off purchase, no in-app purchases, no ads (https://stardewvalleywiki.com/Mobile_Version_History, https://www.stardewvalley.net/stardew-valley-coming-to-mobile/).

Complaints:
- Touch controls fight the player in combat: "The on screen joysticks suck. Tap to move works until you need to do combat… I accidentally click my toolbar, switch from my sword, and get swarmed while holding a geode." (https://www.reddit.com/r/StardewValley/comments/1gqvq60/controls_on_mobile_are_so_frustrating/)
- Tap-to-move misroutes and misfires: the wiki itself warns the character "may suddenly stop, try a different path, or head off in a random direction (very likely a bug)" and that near the screen edge "it is very easy to accidentally change the selected tool, resulting in unexpected gifting or bomb usage" (https://stardewvalleywiki.com/Mobile_Controls).
- No cross-platform multiplayer on iOS, years after PC got it — mobile shipped "not Multiplayer", and Android's is still only "an experimental feature" (https://www.stardewvalley.net/stardew-valley-coming-to-mobile/, https://stardewvalleywiki.com/Mobile_Version_History).
- A long tail of port bugs: the 1.6.15.1 notes alone fix disappearing buildings, a shop crash, an infinite money exploit, an infinite item glitch and saves that would not load (https://apps.apple.com/gb/app/stardew-valley/id1406710800).

Praise:
- Value for a flat price with nothing to buy: "If you are thinking of buying this app, IT IS SO WORTH THE MONEY." (https://apps.apple.com/gb/app/stardew-valley/id1406710800)
- Sheer depth: "This is a great game to lose who knows how many hours to" (https://apps.apple.com/gb/app/stardew-valley/id1406710800), against an advertised "over 50+ hours of gameplay content" (https://apps.apple.com/gb/app/stardew-valley/id1406710800).
- Players who stick with the touch controls say the objection is overstated: "A week after playing Stardew on mobile and it's fine! Idk why all the hate on touch controls. I work it just fine!" (https://www.reddit.com/r/StardewValley/comments/1w1321d/a_week_after_playing_stardew_on_mobile_and_its/)
- The port is kept current with the PC game rather than abandoned — mobile is at 1.6.15 equivalence (https://stardewvalleywiki.com/Mobile_Version_History).

**13. Lesson for RepGarden.** The single most useful correction in this lane: the most beloved farm game in the world **does not kill your crops when you neglect them — it stalls them.** "Unwatered crops do not die, but they will not grow either" is the exact rule RepGarden should adopt for a missed session, because it punishes nothing and still makes attendance visibly matter. Steal two more things: loss attached to a *deadline you were told about* (the season boundary) rather than to absence, and progression that *removes the chore* — the sprinkler is a reward for having watered by hand, which is the right shape for a client who gets fitter and needs less hand-holding. Avoid the session shape and the energy system: Stardew's day needs fifteen uninterrupted minutes, and an exhaustion penalty that halves tomorrow's capacity after you overdid it today is precisely the wrong message for a gym app.

---

### Hay Day

**1. Unit of play.** A whole farm you own and lay out: fields of crops, animals, production buildings (bakery, BBQ grill, sugar mill, sewing machine, loom, cake oven), plus three annexes unlocked by level — a Town with visitors, a Fishing Lake, and the Valley (https://apps.apple.com/gb/app/hay-day/id506627515). One real action maps to one tap-and-timer: you tap a field to sow, tap again when the crop is ready, feed an animal and collect its goods, then feed those goods into a machine that makes a sellable product. The loop is "planting and harvesting crops for experience points and ingredients; collecting manufactured resources for XP; selling manufactured resources for XP and coins; and purchasing new equipment using coins" (https://www.gamedeveloper.com/business/game-monetization-design-analysis-of-hay-day). Goods go to a Barn, crops to a Silo (https://en.wikipedia.org/wiki/Hay_Day).

**2. Session shape.** Built from timers "ranging from 2 minutes to 20+ hours" (https://www.blog.udonis.co/mobile-marketing/mobile-games/hay-day-monetization), so the game expects many short visits rather than one long one. A ten-second visit is: open the farm, tap every ready field and machine, replant, leave — no menu needed, because the farm itself is the dashboard. The longer sit-down is the order board (up to nine truck orders at level 32), the boat dock (a boat every 4 hours, three to five item types across crates), the Roadside Shop, Derby tasks and the Valley (https://hayday.fandom.com/wiki/Truck, https://hayday.fandom.com/wiki/Boat — read via search snippet; the wiki blocks direct fetching). Supercell deliberately removed the scaffolding that would force a longer session: "There's no forced tutorial. No missions or quests in Hay Day. And there's no 'right way to play'" — Timur Haussila, Supercell (https://www.deconstructoroffun.com/blog//2013/01/behind-success-of-hay-day.html).

**3. Absence.** Nothing is lost, ever. The official Supercell page states it outright: "It never rains here, but the crops never die" (https://supercell.com/en/games/hayday/), and the App Store listing sells crops that "never die" as a feature (https://apps.apple.com/gb/app/hay-day/id506627515). An analyst reading the game from the player's side put it: "I was surprised to see the game doesn't punish you for not logging in. If you don't play the game for a while, your crops don't dry out and your starving animals somehow stay alive" (https://www.blog.udonis.co/mobile-marketing/mobile-games/hay-day-monetization). There is no daily streak that can be broken — not confirmed that any streak mechanic exists at all. Instead of punishing absence, the game **pays for return**: a farm inactive over 31 days (and not triggered in the last 365 days) gets Re-engagement Rewards — two days of special offers from visitors, a free day of Tom's services, a free day of tree/bush/rock removal, a free Silo upgrade, a free Barn upgrade, and all animals fed on return (https://ingame.help.supercellsupport.com/hay-day/en/articles/re-engagement-rewards.html, cross-read at https://hayday.fandom.com/wiki/Vacation_Mode). Players treat this as a reason to leave: one thread asks "Would you stop playing and start playing again after 31 days to get Re-engagement Rewards from game?" (https://www.reddit.com/r/HayDay/comments/1b7m4i7/would_you_stop_playing_and_start_playing_again/), and another asks "Took a break for 8 years…is it possible to get back to it?" (https://www.reddit.com/r/HayDay/comments/1tidbec/took_a_break_for_8_yearsis_it_possible_to_get/). The subreddit's own summary of the design: "Nothing Bad Ever Happens in the Oldest Game at Supercell" (https://www.reddit.com/r/HayDay/comments/1ub5k05/nothing_bad_ever_happens_in_the_oldest_game_at/). The only real forfeit in the game is a Derby task you accept and fail inside its time limit (https://myfarm.site/articles/hay-day-derby-events-guide/).

**4. Currency and endogenous value.** Coins are the soft currency, earned by filling truck and boat orders, serving town visitors and selling in the Roadside Shop, and spent on seeds, animals, buildings and expansion supplies — it feeds straight back into the farm (https://en.wikipedia.org/wiki/Hay_Day). Diamonds are the premium currency, "hard currency for skipping wait times and purchasing almost anything", with players earning "minimal diamonds naturally (mostly single units)" (https://www.blog.udonis.co/mobile-marketing/mobile-games/hay-day-monetization); diamonds also buy storage expansions, so the squeeze and the shop are the same system: "Storages get full unless you use diamonds or spend time to gather resources to expand the storages" (https://www.gamedeveloper.com/business/game-monetization-design-analysis-of-hay-day). Vouchers come from truck orders, Valley tokens come in three colours capped at 6,000 each and are spendable only in the Valley shop (https://hayday.fandom.com/wiki/Token — via search snippet). Barn upgrades consume bolts, planks and duct tape; Silo upgrades consume nails, screws and wood panels; each upgrade needs one more of each than the last, and the materials drop from harvesting, producing and mystery crates (https://hayday.fandom.com/wiki/Barn, https://hayday.fandom.com/wiki/Silo — via search snippet). So the currency that actually gates you is a drip of hardware parts, not money. Expansion supplies (land deeds, mallets, marker stakes) cost 403 coins or 12 diamonds each and unlock from level 22 (https://www.thehaytrade.com/guides/hay-day-land-expansion-materials). Supercell's stated intent: "we designed the game so that it could be played truly for free without ever having to pay in order to progress" (https://www.deconstructoroffun.com/blog//2013/01/behind-success-of-hay-day.html).

**5. Stakes, risk and chance.** There is no bet and nothing to lose outside opt-in events. The Derby is the opt-in challenge: each task awards roughly 50–320 points by difficulty, most carry a time limit from 4 hours 30 minutes up to 3 days, and a task not finished in time is not credited (https://myfarm.site/articles/hay-day-derby-events-guide/). Chance is everywhere but always additive: mystery boxes and the Daily Dirt drop expansion supplies at random (https://www.thehaytrade.com/guides/hay-day-land-expansion-materials), boat requests "appear to be random" (https://hayday.fandom.com/wiki/Boat — via search snippet), town visitors arrive on the EGGspress train every 6 hours and some ask to see a specific sanctuary animal for an extra gift (https://hayday.fandom.com/wiki/Town_Visitors — via search snippet). The App Store age rating (9+) lists "loot boxes" (https://apps.apple.com/gb/app/hay-day/id506627515).

**6. Progression.** Experience levels are the spine — they unlock the boat dock at 17, the Derby at 18, farm expansion at 22, the Valley at 25, the Fishing Lake at 27, and the ninth truck order at 32 (https://hayday.fandom.com/wiki/Fishing_Lake, https://myfarm.site/articles/hay-day-derby-events-guide/, https://hayday.fandom.com/wiki/Valley — via search snippets). Beyond levels, the milestones are capacity: each Barn and Silo upgrade, each new patch of land, each Town Station level (up to 12, for 14 visitors a train). Seasons layer on top: the Valley runs roughly three-week seasons (introduced June 2019) and the Derby runs weekly, six days from 08:00 UTC Tuesday to 08:00 UTC Monday with a 24-hour cooldown in which members can opt out or opt back in (https://myfarm.site/articles/hay-day-derby-events-guide/). A Farm Pass season unlocks at level 11 with free and paid tracks (https://www.blog.udonis.co/mobile-marketing/mobile-games/hay-day-monetization).

**7. Social.** Opt-in and layered. Neighbourhoods hold up to 30 players with chat and a weekly Derby (https://apps.apple.com/gb/app/hay-day/id506627515). Help is asked, not imposed: a neighbourhood mailbox/request board lets you ask neighbours for items, and help signs surface in chat (https://hayday.fandom.com/wiki/Mailbox — via search snippet). The Roadside Shop is real player-to-player trade: you set up to ten units of an item in a box at any price from one coin upward, and buyers find you through the Daily Dirt newspaper where you can advertise (https://hayday.fandom.com/wiki/Roadside_Shop — via search snippet, cross-read at https://www.supercheats.com/hay-day/walkthrough/roadside-shop). You can also send your personal train to a neighbour's town (https://hayday.fandom.com/wiki/Town_Station — via search snippet). A reviewer frames the competitive side as self-dosed: the Derby lets you be "as competitive (or chill) as you like" (https://www.playnforge.com/hay-day-review/).

**8. Freedom and identity.** The farm is a layout you author: you place and move buildings, fields, animals, paths and decorations, and the App Store listing sells "Decorate your farm" as a feature (https://apps.apple.com/gb/app/hay-day/id506627515). Decoration is where diamonds go for identity rather than speed, which is exactly what players resent paying for (see complaints). You also choose your sanctuary animals, your neighbourhood, and your shop prices. The refusal to teach is itself an identity choice: "we avoid teaching players to play the game" (https://www.deconstructoroffun.com/blog//2013/01/behind-success-of-hay-day.html).

**9. Signature interaction.** Dragging a finger across a field of ripe wheat and watching the whole row cut and bale under your thumb in one sweep, then dragging back over the bare soil to sow it again — harvest and replant are the same gesture on the same patch of ground, which is why a visit can be ten seconds. Not confirmed as a quoted developer statement; it is the gesture the listing's "grow wheat, corn, and other crops" loop and the review descriptions of tapping and collecting describe (https://apps.apple.com/gb/app/hay-day/id506627515, https://www.playnforge.com/hay-day-review/).

**10. UI type and art.** **Isometric world.** One continuous isometric farm you pan and pinch, with everything diegetic — no stat dashboard, because the barn, the fields and the order board *are* the readout (https://apps.apple.com/gb/app/hay-day/id506627515). The art is "bright, clean, and cartoony, with just enough detail to make everything feel alive without overwhelming your screen" (https://www.playnforge.com/hay-day-review/), described elsewhere as high-quality 2D with a warm, bright palette and a "feel-good" register (https://www.blog.udonis.co/mobile-marketing/mobile-games/hay-day-monetization). The screen is dense but legibly so: the home screen is the farm itself, with ready items flagged by icons above them and the order board, shop and barn sitting in the world as buildings.

**11. Sound and feel.** The feedback is animation-led: "Chickens flap around when you collect eggs, pigs wiggle in the mud, and machines like the bakery or jam maker have fun little animations that make the production cycle feel more satisfying" (https://www.playnforge.com/hay-day-review/). A reviewer called the result "a quietly pleasing experience" (https://www.pocketgamer.com/hay-day/review/). Push notifications carry the loop outside the app — "Milk is ready to be collected" (https://www.gamedeveloper.com/business/game-monetization-design-analysis-of-hay-day). Haptics: not confirmed.

**12. Scale and reception.** App Store GB 4.67 from 73,805 ratings on 27 October 2026 (https://itunes.apple.com/lookup?id=506627515&country=gb); Google Play 100m+ downloads, 4.4 stars from 13.1m reviews (https://play.google.com/store/apps/details?id=com.supercell.hayday). Launched 21 June 2012 on iOS, developer Supercell (https://apps.apple.com/gb/app/hay-day/id506627515). Business model: free to download with in-app purchases — diamonds £0.99–£39.99, coin packs, a £4.99 Farm Pass — plus opt-in rewarded video for higher-level players (https://apps.apple.com/gb/app/hay-day/id506627515, https://www.blog.udonis.co/mobile-marketing/mobile-games/hay-day-monetization); lifetime revenue over $1.2 billion and 300m+ downloads since 2012 (https://en.wikipedia.org/wiki/Hay_Day, https://www.blog.udonis.co/mobile-marketing/mobile-games/hay-day-monetization). DAU/MAU has run around 50–55% (https://www.deconstructoroffun.com/blog//2013/01/behind-success-of-hay-day.html).

Complaints:
- "My Barn and Silo are constantly full, which prevents me from producing items, completing orders, and making meaningful progress in the game… The expansion materials needed to increase storage capacity are extremely difficult to obtain." (https://www.sikayetvar.com/en/hay-day-us/hay-day-storage-problem-makes-progress-impossible)
- "Farm pass is worthless" — 171 upvotes, 61 comments (https://www.reddit.com/r/HayDay/comments/1n5kss1/farm_pass_is_worthless/); a related thread, "Keep playing, quit paying.", drew 136 upvotes (https://www.reddit.com/r/HayDay/comments/1t1x254/keep_playing_quit_paying/)
- "the cost of the only pretty dirt path in game is higher than my will to live" — on getting diamonds for decoration, 196 upvotes (https://www.reddit.com/r/HayDay/comments/11laikv/anyone_have_any_tips_on_how_to_get_diamonds_since/); Pocket Gamer's verdict was "just another freemium time sink" (https://www.pocketgamer.com/hay-day/review/)

Praise:
- "Nothing Bad Ever Happens in the Oldest Game at Supercell" (https://www.reddit.com/r/HayDay/comments/1ub5k05/nothing_bad_ever_happens_in_the_oldest_game_at/)
- "I was surprised to see the game doesn't punish you for not logging in. If you don't play the game for a while, your crops don't dry out and your starving animals somehow stay alive." (https://www.blog.udonis.co/mobile-marketing/mobile-games/hay-day-monetization)
- "Chickens flap around when you collect eggs, pigs wiggle in the mud, and machines… have fun little animations that make the production cycle feel more satisfying" (https://www.playnforge.com/hay-day-review/); and players return after years rather than churning for good — "Took a break for 8 years…is it possible to get back to it?" (https://www.reddit.com/r/HayDay/comments/1tidbec/took_a_break_for_8_yearsis_it_possible_to_get/)

**13. Lesson for RepGarden.** Hay Day proves a fourteen-year retention curve with zero decay, so the pressure must come from *capacity and orders*, not loss: give the client a barn that fills up, a weekly order to fill, and a slow drip of upgrade parts earned from logged sets, so the squeeze is "I have more than I can store" rather than "my plants died". Copy the opt-in Derby shape for the trainer's challenges — a bounded weekly task with a real deadline, which a client can sit out with no penalty, is the only place stakes belong in a 3-days-a-week app — and copy the Re-engagement Reward: pay a returning client with a free capacity upgrade instead of showing them a broken streak. Avoid Hay Day's one genuine failure: gating the identity layer (paths, decoration) behind a currency nobody can earn is the single loudest complaint in its own subreddit, so in a free app with no shop, every cosmetic must be buyable with training, or the garden stops being yours.

---

### FarmVille 2: Country Escape

**1. Unit of play.** A coastal farm you manage: crops, animals (horses, chickens, cows, farm dogs), crafting workshops that turn harvests into recipes like apple pies, and a map of off-farm Places of Interest you send Farm Hands to forage (https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267). One action maps to a tap plus a timer, exactly as in Hay Day; a reviewer called it "a pretty standard 'tap and wait' game" (https://www.withoutthesarcasm.com/posts/farmville-2-country-escape-review/). Storage is split across a Barn, a Crop Silo and Seaway Storage (https://zyngasupport.helpshift.com/hc/en/11-farmville-2-country-escape/section/300-crop-silo/). The essential history: the original FarmVille (Facebook, launched 19 June 2009, peak 83.76m monthly and 34.5m daily active users in March 2010) made the farm itself the thing at risk — "Crops wither if unharvested within 2.5 times their growth duration", with purchasable Farm Cash buying "unwither" items (https://en.wikipedia.org/wiki/FarmVille). It closed on 31 December 2020 because "Facebook was to stop supporting games running on Flash Player… on that day" (https://en.wikipedia.org/wiki/FarmVille).

**2. Session shape.** Short bursts against timers, with the player expected to pick crop lengths to match their own absence: guides advise planting fast crops while you are actively playing and "plant slower crops and start longer crafting jobs so they finish by your next visit" when you leave (https://www.techbloat.com/farmville-2-country-escape-top-10-tips-hints-and-cheats.html). A ten-second visit is harvest, replant, restart a workshop, spin the daily Prize Wheel. The pacing degrades as you level: "wait times have increased to hours rather than minutes" and "soon enough it takes hours upon hours to see progress" (https://www.pocketgamer.com/farmville-2-country-escape/review/, https://www.148apps.com/reviews/farmville-2-country-escape-review/). Crucially it runs with no connection — "Play fully offline — no internet connection required" (https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267), so a session is never blocked by signal, and you "play offline and then upload what's been going on when it's convenient" (https://www.148apps.com/reviews/farmville-2-country-escape-review/).

**3. Absence.** No withering is documented anywhere in Country Escape: the official Zynga help centre's entire Crop & Silo section — "What is the Crop Silo?", "What can the Crop Silo store?", "What happens when my Crop Silo is full?", "How do I upgrade the Barn, Crop Silo and Seaway Storage?" — contains no article on crops withering, spoiling or dying (https://zyngasupport.helpshift.com/hc/en/11-farmville-2-country-escape/section/300-crop-silo/), and veteran players bank ready crops indefinitely as a tactic: "Many of the fast-growing crops I just leave ready to harvest, so that when I need them, I can just harvest and replant them immediately" (https://www.withoutthesarcasm.com/posts/top-answers-farmville-2-country-escape-part-2/).

**Important correction to the brief: I could not confirm that Zynga publicly said it removed withering for Country Escape.** The much-quoted Tim LeTourneau line is from September 2012 and is about FarmVille 2 on Facebook, where he cites withering as the mechanic that is *still present*: "I'd say first and foremost, in most social games, what you're really combatting is time… For example, that your crops wither if you don't come back and take care of them. So it is really positive, the pinch is really the speed at which we progress, or really, the loss of your effort." — Tim LeTourneau, VP of Games, Zynga, interviewed by Kirk Hamilton, 5 September 2012 (https://kotaku.com/zynga-thinks-youll-like-farmville-2-im-not-so-sure-5940700). FarmVille 2 on Facebook kept withering at the same 2.5× multiplier with a Farm Cash "unwither" (https://en.wikipedia.org/wiki/FarmVille_2, https://farmville2.fandom.com/wiki/Unwither). So the honest reading is: withering was dropped between the Facebook line and the 2014 mobile game, but the stated reason is not confirmed.

What *is* well documented is how withering was received on the original: the Unwither Ring cost 250 Farm Cash, about $42 of real money, and was defended on the grounds that "The threat of withering plants is what keeps players engaged and coming back for more on a daily basis" — Libe Goad, 14 February 2010 (https://www.yahoo.com/news/2010-02-14-farmville-unwither-ring-the-worst-thing-to-happen-to-virtual-fa.html). Time named FarmVille one of the "50 Worst Inventions" as "the most addictive of Facebook games" and "a series of mindless chores on a digital farm"; Jonathan Blow criticised it for creating negativity and encouraging friend exploitation; Ian Bogost built Cow Clicker as satire (https://en.wikipedia.org/wiki/FarmVille). No streak mechanic in Country Escape is documented, and no streak protection — not confirmed either way.

**4. Currency and endogenous value.** Coins are the soft currency for seeds, animals and buildings. Keys are the premium currency: they "let you skip wait times and unlock multiple copies of buildings, which are essential for some of the tougher timed quests" (https://www.pocketgamer.com/farmville-2-country-escape/review/), and they also pay for expansion, so they feed back into capacity rather than being cosmetic. They are also the sorest point in the game: keys are "available in very limited number after the initial introductory package" (https://www.148apps.com/reviews/farmville-2-country-escape-review/) and "very hard to come by" despite being "essential for expanding your farm's production" (https://www.withoutthesarcasm.com/posts/farmville-2-country-escape-review/). Experienced-player advice is to refuse the impatience sell entirely: "Treat keys like a long-term upgrade fund, not an emergency button" (https://www.techbloat.com/farmville-2-country-escape-top-10-tips-hints-and-cheats.html). Real money buys key and coin packs from £1.99 (Pile of Keys) to £19.99, plus a Premium Farm Pass (https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267). Cosmetic decoration (flowers, buildings, scenery) exists alongside this (https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267).

**5. Stakes, risk and chance.** Chance is the main spice and it is all upside: a daily Prize Wheel spin with an extra spin for inviting friends, daily mystery chests, a Prize Tent, and Prospector's Corner — Zynga publishes drop rates for the Prize Wheel, Prospector's Corner, the Magic Magnus Show and Pet Pass as separate help sections (https://zyngasupport.helpshift.com/hc/en/11-farmville-2-country-escape/, https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267). Farm Hands are the one genuine gamble of time: you commit hands to a Place of Interest for "a chance to find the rarest and most valuable items", with per-location capacities (Grandma's Glade 2 hands, Pappy's Pond 4, Merryweather Mine 6) and per-hand bonus percentages (http://siege-engine.blogspot.com/2020/03/farmville-2-country-escape-farm-hands.html). Co-op group challenges and limited-time events are the opt-in competitive stakes (https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267). No betting or risked loss is documented.

**6. Progression.** Experience levels unlock crops, buildings and areas, with storage upgrades as the parallel capacity track across Barn, Crop Silo and Seaway Storage (https://zyngasupport.helpshift.com/hc/en/11-farmville-2-country-escape/section/300-crop-silo/). On top sit named seasonal and collection systems — Collections, Wild Trails, Crown Society, and timed events such as Pet Pals, Tiny Tracks and Treasure Trench — each its own chapter with its own rewards (https://zyngasupport.helpshift.com/hc/en/11-farmville-2-country-escape/). Milestones are flagged as "milestone rewards" in the game's own Hot Topics (https://zyngasupport.helpshift.com/hc/en/11-farmville-2-country-escape/). Expansion of land is key-gated and reviewers found it "more restrictive than predecessor regarding decorative options and expansion" (https://www.148apps.com/reviews/farmville-2-country-escape-review/).

**7. Social.** Opt-in, and explicitly redesigned to stop the spam the original was infamous for — the original's social system had players "perform five actions on each other's farms per day by 'visiting' it" and gift-begging was the alternative to paying (https://en.wikipedia.org/wiki/FarmVille). Country Escape replaces that with Farm Co-ops you join or create to "trade goods, complete group challenges, and progress together", with in-game chat (https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267), plus a global market for player-to-player trading and Speed Seed requests to friends (https://www.148apps.com/reviews/farmville-2-country-escape-review/, https://zyngasupport.helpshift.com/hc/en/11-farmville-2-country-escape/). It was built "with optimizations to save time and reduce social spamming" and is "designed for iOS without requiring pestering friends for items" (https://www.148apps.com/reviews/farmville-2-country-escape-review/). Zynga's framing on the mobile relaunch: "The game is better with friends, but that's the player's choice" — Jonathan Knight, VP of Games (https://www.pocketgamer.biz/crops-with-clans-how-zynga-rethought-farmville-2-for-the-post-facebook-generation/). Players sort themselves by intensity, advertising for a "no pressure" co-op (https://www.reddit.com/r/farmville2/comments/1nwh6b7/looking_for_a_no_pressure_coop/).

**8. Freedom and identity.** You decorate the farm "with flowers, buildings, and scenery", name and keep pets and animals including farm dogs and horses, and choose your co-op (https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267). Reviewers rated the customisation thinner than the Facebook original's (https://www.148apps.com/reviews/farmville-2-country-escape-review/). Crafting recipes give a soft identity — which goods you specialise in — rather than a visual one.

**9. Signature interaction.** Sending a Farm Hand off the farm, down the coast road to Grandma's Glade or Merryweather Mine, and getting back a bag of foraged rarities you could not have grown — the game's distinctive move is dispatching a helper into the world and waiting for the surprise, not tending a square (https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267, http://siege-engine.blogspot.com/2020/03/farmville-2-country-escape-farm-hands.html). The original FarmVille's signature was the opposite and is worth naming for contrast: the feed post asking a friend to come and water your dying crops (https://en.wikipedia.org/wiki/FarmVille).

**10. UI type and art.** **Isometric world.** A single continuous isometric coastal farm you scroll, with a map layer for off-farm Places of Interest (https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267). The art is "bright and colorful", with "a hopeful and cheery tone" (https://www.withoutthesarcasm.com/posts/farmville-2-country-escape-review/), and the interface was judged "welcoming enough — pleasant and straightforward" (https://www.pocketgamer.com/farmville-2-country-escape/review/). The screen is dense: crops, animals, workshops, co-op and event buttons all compete. The home screen is the farm, with the Barn, Crop Silo and workshops placed in it as buildings and event entry points layered over the edges.

**11. Sound and feel.** The felt experience reviewers report is progress-bar watching: it "boils down to watching progress bars fill up" (https://www.pocketgamer.com/farmville-2-country-escape/review/), with the appeal being rhythm rather than punch — "There's a certain rhythm to all this growing, feeding, and selling that makes the early levels fly by" (https://www.withoutthesarcasm.com/posts/farmville-2-country-escape-review/). Specific haptics, sound design and completion animations: not confirmed.

**12. Scale and reception.** App Store GB 4.61 from 27,054 ratings on 27 October 2026 (https://itunes.apple.com/lookup?id=824318267&country=gb); Google Play 50m+ downloads, 4.6 stars from 3.23m reviews (https://play.google.com/store/apps/details?id=com.zynga.FarmVille2CountryEscape). iOS release 17 April 2014 (https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267); Wikipedia gives the platform release as 10 April 2014 (https://en.wikipedia.org/wiki/FarmVille). Developer Zynga Inc. Business model: free to download with in-app purchases — key and coin packs £1.99–£19.99, Premium Farm Pass — plus event passes and published gacha drop rates (https://apps.apple.com/gb/app/farmville-2-country-escape/id824318267, https://zyngasupport.helpshift.com/hc/en/11-farmville-2-country-escape/). Metacritic: Metascore 64 from 4 critics, user score 5.3 from 8 ratings (https://www.metacritic.com/game/farmville-2-country-escape/).

Complaints:
- "FarmVille 2: Country Escape is a true time waster. Despite plenty of content that could last weeks, it boils down to watching progress bars fill up." — Pocket Gamer UK, 50/100, Danny Russell, 2 May 2014 (https://www.pocketgamer.com/farmville-2-country-escape/review/)
- Keys are "very hard to come by" yet "essential for expanding your farm's production", and the tap-and-wait loop "gets kind of old after a while" (https://www.withoutthesarcasm.com/posts/farmville-2-country-escape-review/, https://www.148apps.com/reviews/farmville-2-country-escape-review/)
- "Average game but very slow and crashes a lot… Items and expansions can be pricey." — Metacritic user Xbluannax, 5/10 (https://www.metacritic.com/game/farmville-2-country-escape/); storage friction recurs on the subreddit as "Barn and Silo issues" (https://www.reddit.com/r/farmville2/comments/1tkbrsk/barn_and_silo_issues/)

Praise:
- "The game is bright and colorful, and has a hopeful and cheery tone" and manages to feel "fun" and "relaxing" (https://www.withoutthesarcasm.com/posts/farmville-2-country-escape-review/)
- "it's possible to play offline and then upload what's been going on when it's convenient", and it is designed without "pestering friends for items" (https://www.148apps.com/reviews/farmville-2-country-escape-review/)
- "the first few days with FarmVille 2: Country Escape were almost fever-inducing in their addictiveness" (https://www.pocketgamer.com/farmville-2-country-escape/review/); and players self-select their intensity, advertising for a "no pressure" co-op (https://www.reddit.com/r/farmville2/comments/1nwh6b7/looking_for_a_no_pressure_coop/)

**13. Lesson for RepGarden.** The FarmVille arc is the clearest argument in the lane against decay: the mechanic that made the original a phenomenon is also the one that got it called "a series of mindless chores" and spawned a $42 ring whose only job was to switch the punishment off, and the successor that survived on mobile has no withering at all — so never let a missed gym day kill a vegetable, and never sell the client a way to undo a loss. Steal the Farm Hand instead: an opt-in dispatch that costs nothing to skip, runs while the client is away, and returns a random useful thing is the cheapest way to make the evening check-in worth opening, and it needs no trainer input. Avoid Country Escape's two real failures — a scarce premium currency sitting in front of every capacity upgrade, which turned its reviews sour, and timers that stretch from minutes to "hours upon hours" as you level, which is exactly backwards for a client who trains more as they get fitter.

---

### Township
**1. Unit of play.** A town plus a farm in one isometric world: you "plant/harvest crops > craft goods > send them away with trains, planes or zoo orders to collect coins > upgrade your buildings > expand your territory to unlock new crops" (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). One real-world action maps to one tap that starts a real-time timer — "farming and manufacture take time to finish, as the game is in sync with real time" (https://en.wikipedia.org/wiki/Township_(video_game)), and goods are logically composed, e.g. "pizza is cheese, tomato and wheat plus two hours of waiting time" (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game).

**2. Session shape.** Designed as many short returns, not one long sit-down: every action is time-gated, creating "a production puzzle as players have to think about what they produce in which order and when they need to come back" (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). A Play reviewer describes the free-play rhythm bluntly: "you can keep it free if you are willing to play for 3 minutes a day and then wait 24hrs for a pittance of free stuff" (https://play.google.com/store/apps/details?id=com.playrix.township). The ten-second action is harvesting: "Select a field and drag the sickle from the bottom panel to it" or "double-click a field to collect crops if they're already ripe" (https://playrix.helpshift.com/hc/en/3-township/faq/152-farming-fields-crops-and-animals/). The long sit-down is the match-3 side game and the Regatta.

**3. Absence.** Nothing dies or decays. No source found describes crops withering, spoiling or being lost — the official farming help page covers only planting and harvesting with no decay step (https://playrix.helpshift.com/hc/en/3-township/faq/152-farming-fields-crops-and-animals/), the Wikipedia gameplay section describes no loss mechanic (https://en.wikipedia.org/wiki/Township_(video_game)), and the billion-dollar teardown's loop has no decay stage (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). The game even advertises offline play: match-3 is "all available offline!" (https://apps.apple.com/gb/app/township/id638689075). **Absence of a withering mechanic is strongly implied but not confirmed by an explicit source** — the Township wiki returns HTTP 402 to all fetchers. There is no daily streak and therefore nothing to protect. The pressure is spatial, not temporal: the barn. "If too many items accumulate in there, the barn won't be able to accept any new stuff you produce" (https://www.levelwinner.com/township-guide-2021-update-tips-tricks-strategies-to-grow-and-expand-your-town/), and the barn "sets the capacity of all items a player can store and it will fill up very quickly as you level up… The moment you upgrade it, you will reach the new threshold within hours" — "one of the first conversion mechanics" (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). Players feel it: "Storage too limited for produce, materials for upgrade too limited" (https://play.google.com/store/apps/details?id=com.playrix.township).

**4. Currency and endogenous value.** Coins are soft currency from orders and sales, spent on buildings, crops and decorations; Township Cash (T-Cash) is hard currency for timer skips and premium purchases, and notably "the only option to purchase more coins is spending money" (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). A third quasi-currency gates everything structural: trains bring back "building materials, such as nails, paint, hammers and more" needed for construction and barn upgrades (https://www.levelwinner.com/township-guide-2021-update-tips-tricks-strategies-to-grow-and-expand-your-town/). Spending feeds straight back into capacity and production, not cosmetics only — though decoration is a real spend category, with "over 200" decorations available (https://en.wikipedia.org/wiki/Township_(video_game)) sold against "self-expression… visible to visiting players" (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). The real-money layer is perceived badly by long-term players: "Then the game devs sold it. Since then the buyer has turned it into a cash cow. The game is being changed to make it too difficult to play without spending" (https://play.google.com/store/apps/details?id=com.playrix.township).

**5. Stakes, risk and chance.** No betting and no loss of what you built. Chance is layered on top: the App Store listing warns "Some in-game elements (including randomized items) can be purchased for real money" and the listing carries a "Loot Boxes" label (https://apps.apple.com/gb/app/township/id638689075). Mine expeditions use ingots to increase "treasure probability on island expeditions" (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game), the zoo rewards "animal cards" with rarities every 12 completed orders (same), and the Piggy Bank fills as you complete orders then offers a discounted cash bundle (same). Opt-in challenge is the Regatta and the limited-time events, run "in 2-3 weeks cadence" with 7–10 day durations (same).

**6. Progression.** XP levels are the spine — "leveling up by completing orders" unlocks whole new systems at fixed gates: trains at level 5 (https://en.wikipedia.org/wiki/Township_(video_game)), the airport at 17, the mine at 21 (same), the zoo at level 40 (https://medium.com/@aarthi.design/playrixs-township-6418f4ce319d). Milestones are therefore new *kinds* of play rather than bigger numbers, which the teardown calls content unlocks that "change how they play the game" (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). A 28-day Gold Pass season adds a parallel reward track with 30 tiers (same).

**7. Social.** Opt-in and layered. Co-ops allow "sending or requesting materials" and "Players can also ask for help from other players, share excess resources with co-op members or stockpile if they want for personal gains" (https://medium.com/@aarthi.design/playrixs-township-6418f4ce319d). The Regatta is "periodic competition against other Co-ops/teams for rewards and global ratings", needing 30 active players for the global leaderboard — and the teardown openly doubts it: "whether a feature like this really improve the game or burn players out. After all, most of the players playing Township are likely playing the game to unwind" (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). That doubt is borne out: an App Store reviewer describes being "kicked from teams for insufficient task completion" and says the game "has stopped being fun" (https://apps.apple.com/gb/app/township/id638689075?see-all=reviews).

**8. Freedom and identity.** High. "Build your dream town! Construct houses, factories, and community buildings, grow crops on your farm, and decorate your town just the way you like" (https://apps.apple.com/gb/app/township/id638689075), with over 200 decorations (https://en.wikipedia.org/wiki/Township_(video_game)). Decoration is so dominant that a player posted "I never realised that most of my town was decorations until now" (https://www.reddit.com/r/TownshipGame/comments/1uprxkd/i_never_realised_that_most_of_my_town_was/).

**9. Signature interaction.** Dragging the sickle across a ripe field — "the slick use of a sickle to harvest crops, attaching milking device to a cow or mining for metal; everything is naturally mapped to the real world execution" (https://medium.com/@aarthi.design/playrixs-township-6418f4ce319d). Second is the thought-bubble: a building floats a picture of what it wants, visible in the store screenshot as a speech bubble showing a strawberry and sugarcane over the barn (https://apps.apple.com/gb/app/township/id638689075).

**10. UI type and art.** ui_type: **isometric world**. Bright, saturated, chunky 3D-rendered cartoon art — red barn, green roofs, glossy produce, no outlines, everything reads at thumbnail size; Playrix markets "Stunning graphics and charming animations" (https://apps.apple.com/gb/app/township/id638689075). On the App Store home-screen screenshot I counted **seven persistent chrome elements** around the world: a level star with XP bar (top-left), a T-Cash counter with a green "+" buy button (top-right), a coins counter beneath it, a hard-hat build button (bottom-left), and helicopter and train buttons (bottom-right), plus in-world request bubbles over buildings (https://apps.apple.com/gb/app/township/id638689075). **A simultaneous CTA/badge count for the live game is not confirmed** — Playrix's store screenshots are simplified marketing art, and the wiki is unfetchable. Indirect evidence says the live screen is far denser: a review describes "clear tabs for farm, town, factory, orders, zoo, mine, match-3, and events" (https://iphoneappsarena.com/township/), a Metacritic reviewer criticises "poor interface design with confusing button placement" and "the tendency to put activation and cancellation type buttons right next to each other" (https://www.metacritic.com/game/township/), and the top-voted clutter thread on the subreddit is simply titled "Annoying popups" (https://www.reddit.com/r/TownshipGame/comments/1uovwp1/annoying_popups/). Worth noting the density grew over time: a 2017 usability audit praised it, finding "it incorporates many visual elements whilst using less textual information" and that "Ads are discreetly placed inside the gameplay rather than annoying pop-ups that appears out of nowhere" (https://medium.com/@aarthi.design/playrixs-township-6418f4ce319d) — the opposite of what 2026 players say.

**11. Sound and feel.** Not confirmed in detail. What is confirmed: the game leans on animation rather than text — "For every action that is performed there is a clear indication of the outcome… Upon completion it lets the player know with an icon indicating its ready to be occupied" (https://medium.com/@aarthi.design/playrixs-township-6418f4ce319d), and the store promises "charming animations" (https://apps.apple.com/gb/app/township/id638689075). No haptics documentation found.

**12. Scale and reception.** iOS GB rating **4.72** from **263,895** ratings (https://itunes.apple.com/lookup?id=638689075&country=gb). Google Play: **500,000,000+ installs**, 4.60 from 12,956,959 ratings, PEGI 16 (https://play.google.com/store/apps/details?id=com.playrix.township). Launched **2012** on iOS, 2013 on Android (https://en.wikipedia.org/wiki/Township_(video_game)); the GB App Store listing for id 638689075 shows a 23 October 2013 release date (https://itunes.apple.com/lookup?id=638689075&country=gb). Developer **Playrix**. Business model: free-to-play with IAP (£1.99–£6.99 packs listed), a loot-box label, a Gold Pass season pass and Piggy Bank bundles (https://apps.apple.com/gb/app/township/id638689075, https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). By 2021 it had 248M+ downloads and $849M+ revenue (https://en.wikipedia.org/wiki/Township_(video_game)).

Complaints:
- "Annoying popups" — the top-voted clutter thread in r/TownshipGame, 52 upvotes, 13 comments (https://www.reddit.com/r/TownshipGame/comments/1uovwp1/annoying_popups/)
- "poor interface design with confusing button placement… the tendency to put activation and cancellation type buttons right next to each other" (https://www.metacritic.com/game/township/)
- "Storage too limited for produce, materials for upgrade too limited… the game reaches a level where paying is the only way to progress" (https://play.google.com/store/apps/details?id=com.playrix.township)
- "Everything costs too much or takes too long" — describes the experience as "stress inducing" rather than relaxing (https://apps.apple.com/gb/app/township/id638689075?see-all=reviews)
- "This game is stressful now", 83 upvotes (https://www.reddit.com/r/TownshipGame/comments/1sw8z1g/this_game_is_stressful_now/)

Praise:
- "It is very addictive 😄 a lot of fun when competing in competitions. I've joined family members in so we have lots of fun together." (https://play.google.com/store/apps/details?id=com.playrix.township)
- "Almost a year to get there! Looking forward to another. Been a fun relaxing game 💚", 50 upvotes (https://www.reddit.com/r/TownshipGame/comments/1adg8k7/almost_a_year_to_get_there_looking_forward_to/)
- "The town itself is still lovely and that's my favourite bit" — from an otherwise one-star review (https://play.google.com/store/apps/details?id=com.playrix.township)
- "Love this game" — praises the cooperative regatta events and prompt developer fixes (https://apps.apple.com/gb/app/township/id638689075?see-all=reviews)

**13. Lesson for RepGarden.** Township proves that a farm does **not** need withering to create urgency: it uses a *capacity* squeeze (the barn) instead of a *decay* squeeze, so missing three days costs you nothing you built — exactly right for a client on trainer-prescribed rest days (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). Copy the thought-bubble: a vegetable that floats a picture of what it needs turns the whole screen into a single glanceable instruction, readable in the few seconds between sets (https://medium.com/@aarthi.design/playrixs-township-6418f4ce319d). **Avoid** Township's accreted density and its competitive co-op: a 2017 audit called the UI clean, and by 2026 the subreddit's top clutter thread is "Annoying popups" and players say "This game is stressful now" — and the game's own teardown doubts the Regatta because "most of the players playing Township are likely playing the game to unwind" (https://www.reddit.com/r/TownshipGame/comments/1uovwp1/annoying_popups/, https://www.reddit.com/r/TownshipGame/comments/1sw8z1g/this_game_is_stressful_now/, https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). One scene, one badge, no leaderboard that can kick you out.

---

### Gardenscapes

**1. Unit of play.** A derelict estate garden, restored area by area. The unit that grows is the *task*: a cleanup, repair, planting or decoration job bought with Stars. One match-3 level won = exactly 1 Star ("Each star is earned by completing a level, an easy to understand system." — https://www.deconstructoroffun.com/blog/2017/5/15/gardenscapes-one-big-pivot-to-success). Early tasks cost 1 Star, later ones several, and a group of tasks makes up one in-game "day" (https://www.levelwinner.com/gardenscapes-guide-2020-update-tips-tricks-strategies-to-beat-every-level-and-restore-the-garden-to-its-former-glory/). The critical structural fact for RepGarden: **the garden is never the activity.** The activity is an unrelated puzzle; the garden is purely the receipt for having done it (https://en.wikipedia.org/wiki/Gardenscapes:_New_Acres).

**2. Session shape.** Two clearly separated screens. The glance screen is the garden itself with the Stars counter, the coin counter, the lives hearts and the "tablet" that holds the task list; the sit-down screen is the match-3 board. A level runs one to three minutes, and the session is capped by lives, not by will: 5 lives maximum, one lost per failed level, one restored every 30 minutes, so a full bar takes 2.5 hours (Playrix's own help page: "You can have a maximum of 5 lives (or 8 with the Garden Pass during events)" and "one life restores every 30 minutes" — https://playrix.helpshift.com/hc/en/5-gardenscapes/faq/16021-how-to-get-lives/?l=en). In ten seconds you can spend a Star on a task and watch the corner of the garden change, read a line of Austin's dialogue, or take the daily Lucky Spin prize wheel (https://playrix.helpshift.com/hc/en/5-gardenscapes/section/216-gameplay-guide/?l=en). From level 18 there is also a deliberate batching affordance: "Save up your stars instead of spending them task by task, and finish the whole day in one go… a **Complete the Day** button will appear on your tablet" (https://playrix.helpshift.com/hc/en/5-gardenscapes/faq/16471-completing-the-day/?l=en).

**3. Absence.** Nothing decays, ever. Restored areas are permanent; the guide's summary is blunt — tasks are permanent restorations with no maintenance requirement (https://www.levelwinner.com/gardenscapes-guide-2020-update-tips-tricks-strategies-to-beat-every-level-and-restore-the-garden-to-its-former-glory/). Absence is in fact *rewarded*: lives regenerate while you are away, so you come back to a full bar of five (https://playrix.helpshift.com/hc/en/5-gardenscapes/faq/16021-how-to-get-lives/?l=en). There is no streak in the core loop. The only cost of being away is missing time-limited events, the Garden Pass and team competitions, which expire on a calendar you do not control (https://apps.apple.com/gb/app/gardenscapes/id1105855019). Reviews are warm about the no-decay garden and hostile about the event calendar: "Lately I have to dismiss a stack of popups before I can actually start: event announcements, limited-time deals, click here for a reward chain, timers, special passes, side stories. By the time I reach the level I wanted, my mood has gone from cozy to an annoyed 'ugh, fine.'" (https://www.reddit.com/r/Gardenscapes/comments/1tusjja/anyone_else_exhausted_by_how_the_game_keeps/)

**4. Currency and endogenous value.** Two currencies, deliberately split. **Stars** are earned only by winning levels and spent only on garden tasks, and cannot be bought with money at any price — Playrix restricted purchasable currency to coins: "In Gardenscapes, players can only purchase boosters in the core gameplay. Unlocking Narrative and Decorations can only be done by winning the match 3 levels" (https://www.deconstructoroffun.com/blog/2017/5/15/gardenscapes-one-big-pivot-to-success). **Coins** are earned in levels, from teams, from watching ads and from purchase, and are spent on boosters, on extra moves (900 coins for 5 extra moves, escalating on repeat) and on instant life refills (900 coins) (https://www.levelwinner.com/gardenscapes-guide-2020-update-tips-tricks-strategies-to-beat-every-level-and-restore-the-garden-to-its-former-glory/). So Stars feed straight back into the thing you care about and money cannot touch them; coins feed back only into your *ability* to earn Stars. In-app purchases on the GB listing run from 1000 Coins at £0.99 to kit bundles at £4.99–£5.99 (https://apps.apple.com/gb/app/gardenscapes/id1105855019). Lifetime revenue was near $2bn by 2021 on 213m+ installs, about $7 per install (https://en.wikipedia.org/wiki/Gardenscapes:_New_Acres).

**5. Stakes, risk and chance.** Failing a level costs a life, which is the only real loss. Coins can be gambled on sunk cost: buy 5 more moves for 900 coins when you are one move short, then again at a higher price (https://www.levelwinner.com/gardenscapes-guide-2020-update-tips-tricks-strategies-to-beat-every-level-and-restore-the-garden-to-its-former-glory/). Randomness is layered on top: the daily Lucky Spin wheel, and "Challenge levels — a new type of match-3 level that appears randomly" (https://playrix.helpshift.com/hc/en/5-gardenscapes/section/216-gameplay-guide/?l=en). Players widely suspect the difficulty is tuned against them: "Does the game hate me/us? it feels rigged" (https://www.reddit.com/r/Gardenscapes/comments/1ufkc54/does_the_game_hate_meus_it_feels_rigged/).

**6. Progression.** A nested ladder: level → Star → task → the day's progress bar → a completed day → a new garden area. "Once your progress bar reaches 100% and you've completed your current set of tasks, you'll be able to begin a new day", and starting a new day also refills all five lives (https://www.levelwinner.com/gardenscapes-guide-2020-update-tips-tricks-strategies-to-beat-every-level-and-restore-the-garden-to-its-former-glory/). The visible rank is the match-3 level number, and there are "Over 16,000 captivating levels", so the ladder is effectively endless (https://apps.apple.com/gb/app/gardenscapes/id1105855019). The genuine milestone is unlocking a new area of the garden — the treehouse expansion is the one Playrix names as a gate (https://playrix.helpshift.com/hc/en/5-gardenscapes/faq/16471-completing-the-day/?l=en).

**7. Social.** All opt-in and all bolted on beside the garden, never inside it. Teams give free coins and life-sharing through a chat request system, requestable every 4 hours (https://www.levelwinner.com/gardenscapes-guide-2020-update-tips-tricks-strategies-to-beat-every-level-and-restore-the-garden-to-its-former-glory/). The store listing names competitive events called Expeditions, and the help centre has whole sections for Teams and for Events and Competitions (https://apps.apple.com/gb/app/gardenscapes/id1105855019, https://playrix.helpshift.com/hc/en/5-gardenscapes/section/216-gameplay-guide/?l=en). Players recruit for teams on Reddit, so the social layer has real pull (https://www.reddit.com/r/Gardenscapes/comments/1rvlwnu/looking_for_active_team/).

**8. Freedom and identity.** Narrow but well-placed. Each decoration task offers a choice of three designs, and — the detail worth copying — the choice is reversible for free forever: "You have 3 designs to choose from and may change this for free anytime simply by long pressing on the item" (https://www.levelwinner.com/gardenscapes-guide-2020-update-tips-tricks-strategies-to-beat-every-level-and-restore-the-garden-to-its-former-glory/). You cannot place objects freely or lay out the garden; you pick between pre-authored variants. There is a profile and friends system (https://playrix.helpshift.com/hc/en/4-gardenscapes/).

**9. Signature interaction.** Spending a Star from the tablet on a task and watching one corner of the garden visibly transform — the before-and-after. It is also the thing players say has been diluted: "I will grind for stars for an evening, finally buy something, and it turns out to be a bench. Then the game immediately asks for five more stars to move a plant two feet… I want proper wow-the-garden-looks-different moments, not congrats-you-unlocked-sweeping." (https://www.reddit.com/r/Gardenscapes/comments/1u8bssl/rant_makeover_tasks_have_turned_the_garden_into_a/). Worth noting that the gesture the public associates with Gardenscapes is not in the game at all: the ASA banned Playrix's pull-the-pin ads in 2020 because the minigame they showed "was only available after the first twenty levels" and reached by roughly 0.03% of players (https://techraptor.net/gaming/news/uk-asa-upholds-misleading-pin-pulling-puzzle-ad-claims-against-playrix, https://www.littlelaw.co.uk/2020/11/17/gardenscams-advertising-standards-authority-bans-adverts-for-homescapes-and-gardenscapes-games/).

**10. UI type and art.** **Side-on single scene.** The garden is a painterly, warmly lit 2.5D diorama viewed from slightly above and to the side, which you pan across area by area; the art is lush, high-saturation illustrated realism rather than cartoon, with character portraits for Austin the butler and the dog (https://apps.apple.com/gb/app/gardenscapes/id1105855019, https://en.wikipedia.org/wiki/Gardenscapes:_New_Acres). The screen is **dense and getting denser**: garden scene plus Stars counter, coin counter, five life hearts, the tablet task button, the Lucky Spin, the play button and a stack of event icons and timed offer badges. That density is the single most-cited complaint: "it feels like I am supposed to care about five different currencies and multiple boards. I am not trying to min-max. I just want the simple loop: play a level, get stars, decorate, move on." (https://www.reddit.com/r/Gardenscapes/comments/1tusjja/anyone_else_exhausted_by_how_the_game_keeps/)

**11. Sound and feel.** Tactility is the point. Gamezebo's review: "The boards are colorful and lovely to look at, with large puzzle pieces that have a gratifying tactility when moved", and power-ups deliver "extremely satisfying board-wiping eruptions" (https://www.gamezebo.com/reviews/gardenscapes-new-acres-review/). Power-ups escalate by match size — Firecrackers from 4-tile matches, Bombs from 5, Dynamite, TNT Barrels — and the Rainbow Blast is "the only chargeable power-up", a meter that fills and then discharges across the board (https://playrix.helpshift.com/hc/en/5-gardenscapes/section/216-gameplay-guide/?l=en). The detail most worth stealing is Austin as a reactive presence rather than a menu: he "congratulates successful matches, offers encouragement after failures, and performs ambient activities like watering plants, reading the newspaper, posting pictures of the estate on his social media" (https://www.gamezebo.com/reviews/gardenscapes-new-acres-review/). Garden tasks resolve with an animated transformation plus a line of dialogue, and the animations are load-bearing: one long-time reviewer complains the game became "annoying" after visual changes, "preferring previous animations" (https://apps.apple.com/gb/app/gardenscapes/id1105855019). Haptics not confirmed.

**12. Scale and reception.** App Store GB on 27 October 2026: **4.67 from 249,729 ratings** (https://itunes.apple.com/lookup?id=1105855019&country=gb). Google Play: **500m+ downloads**, 4.69 from 10,117,888 reviews (https://play.google.com/store/apps/details?id=com.playrix.gardenscapes). Launched 2016 — Android 5 July, iOS 25 August — by **Playrix**, free-to-play with in-app purchases and rewarded ads; fifth highest-grossing puzzle game by 2019 at $1.5bn, near $2bn lifetime by 2021, plus a further $1.5bn 2022–2024 (https://en.wikipedia.org/wiki/Gardenscapes:_New_Acres).

Complaints:
- The reward stops feeling like a reward: "the makeover tasks feel like I picked up a second job… a conveyor belt of tiny errands that never actually change anything… Slow progress is fine, but not when it feels like ticking boxes with zero payoff." (https://www.reddit.com/r/Gardenscapes/comments/1u8bssl/rant_makeover_tasks_have_turned_the_garden_into_a/)
- Interface and event overload: "I have to dismiss a stack of popups before I can actually start… By the time I reach the level I wanted, my mood has gone from cozy to an annoyed 'ugh, fine.'" (https://www.reddit.com/r/Gardenscapes/comments/1tusjja/anyone_else_exhausted_by_how_the_game_keeps/)
- Distrust of the difficulty curve — players believe levels are tuned to sell boosters: "Does the game hate me/us? it feels rigged" (29 upvotes, 24 comments) (https://www.reddit.com/r/Gardenscapes/comments/1ufkc54/does_the_game_hate_meus_it_feels_rigged/).
- Plus the regulatory one: the ASA ruled Playrix's ads "not representative of the games they were purported to feature" and banned them (https://techraptor.net/gaming/news/uk-asa-upholds-misleading-pin-pulling-puzzle-ad-claims-against-playrix).

Praise:
- The match-3 is a genuinely good micro-break: "The match-3 rounds are perfect for that: quick, a little crossword for my brain, satisfying and done." (https://www.reddit.com/r/Gardenscapes/comments/1u8bssl/rant_makeover_tasks_have_turned_the_garden_into_a/)
- The cosy, nature-y scene is the reason people open the app: "I like the nature-y vibe and the visuals; it is my wind-down after a long day." (https://www.reddit.com/r/Gardenscapes/comments/1tusjja/anyone_else_exhausted_by_how_the_game_keeps/)
- Finished renovations get shown off to other players as achievements in their own right: "Cozy Attic Renovation Completed." (https://www.reddit.com/r/Gardenscapes/comments/168y96w/cozy_attic_renovation_completed/)
- Longevity and the ad-for-coins option are praised on the store listing: "I have played thousands of levels and regularly used the option of watching an ad or two to get extra coins." (https://apps.apple.com/gb/app/gardenscapes/id1105855019)
- Reviewers rate the pacing itself: the game "provides the perfect cycle of challenge and progress, wrapped in a highly polished set of game modes that work together beautifully" (https://www.gamezebo.com/reviews/gardenscapes-new-acres-review/).

One further complaint from the same review, which matters for RepGarden's energy thinking: "there is a hard cap of five lives right now" with slow refresh, forcing waiting periods during hard stages (https://www.gamezebo.com/reviews/gardenscapes-new-acres-review/).

**13. Lesson for RepGarden.** This is the exact architecture RepGarden is proposing — an unrelated effort converted into garden progress — and its two most transferable decisions are both about the currency: **one unit of effort buys exactly one Star, and Stars cannot be bought, ever** (money reaches only the boosters, never the garden). Copy the free, reversible three-design choice too: it gives real identity with no authoring burden. What to avoid is the failure the players name themselves — a conveyor belt of tiny errands where an evening's effort buys "a bench". With only two to five workouts a week, RepGarden has perhaps 12 Stars a month, so each one must buy a visible, nameable change to the plot, not a sub-step of a sub-step; and the "Complete the Day" idea (bank your Stars, spend them in one satisfying go) is the right shape for a once-a-week sit-down. Avoid Playrix's event stack entirely: the cosy scene is what people come for, and every timed badge laid over it moves them "from cozy to an annoyed 'ugh, fine.'"

---

### Grow a Garden (Roblox)

**1. Unit of play.** The unit is a single square garden plot that the player fills with crops: you buy seeds from a stocked shop, plant them on brown plots, wait for them to grow, harvest the produce and sell it for Sheckles to buy rarer seeds — the game's own description reads "Buy seeds from the shop when they restock, plant them, and collect the profits!" (https://games.roblox.com/v1/games?universeIds=7436755782, official description for place 126884695634066). Crops split into single-harvest crops, which are pulled whole and must be replanted, and multi-harvest crops, which stay in the ground and regrow produce repeatedly (https://growagarden.fandom.com/wiki/Crops). A second unit of play sits alongside the garden: pets hatched from eggs placed in your garden, which have weight-scaled passive abilities, stack when duplicated, and occupy 3 equip slots by default (https://growagarden.fandom.com/wiki/Pets). One real-world action maps to one plot: a 5-second shop check plus a click to plant, and the clock does the rest.

**2. Session shape.** The metronome is the shop restock, not the session: the Seed Shop's main stock refreshes every 5 minutes and its Daily Deals every 24 hours, stock is shared globally across all servers, and rarer seeds appear with lower probability (https://growagarden.fandom.com/wiki/Seed_Shop). The Gear Shop likewise "changes every 5 minutes" (https://growagarden.fandom.com/wiki/Gear_Shop). So the ten-second action is real and is the whole game for most visits: open the shop, see if a rare seed rolled in, buy it, plant it, harvest what finished, sell at the Sell Stuff stand (https://growagarden.fandom.com/wiki/Sheckles). The long sit-down session is scheduled by the developers: "Admin Abuse" runs on Saturdays with the major update and on "Watering Wednesday", when the owner spawns special weathers, restocks shops and hands out exclusive seeds and pets, and the wiki tells players to "be online at least half an hour before the update on Saturdays" (https://growagarden.fandom.com/wiki/Admin_Abuse). Three daily quests refresh every 24 hours (https://growagarden.fandom.com/wiki/Daily_Quests). Kotaku described the whole thing as very basic, "more like a prototype of something that will be finished later" (https://kotaku.com/grow-a-garden-roblox-5-million-active-users-record-pc-1851781824).

**3. Absence.** The headline fact, stated by the developers themselves in the game description: "Remember, your garden literally grows while you are offline" (https://games.roblox.com/v1/games?universeIds=7436755782), repeated verbatim on the wiki's Tips page — "Your garden literally grows while you are offline!" — alongside "Pets grow offline when fed!" (https://growagarden.fandom.com/wiki/Tips). Press described the same mechanic: plants "continue to grow even when players are offline" (https://www.dexerto.com/roblox/surprise-roblox-game-reportedly-sets-biggest-player-count-record-in-history-3215598/, https://gamerant.com/grow-a-garden-roblox-fortnite-concurrent-player-count-record/).

Nothing withers. There is no decay, weed, hunger or death mechanic documented anywhere on the wiki: searches for wither, wilt, rot and decay return no absence-penalty mechanic, and the two states that sound like decay are both *rewards* — "Wilted" is an x10 Sheckle multiplier applied by the Weeping Branch crop, and "Rot" is an x8 multiplier applied by the Mandrake pet (https://growagarden.fandom.com/wiki/Crop_Mutations). "Wiltproof" is likewise a x4 value mutation from the Drought weather, not a protection against neglect (same URL). A guide site puts it plainly: "The only thing that happens to your garden when you're offline is the growth of crops" (https://www.droidgamers.com/guides/can-crops-get-mutations-when-youre-offline-in-grow-a-garden/).

What absence actually costs is everything that is *timed*, not everything that is *planted*:

- **A day away.** You miss roughly 288 Seed Shop restocks and 288 Gear Shop restocks, each of which was your only chance at that roll of rare seeds (https://growagarden.fandom.com/wiki/Seed_Shop, https://growagarden.fandom.com/wiki/Gear_Shop); one Daily Deals rotation; three daily quests (https://growagarden.fandom.com/wiki/Daily_Quests); and every weather event that fired. Weather matters because only the two growth-based variants, Gold and Rainbow, can appear offline — "Mutations found during Events and Weathers won't apply to crops if you're not online" (https://www.droidgamers.com/guides/can-crops-get-mutations-when-youre-offline-in-grow-a-garden/, and Gold/Rainbow as the only naturally grown variants at https://growagarden.fandom.com/wiki/Tips). Since weather mutations are where the money is (Shocked, Celestial and similar multipliers), a day offline is a day of plain, unmultiplied fruit. If the day was a Wednesday or Saturday you also missed an Admin Abuse giveaway (https://growagarden.fandom.com/wiki/Admin_Abuse).
- **A week away.** You miss the Saturday update, its Admin Abuse window, Watering Wednesday, and a slice of the running event. Events run on weekly Saturday patches in roughly three-week cycles with event-exclusive crops, mutations and pets that are unobtainable outside the window (https://progameguides.com/roblox/grow-a-garden-garden-games-event-guide/, https://www.thegamer.com/roblox-grow-a-garden-seed-stages-event-evo-seeds-jungle-egg-pets-guide/). Your crops are, however, all still there and fully grown.
- **A month away.** You permanently lose a full event cycle's exclusives, and you return to a changed meta: the wiki's update history shows pets and crops being nerfed and the economy restructured between updates (https://growagarden.fandom.com/wiki/Sheckles). Your garden itself is intact and has been producing the whole time; multi-harvest crops kept regrowing produce automatically (https://growagarden.fandom.com/wiki/Crops).

Streaks: no login-streak system, streak freeze or repair mechanic is documented on the wiki — daily quests simply reset every 24 hours with no counter (https://growagarden.fandom.com/wiki/Daily_Quests). Whether a streak exists at all is **not confirmed**. Whether another player can steal your unharvested fruit while you are offline is also **not confirmed**; the steal product only works on a garden you are standing in (https://growagarden.fandom.com/wiki/Take_Player%E2%80%99s_Fruit).

**4. Currency and endogenous value.** Sheckles ("¢") are the main currency, earned by selling plants or pets at the Sell Stuff stand, from pet abilities such as the Mole, from the Sheckle Rain weather, and as a 100-Sheckle consolation when a paid steal fails; they are spent on the Seed Shop, Gear Shop and Pet Eggs shop and on event shops (https://growagarden.fandom.com/wiki/Sheckles). This is fully endogenous: money exists only to buy more growth, and nothing in the core loop is cosmetic-only. Robux, Roblox's real-money currency, buys the same things faster — 79 Robux for an instant Seed Shop restock, charged per purchase and not permanent (https://growagarden.fandom.com/wiki/Seed_Shop), gear priced from 19 to 279 Robux (https://growagarden.fandom.com/wiki/Gear_Shop), pet and egg slots, cosmetic slots, seed rains and the Forever Pack in the Limited Time Shop (https://growagarden.fandom.com/wiki/Limited_Time_Shop), and 37 Robux to take a crop out of another player's garden (https://growagarden.fandom.com/wiki/Take_Player%E2%80%99s_Fruit). Notably, the Limited Time Shop hides certain offers from players in Australia, Belgium, the UK and the Netherlands "due to gambling laws" (https://growagarden.fandom.com/wiki/Limited_Time_Shop). A third currency, Garden Coins, comes from the prestige loop: a Garden Ascension costs 1T Sheckles, rises by 2T each time, can be done once every 4 hours, and grants 10 Garden Coins spent on permanent capacity upgrades and fences (https://growagarden.fandom.com/wiki/Garden_Ascension).

The hyperinflation is documented: a 10QA Sheckle cap was briefly added because of hoarding and removed on 29 August 2025; Sheckle trading was re-enabled on 3 September 2025 with a 10% tax per trade, which was itself removed seven days later; and the number formatting now runs through quadrillions, quintillions and sextillions, where before 13 September 2025 a quintillion was written as "1,000,000,000B" (https://growagarden.fandom.com/wiki/Sheckles). A community guide frames the suspension as players "swimming in Quintillions of Sheckles, crashing the economy" (https://www.gagdata.com/blog/trading-guide) — the framing is from an SEO guide site, so treat it as community opinion rather than developer statement.

**5. Stakes, risk and chance.** Chance is the engine. Seed Shop stock is a per-5-minute lottery with published per-item restock odds, and Mythical-or-higher plants can only ever have one seed in stock naturally (https://growagarden.fandom.com/wiki/Seed_Shop). Weather is a global random event — "every active server experiences the same weather at the same time" — and each weather rolls mutation chances on your crops: Frost gives "+50% Grow Speed! Higher CHILLED and FROZEN Fruit Chance!", Meteor Shower "Higher CELESTIAL Fruit Chance!", Cyclone a chance of Windstruck, and so on across dozens of standard, event, admin and unreleased weathers (https://growagarden.fandom.com/wiki/Weather). Mutations stack multiplicatively on the fruit's base value, from x2 Chilled up to x10 Wilted and beyond (https://growagarden.fandom.com/wiki/Crop_Mutations); community guides put Shocked at 100x and Celestial at 120x and note players deliberately bait a Thunderstorm-plus-Meteor-Shower overlap for a combined multiplier (https://www.droidgamers.com/guides/grow-a-garden-weather-events-guide/, https://beebom.com/grow-a-garden-weather-events/). Real risk of loss is paid-only and PvP: the 37-Robux steal "occasionally… will fail, and the game will take the players Robux then the player will receive 100 Sheckles back", with the failure chance apparently rising with the crop's value, and every success broadcasts "__ stole from __" to the whole server (https://growagarden.fandom.com/wiki/Take_Player%E2%80%99s_Fruit). Eggs and crates are the other gamble (https://growagarden.fandom.com/wiki/Pets, https://growagarden.fandom.com/wiki/Cosmetics).

**6. Progression.** There is no player XP level. Progression is seed tiers (Common up through Mythical, Divine and Prismatic, gated by restock rarity), plot and inventory capacity, and the pet roster, where a pet's stats depend on its weight and "as a pet grows older, its weight increases, making its abilities more efficient" — so pets are a slow, passive, time-based progression track in their own right (https://growagarden.fandom.com/wiki/Pets). Capacity is the real ladder: 60 pets by default, extendable to roughly 285–300 through gamepasses, Pet Pouch crafting and Ascension upgrades (same URL). The milestone marker is the Garden Ascension prestige reset: you spend 1T Sheckles, each ascension costing 2T more, for Garden Coins and permanent upgrades (https://growagarden.fandom.com/wiki/Garden_Ascension). Seasonally, progression is the event reward track — three-week event cycles with their own shops, crafting tables and exclusive crops (https://growagarden.fandom.com/wiki/Sheckles, https://progameguides.com/roblox/grow-a-garden-garden-games-event-guide/).

**7. Social.** Opt-in but heavily incentivised. Every friend in the same server gives a +10% Sheckle boost, capping at +40% (https://growagarden.fandom.com/wiki/Sheckles), and Roblox itself attributed the game's success partly to "vibrant social interactions — with friends driving play" (https://www.dexerto.com/roblox/surprise-roblox-game-reportedly-sets-biggest-player-count-record-in-history-3215598/). Trading, added in update 1.17.0, moves pets and harvested crops through a Trading Ticket bought from the Gear Shop, up to 13 items per cycle, with both sides' total Sheckle value shown in the UI, a 5-second countdown that resets if an item is removed, a double confirm step, and a hard block on accounts under 10 days old — all explicitly "in order to prevent scamming and being scammed" (https://growagarden.fandom.com/wiki/Trade_System). Those guardrails exist because the scam economy is real: community scam guides list overvalued trades, fake dupe claims, last-second item swaps and urgency pressure as the most common frauds (https://www.gagdata.com/blog/scam-prevention), and Wikipedia records an underground market selling rare items for real money via eBay and Discord in breach of Roblox's terms (https://en.wikipedia.org/wiki/Grow_a_Garden). There is a Sheckle leaderboard in the top-right of the screen (https://growagarden.fandom.com/wiki/Sheckles), and stealing is broadcast server-wide (https://growagarden.fandom.com/wiki/Take_Player%E2%80%99s_Fruit).

**8. Freedom and identity.** Layout and decoration. Cosmetics are placeable decoration objects for your garden, introduced in update 1.07.0, obtained from a Cosmetics Shop and from event crates, including trophies like the Monster Mash and Dino Trophy that function as proof of which events you were present for (https://growagarden.fandom.com/wiki/Cosmetics). Ascension sells fence styles — Laser Fence, Greek Fence — and extra placement, cosmetic and plant inventory slots (https://growagarden.fandom.com/wiki/Garden_Ascension). Save Slots let a player keep more than one plot layout (https://growagarden.fandom.com/wiki/Seed_Shop references the slot system; slot detail at https://growagarden.fandom.com/wiki/Garden_Ascension). Pet naming is **not confirmed**.

**9. Signature interaction.** Two moments, and they are a pair. First, planting a seed and deliberately logging out, knowing the plot works without you — the game says so on its own store page (https://games.roblox.com/v1/games?universeIds=7436755782). Second, the one that brings people back: standing in your garden during a live weather event, having pre-placed the right gear — "Place your Lightning Rod before Thunderstorm and your Star Caller before Meteor Shower" — and then harvesting a fruit that the sky has multiplied dozens or hundreds of times over its base value (https://www.droidgamers.com/guides/grow-a-garden-weather-events-guide/, https://growagarden.fandom.com/wiki/Weather, https://growagarden.fandom.com/wiki/Crop_Mutations). The absence mechanic grows the asset; the presence mechanic multiplies it.

**10. UI type and art.** ui_type: **isometric world** — the closest of the six to a third-person Roblox experience, because what you actually look at is one small square dirt plot seen at an angle from slightly above, with planting rows and shop stands around its edge, and the avatar is a cursor more than a character; it is not a map, not a single side-on scene, and not a creature in a room. The art is deliberately crude: Wikipedia describes "studded textures evocative of old-school Roblox games" (https://en.wikipedia.org/wiki/Grow_a_Garden), and Kotaku called the menus, visuals and gameplay "very basic" (https://kotaku.com/grow-a-garden-roblox-5-million-active-users-record-pc-1851781824) — oversized, saturated, cartoon vegetables on brown soil. The screen is dense: a Sheckle counter bottom-left, a leaderboard top-right, shop buttons down the left side (https://growagarden.fandom.com/wiki/Sheckles, https://growagarden.fandom.com/wiki/Limited_Time_Shop), plus restock timers and weather banners. The home screen *is* the garden — there is no menu front end, you spawn onto your plot.

**11. Sound and feel.** The soundtrack is incongruously classical, featuring Mozart's Rondo Alla Turca (https://en.wikipedia.org/wiki/Grow_a_Garden). The felt feedback is a visible, animated mutation skin on the fruit — each mutation has its own appearance, many of them animated GIFs in the wiki's tables (Blazing, Leeched, Glitched, Brainrot) (https://growagarden.fandom.com/wiki/Crop_Mutations) — plus server-wide text banners for weather onset and for steals (https://growagarden.fandom.com/wiki/Weather, https://growagarden.fandom.com/wiki/Take_Player%E2%80%99s_Fruit). Specific harvest sound effects and haptics: **not confirmed**.

**12. Scale and reception.** Launch year **2025**; the Roblox place was created 2025-03-25T22:32 UTC (https://games.roblox.com/v1/games?universeIds=7436755782) and Wikipedia gives the release date as 26 March 2025 (https://en.wikipedia.org/wiki/Grow_a_Garden). Developer: published by the Roblox group **"The Garden Game"** (group id 35789249) (https://games.roblox.com/v1/games?universeIds=7436755782). Ownership changed hands: it was built in about three days by an anonymous 16-year-old creator, **BMWLux** (also known as DevNamedDavid); in April 2025, when the game had roughly 1,000 concurrent users, **Splitting Point Studios** — led by Janzen "Jandel" Madsen — bought a share and put a development team on it, with BMWLux retaining 50%; Florida-based **Do Big Studios** later took a minority share (https://en.wikipedia.org/wiki/Grow_a_Garden, https://sherwood.news/markets/roblox-hits-a-52-week-high-as-a-wildly-simple-gardening-game-created-by-a-16/). Jandel is the one who runs the live game day to day, spawning weather and giveaways in Admin Abuse, with BMWLux hosting occasional "Stormy Sundays" (https://growagarden.fandom.com/wiki/Admin_Abuse). Business model: free to play on Roblox with Robux microtransactions for instant restocks, gear, slots, packs and steals, no premium purchase (https://growagarden.fandom.com/wiki/Seed_Shop, https://growagarden.fandom.com/wiki/Limited_Time_Shop).

Concurrent-player peak, two independent figures: Dexerto reported **16,411,769** concurrent users on 15 June 2025, beating Fortnite's 14,343,880 from November 2024 and dwarfing Steam's all-time single-game record, PUBG's 3,257,248 (https://www.dexerto.com/roblox/surprise-roblox-game-reportedly-sets-biggest-player-count-record-in-history-3215598/); Roblox community tracker RTC reported a peak of **16,039,994** and compared it to Fortnite's 15.3 million (https://x.com/Roblox_RTC/status/1933887539322245275). Game Rant independently reported 16 million-plus on 14 June 2025 after the 1.10.0 update (https://gamerant.com/grow-a-garden-roblox-fortnite-concurrent-player-count-record/). Wikipedia tracks the climb and the later peaks: ~5 million on 18 May 2025, 11.7 million on 31 May, 16 million-plus on 14 June, **21.3 million on 21 June 2025**, and **22.3 million on 23 August 2025** during a staged "admin war" with the creator of Steal a Brainrot — which then took the record back in September 2025 with 24 million-plus (https://en.wikipedia.org/wiki/Grow_a_Garden). Dexerto notes the figures are community-tracked rather than independently audited, and that bot-inflation accusations were made and disputed (https://www.dexerto.com/roblox/surprise-roblox-game-reportedly-sets-biggest-player-count-record-in-history-3215598/; TD Cowen's fraud allegation and its retraction at https://en.wikipedia.org/wiki/Grow_a_Garden).

Visit count on the day of this research (27 October 2026): **35,993,633,235 visits** — about 36 billion — with **11,458,482 favourites** (https://games.roblox.com/v1/games?universeIds=7436755782); Wikipedia recorded 35.3 billion visits as of May 2026, and notes it was the fastest Roblox game ever to 1 billion visits, in 33 days (https://en.wikipedia.org/wiki/Grow_a_Garden). Roblox like ratio on the day: **89.9%** — 9,440,910 likes against 1,055,643 dislikes (https://games.roblox.com/v1/games/votes?universeIds=7436755782, game page https://www.roblox.com/games/126884695634066/Grow-a-Garden). The same API reported only 13,717 players in-game at the moment of the check and a maxPlayers of 4 for the root place, which is wildly out of line with the press figures and probably reflects root-place configuration rather than live traffic across shards — treat the live concurrency figure as **not confirmed**. It has no App Store or Play listing of its own; it is played inside the Roblox host app (iOS id 431946152), so a GB rating for this game does not exist. Around 35% of the player base is under 13 (https://en.wikipedia.org/wiki/Grow_a_Garden).

Complaints:
- "Most people picture Jandel as some game developer who cares about his fanbase, but they don't realize he cares mostly about the money… He even did a poll to nerf honeysuckle… and people said to not nerf it. And he still nerfed it… They don't even think stuff through." Same post: he spent his last Sheckles on a Tranquil Radar expecting it to collect all the tranquil fruit and "got bothing because it only scans like a 50 stud radius around the player" — i.e. a paid-for item that did not do what the player thought (https://www.reddit.com/r/growagarden/comments/1m4uoz2/im_probably_gonna_quit_grow_a_garden_and_heres_why/).
- Event fatigue, verbatim, from 27 October 2026: "I'm bored!!!. I'm not even putting stuff in the cauldron.. It takes forever to get to 100 percent and nobody puts stuff in there… And don't get me on that stupid trick or treat house lol. I'm over it devs lol" — titled "I miss enjoying Grow a Garden.. Are we getting a third week of this event? .. I hope not.." (https://www.reddit.com/r/growagarden/comments/1xgfm0d/i_miss_enjoying_grow_a_garden_are_we_getting_a/).
- Burnout from the weekly cadence, quoted from a Reddit user by a news report: "I TRULY hope this change happens. The weekly updates are making me feel burned out… events need to happen less frequently or last longer." The developer conceded the point: "Weekly events were just a bit too hard to keep fresh and new… We were neglecting other content we could add to the game, like bug fixes and features" (Jandel, on Discord) (https://www.shanethegamer.com/esports-news/no-more-weekly-updates-grow-a-garden-dev-teases-a-new-era/).
- (Fourth, for completeness.) Press criticism of the shallowness: the menus, visuals and gameplay are "very basic and look more like a prototype of something that will be finished later" (https://kotaku.com/grow-a-garden-roblox-5-million-active-users-record-pc-1851781824), and Wikipedia records the acquiring studios being criticised for "introducing excessive monetization" (https://en.wikipedia.org/wiki/Grow_a_Garden).

Praise:
- "Relaxing gameplay" and "one of Roblox's most laid-back experiences" that "appeals to a broad audience, including both adults and younger players", with the offline growth singled out as the reason players return to "fully grown plants or trees" (https://gamerant.com/grow-a-garden-roblox-fortnite-concurrent-player-count-record/).
- Roblox's own spokesperson attributed the success to "exceptional user retention, vibrant social interactions — with friends driving play — and strong Robux engagement" (https://www.dexerto.com/roblox/surprise-roblox-game-reportedly-sets-biggest-player-count-record-in-history-3215598/).
- The players vote with the like button: 9,440,910 likes to 1,055,643 dislikes, an 89.9% positive ratio, plus 11.46 million favourites (https://games.roblox.com/v1/games/votes?universeIds=7436755782, https://www.roblox.com/games/126884695634066/Grow-a-Garden).
- (Fourth.) Game File's Nicole Carpenter called it "the new generation's FarmVille", and PCGamesN listed it among the best Roblox games of 2025 (https://en.wikipedia.org/wiki/Grow_a_Garden).

**13. Lesson for RepGarden.** Copy the asymmetry, not the content: the garden grows while you are away and nothing ever withers, so returning is always a reward and never a repair job — which is exactly what a client on trainer-prescribed rest days needs, and it is the single mechanic this 36-billion-visit game puts in its own one-line store description (https://games.roblox.com/v1/games?universeIds=7436755782, https://growagarden.fandom.com/wiki/Tips). Put the multiplier on presence instead of the penalty on absence: Grow a Garden's growth-based variants happen offline but its big weather multipliers only land if you are there, so a logged workout should always bank value while a session logged during the week's trainer-set challenge gets the multiplier. Avoid the two things that are visibly burning its players out — a 5-minute restock timer that punishes you for living your life, and a relentless weekly event treadmill that the developer himself admitted was "too hard to keep fresh" while players said the updates were "making me feel burned out" (https://growagarden.fandom.com/wiki/Seed_Shop, https://www.shanethegamer.com/esports-news/no-more-weekly-updates-grow-a-garden-dev-teases-a-new-era/) — and avoid the paid-restock and paid-steal economics entirely, since a free app has no way to make a timed lottery fair.

---

### Animal Crossing: Pocket Camp Complete

**1. Unit of play.** A campsite you decorate, plus a camper/RV and a cabin, with "a total of eight villagers could stay at the Campsite at any one time" (https://nookipedia.com/wiki/Animal_Crossing:_Pocket_Camp). One real-world action maps to one gather-and-trade: you shake trees, fish, net bugs and pick up shells in themed areas, then trade the requested item to a villager for crafting materials — "These materials could be gained by exchanging requested items such as fruit or bugs with villagers" — and Cyrus crafts them into furniture (https://nookipedia.com/wiki/Animal_Crossing:_Pocket_Camp). A separate garden adds 20 planting spots from Camp Manager Level 3 (https://animalcrossingpocketcamp.wiki.gg/wiki/Garden).

**2. Session shape.** Short and repeated: "it seems designed as the kind of game you can play for a few minutes at a time, a couple times a day" (https://www.macworld.com/article/230748/animal-crossing-pocket-camp-review.html). The world is "split into a series of islands that you travel between via a map selection screen," so the glance screen is effectively the map plus one area (https://www.gamezebo.com/reviews/animal-crossing-pocket-camp-review-home-again/). In ten seconds you can "shake trees to gather fruit, toss a line into the river or ocean to snag fish, and get out your net and catch insects" (same URL). The sit-down layer is crafting and decorating: craft times run from "Less than 10 minutes" to "Less than 72 hours" (https://animalcrossingpocketcamp.wiki.gg/wiki/Crafting), and large amenities "take multiple real-life days of construction to be completed" (https://www.gamezebo.com/reviews/animal-crossing-pocket-camp-review-home-again/).

**3. Absence.** **Nothing decays, withers or dies, and there is no streak.** Absence only costs you uncollected resources on timers. Fruit "would always respawn after three hours, unless you use fertiizer to skip through that process"; shells "respawn at far more random times; sometimes the shell timer will refresh in less than an hour, sometimes it will take longer than the aforementioned three hours" (https://www.levelwinner.com/animal-crossing-pocket-camp-hints-tips-strategies-complete-look-resources-inventory-management/). Villager requests "refresh every 3 hours (Starting at 6:00 AM UTC) with a max of 3 per hour, unless a Request Ticket is used" (https://animalcrossingpocketcamp.wiki.gg/wiki/Villager). The garden is the one place with anything decay-shaped, and it is explicitly recoverable: soil dries after about an hour, and "If the dirt remains dry for 2 hours (3 hours total of no water) the flower will wilt, pausing the growth timer. A wilted flower must be watered to continue growing" — a wilted flower is *paused*, not dead — while "A fully bloomed flower left in the garden will maintain wet dirt and will not need to be watered," so a finished flower can be left indefinitely (https://animalcrossingpocketcamp.wiki.gg/wiki/Garden). A reviewer names absence as the reason she avoided the live-service original: "I struggle to keep up with mobile games, especially when forgoing a month or two means falling behind or missing out on content" (https://screenrant.com/animal-crossing-pocket-camp-still-worth-it/). Whether crafting timers advance while the app is closed is **not confirmed** by any source I read. No streak, freeze or repair mechanic found — **not confirmed** that any exists.

*What happened to the live-service retention machinery.* Leaf Ticket sales stopped on "November 27, 2024 at 6:00 AM UTC"; service ended "November 28, 2024 at 3:00 PM UTC"; Complete arrived 2 December 2024; and the save-transfer servers closed "June 2, 2025 at 6:00 AM UTC" (https://animalcrossingpocketcamp.wiki.gg/wiki/End_of_Service). The paid currency went: Leaf Tickets "will **not** transfer," replaced by "Leaf Tokens, which may be obtained from events, achievements, and through bell exchange" (same URL), and the prices were cut hard — "Leaf Tickets have been renamed to Leaf Tokens, and amounts have been adjusted **drastically** across the board", with "a single fortune cookie now costs only 5 Leaf Tokens" versus 50 Leaf Tickets (https://animalcrossingworld.com/2024/12/whats-new-changed-in-animal-crossing-pocket-camp-complete-out-now/). The gacha itself survived but was defanged: Complete Tickets let you "trade for any item in the Complete Item Catalog" (same URL). The retention surfaces that were removed are all the social ones: "features requiring an internet connection such as Market Boxes, gifts, and visiting other players' campsites will not be available" (https://animalcrossingpocketcamp.wiki.gg/wiki/End_of_Service), plus Pocket Camp Club subscription benefits — stamps, craft-time shortcuts, members-only discounts (https://nookipedia.com/wiki/Animal_Crossing:_Pocket_Camp_Complete). FOMO was replaced by a loop: "7 years of events (with exceptions) repeating on a 4 year cycle" (https://animalcrossingpocketcamp.wiki.gg/wiki/End_of_Service), with new content stopping after September 2025 (https://gonintendo.com/contents/43424-animal-crossing-pocket-camp-complete-to-receive-new-items-until-sept-2025). **The real-time clock stayed.** The store listing still promises "tons of seasonal events," "Garden Events and Fishing Tourneys every month," Halloween, Toy Day, Bunny Day and Summer Festival, and notes that although a "constant online connection is not required," temporary data communication occurs for account syncing, **time updates** and downloads (https://apps.apple.com/gb/app/animal-crossing-pocket-camp-c/id6547834967).

*Sub-note — Animal Crossing: New Horizons (Switch), the clearest commercial case of "absence makes a mess, not a loss".* "One new weed will appear each day," and weeds then spread probabilistically by growth stage — "stage 3 weeds spread at 81% unwatered or 100% when watered" — but the mess is capped: "If there is 31 or more weeds present, only one weed will appear once per day, and if there are 150 or more weeds present in the town, no further weeds will spawn and all existing weeds will stop growing" (https://nookipedia.com/wiki/Weed). Crucially the mess is a *resource*: pulled weeds become "clump of weeds" items that can be "sold, used as crafting materials for DIY projects such as medicine, or planted in the ground again" (same URL). Indoors, cockroaches appear "if the player does not enter it for approximately a week or longer," more the longer you are away; "They cannot be caught and must be killed by stepping over them," after which "a small ghost floats into the air and disappears" and "the player does a victory cheer" — tidying is given a win animation (https://nookipedia.com/wiki/Cockroach). Villagers are the one thing Nintendo made safe: "While in previous games villagers could leave without telling you first, in *Animal Crossing: New Horizons* you will always be told when a villager is thinking about leaving" (https://www.gamerevolution.com/guides/646011-can-villagers-leave-without-asking-in-animal-crossing-new-horizons). And Nintendo **did** soften the rest, in the 2.0 free update (November 2021), via a 20,000-Bell Beautiful Island ordinance: "Weed spread rates are reduced by half", "Flowers have a 69% chance of reproducing without requiring water", and "Cockroaches will be removed and will no longer be able to respawn" (https://nookipedia.com/wiki/Ordinance). The lived experience is curiosity, not grief: "Anyone else come back to your Animal Crossing island after four years and find it full of weeds and cockroaches?… while all my villagers are there, there's so many weeds! And cockroaches in my house?" (86 upvotes, 37 comments, https://www.reddit.com/r/CozyGamers/comments/1ouqxco/anyone_else_come_back_to_your_animal_crossing/). New Horizons has sold 50.29 million copies as of 30 June 2026 (https://en.wikipedia.org/wiki/Animal_Crossing:_New_Horizons).

**4. Currency and endogenous value.** Bells from gameplay, plus Leaf Tokens "obtained from events, achievements, and through bell exchange" (https://animalcrossingpocketcamp.wiki.gg/wiki/End_of_Service) and Complete Tickets for catalogue items (https://animalcrossingworld.com/2024/12/whats-new-changed-in-animal-crossing-pocket-camp-complete-out-now/). Spending feeds straight back into the thing you care about — furniture, amenities, the campsite — and into pace, because "The time needed to craft items can be permanently reduced with…Leaf Tokens" (https://gamerant.com/is-animal-crossing-pocket-camp-complete-worth-it-good/). There is now **no** real-money layer inside the game: the listing shows a £17.99 price and no in-app purchases (https://apps.apple.com/gb/app/animal-crossing-pocket-camp-c/id6547834967). The original's layer was lucrative — more than "US$250 million in lifetime player spending" by November 2021 (https://en.wikipedia.org/wiki/Animal_Crossing:_Pocket_Camp) — yet even then reviewers called it "ridiculously generous and non-predatory" (https://www.gamezebo.com/reviews/animal-crossing-pocket-camp-review-home-again/).

**5. Stakes, risk and chance.** No betting and no way to lose anything. The chance layer is the fortune cookie, a gacha with randomised rewards "including rare 5-star items" (https://en.wikipedia.org/wiki/Animal_Crossing:_Pocket_Camp), now 5 Leaf Tokens a pull and backed by a deterministic alternative in Complete Tickets (https://animalcrossingworld.com/2024/12/whats-new-changed-in-animal-crossing-pocket-camp-complete-out-now/). Other randomness: shell respawn timing (https://www.levelwinner.com/animal-crossing-pocket-camp-hints-tips-strategies-complete-look-resources-inventory-management/) and flower cross-pollination, where "The seed color result of cross-pollination depends on the flower colors selected" (https://animalcrossingpocketcamp.wiki.gg/wiki/Garden). Opt-in challenges are the monthly Garden Events and Fishing Tourneys (https://apps.apple.com/gb/app/animal-crossing-pocket-camp-c/id6547834967).

**6. Progression.** Camp Manager level gates features (the garden needs Level 3 — https://animalcrossingpocketcamp.wiki.gg/wiki/Garden); per-villager friendship levels unlock cosmetic control, since "Since 1.2.0, player could change a villager's outfit. This becomes available once the player has reached a certain level of friendship" (https://nookipedia.com/wiki/Animal_Crossing:_Pocket_Camp); amenities are the multi-day milestone build (https://www.gamezebo.com/reviews/animal-crossing-pocket-camp-review-home-again/); and the long arc is the Complete Item Catalog across a four-year event cycle (https://animalcrossingpocketcamp.wiki.gg/wiki/End_of_Service). Player level cap: **not confirmed**.

**7. Social.** Essentially removed. "the traditional friend list is no more"; instead you scan Camper Pass QR codes and those players' characters appear at Whistle Pass, "a completely new location on the map found only in Animal Crossing: Pocket Camp Complete," where K.K. Slider also shows up (https://animalcrossingworld.com/2024/12/whats-new-changed-in-animal-crossing-pocket-camp-complete-out-now/). No visiting, Market Boxes, gifts or help (https://animalcrossingpocketcamp.wiki.gg/wiki/End_of_Service). No leaderboards found. This is the headline regret: "people can no longer visit each other's camps" and that could be "a deal-breaker" (https://gamerant.com/is-animal-crossing-pocket-camp-complete-worth-it-good/).

**8. Freedom and identity.** The campsite, camper/RV and cabin are all decorable (https://nookipedia.com/wiki/Animal_Crossing:_Pocket_Camp); you choose which eight villagers stay; you dress your avatar and, at high enough friendship, the villagers (same URL); you plan a 20-plot garden and breed flower colours (https://animalcrossingpocketcamp.wiki.gg/wiki/Garden); and your Camper Pass is your shareable identity card (https://animalcrossingworld.com/2024/12/whats-new-changed-in-animal-crossing-pocket-camp-complete-out-now/).

**9. Signature interaction.** Handing a villager the exact thing they just asked for and getting materials and friendship back — the three-hourly request loop (https://animalcrossingpocketcamp.wiki.gg/wiki/Villager) fed by shaking a fruit tree (https://www.gamezebo.com/reviews/animal-crossing-pocket-camp-review-home-again/).

**10. UI type and art.** **isometric world.** The Game UI Database records "3D Stylized" graphics with "Isometric/Grid" and "Top-Down" perspectives (https://www.gameuidatabase.com/gameData.php?id=443), and areas are reached from a map screen rather than on foot (https://www.gamezebo.com/reviews/animal-crossing-pocket-camp-review-home-again/). Art is bright, crisp, chibi Animal Crossing — moderately dense, with a persistent icon bar over a 3D scene. The home screen is your campsite with its villagers milling about.

**11. Sound and feel.** **Not confirmed.** The reviews I fetched do not discuss audio or haptics (https://www.macworld.com/article/230748/animal-crossing-pocket-camp-review.html, https://www.gamezebo.com/reviews/animal-crossing-pocket-camp-review-home-again/).

**12. Scale and reception.** iOS GB rating 4.73986 from 1,134 ratings (27 October 2026, https://apps.apple.com/gb/app/animal-crossing-pocket-camp-c/id6547834967). Google Play GB on 27 October 2026: **500k+ Downloads**, 4.1 stars, 11.1k reviews, PEGI 3 (https://play.google.com/store/apps/details?id=com.nintendo.zasa). Launch year: the original released 2017, Complete released 2 December 2024 (https://animalcrossingpocketcamp.wiki.gg/wiki/End_of_Service). Developer Nintendo Co., Ltd. Business model: one-off purchase, £17.99 / $19.99, no in-app purchases, launched at a half-price $9.99 until 31 January 2025 (https://nookipedia.com/wiki/Animal_Crossing:_Pocket_Camp_Complete, https://screenrant.com/animal-crossing-pocket-camp-complete-price-increase-reactions/).

Complaints:
- "I would recommend looking at some gameplay first before buying. i regretted buying it, even at a reduced price." — user tweeetiee (https://screenrant.com/animal-crossing-pocket-camp-complete-price-increase-reactions/)
- The social layer is gone: "people can no longer visit each other's camps," which could be "a deal-breaker for those already on the fence" (https://gamerant.com/is-animal-crossing-pocket-camp-complete-worth-it-good/)
- Content support was time-boxed from the start: new events only "until Sept. 2025" (https://gonintendo.com/contents/43424-animal-crossing-pocket-camp-complete-to-receive-new-items-until-sept-2025)

Praise:
- "PC: Complete is COMPLETELY better than the original." — 1,283 upvotes, 121 comments (https://www.reddit.com/r/ACPocketCamp/comments/1h5svs6/pc_complete_is_completely_better_than_the_original/)
- "Anyone else shocked at how cheap Complete is??" — 423 upvotes, 158 comments (https://www.reddit.com/r/ACPocketCamp/comments/1ge23j9/anyone_else_shocked_at_how_cheap_complete_is/)
- "Making a one-time purchase, offline-only version is actually brilliant. Wished they did that with other apps" (https://www.nintendolife.com/news/2024/08/animal-crossing-pocket-camp-to-end-online-service-in-november); and from a reviewer, "I wouldn't have gotten to experience the joys of Animal Crossing: Pocket Camp if it had never switched to a paid app" (https://screenrant.com/animal-crossing-pocket-camp-still-worth-it/)

**13. Lesson for RepGarden.** Copy the wilt, not the death: a neglected plot should *pause* and recover on one watering, exactly as Pocket Camp's wilted flower "pausing the growth timer" does, and a finished vegetable should sit safe in the plot forever — so a client back from a two-week holiday finds work waiting, not work destroyed. Copy the three-hour refresh too: trainer-derived tasks that reset on a clock mean a missed day costs one batch of small gains and never the garden, which is why nobody in Pocket Camp needs a streak freeze. Avoid New Horizons' uncapped-feeling mess and avoid live-service FOMO: if RepGarden ever shows an "untidy" state it must be capped, convertible into something useful (New Horizons' weeds become craft materials) and clearable in one gesture with a little victory flourish — and limited-time challenges should recur on a cycle rather than expire forever, which is precisely the fix Nintendo applied when it stopped running Pocket Camp as a live service.

---

### Neko Atsume: Kitty Collector

**1. Unit of play.** Not a creature you own — a *collection of visitors*. The store listing states the whole loop: "Playing Neko Atsume: Kitty Collector is as easy as one, two...and that's it! Step 1: Place playthings and snacks in your yard. Step 2: Wait for cats to visit!" (https://apps.apple.com/gb/app/neko-atsume-kitty-collector/id923917775). What accumulates is the Catbook — Wikipedia counts "86 collectible cats, including 26 rare variants with unique interactions" (https://en.wikipedia.org/wiki/Neko_Atsume), while a guide counts 66 across 17 Catbook pages (https://www.levelwinner.com/neko-atsume-kitty-collector-ultimate-guide-get-rare-cats/) and the older store text says "over 40 cat varieties" — the figure has grown with versions, so treat the exact number as version-dependent. One real-world action maps to: put out food and a toy, close the app, come back and photograph whoever turned up.

**2. Session shape.** Seconds, many times a day. "At least 20 times a day, I check in on my virtual cats. I consistently have the impulse to do so, in fact," and "A few quick bursts of attention throughout the day is sufficient enough to keep things going" (https://kotaku.com/the-japanese-cat-game-we-can-t-stop-playing-1701250319). Another reviewer: it is "such a perfect fit for mobile gaming, due to the nature of checking back every now and then for cats" (http://naysgamereviews.blogspot.com/2016/01/mobile-game-review-neko-atsume.html). Ten-second loop: open the yard, see who is there, tap the camera, collect the fish, refill the bowl. The sit-down screen is the shop and the Catbook, reached from "the paw icon in the top corner of your screen" (http://nekoatsumeguide.weebly.com/the-basics.html).

**3. Absence.** The purest case in the set: **nothing decays, nothing dies, there is no streak and there is no fail state.** Polygon's verdict is the clearest statement of the design: "There's no conflict... There are no real achievements, nor any sense of danger. There's neither a failstate nor an ending... You can't let down your cats in Neko Atsume; you can only make them happier" (Allegra Frank, Polygon, quoted at https://www.cbsnews.com/news/fans-are-obsessed-with-neko-atsume-virtual-cat-collecting-game/). Kotaku frames it against the obvious comparison: "It feels a bit like Tamagotchi, without so many responsibilities and inevitable deaths from neglecting those responsibilities" (https://kotaku.com/the-japanese-cat-game-we-can-t-stop-playing-1701250319). The only mechanic that runs down is the food bowl, and it runs down on a published clock — Thrifty Bitz free and lasting 8 hours, Frisky Bitz 30 fish/6 hours, Ritzy Bitz 3 gold fish/3 hours, Bonito Bitz 7 gold/3 hours, Deluxe Tuna Bitz 12 gold/3 hours, Sashimi 5 gold/3 hours (https://www.levelwinner.com/neko-atsume-kitty-collector-ultimate-guide-get-rare-cats/). When it empties, cats simply stop arriving; the cost of absence is forgone fish, never lost fish. Absence is even *recorded kindly*: cats who visited while you were away but were not photographed appear in the Catbook as "a lighter silhouette with their name and date of visit" (same URL) — a near-miss you can still complete later. No streak, no freeze, no repair; none needed.

**4. Currency and endogenous value.** Two currencies, both earned by being absent and coming back. "Cats will come and go, leaving you with gifts of gold and silver fish for you to purchase more toys with," and if you evict a cat by placing an item on it, it "will give you less fish than if you just leave them alone" (http://nekoatsumeguide.weebly.com/the-basics.html) — the game literally pays you for leaving cats alone. Amounts scale with how well your food and goodies match the cat's taste (https://www.levelwinner.com/neko-atsume-kitty-collector-ultimate-guide-get-rare-cats/). "500 silver fish can be traded for 10 gold" (https://www.imore.com/neko-atsume-game-guide-how-collect-all-cats). Fish buy food, goodies, wallpapers, remodels and the yard expansion, which at 180 gold fish unlocks the indoor space and "gives you twice as many spaces for toys as well as cat snacks" (https://www.levelwinner.com/neko-atsume-kitty-collector-ultimate-guide-get-rare-cats/). Spending feeds back hard: "High-quality food stands a much better chance of attracting rare cats than Thrifty Bitz or Frisky Bitz" (https://www.gamezebo.com/walkthroughs/neko-atsume-kitty-collector-tips-cheats-and-strategies/), and rarer cats leave more and better fish — the endogenous loop. Remodels are the one cosmetic-only sink: "Remodeling will not have any added impact or benefit to your cat-collecting or fish-earning activities" (https://www.levelwinner.com/neko-atsume-kitty-collector-ultimate-guide-get-rare-cats/). The real-money layer is gold fish: 70 for £0.99, 170 for £1.99, 270 for £2.99, 400 for £3.99, plus video ads (https://apps.apple.com/gb/app/neko-atsume-kitty-collector/id923917775). It is widely seen as self-defeating: buying gold fish lets you "skip the act of waiting, and the act of waiting is _what makes the game_", and "Neko Atsume is boring when there's nothing to save up fish for" (https://notes.highlysuspect.agency/blog/nekos/).

**5. Stakes, risk and chance.** No bet, no loss, no opt-in challenge. Chance *is* the game: which cats arrive is probabilistic, weighted by food tier and by goodie, and "Rare Cats have a much greater chance of spawning if more expensive Food and Goodies are used" (https://www.levelwinner.com/neko-atsume-kitty-collector-ultimate-guide-get-rare-cats/, https://www.gamezebo.com/walkthroughs/neko-atsume-kitty-collector-tips-cheats-and-strategies/). The nearest thing to a risk decision is Tubbs, the fat cat who eats the whole bowl: rather than shooing him you should "let him leave under his own power" to receive substantial fish as compensation (https://www.gamezebo.com/walkthroughs/neko-atsume-kitty-collector-tips-cheats-and-strategies/) — patience pays, impatience costs. You cannot summon a cat; the single exception is Hermeowne's memento, "the only cat with a memento that can be activated. Using it while your yard is empty will attract a random cat and can be used 4 times, taking 10 days to fully replenish" (https://www.levelwinner.com/neko-atsume-kitty-collector-ultimate-guide-get-rare-cats/).

**6. Progression.** Photograph a cat to collect it: "To collect a cat, you must take its picture and store it in your Cat Book" (https://nekoatsume.fandom.com/wiki/Cats, via https://www.levelwinner.com/neko-atsume-kitty-collector-ultimate-guide-get-rare-cats/). Milestones are Catbook entries, per-cat albums (18 photos over 3 pages, extra pages at 10 gold fish), mementos, the 180-gold yard expansion and the remodel styles (same URL). Mementos are the deliberately slow goal: rare cats leave them only when they meet their preferred goodie (https://www.gamezebo.com/walkthroughs/neko-atsume-kitty-collector-tips-cheats-and-strategies/), and collecting them takes "dozens of visits" over "many weeks" (https://notes.highlysuspect.agency/blog/nekos/).

**7. Social.** None in the app — no friends, visiting, leaderboards or co-op found; **not confirmed** that any exists. The sharing happens outside it, by screenshot: the Kotaku writer photographs cats "when I meet a new cat or buy something new I've had my eye on" and posts them to Twitter alongside colleagues (https://kotaku.com/the-japanese-cat-game-we-can-t-stop-playing-1701250319).

**8. Freedom and identity.** You choose the food, the goodies and their placement in the yellow placement circles, where "bigger toys hold more cats" (http://nekoatsumeguide.weebly.com/the-basics.html); you buy wallpapers; and you pick one of seven remodel styles — "Original, Zen, Rustic, Modern, Western, Sugary, or Cafe" at 280 gold fish each, freely switchable once owned, each with "slightly different placements for Goodies" (https://www.levelwinner.com/neko-atsume-kitty-collector-ultimate-guide-get-rare-cats/, https://lovenekoatsume.wordpress.com/2015/08/18/remodeling/). Identity shows up as ritual rather than avatar — one player: "I always place warm things outside when the weather is cold in real life or in the game, and cooling mats when it's warm outside in real life" (117 upvotes, https://www.reddit.com/r/nekoatsume/comments/ki2j8x/i_always_place_warm_things_outside_when_the/).

**9. Signature interaction.** Opening the app to find cats you did not choose already in your yard, and tapping the camera to keep one — "Take a picture of them as you see them, so they are easier to identify in the future" (https://www.imore.com/neko-atsume-game-guide-how-collect-all-cats). The counter-gesture matters as much: *not* touching them, because moving a cat costs you fish (http://nekoatsumeguide.weebly.com/the-basics.html).

**10. UI type and art.** **side-on single scene.** One illustrated yard, five item spots at first and ten after the expansion, plus a separate indoor area that allows "2 food varieties and up to 2 large toys" (https://www.levelwinner.com/neko-atsume-kitty-collector-ultimate-guide-get-rare-cats/). Art is flat, "drawn in a cute cartoon style" with cats differentiated mainly by markings rather than body shape (http://naysgamereviews.blogspot.com/2016/01/mobile-game-review-neko-atsume.html); a reviewer praises "elegant simplicity of UI" and says "Every element oozes charm and cuteness" (https://www.sigtrent.com/neko-atsume-game-review/). Sparse, not dense: the home screen is the yard itself with whoever is visiting, and a single paw menu in the top corner (http://nekoatsumeguide.weebly.com/the-basics.html).

**11. Sound and feel.** "The music of the game is very much reminiscent of games like Animal Crossing, and gives the same relaxed and playful feel" (http://naysgamereviews.blogspot.com/2016/01/mobile-game-review-neko-atsume.html); music credited to Ryo Shintani (https://en.wikipedia.org/wiki/Neko_Atsume). Sound design is "simple and functional" (https://www.sigtrent.com/neko-atsume-game-review/). Haptics: **not confirmed**. Note the near-absence of completion feedback is itself the feel — the reward is the photograph.

**12. Scale and reception.** iOS GB rating 4.74199 from 2,965 ratings (27 October 2026, https://apps.apple.com/gb/app/neko-atsume-kitty-collector/id923917775). Google Play GB on 27 October 2026: **10m+ Downloads**, 4.8 stars, 351k reviews, PEGI 3 (https://play.google.com/store/apps/details?id=jp.co.hit_point.nekoatsume). Launch: Japan 20 October 2014, English 30 October 2015 (https://en.wikipedia.org/wiki/Neko_Atsume); App Store release date 21 October 2014. Developer Hit-Point Co., Ltd. Business model: free-to-play with optional gold-fish IAP (£0.99–£3.99) and video ads (https://apps.apple.com/gb/app/neko-atsume-kitty-collector/id923917775). The 2015 Western breakout is documented: 4 million downloads by May 2015 and more than 10 million by December 2015 (https://en.wikipedia.org/wiki/Neko_Atsume), 10 million as of January 2016 (https://www.cbsnews.com/news/fans-are-obsessed-with-neko-atsume-virtual-cat-collecting-game/), a CEDEC Award for best game design in August 2015, a GameSpot top-five mobile game of 2015, and a live-action film in April 2017 (https://en.wikipedia.org/wiki/Neko_Atsume). The developer's stated philosophy: "We're not going to put cheats or complexity in it, and we would like to pursue a game that can be enjoyed with only simple operations" — Yutaka Takazaki (same URL).

Complaints:
- Tubbs the food thief is the single most-resented mechanic: "Petition for there to be an item that is a Tubbs deterrent so he stops eating all the food and forcing other cats away. It could be more expensive but worth it in the long run. I'm seriously getting tired of this!" (https://www.reddit.com/r/nekoatsume/comments/ic7por/petition_for_there_to_be_an_item_that_is_a_tubbs/); also "New player here, how can l stop Tubbs from eating all my stuff?" (https://www.reddit.com/r/nekoatsume/comments/yyj7te/new_player_here_how_can_l_stop_tubbs_from_eating/)
- The no-stakes design loses some players outright: "Am I the only one who isn't really having fun?" — 175 upvotes, 60 comments (https://www.reddit.com/r/nekoatsume/comments/1gb3fjt/am_i_the_only_one_who_isnt_really_having_fun/)
- Press agrees it barely qualifies as a game: it "skirts the line of what I'd deem to be a game" with "no kind of appreciable strategy or challenge" (https://www.sigtrent.com/neko-atsume-game-review/), and "if you're after thrills or challenging gameplay then this isn't for you" (http://naysgamereviews.blogspot.com/2016/01/mobile-game-review-neko-atsume.html)
- (Fourth, structural) Paying breaks the game: gold-fish purchases "skip the act of waiting, and the act of waiting is _what makes the game_" (https://notes.highlysuspect.agency/blog/nekos/)

Praise:
- "There's no conflict... There are no real achievements, nor any sense of danger. There's neither a failstate nor an ending... You can't let down your cats in Neko Atsume; you can only make them happier." — Allegra Frank, Polygon (https://www.cbsnews.com/news/fans-are-obsessed-with-neko-atsume-virtual-cat-collecting-game/)
- "It speaks to my soul, and I can't stop playing it" — and "A few quick bursts of attention throughout the day is sufficient" (https://kotaku.com/the-japanese-cat-game-we-can-t-stop-playing-1701250319)
- "best thing to wake up to🥰" — 200 upvotes (https://www.reddit.com/r/nekoatsume/comments/fau4ax/best_thing_to_wake_up_to/); and craftsmanship and cuteness both rated 5/5, "a real pleasure to play" (https://www.sigtrent.com/neko-atsume-game-review/)

**13. Lesson for RepGarden.** Neko Atsume proves retention without stakes: it pays you for *coming back*, not for not-missing — the reward is "who showed up while you were out", which is exactly the shape of a trainer's comment on a filmed set or an unexpected vegetable in the plot, and it is the one mechanic that works identically on a two-session week and a five-session week. Steal the near-miss record too: a greyed-out silhouette with a date ("a vegetable ripened on Tuesday while you were away") invites a return without accusing anyone. Avoid two things: do not make the collection the *only* goal in an app whose real goal is training, because "no appreciable strategy or challenge" loses a measurable slice of players; and never ship a Tubbs — a mechanic that silently eats the thing a client worked for, with no counter and no explanation, is the one design in this app people genuinely resent.

---

### My Tamagotchi Forever
**1. Unit of play.** A single creature you keep alive in a room, which "evolve[s] from one type to another depending on how you care for them. You never know who they might become next!" (https://en.bandainamcoent.eu/tamagotchi/my-tamagotchi-forever). Each real-world care action maps to one tap on a meter: "feed, wash, clean up after it and turn the lights out for a good night sleep to stay happy and healthy" (same). Four meters drive everything — "a sleep meter, a hunger meter, an entertainment meter, and a bathroom meter" (https://www.androidpolice.com/2018/01/04/hands-tamagotchi-forever-everything-love-original-digital-pet-toy-mixed-many-free-play-mechanics/).

**2. Session shape.** Many tiny visits through the day, hard-gated by sleep. A five-star reviewer describes the intended rhythm precisely: "Enough to wanna come back throughout the day, but not an overload of a silly amount of tasks or options of stuff" (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever). The ten-second action is tapping a care button — food, toilet or mood. The long session is Tamatown and the three minigames: "a match-3 puzzle, a platformer with an astronaut, and a rhythm-tapping game" (https://www.androidpolice.com/2018/01/04/hands-tamagotchi-forever-everything-love-original-digital-pet-toy-mixed-many-free-play-mechanics/). The gate is brutal and widely resented: "when you put them to bed it takes TWO HOURS for them to wake up (on 100% energy) and it only lasts about 30 minutes before you have to put them back to bed" (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever).

**3. Absence.** **It cannot die and it cannot leave.** A player who tested it directly: "I tested this hypothesis by ignoring my Tama completely for a week and a half (sorry, lil' guy…) and surprise - healthy adult character"; another: "they never die. just poop all over and cry but they will never leave you" (https://www.tamatalk.com/threads/can-tamas-die-run-away-in-my-tamagotchi-forever.195113/). A long absence returns a creature that "hadn't left at all and was waiting patiently" (same). There is no streak and nothing to protect; the only cost of neglect is cosmetic misery. Perversely the energy economy *rewards* absence: energy depletes only while the Tamagotchi is awake, so leaving it in bed "even while starved, bored, and dirty - conserves energy" (https://my-tamagatchi-forever.fandom.com/wiki/My_Tamagatchi_Forever, via https://www.google.com/search — surfaced in search results; **the fandom page itself could not be fetched, so this specific energy claim is not confirmed at source**).

**ESSENTIAL HISTORY — the 1996 keychain.** The original launched in Japan on 23 November 1996 and in the US on 1 May 1997, selling "about 40 million units worldwide during its run" (https://en.wikipedia.org/wiki/Tamagotchi). It really could die, and fast: characters could "die in less than half a day if it did not receive adequate care" (same). Death was permanent and visually explicit — "Japanese Tamagotchi toys usually feature a ghost and headstone when the pet dies, but English language versions have been changed to show an angel at death. There is sometimes more than one death based on how well the pet was cared for prior to death" (same). The stakes had real-world costs: "Teachers expressed concerns over class disruption as well as general distraction from schoolwork and this eventually led many schools to ban the product", and "Children became emotional over the deaths of their Tamagotchi, leading to teenagers sending them to graveyards for burial" (same). **Modern hardware kept death but added a cushion:** the Tamagotchi Pix has "a sleep Mode that acts as a gentle 'pause' button" where "hunger and happiness meters deplete much slower", while the Uni has no pause button at all (https://uptechnet.com/how-do-you-pause-a-tamagotchi/); poor care still kills on the devices (https://en.wikipedia.org/wiki/Tamagotchi). A paid in-game Sitter costing 100 Gotchi Points on the Uni, which avoids the "Grim Reaper due to total neglect", appeared in search results from sciencedesk.blog but that page returned 403 — **not confirmed**.

**4. Currency and endogenous value.** Two currencies. Coins are earned from minigames, jobs and care and spent on "delicious food, cute costumes and colourful items to decorate Tamatown" (https://en.bandainamcoent.eu/tamagotchi/my-tamagotchi-forever); a reviewer confirms "a simple few ways to earn extra coins and rubies" (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever). Gems are premium and exist chiefly to buy past the sleep gate — "to speed up their sleep you have to watch an ad but then the ad choice will run out and you'll have to pay 3 gems" (same); the developer's own reply confirms "there are many options to accumulate coins and gems in the game" (same). Coins feed back into the creature (food and toys refill meters); gems mostly buy time. The money layer is the single biggest complaint and runs on ads plus a subscription: the developer states "Making any real money purchase will deactivate mandatory ads… Subscription to Tama Club will also disable all ads" (same), and players price it at "£5 MONTHLY" (same). Android Police found IAPs "range all the way up to $99.99 per item" (https://www.androidpolice.com/2018/01/04/hands-tamagotchi-forever-everything-love-original-digital-pet-toy-mixed-many-free-play-mechanics/).

**5. Stakes, risk and chance.** Essentially none — that is the design. There is no bet, no loss and no permadeath (https://www.tamatalk.com/threads/can-tamas-die-run-away-in-my-tamagotchi-forever.195113/). The one genuine uncertainty is evolution: "You never know who they might become next!" (https://en.bandainamcoent.eu/tamagotchi/my-tamagotchi-forever) — and when the randomness fails it stings: "I have NEVER gotten another character, and have now gone through 8 CHICKENS" (https://apps.apple.com/gb/app/my-tamagotchi-forever/id1267861706?see-all=reviews).

**6. Progression.** Life stages are the milestone — baby, toddler, teenager, adult, with players asking for more of each: "Make some more babies, toddlers, teenagers and adults like this please!" (https://apps.apple.com/gb/app/my-tamagotchi-forever/id1267861706?see-all=reviews). Beyond that: levels, jobs and unlocks — "it's been very easy to progress through levels, and one of my virtual pets already has a job!" (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever), plus "New mini games, new characters to unlock and even a customisable house!" (same). Memories are also collected: "collect memorable moments shared with your Tamagotchi characters" (https://en.bandainamcoent.eu/tamagotchi/my-tamagotchi-forever).

**7. Social.** Light, opt-in and mostly asynchronous: "explore Tamatown together, making friends with other Tamagotchi characters", "compare your progression and Tamagotchi-raising skills with your friends" and "share your favourite moments with your friends" (https://en.bandainamcoent.eu/tamagotchi/my-tamagotchi-forever). No co-op obligation and no team that can drop you.

**8. Freedom and identity.** You choose care actions that steer which character you get, dress it in "cute costumes", decorate Tamatown (https://en.bandainamcoent.eu/tamagotchi/my-tamagotchi-forever), and later versions added "a customisable house" (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever). You can also keep more than one: "I've enjoyed looking after both of my virtual pets so far" (same).

**9. Signature interaction.** Tapping the toilet button to clean up the steaming poop sitting on the floor next to your creature — the App Store gameplay screenshot shows exactly this: the creature on a rug with a poop and smell lines beside it, and a toilet icon in the bottom bar (https://apps.apple.com/gb/app/my-tamagotchi-forever/id1267861706). The other is tickling: "tickle your Tamagotchi characters - they love it!" (https://en.bandainamcoent.eu/tamagotchi/my-tamagotchi-forever).

**10. UI type and art.** ui_type: **creature in a room**. Soft, rounded, pastel 3D — a chubby vinyl-toy creature with huge eyes on a rug, orange patterned wallpaper, a window onto the town, a houseplant; everything matte and friendly. The screen is **sparse: seven interactive elements total**, counted from the App Store gameplay screenshot — a circular level badge with a green progress ring (top-left), a character-select button (top-right), and a five-button bottom bar of mood/face, food, toilet, sleep and house/town (https://apps.apple.com/gb/app/my-tamagotchi-forever/id1267861706). The creature owns the centre of the screen with nothing overlapping it. A reviewer names the sparseness as the reason they stayed: "not an overload of a silly amount of tasks or options of stuff. Just cute and simple" (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever).

**11. Sound and feel.** Voiced and animated characters, which is divisive. One reviewer "was having to play with the volume off as for the characters I feel are too interactive in the wrong ways. A combination of too often, too sexualised sounding and over all just not fitting voices" (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever). A photo/AR moment exists: "you have the ability to snap photos while your Tamagotchi is playing with a myriad of toys" (https://www.androidpolice.com/2018/01/04/hands-tamagotchi-forever-everything-love-original-digital-pet-toy-mixed-many-free-play-mechanics/). Haptics not confirmed.

**12. Scale and reception.** iOS GB rating **4.44** from **3,336** ratings (https://itunes.apple.com/lookup?id=1267861706&country=gb). Google Play: **10,000,000+ installs**, 3.97 from 84,741 ratings, labelled "Contains ads" and "In-app purchases" (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever). Launched **2018** (GB App Store release 14 March 2018; the official site says 15 March 2018 on iOS and Android) (https://itunes.apple.com/lookup?id=1267861706&country=gb, https://en.bandainamcoent.eu/tamagotchi/my-tamagotchi-forever). Developer **BANDAI NAMCO Entertainment Europe**. Business model: free, ad-funded, with IAP up to $99.99 and a Tama Club monthly subscription that removes ads (https://www.androidpolice.com/2018/01/04/hands-tamagotchi-forever-everything-love-original-digital-pet-toy-mixed-many-free-play-mechanics/, https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever). Metacritic has no critic score and two negative user reviews (https://www.metacritic.com/game/my-tamagotchi-forever/).

Complaints:
- "Seriously overloaded with ads, several of the mini-games have hacked scores too." (https://www.metacritic.com/game/my-tamagotchi-forever/)
- "when you put them to bed it takes TWO HOURS for them to wake up (on 100% energy) and it only lasts about 30 minutes before you have to put them back to bed. And to speed up their sleep you have to watch an ad but then the ad choice will run out and you'll have to pay 3 gems" (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever)
- "The ads are oppressive. I feel like I get one no matter what I do. Not only that, but for an app geared towards children, the ad choices are terrible." (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever)
- On the sleep timer as a wall: "the amount you must wait is never once revealed to you" and "you can't perform any other actions in the game while your pet is sleeping" (https://www.androidpolice.com/2018/01/04/hands-tamagotchi-forever-everything-love-original-digital-pet-toy-mixed-many-free-play-mechanics/)
- "it's a bit cyclical and there isn't really much to do" (https://apps.apple.com/gb/app/my-tamagotchi-forever/id1267861706?see-all=reviews)

Praise:
- "I really like this… Its super cute and simple. Simple was what I was after. Enough to wanna come back throughout the day, but not an overload of a silly amount of tasks or options of stuff." (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever)
- "It's a beautiful re-imagining and modernisation of a beloved part of many people's child hood." (https://apps.apple.com/gb/app/my-tamagotchi-forever/id1267861706?see-all=reviews)
- "The game has so much more to offer now. New mini games, new characters to unlock and even a customisable house! Really cute and sweet little time waster." (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever)
- "they never die. just poop all over and cry but they will never leave you" — the forgiveness read as affection, not as a flaw (https://www.tamatalk.com/threads/can-tamas-die-run-away-in-my-tamagotchi-forever.195113/)

**13. Lesson for RepGarden.** Bandai ran the experiment for us: the 1996 keychain's permadeath produced school bans and children burying toys in graveyards, and the 2018 mobile app removed death entirely so that ignoring it for "a week and a half" returns a "healthy adult character" — proof that a care loop still works when the creature can only look sad, never be lost (https://en.wikipedia.org/wiki/Tamagotchi, https://www.tamatalk.com/threads/can-tamas-die-run-away-in-my-tamagotchi-forever.195113/). Copy the sparse screen: seven elements, one creature centred, a five-button care bar — that is a glance between sets, where Township is not (https://apps.apple.com/gb/app/my-tamagotchi-forever/id1267861706). **Avoid** the thing that replaced death: a sleep/energy timer the player cannot see and must pay or watch an ad to skip. It is the single most-repeated complaint in both stores, and it punishes exactly the client whose rest day was prescribed by the trainer (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever, https://www.androidpolice.com/2018/01/04/hands-tamagotchi-forever-everything-love-original-digital-pet-toy-mixed-many-free-play-mechanics/). Softening the stakes is right; replacing them with a paywalled clock is not.

---

### Across the lane

- **Permanent loss from simple absence is all but extinct, and the two famous cases are both dead or defanged.** Of the nine, only the original FarmVille (2009, closed 31 December 2020) and the original 1996 Tamagotchi destroyed what you had built when you stopped turning up — and the Tamagotchi could die "in less than half a day" without care (https://en.wikipedia.org/wiki/Tamagotchi, https://en.wikipedia.org/wiki/FarmVille). Everything still running does the opposite. Hay Day advertises it on its own site — "It never rains here, but the crops never die" (https://supercell.com/en/games/hayday/); Grow a Garden puts it in its one-line store description — "your garden literally grows while you are offline" (https://growagarden.fandom.com/wiki/Tips); and My Tamagotchi Forever removed death so completely that a player who ignored theirs for a week and a half came back to "a healthy adult character" (https://www.tamatalk.com/threads/can-tamas-die-run-away-in-my-tamagotchi-forever.195113/). Township, Gardenscapes, FarmVille 2: Country Escape, Pocket Camp Complete and Neko Atsume have no decay at all.

- **Where neglect does register, it pauses rather than destroys — and this is the single most transferable rule in the lane.** Stardew Valley, the most beloved farm game in the world, is explicit: "Unwatered crops do not die, but they will not grow either" (https://stardewvalleywiki.com/Crops). Pocket Camp's wilted flower is "pausing the growth timer" and recovers on one watering (https://animalcrossingpocketcamp.wiki.gg/wiki/Garden). My Tamagotchi Forever's creature can only look sad: "they never die. just poop all over and cry but they will never leave you" (https://www.tamatalk.com/threads/can-tamas-die-run-away-in-my-tamagotchi-forever.195113/). A missed day should stall the plot, never clear it.

- **Real loss attaches to a deadline you accepted or to chance, never to absence — and the chance is nearly always upside-only.** Stardew kills crops at a season boundary the calendar told you about, and by lightning (https://stardewvalleywiki.com/Crops); Hay Day forfeits only a Derby task you opted into and can sit out during the cooldown (https://myfarm.site/articles/hay-day-derby-events-guide/); Gardenscapes costs you a life only for a level you chose to play (https://playrix.helpshift.com/hc/en/5-gardenscapes/faq/16021-how-to-get-lives/?l=en); Grow a Garden's only real loss is a 37-Robux PvP steal (https://growagarden.fandom.com/wiki/Take_Player%E2%80%99s_Fruit). Everywhere else randomness only adds: Neko Atsume's unsummonable visitors, Hay Day's mystery boxes, FarmVille 2's Farm Hands and Prize Wheel, Pocket Camp's fortune cookies, Stardew's 1%-per-day giant crops, Grow a Garden's weather mutations.

- **The pressure that replaces decay is capacity.** The three biggest farm sims all converge on it independently: Hay Day's Barn and Silo, where "Storages get full unless you use diamonds or spend time to gather resources to expand" (https://www.gamedeveloper.com/business/game-monetization-design-analysis-of-hay-day); Township's barn, which "won't be able to accept any new stuff you produce" and refills within hours of every upgrade (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game); and FarmVille 2's Barn, Crop Silo and Seaway Storage (https://zyngasupport.helpshift.com/hc/en/11-farmville-2-country-escape/section/300-crop-silo/). In all three it is simultaneously the top complaint and the top conversion mechanic. "I have more than I can store" creates urgency without taking anything away.

- **Absence is frequently paid for rather than punished.** Hay Day grants Re-engagement Rewards to a farm inactive over 31 days — free Barn and Silo upgrades, free services, all animals fed on return — so openly that players discuss lapsing deliberately to collect them (https://ingame.help.supercellsupport.com/hay-day/en/articles/re-engagement-rewards.html, https://www.reddit.com/r/HayDay/comments/1b7m4i7/would_you_stop_playing_and_start_playing_again/). Gardenscapes refills all five lives while you are away (https://playrix.helpshift.com/hc/en/5-gardenscapes/faq/16021-how-to-get-lives/?l=en). Neko Atsume's cats visit and leave fish *because* you left, and the game pays more for leaving them alone than for touching them (http://nekoatsumeguide.weebly.com/the-basics.html). Pay a returning client; never show them a broken streak.

- **The currency that buys the thing you care about is usually walled off from money, and the identity layer works best free and reversible.** Gardenscapes Stars cannot be bought at any price — only coins and boosters can (https://www.deconstructoroffun.com/blog/2017/5/15/gardenscapes-one-big-pivot-to-success) — while Stardew and Pocket Camp Complete have no in-app purchases at all (https://www.stardewvalley.net/stardew-valley-coming-to-mobile/, https://apps.apple.com/gb/app/animal-crossing-pocket-camp-c/id6547834967). Where money does reach it, that is the loudest complaint in the app: Hay Day's diamond-priced paths ("higher than my will to live" — https://www.reddit.com/r/HayDay/comments/11laikv/anyone_have_any_tips_on_how_to_get_diamonds_since/), FarmVille 2's keys "essential for expanding your farm's production" (https://www.withoutthesarcasm.com/posts/farmville-2-country-escape-review/), Township's "the game reaches a level where paying is the only way to progress" (https://play.google.com/store/apps/details?id=com.playrix.township). Conversely, identity costs nothing where it works: Gardenscapes lets you change any decoration's design "for free anytime simply by long pressing on the item" (https://www.levelwinner.com/gardenscapes-guide-2020-update-tips-tricks-strategies-to-beat-every-level-and-restore-the-garden-to-its-former-glory/) and Neko Atsume's seven remodels switch freely once owned (https://www.levelwinner.com/neko-atsume-kitty-collector-ultimate-guide-get-rare-cats/).

- **Screen density is what long-term players turn on, and the sparsest apps are praised for exactly what they left out.** The two Playrix titles are the densest and draw the same complaint in the same words: Township's top clutter thread is simply "Annoying popups", with another at 83 upvotes titled "This game is stressful now" (https://www.reddit.com/r/TownshipGame/comments/1uovwp1/annoying_popups/, https://www.reddit.com/r/TownshipGame/comments/1sw8z1g/this_game_is_stressful_now/), and Gardenscapes players report having to "dismiss a stack of popups before I can actually start… my mood has gone from cozy to an annoyed 'ugh, fine'" (https://www.reddit.com/r/Gardenscapes/comments/1tusjja/anyone_else_exhausted_by_how_the_game_keeps/). Against that, My Tamagotchi Forever runs seven interactive elements with the creature uncontested in the centre and is praised for it — "not an overload of a silly amount of tasks or options of stuff. Just cute and simple" (https://play.google.com/store/apps/details?id=eu.bandainamcoent.mytamagotchiforever) — and Neko Atsume is one yard and one paw menu (http://nekoatsumeguide.weebly.com/the-basics.html). Density also accretes: a 2017 usability audit praised Township's interface as uncluttered and free of pop-ups, the opposite of what its players say in 2026 (https://medium.com/@aarthi.design/playrixs-township-6418f4ce319d).

- **The signature gesture touches the world directly, and the instruction lives in the world too.** Hay Day's finger-drag that harvests and replants a whole row in one sweep, Township's sickle dragged across a ripe field, Stardew's watering-can sweep along a row of tiles, Neko Atsume's camera tap, Gardenscapes' star spent and a corner of the garden visibly transforming, Grow a Garden's plant-and-log-out. None of them is a menu. The prompts are diegetic as well: Township floats a thought-bubble over a building showing the goods it wants (https://medium.com/@aarthi.design/playrixs-township-6418f4ce319d), Hay Day flags ready items with icons above them in the field (https://apps.apple.com/gb/app/hay-day/id506627515). A whole screen becomes one glanceable instruction.

- **Competition is opt-in everywhere, and the one that can expel you is the one people resent.** Hay Day's Derby has an explicit 24-hour cooldown in which members opt out or back in (https://myfarm.site/articles/hay-day-derby-events-guide/); FarmVille 2 players advertise for a "no pressure" co-op (https://www.reddit.com/r/farmville2/comments/1nwh6b7/looking_for_a_no_pressure_coop/); Grow a Garden only ever rewards friends, at +10% each to a +40% cap (https://growagarden.fandom.com/wiki/Sheckles). Township's Regatta is the cautionary case: an App Store reviewer describes being "kicked from teams for insufficient task completion", and the game's own teardown doubts the feature because "most of the players playing Township are likely playing the game to unwind" (https://apps.apple.com/gb/app/township/id638689075?see-all=reviews, https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game).

- **Timed events are the one mechanic everyone in the lane uses and everyone's players complain about — and looping beats expiring.** Grow a Garden's developer conceded it outright after players said the cadence was "making me feel burned out": "Weekly events were just a bit too hard to keep fresh and new" (https://www.shanethegamer.com/esports-news/no-more-weekly-updates-grow-a-garden-dev-teases-a-new-era/). Gardenscapes stacks passes, side stories and reward chains over the garden; Township runs events on a two-to-three-week cadence (https://www.deconstructoroffun.com/blog/2020/10/13/how-playrix-township-became-a-billion-dollar-game). Pocket Camp is the one that solved it: when Nintendo stopped running it as a live service it put seven years of events on a repeating four-year cycle, so a missed event comes round again rather than being gone for good (https://animalcrossingpocketcamp.wiki.gg/wiki/End_of_Service). For a client who trains two to five times a week, a recurring challenge is the only kind that is fair.

---

# Part 2 · Habit apps that grow a plant or a creature

## Lane: plant and creature habit apps

Collected 27 October 2026 for the RepGarden game-design stage. Seven apps where a real-life
behaviour grows something. App Store figures are the GB storefront on the day, read from
`https://itunes.apple.com/lookup?id=<id>&country=gb`. Play figures are the GB Play listing's
download band. Where a claim could not be confirmed from a primary or reputable source it is
marked "not confirmed".

A note on the review quotes: GB App Store reviews were read through Apple's public review
feed, `https://itunes.apple.com/gb/rss/customerreviews/page=<n>/id=<id>/sortby=mostrecent/json`
(and `sortby=mosthelpful`). That feed URL is the citation for each quoted review.

---

### 1. Finch: Self-Care Pet

#### 1. Unit of play

A single bird — the "birb" — hatched from an egg you choose, living in a "birbhouse" or at a
travel location. The real-world action is completing a **goal** on your own list: anything from
"drink water" to "5 burpees" to a custom task. Each goal completion pays two things at once:
**Energy**, which fills a bar and sends the bird on an **Adventure**, and **Rainbow Stones**,
the shop currency. A typical self-care goal is worth 5 energy
(https://finch.fandom.com/wiki/Energy). So one real action maps to one tick, and the tick
buys both a story event and shop money.

The reciprocal framing is explicit on Finch's own page: "You care for your pet by taking care
of yourself" (https://finchcare.com/about-finch).

#### 2. Session shape

Two shapes, which Finch designs for separately. The morning is a **glance**: a mood check,
tick off a goal or two, and the energy bar fills until the bird "automatically starts an
Adventure" (https://finch.fandom.com/wiki/Energy). The evening is the **sit-down**: the bird
returns from a 6-8 hour adventure wanting to talk, offers a **Discovery**, and you pick one of
two replies that "will influence their personality", then optionally write a Reflection
(https://finch.fandom.com/wiki/Adventuring).

In ten seconds you can: tick a goal, send one friend a Good Vibe (worth 3 energy and 2 stones
the first time each day, https://finch.fandom.com/wiki/Good_Vibes), pet the bird by dragging a
finger over it until red hearts appear (https://finch.fandom.com/wiki/Birbhouse), or claim a
daily quest for 25 stones (https://finch.fandom.com/wiki/Quests). A home-screen widget keeps
the bird visible so "a check-in is never more than a tap away"
(https://makeheadway.com/blog/finch-app-review/).

Crucially, **energy resets to zero at the start of the bird's day**
(https://finch.fandom.com/wiki/Energy) — progress is per-day, not cumulative, so a missed day
costs nothing but that day.

#### 3. Absence

Nothing withers and nothing dies. There is no decay mechanic at all. The only thing absence
touches is the opt-in streak.

- The streak counts "each day you open the Finch app — just checking in is enough"
  (https://help.finchcare.com/hc/en-us/articles/37780736136205-Understanding-Streaks).
- Streaks can be switched off entirely in Preferences
  (https://finch.fandom.com/wiki/Streaks).
- Miss a day and a **Streak Repair Hammer** restores it. You earn "a free Streak Repair Saver
  every 3 adventures, as long as you haven't already reached the maximum of 2 saved repairs",
  and you can buy one for 1,000 Rainbow Stones
  (help centre, above; https://finch.fandom.com/wiki/Streaks).
- **Pause Mode** is the true freeze: choose 1-7 days, and "your streak will be safely frozen
  and won't be affected by your time away". It also hides widgets, stops notifications and
  stops friends sending you Vibes (https://finch.fandom.com/wiki/Pause_mode).
- Coming back after a long gap, you are offered four streak commitment levels to restart at —
  "Baby steps (2 days), Normal, Intermediate, and On fire"
  (https://finch.fandom.com/wiki/Streaks).
- The **day boundary is adjustable**: the day begins two hours before your chosen wake-up
  time, so a late check-in still counts (https://finch.fandom.com/wiki/Streaks).

Third-party reviewers describe this as a stated philosophy: Finch "adopts a helpful
no-punishment philosophy: If you don't meet your goals or you step away from the app for an
extended amount of time, it sends only encouragement"
(https://slate.com/technology/2026/09/finch-app-self-care-wellness-review.html). A user
asking for a "failed" option for goals noted the design constraint themselves: "I understand
... Finch doesn't want to encourage anyone to feel guilty for not meeting a goal"
(https://www.reddit.com/r/finch/comments/1k197sl/i_wish_there_was_a_third_option_besides_skipping/).

**And yet the streak is still where the pain is.** The most upvoted absence thread in r/finch
(219 upvotes, 69 comments) is someone quitting over it: "I took a break for a day, just one
day. I still had a streak repair on me, so I would be fine, right? well, I was wrong. I lost
my 145 day streak... I had never thought of Finch to be so stressful, as it is a self care app.
So I think I'm going to quit"
(https://www.reddit.com/r/finch/comments/1u58y0h/i_lost_my_streak_while_i_still_had_a_streak/).
And: "Ive been really sick and busy the past month and I lost my streak. Now I don't even want
to log in or do anything"
(https://www.reddit.com/r/finch/comments/1q7ejwn/anyone_else_feel_completely_unmotivated_once_they/).
A GB reviewer: "I've loved this app so much that I paid for another year... Including losing a
434 day streak without missing a day"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=1528595748/sortby=mostrecent/json).

So: the creature never punishes you; the streak counter does. The two are deliberately
separable and users still get hurt by the one that was bolted on.

#### 4. Currency and endogenous value

**Rainbow Stones**, earned only by playing — "Rainbow stones can't be bought; you can only get
them by using the app" (https://finch.fandom.com/wiki/Rainbow_Stones). Earned from goals, from
hitting full energy, quests (25 a daily quest, 20/50/100 for weekly milestones, 100 for special
quests), seasonal chests, selling items back, sending Good Vibes, writing reflections, plus
65-80 free stones a day from Mr. Prickles when you open the outfit shop
(https://finch.fandom.com/wiki/Rainbow_Stones, https://finch.fandom.com/wiki/Quests).

Spent on: clothing, birbhouse furniture, body colour dyes, **travel to new locations**
(300 stones for a flight, 200 to come home), streak repair (1,000), shop refreshes, and a
200-stone fee to gift a friend (https://finch.fandom.com/wiki/Rainbow_Stones).

Almost all of it is cosmetic — **except travel**, which unlocks location-exclusive shop items
and new discovery content, and streak repair, which buys back continuity. So there is a thin
but real endogenous loop: stones buy travel, travel unlocks items and stories.

The wiki itself flags the failure mode: "WARNING: Some people find that they become too
focused on getting more stones and buying outfits, and stop paying attention to their Goals.
This is a real problem" (https://finch.fandom.com/wiki/Rainbow_Stones).

**Real money: Finch Plus**, $9.99/month or $69.99/year
(https://makeheadway.com/blog/finch-app-review/); GB reviewers report £39.99 and £60. It buys
*options*, never items: extra shop slots, more vibes, more travel options a day, extra event
rewards, unlimited gifting, unlimited saved outfit combinations. Finch has **no
member-exclusive items** (https://finch.fandom.com/wiki/Finch_Plus). There is also a loyalty
discount ladder — 19% at 25 adventures, rising to 45% at 100 — and a monthly "Guardians"
raffle that sponsors a free month for players who cannot afford it
(https://finch.fandom.com/wiki/Finch_Plus).

Perception is mixed and price-sensitive: "This is a great app but it's incredibly expensive...
At £60 it wasn't cheap"; "The free trial is not free! They charged me £39.99 on day 2 of a 7
day trial" (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=1528595748/sortby=mostrecent/json).

#### 5. Stakes, risk and chance

No betting, no risk of loss. The randomness is all upside:

- **Discoveries** on return from an adventure, sorted into categories, "so there's always
  something new to find" (https://finch.fandom.com/wiki/Adventuring).
- Shop stock rotates daily; travel destinations are "offered in rotation"
  (https://finch.fandom.com/wiki/Adventuring).
- **Goal of the Day** pays "a surprisingly increased number of stones... (The boosted value is
  random.)" (https://finch.fandom.com/wiki/Rainbow_Stones).
- **Micropets** hatch from eggs at Professor Oat's Lab — 66 of them as of October 2026, each
  with its own walk, sleep pose and "unique 'voice'"
  (https://finch.fandom.com/wiki/Micropets).
- Monthly seasonal events with 14-day story locations, and opt-in monthly **Goal Challenges**
  (https://finch.fandom.com/wiki/Quests).
- One genuinely clever inversion: "If you are having a bad day, choose the lowest value on the
  mood selector to get more stones for each click"
  (https://finch.fandom.com/wiki/Rainbow_Stones). The reward goes *up* when you are worse off.

#### 6. Progression

Five growth stages gated on **adventures completed**, not days: Baby (adventures 1-7),
Toddler (8-22), Child (23-42), Teen (43-67), Adult (68+). Each stage raises the energy needed
for an adventure (15 to 20 to 25 to 30 to 35) and shortens its duration (8 to 6-7 to 6 hours),
unlocks a new body part for colour customisation, and at Child unlocks travel
(https://finch.fandom.com/wiki/Stages_of_Growth).

Beyond that: six ongoing **Special Quests** with long ladders (clothing collected 1 to 10,000;
decorations 1 to 10,000; micropets met 1 to 2,000; locations visited 2 to 27; growth stages;
friendship levels) and **Friendship** with your own bird across 10 named levels, "from Pals to
Uber Soulmates" (https://finch.fandom.com/wiki/Quests). Plus a monthly seasonal event cycle.

The milestone that matters is **growing up**, and it is earned by adventures — so a day where
you did nothing simply does not count toward it, rather than counting against it.

#### 7. Social

Opt-in and strictly non-competitive. **Tree Town** is a tree holding up to eight friends'
birds per page, added by friend code or link. There is no leaderboard and no score comparison.
You can:

- Send **Good Vibes** — 14 sentiments (18 with Plus), the first one each day paying you 3
  energy and 2 stones. "Your friend will see an animation of your birb and a message conveying
  your sentiment" (https://finch.fandom.com/wiki/Good_Vibes).
- **Ask for a hug**, which puts a request at the top of friends' Tree Towns
  (https://finch.fandom.com/wiki/Tree_Towns).
- **Invite a friend's birb over** for about an hour, where it accompanies yours at home or on
  an adventure; and pet other people's birds, "which doesn't do much but is incredibly cute".
- Send **gifts** (clothes, furniture, micropets — never colours), one per friend per day free,
  at a 200-stone fee.
- Become **Goal Buddies** on a specific goal: "you can see how your friend is doing, and they
  can see your daily progress as well", including each other's per-goal streaks, with a
  praise action after they complete it.
- See a friend's last four milestones (hatched a micropet, discovered something, travelled,
  grew up).
- Friends never see your writing. Vibes, push and friend requests are each independently
  switchable off (https://finch.fandom.com/wiki/Tree_Towns).

#### 8. Freedom and identity

High. You choose the egg colour, then the bird's **name, pronouns and a trait**. Colour
customisation unlocks body part by body part as the bird grows (beak and body at Toddler,
headpatch and wings at Child, cheeks and feet at Teen, tummy at Adult)
(https://finch.fandom.com/wiki/Stages_of_Growth). You dress it, decorate the birbhouse
(wallpaper, floor, bed, window, door, two carpets, decor), favourite room layouts, equip a
micropet. Discovery replies shape its personality
(https://finch.fandom.com/wiki/Birbhouse, https://finch.fandom.com/wiki/Adventuring).

Goals are fully user-written: "You can write your own custom goals", with suggestions
organised into ten self-care areas (https://finch.fandom.com/wiki/Goals).

#### 9. Signature interaction

**The bird leaving on an adventure because your energy bar filled, and coming home at night
with a story it wants to tell you.** The departure is automatic — you do not press "go", your
day's ticks push the bar to full and it goes (https://finch.fandom.com/wiki/Energy). The
return is a conversation with two reply options that change who the bird is. Second to that:
petting the bird by dragging a finger across it until red hearts come off
(https://finch.fandom.com/wiki/Birbhouse).

#### 10. UI type and art

**Creature in a room**, full-width, one scene. Home shows the bird in its birbhouse or at its
current travel location, with the **energy bar directly above a tick-off checklist of your
goals**, which hides completed items (https://finch.fandom.com/wiki/Finch_App). Art is soft,
rounded, pastel 2D cartoon; the bird is a simple blob with customisable colour zones. Six
bottom tabs: Home, Quests, Shop, Friends (Tree Town), Bag, and the bird's own notebook page.
A top-left hamburger holds everything else.

So: the scene is sparse, the surrounding navigation is not. The Slate reviewer's "Finch
burnout" is partly about that volume of surface
(https://slate.com/technology/2026/09/finch-app-self-care-wellness-review.html).

#### 11. Sound and feel

Micropets each have "their own unique 'voice'" (https://finch.fandom.com/wiki/Micropets).
Petting produces small red heart particles (https://finch.fandom.com/wiki/Birbhouse). Quest
claims have "a little animation each time you claim a reward"
(https://finch.fandom.com/wiki/Quests). Soundscapes and animated guided breathing are in-app
activities rather than feedback (https://finch.fandom.com/wiki/Finch_App). Haptics: **not
confirmed**.

#### 12. Scale and reception

- iOS GB: **4.93**, **78,559** ratings (lookup, 27 Oct 2026).
- Play: **10m+** downloads (https://play.google.com/store/apps/details?id=com.finch.finch).
- Launched 12 May 2021. Developer: **Finch Care Public Benefit Corporation**. Free with the
  optional Finch Plus subscription; no ads (lookup; https://finch.fandom.com/wiki/Finch_Plus).

**Three complaints**

1. The subscription price, repeatedly. "This is a great app but it's incredibly expensive. As
   it's a self care app I did pay for it... At £60 it wasn't cheap and to find out you have to
   pay that yearly came as a shock... You can do NONE OF THIS IN THE FREE APP"
   (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=1528595748/sortby=mostrecent/json).
2. Losing a long streak, including to bugs and device transfers, driving people to quit. "I
   lost my streak while I still had a streak repair, so I'm quitting"
   (https://www.reddit.com/r/finch/comments/1u58y0h/i_lost_my_streak_while_i_still_had_a_streak/);
   "losing a 434 day streak without missing a day" (review feed, above).
3. The reward loop crowding out the point. The Slate reviewer hit "Finch burnout" in six
   weeks and felt she was "performing wellness rather than actually feeling well", with the
   bird "telling me it missed me"
   (https://slate.com/technology/2026/09/finch-app-self-care-wellness-review.html). The wiki
   says the same thing about stones (section 4).

**Three things people love**

1. It works on people who bounce off habit trackers. "Seems daft that looking after a little
   birb keeps me motivated at 45yo, but at this point I'll take whatever works. I'm
   remembering to take meds, do my physio exercises... I am Autistic-ADHD, and so far the
   novelty hasn't worn off" (review feed).
2. The caretaking frame itself. "This really helped me have better sleep and mental health,
   just knowing I would come back to a little Birb every day" (review feed).
3. The cost of entry is one honest tap. "I enjoy this one because the virtual pet is really
   cute and it takes just a moment to be honest about how I really feel"
   (quoted in the App Store listing,
   https://apps.apple.com/gb/app/finch-self-care-pet/id1528595748).

#### 13. Lesson for RepGarden

Take the whole absence architecture: no decay, a reward meter that resets daily so a rest day
is simply a zero rather than a loss, progression counted in *sessions completed* rather than
days elapsed, and a pause mode the client turns on themselves. Take the two-shape session —
a tick between sets, a sit-down at the end where the vegetable has something to tell you —
and take the inversion where a bad day pays more, which fits a gym app where the hard sessions
are the valuable ones. Avoid the daily check-in streak entirely: Finch's own community's
loudest pain is a streak it bolted onto an app that otherwise refuses to punish, and it would
be worse against trainer-prescribed rest days. Also avoid Finch's menu sprawl — six tabs and a
hamburger is the opposite of one scene at a time.

---

### 2. Forest: Focus for Productivity

#### 1. Unit of play

One **tree per focus session**, planted into a persistent **forest** laid out as a grid by
day, week and month. The real action is *not touching your phone* for a chosen length of time.
"Stay off your phone and a tree grows. Leave early and it withers"
(https://apps.apple.com/gb/app/forest-focus-for-productivity/id866450515). The tree grows in
real time as the timer runs (https://www.forestapp.cc/).

This is the cleanest one-to-one mapping in the lane: one block of behaviour, one object, placed
permanently in a visible record.

#### 2. Session shape

A single committed block, default **25 minutes** on the Pomodoro model, with 25-55 minutes
growing a small tree (https://www.theory7.net/support/en-us/tips-tricks/forest-app-focus-by-planting-trees
— third party). The home screen is "an empty patch of ground where your forest will grow, a
timer, and a selection of trees, with one big 'Plant' button front and center" (same source).

Ten seconds is enough to pick a length, pick a species and press Plant. Everything else is
waiting. The *review* of the session — the forest grid, the stats, the tags — is the sit-down
screen.

The current version has broken this and been punished for it. "Just make the app actually
work as a study timer instead of doing too much: one click to plant, one to stop, total time
spent on the Home Screen"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=866450515/sortby=mostrecent/json).

#### 3. Absence

There is no between-session decay — a forest does not rot while you are away. The penalty is
**inside** the session and it is immediate and permanent: "If users leave the app before the
timer ends, their tree withers and dies. **Dead trees remain visible in the forest as records
of interrupted focus sessions**" (https://en.wikipedia.org/wiki/Forest_(application)). A
withered stump sits in your grid forever.

Deep Focus mode hardens it: "try to switch apps mid-focus, and Deep Focus pulls you back. The
only way out is to give up — and let the tree die" (https://www.forestapp.cc/). An **Allow
List** lets you nominate apps you can use without killing the tree (iOS 16+)
(https://apps.apple.com/gb/app/forest-focus-for-productivity/id866450515).

No streak is required to keep the forest. But the December 2025 freemium rebuild added **daily
login events**, and that is the part users read as a betrayal of the premise — see section 12.

#### 4. Currency and endogenous value

Three layers, and the third is new and resented.

1. **Coins**, earned per successful session (a third-party figure: 30 minutes = 10 coins,
   https://makeheadway.com/blog/forest-app-review/ — not developer-confirmed). Spent on new
   tree species, bushes, decorations and soundscapes
   (https://apps.apple.com/gb/app/forest-focus-for-productivity/id866450515).
2. **Real trees.** Coins can be redeemed to have a real tree planted with Trees for the
   Future; third-party guides put the cost at **2,500 coins**
   (https://www.theory7.net/support/en-us/tips-tricks/forest-app-focus-by-planting-trees).
   "Together, our community has planted over 2 million real trees"; Forest "covers the cost
   from app revenue", capped at "up to 5 real trees per account"
   (store listing; https://www.forestapp.cc/). **This is the only item in the whole lane where
   spending the earned currency produces something outside the game.**
3. **Crystal**, a purchasable hard currency, plus "Sunshine Elixir". GB in-app purchases
   include Shovelful of Crystal £0.99, Small pot £4.99, Large bag £10.99, Cartful £21.99, and
   Sunshine Elixir £0.99/£1.99
   (https://apps.apple.com/gb/app/forest-focus-for-productivity/id866450515).

**Real-money model:** Forest launched paid in 2014 and "transitioned in December 2025 to a
free model with optional Forest Plus subscription for enhanced features and higher coin
rewards" (https://en.wikipedia.org/wiki/Forest_(application)). GB Plus pricing on the listing:
£5.99/month, £35.00/year (Early Bird). Plus gives exclusive species, full soundscapes,
analytics and a "3x coin boost" (https://www.forestapp.cc/). Legacy one-time Pro is closed to
new users.

#### 5. Stakes, risk and chance

This is the lane's clearest **chosen stakes** design, and the stake is set by the player before
the session: pick the length, and optionally switch on Deep Focus, which removes the escape
hatch. You are wagering a permanent mark on your own grid against your own attention. There is
no randomness worth naming — no drops, no weather, no visitors. The tension is entirely
self-imposed and entirely legible.

**Plant Together** raises the stake socially: "everyone plants the same tree during a
synchronized session", and if anyone abandons focus, "the whole forest falls"
(https://www.forestapp.cc/).

#### 6. Progression

Unlocked **tree species and soundscapes "as you reach focus milestones"**, achievements with
extra rewards, and a cumulative forest you can review by day, week and month. Real trees are
the top-end milestone, capped at five
(https://apps.apple.com/gb/app/forest-focus-for-productivity/id866450515,
https://www.forestapp.cc/). No levels, no seasons, no evolutions — the record *is* the
progression.

#### 7. Social

Opt-in, and both co-operative and competitive. **Plant Together** rooms with friends and
family for synchronised sessions, where one person's failure kills the shared forest. Plus
"Compete with users around the world and share your forest" — a global leaderboard
(store listing). Tags let you label sessions by subject or project.

#### 8. Freedom and identity

Thin and purely decorative: species choice per session, bushes and decorations, custom tags, a
name for the session. No avatar, no named creature, no home to furnish.

#### 9. Signature interaction

**Pressing Plant and putting the phone face down** — the moment the sapling appears and the
timer starts, the stakes are live. And its mirror: coming back to a dead tree you have to look
at from now on.

#### 10. UI type and art

**Side-on single scene**, becoming a **top-down world** when you look at the forest grid. A
patch of ground, a tree, a ring timer, a Plant button; then a grid of trees and stumps. Flat,
soft illustration, muted greens, very little chrome historically. The current version is the
subject of a design revolt: "Clunky UI, three taps to finish a timer when it used to take one,
too many animations to collect bs"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=866450515/sortby=mostrecent/json).

#### 11. Sound and feel

The tree growing in real time is the main animation. Soundscapes play during sessions and
"Mindful Space combines calming soundscapes, breathing exercises, and gentle animations"
(store listing). The post-session reward animation is the specific thing users want removed:
"New update makes me click and watch an animation to 'claim coins' after I finish a session.
Adds so much time. I don't want this extra gamification - please make it optional" (review
feed). Haptics: **not confirmed**.

#### 12. Scale and reception

- iOS GB: **4.79**, **20,504** ratings (lookup, 27 Oct 2026).
- Play: **10m+** downloads (https://play.google.com/store/apps/details?id=cc.forestapp).
- Launched on iOS 10 May 2014 by **Seekrtech Co., Ltd.** (creators Marcus Pi and Amy Cheng).
  Paid until December 2025, then free with Forest Plus plus a purchasable Crystal currency
  (https://en.wikipedia.org/wiki/Forest_(application)). The listing claims 60 million users
  and top-productivity-app status in 136 countries.

**Three complaints** — all, strikingly, about *adding game to a focus app*:

1. The gamification is now the distraction. "Was a loyal user of Forest for 5 years... The team
   introduced more trees along with daily login events and timed events. This completely
   defeats the point of getting off your phone and focusing. **When your focus app needs you
   to log in daily and rewards you with cosmetics, it is no longer a focus app, it's part of
   the problem**"
   (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=866450515/sortby=mostrecent/json).
   And: "Originally brilliant focus app turning into its own distraction land" (same feed).
2. Friction added to the core loop. "why does it now take several clicks and animations to
   collect rewards and move onto the next tree??? that's poor. ive used this app since 2018
   and the recent update has made it so user unfriendly" (same feed).
3. The move to subscription and what paid users lost. "I paid for the old one-time premium
   version, but now they are pushing a paid subscription aggressively... They also changed the
   UI from everyone's beloved minimalist design to a very flashy, impractical and distracting
   one" (same feed). There is a petition: "Respect Pro Users and Restore the Features We
   Already Paid For"
   (https://www.change.org/p/forest-respect-pro-users-and-restore-the-features-we-already-paid-for).

**Three things people love**

1. The dead tree works. "Forest works well, and if your goal is to be more in the moment,
   ignore your phone and actually talk to your friends when you are with them, this is the app
   for you" — The New York Times, quoted on the listing
   (https://apps.apple.com/gb/app/forest-focus-for-productivity/id866450515).
2. The forest as a record of your own attention — "a visible record of every minute you chose
   depth over distraction" (https://www.forestapp.cc/), echoed by users who keep it for years.
3. Real trees. Two million planted via Trees for the Future makes the earned currency mean
   something outside the app (store listing, https://www.forestapp.cc/).

#### 13. Lesson for RepGarden

Forest proves that a **chosen, pre-committed stake** beats an imposed penalty: the client sets
the terms, so the loss is theirs and it is fair. A gym analogue is opt-in — "I'm committing to
three sessions this week" — where the vegetable's outcome is decided by a promise the client
made, not by the app's calendar. And the permanent record of both successes and misses in one
grid is honest in a way a streak is not.

The warning is louder than the lesson, though. Forest's own long-term users are abandoning it
because the game layer grew into the app's way: daily login events, claim animations, extra
taps and cosmetics in a tool whose job was to get out of the way. For a game that lives in a
gym between sets, every tap added to the core loop is a cost, and "one click to plant, one to
stop" is the standard to hold to.

---

### 3. Flora - Green Focus

#### 1. Unit of play

A **plant per focus session**, placed into a **Garden** that is a single left-to-right row in
planting date order, with the newest on the right
(https://flora.appfinca.com/faq/). Same core as Forest: plant a seed, stay off the phone, and
"as you work hard, the seed will grow into a healthy tree"
(https://apps.apple.com/gb/app/flora-green-focus/id1225155794). "If you cannot resist the
temptation of using your phone and leave the app while growing a tree, the tree will be
killed!" (store listing).

Where Flora differs: trees can be **tagged to a to-do item**, and the session's minutes feed a
goal progress bar on that to-do (https://flora.appfinca.com/faq/). So a session maps to a tree
*and* to a named objective.

#### 2. Session shape

Pick a duration, press Start. Two refinements that matter for a gym:

- **Pause** — "simply press the 'Pause' button when growing a tree. Then you can go to any
  other apps without killing the tree... The pause time will be subtracted from the final
  duration." Pause is **disabled whenever a Price is attached**
  (https://flora.appfinca.com/faq/).
- **Overtime** — "A focus session does not end when the tree grows. So, keep working! During
  this phase, the focus duration will automatically count up" until you press "See Tree"
  (same).

The sit-down screens are the Garden, My Stories (a photo-and-note feed per session), To-Dos
and Stats (daily, weekly, monthly, yearly).

#### 3. Absence

No decay between sessions, same as Forest — but with one quietly brilliant detail. "The trees
in your Garden naturally shift towards the left over time. To keep your garden vibrant and
full of life, it's important to plant new trees (and stay focused on tasks) regularly, just as
you would care for a real-world garden" (https://flora.appfinca.com/faq/). Absence does not
kill anything; it just slides your visible garden out of frame and leaves a gap. The FAQ even
answers "Why is there a gap (empty space) to the right of the plants in my Garden?" — the gap
*is* the record of absence.

Streaks exist only per to-do, opt-in: "you will get a winning streak if you successfully grow
trees and tag them with the to-do in successive days" (same).

The in-session death is also recoverable in a way Forest's is not: **False Detection**
reporting. "If you get your tree killed and think it was not your fault, please report a
'False Detection'... If verifying that it is indeed a false detection, we will revive your
tree" (same). This exists because the detection is unreliable, which is Flora's single biggest
review problem (section 12).

#### 4. Currency and endogenous value

- **Flora Bits / credits**, earned by focus time, used to unlock plants on a "Grand Tour" of
  stops. The latest update line reads "Pledge a Price using Flora Bits"
  (https://apps.apple.com/gb/app/flora-green-focus/id1225155794). This replaced an earlier
  system and is unpopular: "Locking trees behind these credits, rather than requiring a set
  time to dedicate towards unlocking each (such as 25 minutes) betrays the purpose of the app
  as a Pomodoro timer and demotivates users as it now requires several hours to unlock trees"
  (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=1225155794/sortby=mosthelpful/json).
- **Badges** at total-hours thresholds, including "Expert Planter", which gates the Big Garden
  view (https://flora.appfinca.com/faq/).
- Cosmetic value is unusually *compositional*: the FAQ coaches you on garden aesthetics —
  "Avoid planting trees in succession... intersperse them with flowers or fruit plants to create
  a denser, more vibrant look... Designate certain plants to commemorate special events in your
  life" (same). The reward is a picture you authored over months.

**Real money.** "Is there a 'paid version' of Flora? **No. There is only one, free version**"
(https://flora.appfinca.com/faq/). Revenue comes from one-off tour packs (GB: Amazon Rainforest
Tour £0.99-£1.99, Drylands' Marvels Tour £1.99 —
https://apps.apple.com/gb/app/flora-green-focus/id1225155794) and from the two opt-in services
below.

#### 5. Stakes, risk and chance — the Price mechanic

This is the one real-money stake in the lane, and the detail is instructive.

Flora "proudly offers the opt-in **Price and Care** services that let you plant real trees on
the earth if you kill or successfully grow a tree in the app" (store listing). The Price is a
cash amount you set on yourself before a session; kill the tree and you pay it, and the money
plants a real tree through Trees for the Future or Eden Reforestation Projects
(https://flora.appfinca.com/, https://flora.appfinca.com/faq/).

The safeguards are the interesting part:

- **It is self-reported.** "When using the Price feature, you are not charged unless you
  confirm that you killed a tree by pressing the '**Honor My Price**' button on the red focus
  screen" (https://flora.appfinca.com/faq/). The app will not take your money without you
  pressing a button that says you deserved it.
- Setting a non-zero Price **automatically disables Pause** for that session — the stake buys
  away your own escape hatch (same).
- False Detection reporting and a manual refund path by email both exist for the Price (same).
- **Flora Care** is the inverse: a subscription that plants a real tree when you *succeed*.
  Third-party reporting puts it at $9.99 for a tree per 24 hours of focus and $1.99 for a tree
  per 120 hours (https://www.makeuseof.com/stay-productive-using-flora-app/ — not confirmed on
  Flora's own pages).

**How reviews receive it:** barely at all. Across eight pages of GB reviews sorted by most
recent and six by most helpful, not one review mentions the Price, betting or being charged for
a dead tree. The complaints are overwhelmingly about false tree deaths, the Bits economy and
bugs. The one Price-adjacent signal is the "Greyed out app during dispute?" thread in r/FloraApp
(https://www.reddit.com/r/FloraApp/comments/192iwrt/greyed_out_app_during_dispute/). Read
charitably, the self-report gate has worked: because nobody is billed by surprise, nobody is
angry about it — and because it is strictly opt-in and self-reported, hardly anyone uses it.
That is the trade. **Not confirmed:** any published take-up figure.

The social stake is stronger in practice: in a group room, "If you are the host of the session,
**everyone's tree will be killed** because the session will be terminated. If you are a guest...
you will only kill the tree grown by yourself" (https://flora.appfinca.com/faq/). And success
pays a peer's tree: "each participant of a successful group focus session... win[s] an additional
tree grown by a random peer. Are you ready to win your friend's trees?" (same).

#### 6. Progression

A **Grand Tour** of stops, each unlocking new plant species, driven by accumulated focus time
via Bits; total-hours badges; per-to-do goal bars and repeating goals that reset daily, weekly
or monthly; the Big Garden unlocked at Expert Planter
(https://flora.appfinca.com/faq/, store listing). Students in the reviews track their stage
("I was on stage 16").

#### 7. Social

The strongest social layer in the lane, and opt-in. Friends by QR code or contacts. **Rooms**:
host or join by passcode, preview a room's time remaining before joining, pick your own plant
as a guest. Chat and a shared story feed. A friends leaderboard of total hours. Per-story
visibility control ("Only Me"), with the FAQ gently discouraging it: "your story may be a
great motivator to your friends and could trigger fun interactions"
(https://flora.appfinca.com/faq/). Flora cites Festinger, Heider and Newcomb in the FAQ as the
basis for co-focus, which is unusual honesty about the mechanism (same).

Reviews confirm it is the retention hook: "Loads of my college friends and I love this app and
use it as competition to study"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=1225155794/sortby=mosthelpful/json).

#### 8. Freedom and identity

Plant species per session; **garden composition** (the deliberate aesthetic above); a
"What to focus on next?" note before and an "Attach a message" note after, plus session photos;
to-do names and tags. No avatar or creature.

#### 9. Signature interaction

**Setting a Price on yourself and watching the Pause button go away.** The gesture that is
unmistakably Flora is pressing "Honor My Price" on the red screen — voluntarily paying for your
own failure. Second: joining a friend's live room mid-session and growing in parallel.

#### 10. UI type and art

**Side-on single scene** during focus (ground, plant, timer), and a **top-down/side-scrolling
world** for the Garden row. Flat vector plants, bright saturated greens, a green focus screen
that turns **red** when the tree is killed — the clearest colour-state signal in the lane.
Dense by current standards: tabs for Garden, To-Dos, Stats, Stories, Friends, plus a seed
picker, people icon, key icon, tag icon. "I feel like it's severely lacking instructions/a
tutorial though. I have been using the app for 2 days and still don't understand the concept of
the trees, world tour, prizes, etc and how they all fit together"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=1225155794/sortby=mosthelpful/json).

#### 11. Sound and feel

Notification when the tree grows up even on a locked phone; the green-to-red screen flip on a
kill; growth animation. Sound and haptics: **not confirmed**.

#### 12. Scale and reception

- iOS GB: **4.76**, **84,985** ratings (lookup, 27 Oct 2026) — the largest GB rating count in
  the lane.
- Play: **100k+** downloads
  (https://play.google.com/store/apps/details?id=com.appfinca.flora.android). Flora is
  overwhelmingly an iOS product.
- Launched 8 October 2018. Developer: **AppFinca Inc.** Free, with one-off tour packs and the
  opt-in Price and Care services; no paid tier (store listing;
  https://flora.appfinca.com/faq/).

**Three complaints**

1. **False kills — the dominant complaint.** "Whenever i click the pause button to quickly
   check something on another app, when i return to flora it says that 'I' killed the tree,
   despite the fact i clicked the pause button... i may have been focused for 2 hours then all my
   progress is lost" and "My trees keep getting killed when I'm not going on any restricted
   apps... they almost always get killed right towards the end of my sessions"
   (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=1225155794/sortby=mosthelpful/json).
   Also r/FloraApp: "My tree keeps dying"
   (https://www.reddit.com/r/FloraApp/comments/1c2zhzw/my_tree_keeps_dying/).
2. **The Bits economy stretched the reward out of reach.** "I found the fun in studying for
   little time like half an hour and letting my timer run over and still unlocking a cool
   surprise plant rather than now having to study for 325 minutes (5.4 hours) just to unlock a
   plant that was worth 5 minutes before!!!???" and "The new 'bit' system is frankly
   horrendous, with poor tracking and incredibly unrealistic prices" (same feed).
3. **An update broke the garden people had built.** "I used to love being able to rearrange my
   garden however due to the linear nature of the new update my garden looks odd and all the
   plants i've grown in previous months have grouped so they look very odd" (same feed); and on
   Reddit, "They just destroyed the app. Nice one flora i just lost many hours of my session
   and now my trees died"
   (https://www.reddit.com/r/FloraApp/comments/1i7jlbb/they_just_destroyed_the_app_nice_one_flora_i_just/).

**Three things people love**

1. The threat of the dying plant, as a threat. "It warned me that if I open the specific
   blocked apps then my plant would die which is actually a really nice motivation to keep
   working and stay off my phone" (review feed).
2. Studying together. "I like the slightly social element to it where you can revise with
   friends and plant trees because my garden looks truly beautiful now!!" (review feed).
3. The garden as evidence of work done. "seeing a big number under my total hours for the week
   makes me feel like i've actually achieved something" (review feed).

#### 13. Lesson for RepGarden

Two things transfer directly. First, the **Price pattern**: if RepGarden ever wants a stake, the
charge is self-reported — the client presses the equivalent of "Honor My Price" — and taking the
stake removes the client's own escape hatch. No automatic penalty, ever. Second, Flora's absence
model is the gentlest honest one in the lane: miss a week and nothing dies, your garden row just
**slides left and leaves a visible gap**. That is a reproach without a punishment, and it maps
cleanly onto a vegetable patch where the beds you did not plant are simply empty.

The avoid is sharp and specific to a gym: **never let the app decide you failed on evidence it
cannot trust.** Flora's rating is dragged down almost entirely by false kills, because the app
asserts a failure the user knows did not happen. RepGarden can only see sessions logged, so the
game must never infer a miss it cannot prove, and every negative state needs a one-tap "that
wasn't me" route. Also avoid stretching a reward's price after people have learned it: the Bits
change lost Flora years-long users overnight.

---

### 4. Plant Nanny Cute Water Tracker

#### 1. Unit of play

**One plant at a time** in a pot, plus a **greenhouse** of finished plants. The real action is
drinking a glass of water: "Each glass of water you drink helps grow the cute plants in your
garden so you can both thrive!" (https://sparkful.app/plant-nanny). You log a glass by
"pressing and holding the water button on the main screen"
(https://mobilesyrup.com/2019/03/17/plant-nanny2-water-health-app-review/), which pours water
into the pot and raises the plant's level.

Of all seven, this is the closest to RepGarden's premise: a specific repeated real-world act,
several times a day, each one visibly feeding one growing plant. Plants come in **three
difficulty levels** so you can match the commitment you are willing to make (store listing,
https://apps.apple.com/gb/app/plant-nanny-cute-water-tracker/id1424178757).

#### 2. Session shape

Pure glance, many times a day. Onboarding asks weight and activity level, computes a daily
target and "breaks it down into a number of 'cups' to drink"
(https://mobilesyrup.com/2019/03/17/plant-nanny2-water-health-app-review/). After that each
interaction is a single press-and-hold. A widget shows the plant and hydration at a glance
(store listing). The sit-down screens are the greenhouse, monthly comparison charts and the
plant's own page (personality, dialogue, name).

#### 3. Absence

**The plant wilts but cannot die.** "In Plant Nanny 2, the plant will never 'die' — the
animation will instead look as though your plant has 'wilted' since the last time you opened
your app. Now if that happens, no worries, just drink a glass of water, and your plant perks up
and returns to its lively animation"
(https://mobilesyrup.com/2019/03/17/plant-nanny2-water-health-app-review/; same mechanic
summarised at https://sparkful.app/plant-nanny). Recovery costs exactly one glass — the same
action that would have prevented it.

There is also an **over-watering** state: log too fast and "you might drown the plant.
Thankfully, the app will warn you. You'll see a blue, stressed-out emoji next to it, and a
dialog box will tell you to slow down" (mobilesyrup, above). This is a genuinely two-sided
feedback loop — the only one in the lane — and it misfires: "every time I log 400ml I get a
message that pops up telling me I'm drinking too fast. This isn't the case as it happens even
when I log a single glass"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=1424178757/sortby=mosthelpful/json).

No streak is central; there are "mini-challenges" and subscriber "5 daily challenge rewards"
(store listing; https://sparkful.app/plant-nanny). Clovers come partly from "Daily login
rewards" (https://fourdesire.helpshift.com/hc/en/8-plant-nanny-1687933580/section/89-plants-pots-creatures-and-greenhouse-1706601857/).

Reviews show the wilt lands emotionally even though it is harmless: "when I don't drink enough
water my plant starts to die so they helped me realise okay I need to drink more water" and,
less happily, "there sits my plant almost crying because I gave him 5/11 cups of water in one"
(review feed, above).

#### 4. Currency and endogenous value

**Clovers**, earned "through achievements, medals, Daily login rewards, and clicking buddies"
(https://fourdesire.helpshift.com/hc/en/8-plant-nanny-1687933580/section/89-plants-pots-creatures-and-greenhouse-1706601857/)
— and buyable with real money (GB: Pile of Clovers £1.99, Pack of Clovers £4.99,
https://apps.apple.com/gb/app/plant-nanny-cute-water-tracker/id1424178757). Spent on new plants
and special pots, plus decor like flowerpots, rugs and lamps (store listing).

Spending feeds back weakly: a new plant is a new growth loop, so plants are the endogenous part
and pots are cosmetic. The feedback got *worse* in an update, and users noticed precisely what
was lost: "the new update removed the seeds which was a fun goal and a good way to interact with
previous plants" and "You used to be able to collect nuts everyday in order to buy the next
plant or flower pot. Also, depending on what 3 plants you'd grown in a single tree hole you
could earn more nuts with certain combinations, which made you think strategically about which
plants to pick... ALL that is gone now. No more strategising. No more fun"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=1424178757/sortby=mosthelpful/json).

**Real money: the SPARKFUL subscription.** GB in-app purchases list Monthly at £3.99, £4.99 and
£7.99 tiers, Biannual £38.99 and Annual £69.99 (store listing). It unlocks "50+ exclusive
plants, plus a monthly limited edition plant", a plant widget with seven reminder options, five
daily challenge rewards and custom plant names (https://sparkful.app/plant-nanny). The listing
also claims "Subscribers are 2.4x better at sticking with their goals!" (store listing).

Reception is the worst in the lane on price. "I like this app, and started off using the free
version, which was great, but then it gets far too samey... So then I went to subscribe — £70 per
year!! That's ridiculous for what it is" (review feed). "£7 pounds a month is a little
ridiculous" (same).

#### 5. Stakes, risk and chance

No betting, no risk. Randomness is in the **creatures**: "mysterious new creatures" visit, and
they appear "when the tree hole is filled with three plants and the greenhouse is obtained",
with a help article specifically on "Why same creatures appear" and another on "Growing shiny
plants" (help centre, above; store listing). There is a monthly limited-edition plant for
subscribers and achievement medals (https://sparkful.app/plant-nanny).

#### 6. Progression

Three nested loops. Within a plant: levels rise with watering until **max level**. Then: "When
it reaches max level, move it to a Treehole in your Greenhouse, choose a new plant, and start
over" — a **harvest**. Then: fill a tree hole with three plants to earn the greenhouse and
attract creatures; collect across 50+ plants and three difficulty tiers; earn medals
(mobilesyrup, above; help centre, above; store listing).

The harvest is the milestone, and it is the cleanest progression structure in the lane: grow,
complete, retire to a collection, start the next one. Finishing a plant does not end the game,
it starts the next plant and permanently enlarges the display.

Its weakness is content supply: "I had completed all the free plants within a month or so" and
"once you use 6 plants there are no new varieties you can get and eventually because of this
the motivation starts to wear off" (review feed).

#### 7. Social

Minimal. Clovers can be earned by "clicking buddies" (help centre, above), implying a light
friend list, but there are no leaderboards, visiting or co-op in the listing or help centre.
**Not confirmed** that any meaningful social layer exists.

#### 8. Freedom and identity

Choose each plant (by species and by difficulty tier), **name it** (custom names are a
subscriber feature), choose its pot, and even "edit plant personalities and dialogues" (help
centre, above). Decorate the greenhouse. Set glass size and daily target.

#### 9. Signature interaction

**Press and hold the water button and watch the water pour into the pot** — a physical,
duration-based gesture rather than a tap, which makes the act of logging feel like the act of
watering. One reviewer wants it finer still: "i would much prefer holding down the drink button
then letting it go and it doesnt count as one cup unless you have actually drunk one cup"
(review feed).

#### 10. UI type and art

**Creature in a room** — effectively a single plant in a pot in a framed scene, sparse, with the
water button and the day's cup count. Art is bright, chunky, big-eyed cartoon with faces on the
plants; the original used a window with changeable scenery, which some prefer: "I prefer the
style and look of the first version and find the plants cuter, and prefer the window background
with scenery that can be changed" (review feed). The greenhouse is a second, denser scene.

The home screen's problem is advertising, not density: "Every time you open the app or log a
drink you get ads popping up... There are ads posted all over the app" (review feed).

#### 11. Sound and feel

Confirmed and loved. "the art is great, the plants are cute, **the sounds and music are
endearing**" and "I really like that there is a song playing in the background <3" (review
feed). Plants have per-plant dialogue and personalities (help centre, above), and animate
between lively and wilted states. Haptics: **not confirmed**.

#### 12. Scale and reception

- iOS GB: **4.70**, **10,392** ratings (lookup, 27 Oct 2026). Note one reviewer flags
  rating-for-reward prompting: "Not sure how it is but this seems like corruption: give it 5
  stars and you get rewards..." (review feed) — treat the average with that in mind.
- Play: **5m+** downloads
  (https://play.google.com/store/apps/details?id=com.fourdesire.plantnanny2).
- Plant Nanny 2 released 17 January 2019 (the original was 2013). Developer: **SPARKFUL INC.**
  (formerly Fourdesire). Free with ads, a clover currency purchasable for cash, and the
  SPARKFUL subscription (lookup; https://en.wikipedia.org/wiki/Plant_Nanny).

**Three complaints**

1. Subscription price against a thin free tier. "£70 per year!! That's ridiculous for what it
   is... So instead I downloaded Waterllama for £10 lifetime fee"
   (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=1424178757/sortby=mosthelpful/json).
2. Growth too slow to feel like a reward. "The issue is the low reward, it takes forever to get
   your plant to grow and there's no sense of reward / accomplishment with that then so it
   quickly becomes boring and I had to delete it" (same feed).
3. An update removed the one strategic choice. The seeds/nuts system that rewarded picking
   complementary plants for a tree hole was cut: "No more strategising. No more fun. It's
   pretty aimless" (same feed).

**Three things people love**

1. Caring for something else is the motivator. "if I feel like I have to do something to 'look
   after' someone/something else (even if it's not a real thing) I'm more likely to do it than
   if it's just for myself" (review feed).
2. It changes behaviour fast. "This app is perfect because people with adhd are motivated by
   the entertainment... I wasn't drinking AT ALL and because of this app I reached 2L per day in
   only two weeks" (review feed).
3. The craft — art, plants, music. "the art is great, the plants are cute, the sounds and music
   are endearing" (review feed).

#### 13. Lesson for RepGarden

This is the closest model to copy. Take the **three-loop progression**: grow one vegetable to
maturity, harvest it into a permanent collection, start the next — so completion is both a
milestone and a reset, and the collection is the long-run display. Take the **wilt that cannot
kill**, where recovery costs exactly one unit of the ordinary action; a vegetable that droops
after a missed week and perks up on the next logged set is honest, legible and unpunishing. And
take the press-and-hold gesture: making the log feel like the care.

Three things to avoid. Content starvation: Plant Nanny's free users run out of plants in a month
and leave, so RepGarden needs enough vegetables, or enough procedural variation, to outlast a
client's first season. Growth too slow to register: a plant that visibly moves only twice a day
is not a reward, and in a gym the client needs to see the needle move on the session they just
did. And never cut a mechanic that gave players something to think about — the nuts-and-
combinations removal cost Plant Nanny its most engaged users.

---

### 5. Habitica: Gamified Taskmanager

#### 1. Unit of play

An **RPG avatar** with HP, XP, level, gold, mana, gear, pets and mounts. The real action is
checking off one of three task types: a **Daily** (scheduled, punishing), a **Habit** (positive
or negative, repeatable, unpunishing) or a **To Do**. "When you do something in real life, check
it off in the app and receive gold, experience, and items that can be used in-game!"
(https://apps.apple.com/gb/app/habitica-gamified-taskmanager/id994882113).

There is no plant and no creature you tend — the thing that grows is *you*, as a character
sheet. That abstraction is exactly what reviewers complain about: "Your avatar is a bit avatar...
Even on a larger phone the avatar size is a stamp"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=994882113/sortby=mostrecent/json).

#### 2. Session shape

A checklist, morning and night. The daily rollover is a named event, **Cron**, with a "Record
Yesterday's Activities" screen and a "Start My New Day" button
(https://habitica.fandom.com/wiki/Rest_in_the_Inn). Ten seconds is enough to tick a Daily.
Everything else — party chat, quests, equipment, stat allocation, challenges, the market — is
sit-down work, and there is a lot of it.

#### 3. Absence — the punishment model, in full

This is the lane's cautionary case and the detail is worth having exactly.

- Max HP is **50 and cannot be raised**, at any level
  (https://habitica.fandom.com/wiki/Health_Points).
- A missed Daily costs HP at **2 (easy), 3 (medium) or 4 (hard)** base damage, reduced by the
  Constitution stat (same).
- Damage **escalates with neglect**: each miss reddens the task, and "Damage is lower when the
  task is closer to blue, while a redder task will increase damage" (same). So the longer you
  are away, the harder each individual miss hits.
- At **0 HP you die**: "losing one level, all of their gold, and one piece of equipment" (same).
- Damage also arrives **from other people**: on a boss quest you take damage "whenever a player
  or *any* of their party members fails to complete one or more Dailies", which "means that a
  player may take damage at seemingly random times of the day depending on when a party member
  logs in" (https://habitica.fandom.com/wiki/Damage_to_Player).

Protections exist and are substantial, but they are all opt-in and buried:

- **Pause Damage** (historically "Rest in the Inn"): "Missed Dailies won't damage you; Bosses
  won't do damage for your missed Dailies... **Players will not lose any health or streaks** for
  Dailies that they do not complete", while you still earn for anything you do complete
  (https://habitica.fandom.com/wiki/Rest_in_the_Inn).
- **Record Yesterday's Activities** lets you tick yesterday's Dailies before the day turns —
  "it always gives you the chance to tick them off the next day..." (GB review feed).
- **Checklists subdivide the penalty**: "a checklist that is three-quarters complete will deal
  only a quarter as much damage as a Daily with no checklist items checked off"
  (https://habitica.fandom.com/wiki/Damage_to_Player).
- Health potions (25 gold for 15 HP), levelling up (full heal), Healer skills, Rogue Stealth,
  and a "Fix Character Values" button for unfair loss
  (https://habitica.fandom.com/wiki/Health_Points).

**What users say the punishment does to retention.** The evidence is direct and consistent:

> "Logically I know my character taking damage is just a game mechanic. **Emotionally it lands
> like real failure** for some reason and once I'm in that headspace I just stop opening the app
> entirely for like weeks at a time. **I've come back to habitica probably 5 times at this
> point.** Each time I lose my streaks and have to rebuild dailies from zero which honestly
> makes me want to just delete and start fresh... I just keep falling into this guilt loop where
> missing 1 day makes me feel so bad about the character that I avoid the app for a month,
> which obviously makes everything worse"
> (https://www.reddit.com/r/habitica/comments/1sl35qk/longtime_habitica_players_how_do_you_handle_the/)

> "Decent but health running out v demotivating... the app zeroed my health even though I was
> logging on to register something positive — I don't appreciate how this wipes off all your
> progress (all coins gone...) it is quite demotivating"
> (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=994882113/sortby=mostrecent/json)

> "Buggy as hell... dailies not resetting, health going down despite ticking everything off. Had
> to uninstall as **was actually demotivating**" (same feed)

There is a counter-current, which matters for an honest reading: some players want *more*
consequence. "Been using Habitica for a while... I noticed I can skip a few days and come back
without much impact... what if your stats actually rusted or decayed when you stopped showing up?
... The fear of losing progress is way more motivating than the reward of gaining it. Curious
what the community thinks. Would you want something like that in Habitica, or is the current
system better because it's more forgiving?"
(https://www.reddit.com/r/habitica/comments/1secb6b/does_anyone_else_wish_habits_had_real/, 12
upvotes, 20 comments). And a thread in the same subreddit pushes back on streaks generally:
"Every app is adding streaks — and it feels like a psychological attack... You don't want to lose
the streak, so you open the app — not because you need it, but because your brain feels
pressure"
(https://www.reddit.com/r/habitica/comments/1qqcfvw/every_app_is_adding_streaks_and_it_feels_like_a/,
43 upvotes, 25 comments).

So the community is split between "punishment made me quit" and "I want real stakes" — and the
people who quit are the ones who are not posting any more.

**The rest-day problem, stated by users almost verbatim for RepGarden:**

> "I would also like to be able to differentiate between weekday and weekend tasks as **my
> avatar lost health when I didn't work on work projects on the weekends**... At least set what
> days the task is relevant to for non 9-5ers." (GB review feed)

> "Main issue is you can set a task to be completed once a day, once a week or once a month only
> — nothing in between. **How about if I want to visit the gym twice a week?**" (GB review feed)

> "No truly weekly tasks... There are dailies, which you can set to be grey or to only repeat every
> week, but the tick box unchecks itself every day regardless. You could also set them to be
> habits but **then there's no penalty for missing them. This is a deal breaker for me.**" (GB
> review feed)

Habitica does support per-weekday Daily scheduling (the store listing advertises "Automatically
repeating tasks scheduled for your daily, weekly, or monthly routines"), but enough users
cannot find or make it work for a two-to-five-times-a-week pattern that they leave over it.

#### 4. Currency and endogenous value

**Gold**, earned by completing anything, spent on equipment, health potions, quest scrolls and
user-defined custom rewards. **XP** levels the character. **Mana** powers class skills. **Gems**
are the premium currency, bought with cash or earned slowly, spending on quests, pets, cosmetics
and the Fortify Potion (4 gems) and Orb of Rebirth (6 gems)
(https://habitica.fandom.com/wiki/Health_Points,
https://habitica.fandom.com/wiki/Damage_to_Player, store listing).

Spending feeds back strongly: gear raises stats, which reduce the damage you take and increase
boss damage. Levelling up fully restores HP, so progress literally heals you. That is a real
endogenous economy — and it is also what makes the system too big to learn.

**Real money:** free and open source, funded by gem purchases and an optional subscription. "It
is surprisingly free" (GB review feed). But: "recently the bugs and content you must constantly
pay for has really irked me... All I ever see in their news is pushing out more content for people
to purchase" (same feed).

#### 5. Stakes, risk and chance

The highest-stakes design in the lane, and most of it is not chosen. Negative Habits cost HP on
each click. Boss quests make your misses damage your friends and theirs damage you. Death costs
a level, all gold and a piece of equipment. Randomness: item **drops** from completing tasks,
quest-scroll drops, pet eggs and hatching potions, seasonal events and grand challenges
(store listing; https://habitica.fandom.com/wiki/Health_Points).

#### 6. Progression

Levels (unbounded), classes unlocked at level 10 (Warrior, Mage, Healer, Rogue), stat point
allocation, gear tiers, pets and mounts collections, quest chains with bosses and collection
quests, seasonal events, and Challenges with shared task lists (store listing;
https://habitica.fandom.com/wiki/Health_Points).

It flattens: "once i've got to a higher level, getting exp and levelling up doesn't feel as
rewarding as its sort of become routine and levels don't really mean as much when you've already
levelled up many times. And bosses [aren't] that challenging when you complete all dailies" (GB
review feed).

#### 7. Social

Opt-in but consequential. **Parties** for accountability and boss quests — where your missed
Dailies damage your party-mates, the strongest social obligation in the lane. **Challenges** are
shared task lists you adopt into your own list. **Guilds and the Tavern were removed on 8 August
2023** (https://habitica.fandom.com/wiki/Rest_in_the_Inn), which users still mourn: "Please
bring back tavern" (GB review feed). Reviews like the competition: "I love how you can form a
group, and it started some competition between us" (same feed).

#### 8. Freedom and identity

The most task freedom and the most avatar freedom. Fully user-written Habits, Dailies and To Dos
with per-task difficulty, colour-coded value, tags, checklists and reminders. "Inclusive avatar
customizations: wheelchairs, hair styles, skin tones, and more", collectable gear, pets and
mounts, custom colour themes with dark mode, and user-defined real-life rewards bought with gold
(store listing). Users invent their own organisation systems on top — emoji prefixes, tag
schemes (https://www.reddit.com/r/habitica/comments/nfjp3j/heres_my_take_on_organizing_tasks_on_habitica/,
194 upvotes).

#### 9. Signature interaction

**Opening the app the next morning and seeing the red damage notification for what you did not
do.** The "Start My New Day" / Record Yesterday's Activities screen at Cron is the moment that
defines Habitica — the daily reckoning.

#### 10. UI type and art

**Minimal stat/figure.** A header with HP, XP and mana bars beside a small pixel-art avatar,
over four tabbed lists of tasks. Retro 16-bit pixel art for gear, pets and bosses. Dense: it is
a task manager with an RPG header, and both halves are busy. "It's quite difficult to use and
navigate, but if you get used to it; it becomes easy"; "it's a tiny bit complicated with lots of
extras in the menu" (GB review feed).

#### 11. Sound and feel

Weak, and users say so. "there could be more satisfying features like animations, and it is
generally quite static"; "i want more gamification in it. also some animation would be great!"
(GB review feed). Damage and level-up produce corner notifications rather than a scene. Sound
and haptics: **not confirmed**.

#### 12. Scale and reception

- iOS GB: **4.04**, **378** ratings (lookup, 27 Oct 2026) — by far the lowest rating and the
  smallest GB count in the lane, despite being the oldest and best known.
- Play: **5m+** downloads
  (https://play.google.com/store/apps/details?id=com.habitrpg.android.habitica).
- iOS release 7 July 2015. Developer: **HabitRPG, Inc.** Free and open source, funded by gems
  and an optional subscription (lookup; store listing).

**Three complaints** (beyond the punishment evidence in section 3)

1. Bugs that cause *unearned* punishment, which is far worse than punishment. "dailies not
   resetting, health going down despite ticking everything off. Had to uninstall as was actually
   demotivating"; "Why do I sometimes get my health lowered when competing tasks?"
   (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=994882113/sortby=mostrecent/json;
   https://www.reddit.com/r/habitica/comments/1x1dfze/why_do_i_sometimes_get_my_health_lowered_when/).
2. Scheduling cannot express a real routine (section 3) — the gym-twice-a-week complaint is the
   exact shape of RepGarden's constraint.
3. The reward layer looks and feels cheap. "Works ok but the graphics for the rewards are
   literally appalling. Your avatar is a bit avatar, you can win pets etc by doing the goals but
   why would you want to?" (GB review feed).

**Three things people love**

1. It reaches people other trackers do not. "I'm one of those people who bounced off every
   regular habit tracker out there but somehow seeing my character get gear and level up
   actually keeps me coming back. The rpg thing genuinely works for me when nothing else does"
   (https://www.reddit.com/r/habitica/comments/1sl35qk/longtime_habitica_players_how_do_you_handle_the/);
   "Incredible motivator for ADHDers such as myself" (GB review feed).
2. Group accountability. "I love how you can form a group, and it started some competition
   between us" (GB review feed).
3. The forgiveness features, when found. "Sometimes I forget to check in and tick off my
   Dailies, but **it always gives you the chance to tick them off the next day...**"; "I
   appreciate the ability to tick off yesterday's tasks as sometimes I forgot or fall asleep"
   (GB review feed).

#### 13. Lesson for RepGarden

Habitica is the design RepGarden must not be. HP loss for missed Dailies, escalating damage for
longer absences, and death that wipes gold and a level produce a documented churn pattern: a
miss reads as real failure, the client avoids the app for weeks, and they return from zero or
not at all — "I've come back to habitica probably 5 times." Combine that with a scheduler that
cannot express "the gym twice a week" and you have exactly the failure mode a trainer-prescribed
2-5 sessions a week would hit. Nothing in RepGarden should take anything away for a session not
done.

Two things are worth stealing. **Record Yesterday's Activities** — a one-tap way to log
retrospectively, repeatedly named as a favourite feature — fits a client who finished training
and forgot to log until the evening. And the **checklist that subdivides the penalty**, where a
part-finished item counts proportionally, is the right shape for a part-finished workout: credit
what was done rather than scoring the whole session pass or fail.

---

### 6. Focus Friend, by Hank Green

#### 1. Unit of play

A **bean** in a room, which knits while you focus. "Set a focus timer, your bean starts knitting
socks while you focus on your tasks" (https://focusfriend.me/). The output of the real action is
**socks** — the currency — which buy furniture for the bean's room. "Complete your focus session
successfully, and your bean will reward you with socks that you can trade for beautiful
furniture to decorate its bean's room" (same).

The design decision worth noting: the bean is not the thing that grows. The **room** is. The
creature is the reason you care, the room is the record.

#### 2. Session shape

A single focus block with Pomodoro breaks, and the breaks are where the game lives:
"Take productive breaks between focus sessions. **Decorate your bean's room during break
time!**" (https://focusfriend.me/). So the glance screen and the sit-down screen are
deliberately separate activities at separate times — focus is passive, decorating is active.
A **Live Activity** shows the bean's progress on the lock screen, so you can check without
opening anything (same).

A reviewer describes the loop precisely: "I like starting a writing session scoping out what
furniture I want to buy and then seeing if I can do enough writing to earn it. It's a nice come
down after a day of writing to buy things with what I've earned"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=6742278016/sortby=mostrecent/json).

#### 3. Absence

There is **no decay, no wither, no streak and no between-session penalty** — the most restrained
absence model in the lane alongside Brainrot. The only consequence is emotional and in-session:
"If you interrupt your Bean by turning off the timer, they'll be **really really sad**"
(https://apps.apple.com/gb/app/focus-friend-by-hank-green/id6742278016), and "your bean drops its
stitches and becomes really, really sad" (https://focusfriend.me/).

That is the whole punishment: a sad bean, for a few seconds, for a session you chose to abandon.
Nothing is deleted, no counter resets, nothing is owed. No review in the GB feed complains about
the penalty — the complaints are all about running out of things to buy.

#### 4. Currency and endogenous value

- **Socks**, earned by completed focus sessions, spent on "hundreds of decorations" across
  multiple rooms — bedroom, bathroom, garden and a street view, in themes including "lo fi and
  greenhouse" (https://focusfriend.me/, store listing).
- **Scarves**, a second tier tied to the paid plan, which buy the best decorations (store
  listing; review feed).

Spending is purely cosmetic — it does not make focusing easier or sessions more productive. But
because the room is the only progress display, cosmetic *is* the progression here, which is why
running out of it is fatal (section 12).

**Real money:** free, with Focus Friend Pro at £3.99/month, £19.99/year or £39.99 lifetime, and
paid bean skins (Blue Jello Bean £2.99, Base Bean Pack £3.99, Kitt-ney Bean £4.99, Jelly Bean
Pack £5.99) (https://apps.apple.com/gb/app/focus-friend-by-hank-green/id6742278016). No ads —
which users single out: "It's easy to use, has a simple interface & **doesn't have ads which is
a rarity nowadays**" (review feed).

The paywall placement is the main grievance: "I think you need to be able to get scarves without
paying £30. All the good decorations require scarves"; and app-blocking is behind it too — "in
deep focus mode it blocks virtually every app including Spotify... the ability to allow certain
apps is behind a paywall" (review feed).

#### 5. Stakes, risk and chance

Almost none, by design. No bet, no risk of loss, no randomness in the GB listing or on the site.
The only stake is the bean's feelings. Deep Focus Mode is the one opt-in hardening: "Lock
distracting apps during focus sessions" via iOS Screen Time (https://focusfriend.me/).

#### 6. Progression

Decoration catalogue completion, room by room. Rooms were added after launch to extend it, and
completion is visibly reachable: "I have finished the whole inside of the houses and I have now
started decorating the outside, since I am going to finish everything quite soon, **can you pls
add some other things for me to get?**" (review feed). There are no levels, seasons or
evolutions. Google Play named it **App of the Year 2025**
(https://techcrunch.com/2025/11/18/hank-greens-focus-friend-is-google-plays-app-of-the-year).

#### 7. Social

**None.** Neither the site nor the store listing mentions friends, visiting, leaderboards or
co-op. The one social-adjacent thing is cosmetic: you can dress your bean as Hank or John Green
(store listing). This is a deliberate omission in the most successful launch in the lane.

#### 8. Freedom and identity

Bean skin (several free, several paid), room decoration across multiple rooms and themes, session
tags. The bean has a name — users call it Alby — and reviewers want it to do more: "I kind of
wish that Alby could do some actions like for example they could actually sit on a chair or
something" (review feed).

#### 9. Signature interaction

**Starting a timer and watching a bean knit.** It is passive, ambient and visible on the lock
screen through a Live Activity — the companion works while you work, and the needles stopping is
the failure signal. The paired moment is spending socks on furniture during a break.

#### 10. UI type and art

**Creature in a room**, sparse, one scene. A bean in a decorated room with the timer; the room
fills in over weeks. Soft, flat, cosy cartoon with a legume as the protagonist — closer to a
cosy game than a productivity app, and widely described that way. Lo-fi music plays: "The music
helps my brain stay focused for as long as it plays" (review feed).

#### 11. Sound and feel

Lo-fi music during sessions (review feed), the knitting animation, the bean's sad animation on
interruption, and a Live Activity that animates on the lock screen (https://focusfriend.me/).
Haptics: **not confirmed**.

#### 12. Scale and reception

- iOS GB: **4.75**, **733** ratings (lookup, 27 Oct 2026) — small GB base for a US phenomenon.
- Play: **1m+** downloads
  (https://play.google.com/store/apps/details?id=com.underthing.focus.friend).
- Released 23 July 2025 (soft launch "in late July"), US launch 17 August 2025. Developer:
  **B-Tech Consulting Group LLC**, built by **Hank Green with Bria Sullivan**, founder of mobile
  game studio Honey B Games. "The top free app in Apple's App Store... After soft-launching in late
  July, the app has risen all the way to the top of the App Store in the U.S., Australia, Canada,
  Ireland, and New Zealand, **amassing 740,000 downloads**"
  (https://www.fastcompany.com/91388304/focus-friend-app-store-hank-green-bria-sullivan). It went
  on to win **Google Play App of the Year 2025**
  (https://techcrunch.com/2025/11/18/hank-greens-focus-friend-is-google-plays-app-of-the-year).
  Free with Pro subscription and paid skins. The app carries no ads (review feed; the GB listing
  shows in-app purchases only) — reported as a deliberate choice by Green, **not confirmed** from
  a directly quotable primary source.

**Three complaints**

1. **Content exhaustion — the number one complaint.** "After a few days you have enough to buy
   whatever you want for your room, and even with the additional paid options, after that point
   it just becomes any other timer. Which is fine, it's a cute timer, but **the actual novelty
   wears off very quickly when you have nothing left to work towards**"
   (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=6742278016/sortby=mosthelpful/json).
   Also: "Makes me feel sad that bean only has one room... I need an objective to stay focussed on
   cutting down my screen time but this was short lived"; "Quickly a little stale" (same feed).
2. The paywall sits on the features that make it work. "having to pay to select which apps it
   restricts is a bit counterintuitive. Deleted after an hour or so since it wasn't even blocking
   TikTok (the whole reason I downloaded it)"; "the paywall to unlock the non hidden features
   (scarfs) is really sucky" (same feed).
3. Crashes losing the session's reward. "it crashes after every countdown ends and it does not
   save whatever bean has knitted"; "i finish a focus session and get nothing cus it crashes"
   (same feed).

**Three things people love**

1. It gets ADHD users started. "As an ADHDer this has made it 10x easier to just get started
   with what I need to do" and "I have ADHD and this has helped me so much!... and I get to
   decorate a super cute house"
   (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=6742278016/sortby=mostrecent/json).
2. Earning the decoration. "I love being able to 'earn' socks so I can decorate various rooms
   for my bean. It motivates me to put my phone away on focus mode more frequently" (same feed).
3. The companionship, and the restraint. "It's like having a cute work buddy"; "simple interface
   & doesn't have ads which is a rarity nowadays" (same feed).

#### 13. Lesson for RepGarden

Focus Friend shows that **a sad companion is enough**. No streak, no decay, no leaderboard, no
social layer, nothing taken away — and it reached number one in five countries and won Google
Play's App of the Year. For RepGarden, that licenses the gentlest possible absence model: the
vegetable does not have to die or wither, it is enough that it is visibly waiting. Steal the
split rhythm too: the game is passive while the client trains and active in a decorating moment
afterwards, which is exactly the glance-then-sit-down shape a gym demands.

The thing to avoid is its one real failure: a **finite cosmetic catalogue is a retention cliff**.
Users emptied the shop in days, and the app's only progression display stopped moving. RepGarden
must make the spend loop renewable — new vegetables, seasons, plot expansion, variations that
depend on what the client actually trained — rather than a fixed catalogue they will finish.
And do not put the mechanic that makes the app work behind a paywall, which in a free trainer's
app means: nothing the training loop needs is ever gated.

---

### 7. Brainrot: Screen Time Control

#### 1. Unit of play

A **brain avatar** with a health percentage that decays as you use your phone. "Pick the apps
and sites to block, set schedules, and **watch your cute brain avatar decay as you doom scroll.
The visual nudge helps you put the phone down**"
(https://apps.apple.com/gb/app/brainrot-screen-time-control/id6744338972). "Brain health" is
calculated from "your screen time compared to your set goal"; exceeding the target lowers the
score (https://thebrainrotapp.com/faq.html).

The inversion is the whole design: everywhere else in the lane the real action *grows*
something; here the real action *rots* something. There is exactly one object and one number.

#### 2. Session shape

The app is mostly not a session at all — it runs in the background off the Screen Time API and
surfaces as a widget and a brain. The interaction that matters is an **interception**: before you
open a blocked app you "have a chat with my brain", which "triggers reflection on necessity"
(review quoted on the store listing). One reviewer: "on down time knowing id need to 'have a chat
with my brain' means im already reaching for my phone less and less... **This really triggers a
thought on whether you actually need to use an app or not.** It's more than just 'put in a
passcode to enter app'"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=6744338972/sortby=mostrecent/json).

Sit-down screens: a weekly screen-time report, daily "Brain Rot" bar charts, and "Weekly
Offenders" (https://mwm.ai/apps/brainrot-screen-time-control/6744338972,
https://thebrainrotapp.com/faq.html).

#### 3. Absence

Inverted. Absence from your *phone* is the win; absence from the *app* does nothing at all. There
is no streak, no wither, no penalty for not opening it — the FAQ documents no streak feature
(https://thebrainrotapp.com/faq.html).

Decay and recovery are both continuous and symmetric: "Your brain avatar in the app **visually
heals** as you reduce usage, providing motivation to continue your digital detox journey", and
detox sessions show "a regenerating brain avatar and a clear countdown timer"
(https://thebrainrotapp.com/faq.html,
https://mwm.ai/apps/brainrot-screen-time-control/6744338972). Recovery needs no currency, no
repair item and no apology — just better behaviour, immediately reflected.

The emotional threshold is low and that is the point: "the little cartoon brain is so cute and
it's SO SAD when [it] start[s] to look sad when he even gets to 80%" (review quoted on
https://apps.apple.com/gb/app/brainrot-screen-time-control/id6744338972). The avatar reacts at a
20% deviation, not at failure.

But the same mechanic draws the lane's sharpest criticism of guilt as a design material: "Beware:
Design for people with no self control. **This app does not have any accommodation for any
positive behavioural inputs.** It is designed to have you make declarations with every prompt and
question that you ar rotting your brain... even when I told It I only spend 1 hour a day on a
screen... it still only gave me options that say I have bad sleep, doom scrolling implications,
procrastination and misfocus... **be careful not to be mislead to think that you are damaged
goods**"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=6744338972/sortby=mosthelpful/json).

#### 4. Currency and endogenous value

**There is none.** No coins, no shop, no collection, no cosmetic economy earned by behaviour. The
only unlockables are paid: "new illustrations, animations, unlockable themes and app icons" in
the version notes (store listing). The brain's health *is* the score, the reward and the display,
all at once.

**Real money:** subscription-only and hard-gated. Published prices: "Monthly subscription for
$3.99, and yearly subscriptions ranging from $9.99 to $49.99"
(https://thebrainrotapp.com/faq.html); GB in-app purchases list Weekly £3.99-£4.99, Monthly
£8.99, Yearly £19.99-£49.99 (store listing). The listing states plainly: "*All features described
above require a subscription.*" (store listing).

This is the single most-criticised thing about any app in the lane — see section 12.

#### 5. Stakes, risk and chance

No bet, no chance, no drops, no weather, no visitors. The only stake is the brain's visible
condition, and it is continuous rather than binary — unlike Forest's tree, there is no moment of
death, just a slide.

#### 6. Progression

Almost none, and deliberately. Brain health is a dial, not a ladder: it can go back down. The
only accumulating record is the weekly report and the daily bar chart
(https://mwm.ai/apps/brainrot-screen-time-control/6744338972). Paid themes and app icons are the
only unlock track (store listing). Nothing marks a milestone.

#### 7. Social

**None documented.** "No social or sharing capabilities are documented"
(https://thebrainrotapp.com/faq.html).

#### 8. Freedom and identity

Thin: choose which apps and sites to block, set daily allowances, block whole categories, set
schedules for bedtime, mornings and meetings, and set the screen-time goal the brain is scored
against (https://thebrainrotapp.com/faq.html). Paid themes and icons. The brain is not named,
customised or dressed.

#### 9. Signature interaction

**The brain getting visibly sicker on your home-screen widget as the day goes on** — and the
"chat with my brain" gate you have to pass before opening a blocked app, which is a reflection
prompt rather than a passcode.

#### 10. UI type and art

**Minimal stat/figure** — arguably the most restrained screen in the lane. A single cartoon brain
with a health percentage, and a bar chart underneath. Simple, friendly, expressive 2D character
art; the whole proposition is one character and one number. App size is 134MB against Forest's
869MB and Flora's 697MB (store listings), which is itself a measure of how little is there.

#### 11. Sound and feel

The brain's facial states are the feedback — it "cries or gets sick if you try to by pass it"
(https://itunes.apple.com/gb/rss/customerreviews/page=1/id=6744338972/sortby=mostrecent/json);
illustrations and animations are listed in the version notes (store listing). Sound and haptics:
**not confirmed**.

#### 12. Scale and reception

- iOS GB: **4.37**, **2,573** ratings (lookup, 27 Oct 2026) — the lowest-rated app in the lane
  bar Habitica, and the reviews explain exactly why.
- Play: **not confirmed.** No Smolworks listing was found in a GB Play search for "Brainrot
  Smolworks screen time"; the Brainrot-named Android apps belong to other developers. A
  third-party aggregator claims "1M+ downloads" without naming a store
  (https://mwm.ai/apps/brainrot-screen-time-control/6744338972) — treat as unverified. Appears
  to be iOS-only.
- Released 20 May 2025. Developer: **Smolworks Inc**. Subscription-only; all features require a
  subscription (lookup; store listing).
- Monitoring runs entirely on-device via Apple's Screen Time API: "all monitoring and blocking
  run *entirely* on your device. Your browsing data never leaves your phone" (store listing).

**Three complaints**

1. **The hard paywall after a guilt-trip onboarding** — the overwhelming majority of critical
   reviews. "The app asks questions about your day-to-day screen time and **guilt trips you with
   how much time you're wasting on your phone. Then you have to pay to actually even use the app
   as you can't get past the paywall.** So essentially, it's deceiving, not free and actively
   makes u spend more time on your screen by downloading it"
   (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=6744338972/sortby=mostrecent/json).
   And: "Everything leads you to feel bad about spending the next 15 years on your phone, and
   without even giving the app a try it leads you STRAIGHT to the transaction. **I feel guilt
   tripped into paying for my addiction**"
   (https://itunes.apple.com/gb/rss/customerreviews/page=1/id=6744338972/sortby=mosthelpful/json).
2. The blocking is unreliable, so the brain's number is fiction. "my brain health always stays at
   99 even when i use apps for an hour+"; "The app does not work automatically. Every day I have
   to open the app and check it manually, only then the limits start working... **Now my brain
   already know this workaround, so I keep scrolling all day**" (same feeds).
3. Review prompting during onboarding, before the app has been used. "As you're setting up the
   app, you're prompted to leave a review several times (which seems pushy as you've not even set
   up the app yet let alone experienced it)"; "it then asks for a REVIEW?! You literally haven't
   used the app yet" (same feeds). One reviewer: "Other reviews are bots. Data is fake."

**Three things people love**

1. The avatar does the work a number cannot. "as a visual person I love the little brain that
   makes me question the value of what I'm doing on my phone. It delays the automatic doom
   scrolling tendencies by asking you questions. The little brain cries or gets sick if you try
   to by pass it" (review feed).
2. The reflection gate. "knowing id need to 'have a chat with my brain' means im already reaching
   for my phone less and less... more than just 'put in a passcode to enter app'" (review feed).
3. It is simple and it works. "It keeps me off my phone so much... and I like the little brain
   character"; "It's getting me on the right track so far" (review feed).

#### 13. Lesson for RepGarden

Brainrot earns its place as Ahmed's example of restraint: **one character, one number, one
screen, no currency, no shop, no streak, no social, no progression ladder** — and a 4.37 rating
whose complaints are all about money and reliability, never about the game. It demonstrates that
a continuously-reactive avatar with a *symmetric* decay-and-heal dial needs no economy at all, and
that an avatar reacting at a 20% deviation rather than at outright failure is enough to change
behaviour. A vegetable whose condition tracks sessions-done-against-sessions-planned, visible on
the home screen, needs nothing bolted to it to mean something.

Two cautions. First, with no currency and no progression there is **nothing to come back for**
once the habit is formed — Brainrot has the lane's thinnest long game, and RepGarden needs the
client in the app for months. Second, guilt as the only material is dangerous: Brainrot's
onboarding tells people they are "damaged goods" and the reviews turn on it. A trainer's clients
are already paying someone to tell them what they are not doing; the vegetable should show the
state of play, not pass judgement on it.

---

### Across the lane

- **Nothing in the lane punishes absence, and the one app that does has the worst rating.**
  Finch, Forest, Flora, Plant Nanny, Focus Friend and Brainrot all impose zero cost for a day,
  a week or a month away. Habitica — the only app with real penalties — sits at 4.04 in GB
  against 4.37-4.93 for the rest, and its users describe a documented churn loop: "missing 1 day
  makes me feel so bad about the character that I avoid the app for a month" (Habitica, 3).

- **Penalties work when the player chose the stake and the app is certain of the facts; they
  backfire when either is missing.** Forest's dead tree and Flora's killed plant are accepted —
  the user set the timer and knows what they did — and Flora even makes its cash stake
  self-reported ("Honor My Price"). But Flora's rating is dragged down almost entirely by *false*
  kills, and Habitica's angriest reviews are about HP lost "despite ticking everything off".
  Asserting a failure the user knows did not happen costs more than the penalty ever gained.
  (Forest 3/5, Flora 5/12, Habitica 12.)

- **A streak is a separate system from a creature, and it is where the pain is.** Finch refuses
  to punish anywhere except the opt-in check-in streak — and the streak is the subject of its
  most upvoted community complaint and its quitting posts (Finch, 3). Habitica's subreddit has a
  43-upvote thread calling streaks across all apps "a psychological attack". Forest, Focus Friend,
  Plant Nanny and Brainrot have no daily streak at all and are rated 4.37-4.79. (Finch 3,
  Habitica 3, Focus Friend 3, Brainrot 3.)

- **The best absence models make the cost a gap rather than a loss.** Flora's garden "naturally
  shift[s] towards the left over time" leaving a visible empty space; Plant Nanny's plant wilts
  and revives on one glass; Forest keeps the dead stump in the grid as a permanent honest record.
  All three show what happened without taking anything back. (Flora 3, Plant Nanny 3, Forest 3.)

- **Every app that can punish also offers an explicit pause, and the two leaders name it as a
  feature.** Finch's Pause Mode freezes the streak for 1-7 days and also silences widgets,
  notifications and friend pings; Habitica's Pause Damage protects both health and streaks.
  Flora's Pause subtracts paused time from the session instead of killing the tree. Being able to
  declare "I'm away" is table stakes. (Finch 3, Habitica 3, Flora 2.)

- **Progression that counts completed actions survives rest days; progression that counts
  elapsed days does not.** Finch's bird grows on *adventures completed* (7, 22, 42, 67) and its
  energy resets daily, so an untrained day is a zero and not a minus. Plant Nanny levels per
  glass and harvests at max. Habitica's Dailies count calendar days and its users leave over it:
  "How about if I want to visit the gym twice a week?" (Finch 6, Plant Nanny 6, Habitica 3.)

- **The retention cliff in this lane is content exhaustion, not punishment.** Focus Friend's top
  complaint is emptying the furniture shop in days; Plant Nanny's free users finish the plants in
  a month; Habitica's levels stop meaning anything at the top; Brainrot has nothing to collect at
  all. Finch is the outlier that solved it, with 66 micropets, 27 locations, monthly seasonal
  events and quest ladders reaching 10,000 items — and it has the lane's highest rating.
  (Focus Friend 12, Plant Nanny 6, Habitica 6, Brainrot 6, Finch 6.)

- **Currency earned by behaviour and unbuyable with cash is trusted; the moment it is sold, the
  loop is suspected.** Finch states that "Rainbow stones can't be bought" and has no
  member-exclusive items — and the complaints are about subscription price, never about the
  economy. Forest introduced a purchasable Crystal and daily login events in its December 2025
  freemium shift and triggered a petition and five-year users leaving. Plant Nanny sells clovers
  and removed the seed system; Flora's Bits repricing lost it years-long users. (Finch 4,
  Forest 4/12, Plant Nanny 4, Flora 4/12.)

- **Adding game to a utility is the loudest failure mode of all.** The single sharpest review in
  the lane is Forest's: "When your focus app needs you to log in daily and rewards you with
  cosmetics, it is no longer a focus app, it's part of the problem." Users of Forest, Flora and
  Plant Nanny all left over updates that added taps, animations and claim screens to a loop that
  used to be one press. In a gym, between sets, that cost is multiplied. (Forest 12, Flora 12,
  Plant Nanny 12.)

- **Social works when it is encouragement and opt-in; it hurts when it transfers blame.** Finch's
  Tree Town has no leaderboard at all — only Vibes, hugs, gifts and Goal Buddies — and Finch is
  the highest-rated. Flora's co-focus rooms are its main retention hook. Habitica's boss quests
  make your missed Dailies damage your friends, and your friends' misses damage you at
  unpredictable times. Focus Friend has no social layer whatsoever and hit number one in five
  countries. (Finch 7, Flora 7, Habitica 3/7, Focus Friend 7.)

- **The caretaking frame is what people say actually moves them — not the points.** Across four
  apps, reviewers describe the same mechanism in their own words: "if I feel like I have to do
  something to 'look after' someone/something else (even if it's not a real thing) I'm more likely
  to do it than if it's just for myself" (Plant Nanny); "just knowing I would come back to a
  little Birb every day" (Finch); "It's like having a cute work buddy" (Focus Friend); "the little
  brain cries or gets sick" (Brainrot). ADHD and neurodivergence are named explicitly in every
  one of those four review sets. The character is the mechanic.

- **Guilt is a material with a sharp edge.** The two apps that lean on the creature's distress
  hardest draw the lane's most uncomfortable reviews: Slate's writer hit "Finch burnout" in six
  weeks and felt she was "performing wellness rather than actually feeling well", and a Brainrot
  reviewer warns "be careful not to be mislead to think that you are damaged goods". A sad
  companion for a few seconds (Focus Friend) is enough; a companion that tells you it missed you
  is too much. (Finch 12, Brainrot 3, Focus Friend 3.)

---

# Part 3 · Activity games and the baseline

## Lane: real physical activity drives a game world — plus the baseline everyone copies

Collected 27 October 2026. Six apps: Pikmin Bloom, Pokémon GO, Zombies Run!, Walkr, Sweatcoin,
Duolingo. All App Store figures are the GB storefront on 27 October 2026, read from
`https://itunes.apple.com/lookup?id=<id>&country=gb`. Play install bands read from the GB
Play listing the same day.

---

### 1. Pikmin Bloom

App Store id 1556357398. Developer now listed as **Scopely Explore, Inc.**, previously Niantic
under Nintendo licence (https://itunes.apple.com/lookup?id=1556357398&country=gb;
https://en.wikipedia.org/wiki/Pikmin_Bloom).

#### 1. Unit of play

Three things grow at once, all driven by steps. **Seedlings** become Pikmin: a seedling sits in a
slot in the Planter Pack and matures after "either 100, 1,000, 3,000, 5,000, or 10,000" steps, at
which point you pluck it and gain one Pikmin (https://www.pikminwiki.com/Pikmin_Bloom). **Flowers**
are planted on the real map automatically as you walk — "flowers are placed automatically as you
move", and the app keeps planting even when closed, "until the petals are used up or you press the
end button yourself" (https://niantic.helpshift.com/hc/en/23-pikmin-bloom/faq/2855-planting-flowers/).
**Pikmin themselves bloom**: fruit is tapped to distil nectar, nectar is fed to a Pikmin, flowers
open on its head, and tapping those flowers harvests petals, which are the fuel for planting more
flowers (https://www.pikminwiki.com/Pikmin_Bloom). So one real-world action — a walk — maps to
petals spent, flowers laid on the map, seedlings advanced and fruit carried home.

The loop closes on itself: steps -> seedlings/fruit -> nectar -> petals -> flowers -> Big Flowers ->
more fruit. Nothing in it is cosmetic.

#### 2. Session shape

There is a genuine two-speed design. The **glance** is: open, see your squad trailing you on the
map, tap "start flower planting", lock the phone, walk. The reviewer at Nintendo Life describes it
as "more 'pedometer with benefits' than all-encompassing time sink" and notes the app passively
collects while backgrounded (https://www.nintendolife.com/reviews/mobile/pikmin-bloom). Ten seconds
is enough to start planting, pluck a matured seedling, or tap a returned expedition.

The **sit-down** is the nightly Lifelog lookback. "Each day at 9:00pm (or another time the player
sets), the game will try to send a notification"; the lookback counts your steps while your Mii and
Pikmin squad walk a zig-zag path, then invites you to pick a photo from that day's camera roll and
rate the day with a happy, neutral or sad face (https://www.pikminwiki.com/Lifelog). A weekly
lookback follows Sunday's, with a total-steps graph against last week, a places-visited map, flower
planting records and a "Photo of the Week".

#### 3. Absence

No death, no withering of your collection, no streak. The world is explicitly safe: it "consists of
peaceful flower gardens and flowers, devoid of the native creatures that hinder or kill Pikmin — as
well as harsh conditions", combat is "harmless to the Pikmin", and "it's always day on Pikmin
Bloom's map", unlike the console games where Pikmin die at night
(https://www.pikminwiki.com/Pikmin_Bloom).

Three things do expire, and all of them are the *world*, not your progress:
- Planted flowers are "automatically removed after 5 days"; flowers inside a Big Flower's radius
  last until that Big Flower returns to leaf (https://niantic.helpshift.com/hc/en/23-pikmin-bloom/faq/2855-planting-flowers/).
- Most expeditions "expire after 3 days if not collected", though gift expeditions never expire
  (https://www.pikminwiki.com/Expedition).
- A single soft decay exists for over-farming: harvest petals from the same Pikmin six times inside
  two hours and it enters a **withered** state with its flowers gone — and it recovers simply by
  your walking more than 1,800 steps that day (https://www.pikminwiki.com/Pikmin_Bloom).
  This is the one genuinely transferable decay in the lane: the punishment is for milking the
  resource, and the cure is the real-world behaviour the app wants.

What reviews say: the complaints are not about absence, they are about *pressure*. A 211-upvote
post is titled "I didn't open the game in one week and feel much better!" and says: "what has been
a cool, stressless game, that made me go out and walk more and achieve goals at my own pace, became
a really stressful experience, where I had to make missions in set short timeframes, just to get
disappointed with duplicate decor Pikmin… A game should be fun, not stressful."
(https://www.reddit.com/r/PikminBloomApp/comments/1086ge9/i_didnt_open_the_game_in_one_week_and_feel_much/)

#### 4. Currency and endogenous value

Earned: **petals** (from blooming Pikmin), **nectar** (from fruit), **fruit** (from expeditions and
mushrooms), **seedlings**, and **coins**. Petals and nectar feed straight back into the thing you
care about — more petals means a longer flower trail, and you get "one bonus coin" for every 250
flowers planted in a single planting session, capped at 60 coins a day
(https://niantic.helpshift.com/hc/en/23-pikmin-bloom/faq/2855-planting-flowers/).

The real-money layer is coins at £0.99 / £4.99 / £9.99 / £19.99, plus £1.99 storage expansions for
Pikmin, postcards, seedlings, petals and nectar, and a £1.99 Starter Box
(https://apps.apple.com/gb/app/pikmin-bloom/id1556357398). Perception is mixed and tied to events:
a 152-upvote complaint says "I got stuck on 'Plant 1500 white anniversary roses' because no matter
how many mushrooms I did… it refused to give me any after I ran out… And I don't want to use my
coins for flowers I should just be able to get from playing the game!"
(https://www.reddit.com/r/PikminBloomApp/comments/1tk9mxt/i_hate_this_game_sometimes_complaint/)
Lifetime gross was $44 million by April 2024 (https://en.wikipedia.org/wiki/Pikmin_Bloom).

#### 5. Stakes, risk and chance

Almost no risk, plenty of chance. Mushroom battles are the only "combat" and are harmless; up to
30 players can collaborate on one (https://www.pikminwiki.com/Pikmin_Bloom). Randomness carries the
surprise instead: which seedling type you get, which Decor Pikmin a location yields, and which
flower a Big Flower blooms into — in November 2026 Big Flowers "may occasionally bloom into
cyclamens, clematis, marigolds, salvias, thistles, or geraniums" when you plant ordinary petals
around them (https://gonintendo.com/contents/66481-pikmin-bloom-nov-2026-community-days-announced-big-flower-forecast-shared).
Monthly flower rotation also changes combat strength: in November, "Pikmin with geraniums blooming
on their head will be stronger against mushrooms" (same source).

#### 6. Progression

Player **level** gates features — "to go up a level, a defined set of tasks has to be completed",
unlocking features progressively; expeditions unlock at level 3
(https://www.pikminwiki.com/Pikmin_Bloom, https://www.pikminwiki.com/Expedition). Beyond that,
progression is **collection**: "over 150 types of unique Decor Pikmin"
(https://itunes.apple.com/lookup?id=1556357398&country=gb), badges, and the monthly Community Day
badge themed on that month's flower (https://www.pikminwiki.com/Event/Community_Days). The month
itself is the season: a new Flower of the Month and a Big Flower Forecast posted at the end of every
month (https://gonintendo.com/contents/66481-pikmin-bloom-nov-2026-community-days-announced-big-flower-forecast-shared).

#### 7. Social

Opt-in and almost entirely co-operative. Friends, postcards sent between friends, and "Party Walks"
together with no objective (https://www.pikminwiki.com/Pikmin_Bloom). Mushroom battles take up to
30 players. **Weekly Challenges** start every Monday and are the cleanest model in the lane: you
join with up to 4 friends, friends-of-friends, random players, or solo, pick a steps challenge, a
flower-planting challenge or both — and crucially, "reaching the required step goal will get you
some rewards and, if you don't reach it – there are participation prizes too"
(https://pikminbloom.com/en/news/0428, https://www.pikminwiki.com/Weekly_challenge,
https://niantic.helpshift.com/hc/en/23-pikmin-bloom/faq/3404-weekly-challenges/). There is no
leaderboard ranking players against each other.

#### 8. Freedom and identity

A **Mii** avatar walks the map with you; you dress it, choose which Pikmin are in your squad (and
"select a dream team of Pikmin to increase your score" against mushrooms), name and favourite
Pikmin, collect Decor Pikmin as a wardrobe, and write Lifelog entries of up to 300 characters with
optional location tags (https://itunes.apple.com/lookup?id=1556357398&country=gb,
https://www.pikminwiki.com/Lifelog). The Lifelog's day-rating faces are a form of self-expression
the game does nothing mechanical with — it is a diary, not a score.

#### 9. Signature interaction

Two candidates, and they are both quiet. The first is **the trail**: a squad of Pikmin walking in a
line behind your Mii, laying a visible ribbon of flowers along the actual streets you walked, which
other nearby players can see. The second is **the nightly lookback** — step count animated along a
zig-zag path, then "pick a photo from today and rate your day". If RepGarden takes one thing from
this lane, it is the lookback.

#### 10. UI type and art

**Map.** A Google-Maps-derived top-down/tilted world with your Mii at the centre
(https://www.nintendolife.com/reviews/mobile/pikmin-bloom). Art: soft, pastel, hand-made Nintendo
charm — round Pikmin with leaves and flowers on their heads against a desaturated real-world map;
the reviewer notes "the Pikmin IP really suits the chilled, feelgood vibe". The screen is **sparse**
by map-game standards: the map, a squad, a petal counter, and a small ring of buttons. Home screen
= the live map with your avatar, squad, flower trail and nearby Big Flowers and mushrooms.

#### 11. Sound and feel

Not confirmed in detail from a citable source. Documented feedback moments are the bloom animation
when nectar is fed and flowers open on a Pikmin's head, petal harvest by tapping the flowers, and
Big Flowers that "emit sparkles for one hour" after blooming
(https://niantic.helpshift.com/hc/en/23-pikmin-bloom/faq/2855-planting-flowers/). Pikmin voices and
haptics: not confirmed.

#### 12. Scale and reception

- App Store GB on 27 Oct 2026: **4.75 stars from 5,821 ratings**
  (https://itunes.apple.com/lookup?id=1556357398&country=gb).
- Play Store GB: **5M+ downloads** (https://play.google.com/store/apps/details?id=com.nianticlabs.pikmin&hl=en_GB).
- Launched globally 1 November 2021 (store release date, same lookup); Metacritic 65/100
  (https://en.wikipedia.org/wiki/Pikmin_Bloom).
- Business model: free, with coins bought for real money and storage upgrades
  (https://apps.apple.com/gb/app/pikmin-bloom/id1556357398).

Three complaints:
1. Event grind turns a calm game stressful — "I had to make missions in set short timeframes, just
   to get disappointed with duplicate decor Pikmin… A game should be fun, not stressful."
   (https://www.reddit.com/r/PikminBloomApp/comments/1086ge9/i_didnt_open_the_game_in_one_week_and_feel_much/)
2. Event requirements outrun the supply of the resource they need, pushing you towards coins — "it
   refused to give me any after I ran out… I don't want to use my coins for flowers I should just be
   able to get from playing the game!"
   (https://www.reddit.com/r/PikminBloomApp/comments/1tk9mxt/i_hate_this_game_sometimes_complaint/)
3. It runs thin as a game — "It's a glorified pedometer; expect more 'game' and you'll likely be
   disappointed" (https://www.nintendolife.com/reviews/mobile/pikmin-bloom); a GB reviewer echoes
   it: "it's starting to become boring already"
   (https://apps.apple.com/gb/app/pikmin-bloom/id1556357398, Lealiketea, 19/12/2022).

Three things loved:
1. It is FOMO-free and forgiving — "a pleasantly FOMO-free experience" that "feels healthier than
   typical free-to-play games" (https://www.nintendolife.com/reviews/mobile/pikmin-bloom).
2. It works as a recovery and motivation tool — GB review titled "A great game and tool for
   recovery!" from someone who came for a pedometer
   (https://apps.apple.com/gb/app/pikmin-bloom/id1556357398, Greggy sausage rolio, 19/11/2022).
3. People accept that it is a "non-game" and value it anyway — "Firstly I really enjoy this
   non-game. It isn't a game, but it is motivation to get out and walk" (same page, Msads1,
   21/12/2021).

#### 13. Lesson for RepGarden

This is the closest existing model to "train and something grows", and the parts that transfer are
the end-of-session lookback and the no-punishment challenge. Copy the nightly lookback almost
literally: after a workout, animate what the client actually did (sets, a PB, sessions this week),
let them attach one photo and rate how the session felt, and keep that diary unscored. Copy the
Weekly Challenge shape too — a shared vegetable-patch goal with a participation reward when the
group falls short, never a ranking. Copy the withered-Pikmin rule as the only decay: it punishes
over-farming the game, not absence from it, and it heals through the real behaviour. What to avoid
is Pikmin Bloom's own failure: timed event quotas that demand a resource the game then withholds
turned its calmest players into stressed ones who quit. For a gym app whose rest days are
prescribed, any time-boxed quota is the same trap.

---

### 2. Pokémon GO

App Store id 1094591345. Developer now **Scopely Explore, Inc.** — Niantic sold its games business
to Scopely for $3.5 billion, closing 29 May 2025
(https://itunes.apple.com/lookup?id=1094591345&country=gb,
https://www.blog.udonis.co/mobile-marketing/mobile-games/pokemon-go).

#### 1. Unit of play

Nothing is tended; a **collection** accumulates. Walking is a raw input that feeds three meters at
once. Adventure Sync "allows you to record your kilometers traveled even when the Pokémon GO app
isn't open", tracking distance for **egg hatching**, **Buddy candy**, weekly goals and Adventure
Sync rewards (https://niantic.helpshift.com/hc/en/6-pokemon-go/faq/3265-adventure-sync/). A Buddy
earns 1 candy per km at its tier of 1/3/5/20 km, and eggs hatch at 2/5/7/10/12 km of walking
(https://pokemongohub.net/post/guide/go-hub-guide-to-hatching/). The headline unit, though, is the
**Pokédex** — "complete your Pokédex to become stronger"
(https://itunes.apple.com/lookup?id=1094591345&country=gb).

#### 2. Session shape

Short, repeated, location-triggered. Players average 45 minutes of play a day, in many short bursts
rather than one sitting (https://www.blog.udonis.co/mobile-marketing/mobile-games/pokemon-go). Ten
seconds buys you: spin a PokéStop, throw one ball, open a gift. The longer sit-down is a raid, a GO
Battle League set, or the weekly Adventure Sync fitness report. There is also a true glance-only
surface: "an optional home screen widget to track egg incubation and buddy candy progress"
(https://niantic.helpshift.com/hc/en/6-pokemon-go/faq/3265-adventure-sync/).

#### 3. Absence

Your collection is permanent, and this is the lane's strongest evidence that a bank beats a streak.
A player returning after ten years wrote: "I haven't opened this game since late 2016 and just
reinstalled it 3 days ago… I still have a couple hundred original 2016 Pokemon sitting safely in my
storage" (https://www.reddit.com/r/pokemongo/comments/1vsj88b/returning_after_a_10year_break_since_2016_and/).
The same post shows the real cost of absence, which is comprehension, not loss: "To say I am
completely overwhelmed is a massive understatement. There are shadow Pokemon, routes, party play,
dynamic raids, and so many generations I don't recognize. I feel like a time traveler!"

The streaks, by contrast, are brutal and unprotected. Daily Discovery gives XP and Stardust for your
first catch and first PokéStop spin each day, with a seventh-day multiple, and "Missing a single day
resets both streaks to day 1" — no freeze, no repair, no grace
(https://www.switchbladegaming.com/pokemon-go/daily-discovery-guide/). Current figures on that page:
first catch 500 XP + 600 Stardust, rising to 2,500 XP + 3,000 Stardust on a 7-day streak; first spin
500 XP + items, rising to 2,500 XP + a larger bundle. The day runs midnight to 23:59 local time.
Earlier figures were higher (1,500 XP / 1,800 Stardust, and 6,000 / 9,000 at day 7 in 2016 —
https://www.forbes.com/sites/davidthier/2016/11/08/first-catch-of-the-day-pokestop-how-daily-bonuses-and-streaks-work-in-pokemon-go/,
page fetch blocked by Forbes, figures from search summary), so the amounts have been rebalanced but
the reset rule has not.

Whether gym-defending Pokémon or Buddy mood decay during a long absence: **not confirmed**.

#### 4. Currency and endogenous value

Four layers. **Stardust** and **Candy** are purely endogenous — they power up and evolve the
Pokémon you already care about and cannot be bought directly. **XP** buys Trainer level, which gates
what you can catch. **PokéCoins** are the real-money currency, spent on bag and storage space,
incubators, raid passes and incense; players can earn a trickle by defending gyms. Pokémon GO has
taken roughly **$9.1 billion in gross player spending over ten years** and more than $1 billion in
2025 alone (https://www.blog.udonis.co/mobile-marketing/mobile-games/pokemon-go). Perception of the
money layer is the single loudest grievance in the subreddit: the top complaint post on the subject
has 3,587 upvotes and is titled "Sometimes I ask myself if I'm being too hard on Niantic. Then I
remember all the 💩 decisions they've made in the past 2 years, and their complete ignorance towards
the playerbase"
(https://www.reddit.com/r/pokemongo/comments/1ctuqvq/sometimes_i_ask_myself_if_im_being_too_hard_on/),
and a dedicated analysis is titled "The Drastic Rise of Paid Tickets and Research During the Season
of Timeless Travels: A Month By Month Analysis"
(https://www.reddit.com/r/pokemongo/comments/1b0rgs3/the_drastic_rise_of_paid_tickets_and_research/).
Even the monthly Community Day now carries a ticket — "US$1.99 (or the equivalent pricing tier in
your local currency)" (https://pokemongo.com/en/news/communityday-november-2026-pawniard).

#### 5. Stakes, risk and chance

Chance is the engine. Spawn tables, shiny rates, egg contents, and "Special Background" variants are
all rolls. Opt-in risk exists in PvP (GO Battle League), raids where you can faint and must retry,
and timed research. No betting mechanic. The Community Day structure is the clearest "surge" design
in the lane: a fixed three-hour window, 14:00–17:00 local, in which one species floods the map with
a raised shiny rate, plus stacked bonuses — on 21 November 2026, "1/4 Egg Hatch Distance, 2× Candy
for catches, 2× Candy XL chance (level 31+), 3-hour Incense duration, 1-hour Lure Modules, One
additional Special Trade, 50% reduced Stardust for trades"
(https://pokemongo.com/en/news/communityday-november-2026-pawniard).

#### 6. Progression

Trainer level (gated by XP and by level-up task sets), the Pokédex, medals, per-Pokémon power-up and
evolution, seasons of roughly three months, and the GO Battle League rank ladder. The Community Day
move — "Kingambit learns 'Kowtow Cleave' when evolved during or within 4 hours after the event" — is
a milestone that only exists inside a window (same source).

#### 7. Social

Deep and partly mandatory. Friends with friendship levels, daily gift exchange, trading (cheaper
during events), raids that in practice need several players, GO Battle League PvP, three teams,
Party Play and Routes. Much of the highest-value content is unreachable solo, which is the opposite
of what RepGarden needs.

#### 8. Freedom and identity

Avatar customisation and team choice ("Join one of the three teams and customize your avatar"),
Buddy choice ("Choose your Buddy Pokémon from your Pokédex to travel at your side"), nicknames, and
AR photography (https://itunes.apple.com/lookup?id=1094591345&country=gb).

#### 9. Signature interaction

The **swipe-flick of a Poké Ball** at a creature standing on the pavement in front of you, with the
coloured target ring shrinking for an Excellent throw. Nothing else in mobile gaming reads as this
app in one gesture.

#### 10. UI type and art

**Map.** A stylised, pastel, low-detail version of the real street map, with your avatar centred and
PokéStops and gyms as floating icons — deliberately legible while walking. The catch screen breaks
out of the map into a full-screen first-person scene (or live AR camera). Dense by comparison with
Pikmin Bloom: a nearby-Pokémon tray, a bag, a Pokédex, raid banners, event banners and research
tickers. Home screen = the live map plus event banner.

#### 11. Sound and feel

Not confirmed from a citable source in this pass. Documented feedback: push notifications when buddy
candy or an egg hatch milestone is reached
(https://niantic.helpshift.com/hc/en/6-pokemon-go/faq/3265-adventure-sync/), and the full-screen
weekly fitness report. Ball-throw haptics and catch sounds: **not confirmed**.

#### 12. Scale and reception

- App Store GB on 27 Oct 2026: **4.10 stars from 96,457 ratings**
  (https://itunes.apple.com/lookup?id=1094591345&country=gb) — the lowest in this lane by a wide
  margin, and the only one below 4.4.
- Play Store GB: **500M+ downloads** (https://play.google.com/store/apps/details?id=com.nianticlabs.pokemongo&hl=en_GB).
- Launched 14 July 2016 (store release date). 800 million lifetime players, 1 trillion Pokémon
  caught as of July 2026 (https://www.blog.udonis.co/mobile-marketing/mobile-games/pokemon-go).
- Business model: free with PokéCoins, event tickets and bundles.

Three complaints:
1. Sustained distrust of the operator's decisions — 3,587-upvote post on "all the 💩 decisions
   they've made in the past 2 years, and their complete ignorance towards the playerbase"
   (https://www.reddit.com/r/pokemongo/comments/1ctuqvq/sometimes_i_ask_myself_if_im_being_too_hard_on/).
2. Creeping paywalling of events — "The Drastic Rise of Paid Tickets and Research"
   (https://www.reddit.com/r/pokemongo/comments/1b0rgs3/the_drastic_rise_of_paid_tickets_and_research/).
3. The design is experienced as compulsion by long-term players — a 365-upvote post titled "Day 1
   player: Leaving this addiction behind"
   (https://www.reddit.com/r/pokemongo/comments/12hhz3k/day_1_player_leaving_this_addiction_behind/).

Three things loved:
1. It changes how people treat walking and their own bodies — 10,396-upvote post: "Be nice to people
   playing GO despite what they look like. Some people play this game to better themselves."
   (https://www.reddit.com/r/pokemongo/comments/4swhlq/be_nice_to_people_playing_go_despite_what_they/)
2. The collection survives anything, so returning is possible at all — "a couple hundred original
   2016 Pokemon sitting safely in my storage… On the bright side, I am hooked again"
   (https://www.reddit.com/r/pokemongo/comments/1vsj88b/returning_after_a_10year_break_since_2016_and/).
3. Walking with a companion creature is the emotional core, and players asked for it before it
   existed — 23,332-upvote request: "Allow us to walk with a Pokemon, and give them passive
   abilities"
   (https://www.reddit.com/r/pokemongo/comments/4uaidt/suggestion_allow_us_to_walk_with_a_pokemon_and/).

#### 13. Lesson for RepGarden

Take Adventure Sync's principle — the game must accrue from recorded activity whether or not the app
is open, so a client who logs a session and closes the app still finds something grown next time —
and take the **bank** model: a permanent collection means a ten-year absence is recoverable, which a
streak never is. Take the three-hour Community Day as the template for Benji's challenge weeks: a
narrow window with stacked bonuses, announced in advance. Avoid two things outright: the unprotected
daily streak, which in a 3-times-a-week gym app would reset on every prescribed rest day, and the
accumulation of systems — the returning player's "I feel like a time traveler" is what happens when
a game keeps adding mechanics and never gives an absent player a way back in.

---

### 3. Zombies, Run!

App Store id 503519713. Developer **Zombies Run! Ltd** (formerly Six to Start), co-created with
novelist Naomi Alderman, Kickstarter-funded in October 2011 raising $72,627 from 3,464 backers
(https://itunes.apple.com/lookup?id=503519713&country=gb, https://en.wikipedia.org/wiki/Zombies,_Run!).

#### 1. Unit of play

Two units, stacked. The **story** is the real engine: "Every run becomes a mission. You're Runner 5,
and through your headphones the story unfolds"
(https://itunes.apple.com/lookup?id=503519713&country=gb). Underneath it, **Abel Township** is the
thing that grows: you start with "a farmhouse, defence tower, and armoury" and construct hospitals,
housing and recreation areas, improving the base's "defence, morale and population" with supplies
and materials earned on runs (https://support.zombiesrungame.com/hc/en-us/articles/4421007214353-Base-Builder,
reached via search summary — the page blocks direct fetch; corroborated at
https://en.wikipedia.org/wiki/Zombies,_Run!). One real action — one run — maps to one story episode
advanced, plus supplies picked up automatically along the way, plus materials for finishing.

#### 2. Session shape

The opposite of a glance. Missions last "35 minutes to an hour"
(https://en.wikipedia.org/wiki/Zombies,_Run!), and the run itself is **hands-free**: "Supplies are
collected automatically, so you do not need to tap the screen while moving — you just listen, move,
and let the story unfold" (https://www.pokeep.com/lbs-games/zombies-run-guide.html). The screen
during a run shows progress through the mission as segments across the top.

The sit-down is afterwards, in Base Builder: "At the top of the screen you can see a bar containing
your base's stats", and you spend what you brought home
(https://www.nerdophiles.com/2013/07/24/zombies-run-update-boasts-streamlined-features-and-base-customizability/).
Ten seconds, in this app, is only enough to start a mission or claim supplies — which is exactly the
shape RepGarden cannot use mid-workout and can use at the end of one.

#### 3. Absence

No streak, no decay, no loss. Nothing in the official material or the Wikipedia entry describes a
penalty for not running; the base and your mission progress wait. What does gate you is content, not
time: free users "can unlock one mission for free each week" (https://zrx.app/news/Get-started-with-zr),
and free users collect "up to 10 supplies per run, while members have no limit"
(https://support.zombiesrungame.com/hc/en-us/articles/4421007214353-Base-Builder, via search
summary). So an absent free player comes back to a *bigger* backlog of unlocked missions, not a
punished one.

Reviews on absence: **not confirmed** — no subreddit evidence was obtainable (r/ZombiesRun and
r/zombiesrun both returned nothing through the Reddit API used).

#### 4. Currency and endogenous value

**Supplies** (collected automatically while moving, "about 30 supplies an hour") and **materials**
(awarded for completing a story mission, with a fixed number available per mission) both go into
buildings, and "Expanding structures unlocks missions and influences story events"
(https://en.wikipedia.org/wiki/Zombies,_Run!). On paper that is textbook endogenous value: exercise
-> supplies -> buildings -> more story.

In practice it is the lane's clearest warning. A reviewer who liked the app wrote that base upgrades
"lack gameplay impact" and "produce no tangible effects, making resource collection feel 'pointless'
despite the underlying concept of incentivizing continued app use"
(https://blog.patientrock.com/zombies-run/). A currency only feels endogenous if spending it visibly
changes something the player already cares about.

The money layer is a subscription, and the GB price list is long: Membership £6.99 and £49.99, VIP
£87.99, Pro 1 month £2.99, Pro 1 year £7.99 or £19.99, plus legacy £24.99 and an Abel Club offer at
£12.99 (https://apps.apple.com/gb/app/zombies-run/id503519713). It launched as a paid app and moved
to free-to-play with subscriptions by May 2015 (https://en.wikipedia.org/wiki/Zombies,_Run!).

#### 5. Stakes, risk and chance

The **zombie chase** is the best opt-in risk mechanic in the lane. When a chase triggers, the app
takes your average pace over the previous 30 seconds and requires you to go 20% faster by default;
"In order to escape you must either run at this increased pace for at least 100 seconds OR you need
exceed that pace and pull much farther ahead from your chasers"
(https://support.sixtostart.com/hc/en-us/articles/203780596-How-do-Zombie-Chases-work-I-keep-getting-caught-).
Three design choices make it safe to offer: chases are **optional** and can be switched off;
subscribers can tune the required increase anywhere "between 10-30%"; and being caught "will not
cause you to 'fail' a mission or episode and force you to restart" — you lose one item from your
inventory and keep running. Wikipedia puts the same mechanic as interval training with a cost:
"Failure results in losing collected supplies" (https://en.wikipedia.org/wiki/Zombies,_Run!).

Chance is light: which supply item you pick up is randomised.

#### 6. Progression

**Chapters.** Twelve seasons through May 2026, 371 missions, with season 1 at 23 missions and later
seasons typically 30–40 (https://en.wikipedia.org/wiki/Zombies,_Run!); the store claims "500+
missions across 11 seasons and counting"
(https://itunes.apple.com/lookup?id=503519713&country=gb). Alongside it: a Couch-to-5K training
programme described as "an expert-designed 8 week program" (https://zombiesrungame.com/), virtual
races (16, VIP-gated), airdrop missions, trophies, and the base's own build-out. Milestones are
narrative — a season ending — rather than numeric.

#### 7. Social

Thin and optional: virtual races, and historically leaderboards and shared runs. There is no
friends-visit or co-op core. This is the one app in the lane that proves a retention engine can run
with essentially no social layer, because the story carries it.

#### 8. Freedom and identity

You are cast, not created: you are **Runner 5**, a deliberately silent protagonist, which lets the
story address you directly. Customisation is the base layout and which buildings to prioritise, the
chase intensity setting, mission order, and your own music — "Your music, your soundtrack. The story
weaves between tracks from your own playlists"
(https://itunes.apple.com/lookup?id=503519713&country=gb).

#### 9. Signature interaction

**"Zombies detected."** The robotic voice cutting into your music, and the sprint that follows. The
reviewer notes the chases "deliberately occur during physically challenging moments"
(https://blog.patientrock.com/zombies-run/). The gesture is not on the screen at all — it is in the
body.

#### 10. UI type and art

**Minimal stat/figure**, deliberately. During a run the screen is a progress bar of mission segments
over distance, pace and calories; you are not meant to look at it. The game's one real "world"
screen is the Base Builder, an isometric SimCity-like township — "The Base Builder is the real meat
of the Zombies, Run! visual interface"
(https://www.nerdophiles.com/2013/07/24/zombies-run-update-boasts-streamlined-features-and-base-customizability/).
Home screen = expandable **mission cards** with a download button and run options, swipeable between
seasons and Radio mode. Sparse, text-and-card led, dark post-apocalyptic palette.

#### 11. Sound and feel

This is the app where sound *is* the product. "Strong voice acting throughout, with later seasons
adding quality foley effects"; the narrator's robotic "Zombies detected" announcement "effectively
signals danger"; the story is interleaved with the player's own playlist between clips
(https://blog.patientrock.com/zombies-run/). Audio is also the failure channel: you hear the horde
closing. Haptics: **not confirmed**.

#### 12. Scale and reception

- App Store GB on 27 Oct 2026: **4.76 stars from 4,725 ratings**
  (https://itunes.apple.com/lookup?id=503519713&country=gb) — the highest in the lane.
- Play Store GB: **1M+ downloads** (https://play.google.com/store/apps/details?id=com.sixtostart.zombiesrunclient&hl=en_GB).
- Released 27 February 2012 on iOS, June 2012 on Android; became "the highest-grossing Health &
  Fitness app" within two weeks; over 750,000 players by 2014; the store now claims "over 10 million
  runners" (https://en.wikipedia.org/wiki/Zombies,_Run!,
  https://itunes.apple.com/lookup?id=503519713&country=gb).
- Business model: free trial content plus subscription tiers (Membership, Pro, VIP).

Three complaints:
1. The game layer is inert — base upgrades "produce no tangible effects, making resource collection
   feel 'pointless'" (https://blog.patientrock.com/zombies-run/).
2. Tracking failures break the illusion — "Love the idea of this app, and the stories are really
   engaging… However, I've had massive GPS issues when using the app"
   (https://apps.apple.com/gb/app/zombies-run/id503519713, Loubylou101, 22/03/2021).
3. A long tail of audio and sync bugs across version 12 — story clips stopping after chases, music
   continuing after workouts end, workouts not marked complete, unsynced run logs
   (https://support.zombiesrungame.com/hc/en-us/articles/206119647-Known-Issues-Zombies-Run, via
   search summary; the page itself blocks fetching).

Three things loved:
1. The story makes the workout disappear — "The stories are just the thing to keep your mind
   engaged" (https://apps.apple.com/gb/app/zombies-run/id503519713, Kirana98, 01/10/2018).
2. Tunable difficulty is appreciated as a feature, not a setting — "I like to alter how I get chased
   by the Zoms… It has so many little plans for training it is a fantastic motivator" (same page,
   moosey1984, 31/01/2018).
3. It gets non-runners running — "This app has helped me massively with my fitness… the writing is
   excellent" (same page, Lukan Kai, 15/07/2020); the store leads with inclusivity: "Total beginner
   or marathon veteran, it works anywhere and at any speed — jog in a park, walk a trail, use a
   treadmill, or work out in a wheelchair"
   (https://itunes.apple.com/lookup?id=503519713&country=gb).

#### 13. Lesson for RepGarden

The transferable idea is the **opt-in intensity spike with a capped loss**: Benji can mark a set as a
"push set", the client opts in, and failing costs one harvested vegetable rather than resetting
anything — chases work precisely because they are optional, tunable, and cannot fail the session.
Also transferable: the app asks nothing of the hands during the activity and everything afterwards,
which matches a gym where the phone is in a pocket between sets. The warning is sharp and directly
relevant: Zombies Run's own players call its base-building pointless because the buildings do not
change anything. If RepGarden's vegetables are harvested into a patch that has no effect on anything
the client cares about, the same verdict follows — the patch must unlock something the client wants,
whether that is Benji's next challenge, a new plot, or a visible record of what they lifted.

---

### 4. Walkr: Fitness Space Adventure

App Store id 834805518. Developer now listed as **SPARKFUL INC.** — the same studio as Fourdesire,
which also made Plant Nanny (https://itunes.apple.com/lookup?id=834805518&country=gb). **Still
maintained**: version 7.36.5 shipped 23 October 2026, four days before this reading (same lookup).

#### 1. Unit of play

A **galaxy** of planets, fuelled by steps. "Your daily steps are automatically recorded and
converted into energy fuel for your spaceship", and the galaxy holds "100+ fascinating planets and
30+ mission goals" (https://itunes.apple.com/lookup?id=834805518&country=gb). Steps -> energy ->
spaceship travel -> planets discovered -> planets levelled up and decorated with "satellites and
wonders", each generating resources (https://sparkful.app/walkr). It is an idle/resource-collection
game with walking as the accelerant: "energy (gained from walking) is used to expedite the
processes" (https://en.namu.wiki/w/Walkr, via search summary).

#### 2. Session shape

Glance-dominant. Keep the phone in your pocket and "the energy converter will automatically recharge
your spaceship" (https://sparkful.app/walkr). On opening, you tap **Boost** to spend energy and
speed exploration, collect coins that planets generated while you were away, and feed creatures —
"Tap Boost (which will cost you points) to speed exploration"
(https://www.commonsensemedia.org/app-reviews/walkr-a-gamified-fitness-app). An alien character
speaks in text bubbles to tell you what to do next (same source). Ten seconds is enough for a full
round of collect-and-boost.

#### 3. Absence

No decay and no streak, because it is an idle game: planets keep producing while you are away and
you harvest on return — "coins can be generated without doing anything at all as long as you come
back to collect them" (https://en.namu.wiki/w/Walkr, via search summary). The cost of absence is
unspent energy capacity and uncollected yield, not loss.

One hard limitation reads as a penalty for the wrong user: "since most phones do not record activity
for wheelchair users this app does not apply to me" — a 2025 GB review titled "No good for
wheelchair users but the concept is cool"
(https://apps.apple.com/gb/app/walkr-gamified-fitness-walk/id834805518, OBee218, 01/08/2025).

#### 4. Currency and endogenous value

**Energy** (from steps) is the endogenous currency: it only buys travel and boosts, which only
produce more galaxy. **Coins** are the planet-economy currency; creating an Epic room costs 5,000
coins (https://en.namu.wiki/w/Walkr, via search summary). **Cubes** are the premium currency —
"easily obtainable within the game by doing deliveries or finding them floating around" and also
"bought, earned from epics, or obtained by watching ads" (same source). GB prices run from £0.99
(Time Machine) and £1.79 (Super Pilot) through cube bundles at £1.99/£4.99/£19.99/£49.99/£99.99,
plus an Ads Remover at £1.99 and a cross-app SPARKFUL subscription at £7.99/month or £69.99/year
(https://apps.apple.com/gb/app/walkr-gamified-fitness-walk/id834805518).

#### 5. Stakes, risk and chance

No betting and no loss. Chance comes from cubes "found floating around", from which planets and
creatures appear, and from rare elements. **Epics** are the structured risk-free group goal:
"journeys that can be played by 4 to 10 people… taking about at least 40 hours to a maximum of 182
hours to finish" (https://en.namu.wiki/w/Walkr, via search summary).

#### 6. Progression

Planet collection (100+), mission goals (30+), spaceship upgrades, planet levels with satellites and
wonders, and a competitive ladder — "Compete with friends from Comet to Galaxy League and grow
together" (https://itunes.apple.com/lookup?id=834805518&country=gb). Milestones are a new planet
discovered or a creature returned home.

#### 7. Social

Opt-in and co-operative: "Invite friends to become your co-pilot and receive extra energy fuel";
fleets of captains; "Visit the Planet Lab with friends to share energy fuel and unlock amazing
planet wonders"; Epics as 4–10-person quests; and the Comet->Galaxy League ladder (same store
listing, plus https://sparkful.app/walkr). Fleets function as guilds where you can "assist Lab
members with free upgrades to their planets" (https://en.namu.wiki/w/Walkr, via search summary).

#### 8. Freedom and identity

Your galaxy is the identity object: which planets you collect, how you level and decorate them with
satellites and wonders, which spaceship you fly, and which creatures you have rehomed
(https://sparkful.app/walkr).

#### 9. Signature interaction

**Tap Boost** and watch the spaceship surge — spending the day's walking as literal fuel in a single
gesture (https://www.commonsensemedia.org/app-reviews/walkr-a-gamified-fitness-app).

#### 10. UI type and art

**Side-on single scene.** A vertical cross-section of space with the spaceship, planets above and
below, energy counter in the upper left, and an alien speaking in text bubbles. Art: soft, rounded,
pastel cartoon illustration — the same gentle style as Plant Nanny. The screen is **dense** and that
is its main criticism: "With so many options and so much going on… it can begin to feel simply too
complicated", and players unfamiliar with games "may struggle with unclear objectives"
(https://www.commonsensemedia.org/app-reviews/walkr-a-gamified-fitness-app).

#### 11. Sound and feel

Not confirmed from a citable source. The one feel claim available is a reviewer's: the game is "cute
and smooth as a baby's bottom"
(https://apps.apple.com/gb/app/walkr-gamified-fitness-walk/id834805518, Culwenimos, 19/02/2018).

#### 12. Scale and reception

- App Store GB on 27 Oct 2026: **4.59 stars from 630 ratings** — the smallest audience in the lane
  (https://itunes.apple.com/lookup?id=834805518&country=gb).
- Play Store GB: **1M+ downloads** (https://play.google.com/store/apps/details?id=com.fourdesire.spacewalk&hl=en_GB).
- Released 17 July 2014; won an App Store Best Game award; claims "over 3,000,000+ iOS players"
  (https://itunes.apple.com/lookup?id=834805518&country=gb).
- Business model: free with ads, consumable cubes, an ad remover, and a cross-app subscription.

Three complaints:
1. Too much going on — "With so many options and so much going on… it can begin to feel simply too
   complicated" (https://www.commonsensemedia.org/app-reviews/walkr-a-gamified-fitness-app).
2. Destructive save handling — "I misclicked and my previous game save auto filled and replaced my
   new game. I got incredibly annoyed"
   (https://apps.apple.com/gb/app/walkr-gamified-fitness-walk/id834805518, Shanellexxx, 04/10/2021).
3. Step-only input excludes people — wheelchair users get nothing from it (same page, OBee218,
   01/08/2025).

Three things loved:
1. It rewards an otherwise dead part of the day — "I enjoy this app constantly, it gives me an extra
   reason to smile after doing the long commute" (same page, marbledmayhem, 29/12/2017).
2. It makes health feel compulsive in a good way — review titled "Being healthy has become
   addictive!" (same page, Culwenimos, 19/02/2018).
3. Co-operation pays — co-pilots, fleets and Planet Lab visits all grant extra fuel rather than
   ranking players against each other (https://sparkful.app/walkr).

#### 13. Lesson for RepGarden

Walkr shows that an idle harvest is a better absence model than a streak: the patch keeps producing
while the client is away, so returning is a reward rather than a reckoning, and a prescribed rest day
costs nothing. It also shows the cost of letting the economy sprawl — energy, coins and cubes across
planets, satellites, wonders, fleets, labs, epics and leagues is why reviewers call a walking game
"too complicated". For a one-handed, few-seconds-between-sets app, RepGarden should keep exactly one
earned thing and one place to spend it, and let the vegetable patch be the only screen.

---

### 5. Sweatcoin

App Store id 971023427. Developer **Sweatco Ltd**
(https://itunes.apple.com/lookup?id=971023427&country=gb).

#### 1. Unit of play

Nothing grows. A **wallet** fills. Verified outdoor steps convert to a currency at roughly "1
sweatcoin per 1,000 verified steps", and the free tier caps earning at about 10 sweatcoins a day
(https://www.fitcoin.co/articles/sweatcoin-review). Verification is strict: it "uses your phone's
step sensor combined with GPS to count verified outdoor steps… Indoor steps, treadmill steps, gym
steps and any movement without GPS lock simply do not count"
(https://selectra.co.uk/mobile/guides/technology/sweatcoin). That exclusion alone disqualifies the
model for a gym app.

#### 2. Session shape

Pure glance, and heavily ad-monetised. Open, see today's steps and balance, "scroll down to the
'Daily Rewards' section in the home page and hit 'Claim'", watch an ad, unlock two further rewards
by walking more and watching another full ad, then spin the "Spin and Win" wheel
(https://help.sweatco.in/hc/en-us/articles/360012676432-What-are-daily-rewards). The review estimate
is "4 to 6 ad touchpoints a day if you use the app actively"
(https://www.fitcoin.co/articles/sweatcoin-review).

#### 3. Absence

Earning simply stops; the balance persists. There **is** a streak — "A walking streak is when you
walk every day without missing a beat. Keep walking daily to keep your streak alive"
(https://help.sweatco.in/hc/en-us/articles/360012676432-What-are-daily-rewards) — and, uniquely in
this lane, the repair is a straight purchase: the GB in-app purchase list includes **"Restore your
longest streak — £0.99"** (https://apps.apple.com/gb/app/sweatcoin-walking-step-tracker/id971023427).
That is the honest end point of streak design: once the streak is the asset, selling its restoration
is the business model.

#### 4. Currency and endogenous value

**Sweatcoins** are entirely **exogenous** — they buy nothing that improves the walking. They go to
"brand discounts, free trials, the occasional physical product, daily auctions, and charity
donations" (https://www.fitcoin.co/articles/sweatcoin-review). This is the lane's control
experiment, and the result is poor. Independent analysis puts practical worth at "1 to 5 cents per
sweatcoin", giving "$0.50 to $2 a month in usable value" at 10,000 daily steps (same source); a UK
guide puts it at "roughly £3 to £30 of cashable value per year"
(https://selectra.co.uk/mobile/guides/technology/sweatcoin). The good offers vanish: "the genuinely
good offers (free items, popular gift cards) appear in limited quantities and disappear within
hours", and most redemptions are discount codes that require spending more money
(https://www.fitcoin.co/articles/sweatcoin-review).

Real-money layer: Premium at £4.99 and £24.99, trial tiers at £24.99 and £27.99, Trouble Maker packs
at £0.99/£5.49/£9.99, a 10x Entries Power-Up at £1.99, and the £0.99 streak restore
(https://apps.apple.com/gb/app/sweatcoin-walking-step-tracker/id971023427). Premium tiers mainly
raise the daily earning cap, to 15, 20 or 30 sweatcoins
(https://selectra.co.uk/mobile/guides/technology/sweatcoin).

#### 5. Stakes, risk and chance

Chance is the whole retention mechanic once the currency's value is this thin. "Scratch Cards and
Super Draws with prizes like iPhone, PlayStation, Amazon Gift Cards", where "Every Sweatcoin you
have in your balance gives you one chance to win", plus daily auctions and the Spin and Win wheel
(https://help.sweatco.in/hc/en-us/articles/360012676432-What-are-daily-rewards,
https://www.fitcoin.co/articles/sweatcoin-review). There is a 10x Entries Power-Up you can buy for
£1.99 — paying to improve lottery odds
(https://apps.apple.com/gb/app/sweatcoin-walking-step-tracker/id971023427).

#### 6. Progression

Badges only: "Hit your daily step goals and collect unique badges for each milestone achieved"
(https://itunes.apple.com/lookup?id=971023427&country=gb). No levels, no seasons, no world.

#### 7. Social

Lightweight and comparative: "Compete with friends to see who can maintain the longest step streak",
and "You can absolutely spy on your friends' steps… Invite friends to the app (and get rewarded for
it!) and follow them to see how they're doing"
(https://itunes.apple.com/lookup?id=971023427&country=gb,
https://help.sweatco.in/hc/en-us/articles/360012676432-What-are-daily-rewards). Referral is a
monetised growth loop rather than a play feature.

#### 8. Freedom and identity

Essentially none. No avatar, no world, no naming, no decoration. The only choice is which offers to
redeem.

#### 9. Signature interaction

The **step-to-coin conversion counter** ticking over on the home screen — and, behind it, the
verification that silently discards steps it does not trust.

#### 10. UI type and art

**Minimal stat/figure.** A scrolling card feed: today's steps, a balance, Daily Rewards claim
buttons, offer tiles, draw entries. Flat, bright, fintech-adjacent design with no illustration or
world. Dense with promotional cards. Home screen = steps, balance, claimable rewards and offers.

#### 11. Sound and feel

Not confirmed. The documented feedback moments are the claim button, the Spin and Win wheel and the
scratch card reveal, all borrowed directly from gambling interfaces
(https://help.sweatco.in/hc/en-us/articles/360012676432-What-are-daily-rewards).

#### 12. Scale and reception

- App Store GB on 27 Oct 2026: **4.49 stars from 71,224 ratings**
  (https://itunes.apple.com/lookup?id=971023427&country=gb).
- Play Store GB: **100M+ downloads** (https://play.google.com/store/apps/details?id=in.sweatco.app&hl=en_GB).
- Released 5 May 2016. Business model: ads, subscription cap raises, consumables, affiliate
  marketplace, and an associated SWEAT token.

Three complaints:
1. The rewards are not worth the steps — the reviewer "criticizes weak reward offers and
   discrepancies between tracked steps and challenge counts"
   (https://apps.apple.com/gb/app/sweatcoin-walking-step-tracker/id971023427, DW_6!, 07/05/2024);
   independent valuation agrees at "1 to 5 cents per sweatcoin"
   (https://www.fitcoin.co/articles/sweatcoin-review).
2. Promised rewards not honoured — "Influencer Program scam !?", a user claiming a completed
   referral challenge never paid out
   (https://apps.apple.com/gb/app/sweatcoin-walking-step-tracker/id971023427, -(bojidar)-, 22/12/2018).
3. Features break and support does not help — "I have had this app for several years and it
   certainly has encouraged me to be more active", followed by missing coin-transfer features and
   unhelpful support (same page, Arthriticgran, 30/01/2025).

Three things loved:
1. The financial framing does move people — "Financially-Incentivised Wellbeing", a reviewer
   enjoying the comparison charts and incentives (same page, jeraenium, March 6).
2. It encourages more movement even when the payout is small — "it certainly has encouraged me to
   be more active" (same page, Arthriticgran, 30/01/2025).
3. Passive, low-battery tracking that needs no attention — "Sweatcoin's pedometer runs smoothly in
   the background, tracking your steps accurately without draining your battery"
   (https://itunes.apple.com/lookup?id=971023427&country=gb).

#### 13. Lesson for RepGarden

Sweatcoin is the counter-example that justifies RepGarden's design brief. When the reward is external
to the activity, its value gets measured in pounds, found wanting, and the app has to replace meaning
with lotteries, ads and a £0.99 streak restore. A free app with no shop cannot and should not compete
on that ground. The transferable detail is the inverse: whatever a client earns must be spendable
only inside the garden, so there is no exchange rate to be disappointed by. The second lesson is
about verification — Sweatcoin's GPS-verified outdoor steps make gym work invisible, and RepGarden's
input has the same exposure: it can only see logged sets, so the game must never imply it can judge
effort.

---

### 6. Duolingo — the baseline

App Store id 570060128, now listed as **Duolingo: Language & Chess**. Founded 2011 by Luis von Ahn
and Severin Hacker; public release June 2012; iOS listing dated 13 November 2012
(https://itunes.apple.com/lookup?id=570060128&country=gb, https://en.wikipedia.org/wiki/Duolingo).

#### 1. Unit of play

A **number**: the streak, "the number of days in a row you've completed a lesson", shown as a flame
on the home screen (https://blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals/).
Nothing grows and nothing is tended — the unit of play is a counter plus a path of lesson nodes. One
real action, a lesson of a few minutes, maps to XP, a day of streak, and a position in this week's
league.

This is the crucial structural difference from every other app in this lane: Duolingo has **no world
and no object of care**, which is exactly why losing the counter is catastrophic.

#### 2. Session shape

Designed around one short sit-down a day, with a configurable **daily goal** of roughly five to
twenty minutes (https://trophy.so/blog/duolingo-gamification-case-study). The ten-second surface is
the **home screen widget**, which shows the streak and whether today is done — Duolingo credits the
widget as a core accountability device
(https://blog.duolingo.com/how-duolingo-streak-builds-habit). Notably, Duolingo's own research found
that long sessions are a warning sign: "learners who binge on Duolingo lessons were much more likely
to abandon the app than learners who pace themselves appropriately"
(https://blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals/).

#### 3. Absence

One missed day ends the streak, and the whole engine is built on how much that hurts. The mechanics
around it, and the numbers Duolingo publishes for them, are the most useful data in this lane:

- **Streak Freeze** pauses the streak for a day. You can equip **two at a time**, and doubling the
  capacity "increased the relative number of active learners on Duolingo every day by +0.38%"
  (https://blog.duolingo.com/how-duolingo-streak-builds-habit).
- Duolingo's stated reasoning for the freeze is worth quoting as design philosophy: "At first, this
  may seem like a dishonest way to maintain a streak, but having this type of leeway actually helps
  people stay persistent", citing a University of Pennsylvania / UCLA study that "offering people a
  little 'slack' as they pursue their goals can actually be more motivating than having a rigid set
  of rules"
  (https://blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals/).
- A **Weekend Amulet** test let users keep a streak across a weekend; those offered it were "4% more
  likely to come back a week later and 5% less likely to lose their streak" (same source).
- Third-party analysis of freeze access reports "roughly 4.5x longer streaks by day 21" and, at the
  14-day mark, 30.63 days with freezes against 18.87 without
  (https://trophy.so/blog/duolingo-gamification-case-study).
- **Streak Repair** costs 500 gems and does not work retroactively on an old break; Super
  subscribers get automatic repair, which "will automatically buy the streak freeze for you by using
  gems if you miss a day", plus a monthly repair credit
  (https://duolingoguides.com/duolingo-missing-streak/, https://lingoly.io/duolingo-streak-freeze/).
- **Streak Society** at 365 days gives VIP status; at 100 days you get 3 extra streak freezes,
  renewed every 100 days (https://duolingoguides.com/how-appears-if-you-pass-365-days-on-duolingo/).
- Milestone animations on selected streak days raised 7-day retention by **+1.7%**; motivation gain
  is front-loaded — a **50%** increase in motivation from day 2 to day 3 versus **0.5%** from day
  200 to 201; **6+ million** users hold streaks of 7+ days; users reaching a 7-day streak complete
  courses at **3.6x** the rate (https://blog.duolingo.com/how-duolingo-streak-builds-habit).

And here is the cost. The top streak-loss threads on r/duolingo are among the subreddit's most
upvoted posts, and every one of them is a person whose life intervened:
- "Lost my 595 day streak because of a funeral :(" — 2,900 upvotes
  (https://www.reddit.com/r/duolingo/comments/1qw74yh/lost_my_595_day_streak_because_of_a_funeral/)
- "I lost a 1043-day streak because our ousted government shut down the Internet" — 1,591 upvotes
  (https://www.reddit.com/r/duolingo/comments/1epzb0c/i_lost_a_1043day_streak_because_our_ousted/)
- "I have lost my 960+ streak due to surgery." — 1,560 upvotes
  (https://www.reddit.com/r/duolingo/comments/161obff/i_have_lost_my_960_streak_due_to_surgery/)
- "Cannot reach support--streak lost" — 2,449 upvotes
  (https://www.reddit.com/r/duolingo/comments/1pr8h89/cannot_reach_supportstreak_lost/)
- "This is the final straw" — 3,173 upvotes
  (https://www.reddit.com/r/duolingo/comments/1l6yi7u/this_is_the_final_straw/)
- "Saying goodbye today" — 1,565 upvotes
  (https://www.reddit.com/r/duolingo/comments/1hs23w1/saying_goodbye_today/)

The pattern is unambiguous: the streak's power and its biggest churn event are the same mechanic.

#### 4. Currency and endogenous value

**XP** is the pure feedback currency — it provides "immediate positive feedback" and is the common
unit linking lessons, leagues and quests (https://trophy.so/blog/duolingo-gamification-case-study).
**Gems** are the spendable currency, earned from lessons, chests and league finishes (e.g. 60 gems
for a top-three finish, https://duolingo.deconstructoroffun.com/mechanics/leagues) and spent on
streak freezes, streak repair at 500 gems, and energy or heart refills. Gems are also sold for cash:
£0.99 to £9.99 for chests and carts of 1,200 to 3,000 gems
(https://apps.apple.com/gb/app/duolingo-language-chess/id570060128).

The third currency is the one that gates play. **Hearts** were lives: five maximum, one lost per
wrong answer, and "Once you run out of all of your hearts, you are no longer able to complete any
lessons", with one heart back every 4 hours (20 hours for a full refill), or from a practice
session, an ad, or 450/360 gems
(https://duolingoguides.com/what-happens-when-you-run-out-of-hearts-on-duolingo/,
https://duolingoguides.com/duolingo-hearts-refill/). In **May 2025** Duolingo announced a switch
from Hearts to **Energy**: you start with 25 units, "lose one unit for each mistake", and refill by
watching an ad (+5), opening chests, random bonuses for correct answers, or 750 gems — framed as
"more motivating as it rewards learners for correct answers rather than punishing them", with iOS
first and Android later in 2026 (https://lingoly.io/energy-duolingo/). Super Duolingo and Max remove
the limit entirely.

Money layer: Super Duolingo at £8.99, £12.49, £59.99, £68.99 and £86.99 in GB
(https://apps.apple.com/gb/app/duolingo-language-chess/id570060128). Revenue was **$1.04 billion in
2025** with net income of $414.1 million, 130 million monthly active users in Q1 2025 and 10.9
million paying subscribers in June 2025 (https://en.wikipedia.org/wiki/Duolingo). DAU grew from
about 5 million in 2020 to over 40 million by 2024
(https://trophy.so/blog/duolingo-gamification-case-study).

#### 5. Stakes, risk and chance

The **Streak Wager** is the clearest opt-in bet in the whole research set: spend in-game currency to
commit to a seven-day streak for double the stake back, and Duolingo's A/B test found "statistically
significant increases in Day-1, Day-7 and Day-14 user retention, with Day-7 retention showing the
greatest improvement at **+14%**"
(https://blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals/).
Weekly league demotion is involuntary risk. Chance comes from treasure chests, random energy
bonuses, and timed quests.

#### 6. Progression

Four overlapping ladders. The lesson path with units and section completions; **XP**; the **streak**
with milestone animations and the 365-day Streak Society; and **leagues**. Achievements split into
"Personal Records (immediate, performance-based) and Awards (milestone-based)", and the data is
instructive — "43.1% of custom-achievement unlocks happen on day one", with retention rising
monotonically from 32.26% for the easiest tiers to 74.17% for the hardest
(https://trophy.so/blog/duolingo-gamification-case-study).

#### 7. Social

Mostly **competitive and not opt-in**, which is the part RepGarden must not copy. Leagues put you in
a weekly pool of about 30 learners "ranked by XP earned over 7 days", matched by pace "so someone
doing 5 lessons a week isn't dropped against power users doing 100"
(https://duolingo.deconstructoroffun.com/mechanics/leagues). Ten tiers — Bronze, Silver, Gold,
Sapphire, Ruby, Emerald, Amethyst, Pearl, Obsidian, Diamond — with promotion rates that tighten as
you climb: Bronze 67%, Silver 50%, Gold 33%, Sapphire–Pearl 23%, Obsidian 17%, Diamond 0%. Bottom
finishers are demoted. There is "no double-promotion", so "Bronze to Diamond is a ten-week journey
at minimum" and "There's no week the user can skip" (same source). The site's headline claim is that
leagues drive "+25% lesson completion".

The co-operative layer is better and newer: **Friend Streaks** with up to five friends
(https://en.wikipedia.org/wiki/Duolingo), friends quests and head-to-head challenges, which analysis
calls "a more durable re-engagement driver than anonymous competition"
(https://trophy.so/blog/duolingo-gamification-case-study).

#### 8. Freedom and identity

Thin: avatar customisation with seasonal suits, a chosen daily goal, course choice, and username
(https://en.wikipedia.org/wiki/Duolingo). You cannot name, decorate or arrange anything that
persists.

#### 9. Signature interaction

The **streak flame ticking over to the next number**, with its milestone animation — Duolingo
explicitly designs for this moment, adding animations to make extending a streak "feel as satisfying
as possible" (https://blog.duolingo.com/how-duolingo-streak-builds-habit). Running a close second is
Duo the owl's notification, which became a cultural artefact: the owl was memed as "stalking" users
and the company leaned in with April Fools' campaigns and a Saturday Night Live parody
(https://en.wikipedia.org/wiki/Duolingo).

#### 10. UI type and art

**Minimal stat/figure** with character. A vertical path of lesson nodes, a top bar of streak, gems
and energy, and a bottom tab bar; lessons are full-screen single-question cards. Art: flat, bright,
high-contrast vector illustration with a cast of named characters and heavy animation on Duo. The
screen is **sparse per view** but the app is **dense in aggregate** — streak, gems, energy, league,
daily quests, friend streaks and achievements all compete for the same top bar. Home screen = the
lesson path plus the streak flame, gem count, energy and current league icon.

#### 11. Sound and feel

Duolingo's feedback design is its most copied feature: correct-answer chimes, the wrong-answer buzz,
full-screen celebration animations, and milestone streak animations credited with a **+1.7%** lift
in 7-day retention (https://blog.duolingo.com/how-duolingo-streak-builds-habit). League results
arrive as a full-screen "League Results" animation with push notifications tied to ranking changes
(https://duolingo.deconstructoroffun.com/mechanics/leagues). Specific haptic patterns: **not
confirmed**.

#### 12. Scale and reception

- App Store GB on 27 Oct 2026: **4.70 stars from 993,536 ratings**
  (https://itunes.apple.com/lookup?id=570060128&country=gb).
- Play Store GB: **500M+ downloads** (https://play.google.com/store/apps/details?id=com.duolingo&hl=en_GB).
- Launched 2012; $1.04bn revenue and $414.1m net income in 2025; 130m MAU; 10.9m paying subscribers
  (https://en.wikipedia.org/wiki/Duolingo).
- Business model: free with ads, Super Duolingo, Duolingo Max, and gem purchases.

Three complaints:
1. The streak punishes life events and support cannot fix it — "Lost my 595 day streak because of a
   funeral :(" (2,900 upvotes,
   https://www.reddit.com/r/duolingo/comments/1qw74yh/lost_my_595_day_streak_because_of_a_funeral/),
   and "Cannot reach support--streak lost" (2,449 upvotes,
   https://www.reddit.com/r/duolingo/comments/1pr8h89/cannot_reach_supportstreak_lost/).
2. The game displaces the learning — critics note you can become "better at protecting a
   language-learning streak than actually learning the language", and that "a 1,000-day streak means
   you opened an app 1,000 times, but it doesn't mean you can have a conversation"; a 2023 study
   found Duolingo English learners "did not significantly learn much grammar"
   (https://intelligentfly.news/duolingo-gamification-language-learning/,
   https://spellings.app/blog/duolingo-effect, https://en.wikipedia.org/wiki/Duolingo). A GB
   reviewer puts it mildly: it "should only be one weapon in your arsenal of language learning"
   (https://apps.apple.com/gb/app/duolingo-language-chess/id570060128, forefix, 12/01/2024).
3. Hearts punished the thing learning requires — "learning a language requires making mistakes, and
   punishing someone for getting a conjugation wrong by 'locking' them out of the app is the
   opposite of how the brain learns"
   (https://screenwiseapp.com/guides/duolingo-and-language-learning-apps); a paywalled timer change
   drew the same objection — "The flash card frenzy time has now been reduced making it impossible
   to complete… really frustrating when you're paying the full price"
   (https://apps.apple.com/gb/app/duolingo-language-chess/id570060128, anandac03, 27 Sept). An
   academic case study documents the general failure mode: "When Gamification Spoils Your Learning"
   (https://arxiv.org/pdf/2203.16175). The 2025 "AI-first" announcement produced "mass
   unsubscriptions and streak cancellations in protest" (https://en.wikipedia.org/wiki/Duolingo).

Three things loved:
1. The streak genuinely builds the habit, by Duolingo's own numbers: 6+ million users on 7+ day
   streaks, and 7-day-streak users completing courses at 3.6x the rate
   (https://blog.duolingo.com/how-duolingo-streak-builds-habit).
2. The forgiveness mechanics are appreciated and measurably effective — two equippable freezes
   (+0.38% DAU), the Weekend Amulet (4% more likely to return, 5% less likely to lose a streak)
   (https://blog.duolingo.com/how-duolingo-streak-builds-habit,
   https://blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals/).
3. The feel of it — "Duolingo's gameification makes learning fun and easy to keep coming back"
   (https://apps.apple.com/gb/app/duolingo-language-chess/id570060128, forefix, 12/01/2024), and
   "This app is amazing!… the best language app I have ever used" (same page, 5 Oct).

#### 13. Lesson for RepGarden

Duolingo is the skeleton everyone copies, and RepGarden should copy the forgiveness research and
reject the "daily" in daily streak. Duolingo's own data is an argument for slack: two freezes raised
daily actives, the Weekend Amulet made people more likely to return and less likely to break, and
binge sessions predicted abandonment. Translated to a gym app whose rest days are prescribed by the
trainer, the streak unit must be **sessions done against sessions planned in a week** — Benji's
programme defines the denominator, so the rest day is a scheduled zero, not a miss. Take the widget,
the milestone animation and the front-loaded motivation finding (50% from day 2 to 3 against 0.5%
from day 200 to 201, so celebrate early and often and stop inflating late milestones). Avoid three
things: hearts or energy, which punish failed reps in a place where failing reps is the point;
leagues, where "There's no week the user can skip" would be a liability for clients training twice a
week next to clients training five times; and any mechanic whose loss cannot be undone, because the
highest-upvoted posts in r/duolingo are funerals, surgery and outages.

---

### Across the lane

- **A bank beats a streak for absence.** Pokémon GO's ten-year returner still had "a couple hundred
  original 2016 Pokemon sitting safely in my storage"; Walkr's planets keep producing coins while
  you are away; Pikmin Bloom never kills anything. Meanwhile Duolingo's most upvoted posts are
  streak losses caused by a funeral, surgery and an internet shutdown, and Sweatcoin sells streak
  restoration for £0.99. (Pokémon GO, Walkr, Pikmin Bloom vs Duolingo, Sweatcoin)
- **Where decay exists at all, it punishes over-farming, not absence.** The only decay worth copying
  in the lane is Pikmin Bloom's withered state — harvest the same Pikmin six times in two hours and
  its flowers vanish, and it recovers when you walk 1,800 steps. Impermanence elsewhere is the
  world, not the player: planted flowers clear after 5 days, expeditions expire in 3. (Pikmin Bloom)
- **Endogenous currency is load-bearing, and players notice instantly when it is faked.** Pikmin
  Bloom's petals -> flowers -> fruit loop closes; Walkr's energy only buys more galaxy. Zombies
  Run's supplies look endogenous but a sympathetic reviewer calls the collection "pointless" because
  upgrades "produce no tangible effects", and Sweatcoin's external currency gets priced at 1–5 cents
  and backfilled with lotteries. (Pikmin Bloom, Walkr vs Zombies Run, Sweatcoin)
- **Opt-in risk works when loss is capped and failure is not failure.** The zombie chase is
  optional, tunable from 10–30% faster, and being caught costs one item and "will not cause you to
  'fail' a mission". Duolingo's Streak Wager raised day-7 retention 14% by letting people stake
  their own currency. Nothing in the lane imposes involuntary loss and survives it well. (Zombies
  Run, Duolingo)
- **Co-operative social retains; ranked social churns.** Pikmin Bloom's Weekly Challenges pay
  "participation prizes" when a group misses its shared goal, 30 players can hit one mushroom
  together, and Walkr's co-pilots, fleets and labs all grant fuel. Duolingo's leagues demote the
  bottom and promise "no week the user can skip" — effective at +25% lesson completion, and the
  thing that makes a slower learner's week feel like a failure. (Pikmin Bloom, Walkr vs Duolingo)
- **Two-speed sessions are the norm: a passive glance plus one sit-down.** Background accrual via
  HealthKit or Adventure Sync, a home-screen widget, and then one longer moment — Pikmin Bloom's 9pm
  lookback, Pokémon GO's weekly fitness report, Zombies Run's post-run Base Builder, Walkr's
  collect-and-boost. (all six)
- **The retrospective is the most undervalued mechanic in the lane.** Pikmin Bloom's nightly
  lookback animates your steps, offers a photo from your camera roll, lets you rate the day with a
  face, and rolls up on Sunday with a steps graph and a places-visited map; Pokémon GO sends a
  weekly fitness report. It costs the game nothing, needs no content, and is the only mechanic here
  that makes the player feel seen rather than scored. (Pikmin Bloom, Pokémon GO)
- **Punishing mistakes is the one design choice everyone now regrets.** Duolingo's hearts locked
  learners out for wrong answers and were replaced in May 2025 by Energy, explicitly reframed as
  rewarding correct answers instead of punishing errors; Pikmin Bloom removed death and night from a
  series built on both. (Duolingo, Pikmin Bloom)
- **Timed quotas turn calm players into quitters.** Pikmin Bloom's best-argued complaint is from a
  player who loved walking "at my own pace" until events demanded fixed amounts in short windows;
  Pokémon GO's longest-running grievance is paid tickets and compressed event windows. A surge
  (Community Day's three hours, with announced bonuses and nothing lost by skipping it) is the safe
  version. (Pikmin Bloom, Pokémon GO)
- **Story outperforms systems, and costs more.** Zombies Run has the thinnest game layer, no streak
  and almost no social features, and holds the lane's highest rating (4.76) on 500+ missions of
  written and voiced content. The reward is "so much fun you'll forget you're working out" — bought
  with writing, not mechanics. (Zombies Run)
- **Rating as a signal of pressure.** The two apps with the hardest unprotected demands sit lowest
  and most contested: Pokémon GO at 4.10 from 96,457 GB ratings, Sweatcoin at 4.49. The forgiving
  ones sit highest: Zombies Run 4.76, Pikmin Bloom 4.75, Duolingo 4.70, Walkr 4.59. (all six)

---

