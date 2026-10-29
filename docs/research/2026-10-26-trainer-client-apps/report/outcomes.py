def cnt(k):
    return sum(1 for n in ORDER if PL[n]["gamification"].get(k) is True)
ladder=[("Habit checklist",cnt("habit_tracking"),"a list of daily things to tick"),("Leaderboards",cnt("leaderboards"),"ranked lists of clients"),("Challenges",cnt("challenges"),"a time-boxed contest, usually with a leaderboard"),("Streaks",cnt("streaks"),"consecutive days or weeks, reset on a miss"),("Badges",cnt("badges"),"a milestone sticker"),("Points",cnt("points"),"a score for doing things"),("Levels or XP",0,"progression that unlocks something"),("Avatars, a character",0,"someone to be"),("A world that grows",0,"somewhere to be")]
goals=f'''<div class="mono eb">Why this report</div><h2>What we wanted to know, and what we found.</h2>
<p class="lead">RepGarden is being built for Benji, a personal trainer, and his clients. Before the first screen is drawn, this report answers six questions about the apps trainers already use, so that the feature list, the second-phase game design and the way RepGarden finds trainers rest on what the market does rather than on guesses.</p>
<table style="margin:4mm 0 6mm"><tr><th style="width:46%">The question</th><th>The short answer</th></tr>
{"".join(f"<tr><td><b>{q}</b></td><td>{a}</td></tr>" for q,a in [
("Who are the platforms, and how big are they really?","Fourteen that matter, in three kinds of business. Company trainer counts are inflated; store ratings are the honest signal. Pages 7–8."),
("What do they charge, and whom?","The trainer, per client band, from $9 to $700 a month; clients pay nothing; nobody bills clients through Apple. Page 9."),
("Which features are standard, and which are rare?","Programmes, libraries, calendars, push and chat are universal. A client filming a set is on five of fourteen. A trainer marking that video up is on none. Pages 10 and 12."),
("How do they gamify, if at all?","Thinly. Three have a real layer, built from habit lists, leaderboards, streaks and badges. Nobody has levels, a character or a world. Pages 6 and 11."),
("How do they find trainers and clients?","The trainer first, on eleven of fourteen. Referral schemes, certification bodies, gyms, search, named faces, and paid ads that all sell a free trial. Pages 13–14."),
("Is this a business anyone pays for?","Yes: four acquisitions in six years, one profitable UK independent, and a crowded, cheap middle. Page 5.")]
)}</table>
<h3>What the report changes</h3>
<div class="grid3">
<div class="card"><div class="n">The feature list holds, with one sharpening</div><div class="d">Everything in the MVP is either standard or the gap. The sharpening: the reply to a client's video must land on a moment in the clip, because that is the one thing nobody has. Page 3.</div></div>
<div class="card"><div class="n">The website sells to trainers</div><div class="d">Clients never find these apps on their own. The marketing site, Benji as its first face, and later a referral scheme are the growth plan; the store listing is for approval. Page 4.</div></div>
<div class="card"><div class="n">The second phase has no one to copy</div><div class="d">The market's gamification stops at streaks and leaderboards. A garden that grows with a client's training is a different kind of thing, and the evidence says it is unoccupied. Page 6.</div></div></div>
<p class="small" style="margin-top:5mm">Pages 2–6 are the outcomes. Pages 7–15 are the evidence, platform by platform. Page 16 is the method. Every figure was read on 26 October 2026 from the platform's own pages or store listing; marketing claims are marked as such.</p>'''
feat_out=f'''<div class="mono eb">Outcome 1 · The app</div><h2>Are our features the right ones?</h2>
<p>The MVP list was written from Benji's call before the research. Set against fourteen platforms, it holds.</p>
<table class="dense"><tr><th style="width:27%">In the MVP</th><th style="width:47%">What the market does</th><th style="width:26%">Verdict</th></tr>
{"".join(f"<tr><td><b>{a}</b></td><td class=small style='color:#4B5766'>{b}</td><td class=small>{c}</td></tr>" for a,b,c in [
("Invite-only accounts; trainer and client roles","Eleven of fourteen work exactly this way; TrueCoach's listing tells clients they are there because their trainer subscribed","<span class=tick>Keep</span>"),
("Exercise → workout → programme, assigned to dates","Universal. Everfit and TrainHeroic add a block or section level inside the workout; Trainerize sells reusable templates","<span class=tick>Keep</span>. Copying a programme is expected"),
("A stock exercise library, the trainer's own clips on top, a fallback image","Every platform ships a library of 1,000+ stock clips and lets the trainer add their own. The same shape; where the stock library comes from is being researched","<span class=tick>Keep</span>"),
("Calendar first; today's workout; log sets; mark complete","Universal. Rest days and empty days are blank on most apps","<span class=tick>Keep</span>"),
("Film a set, with a note; trainer replies on that set","Upload on five of fourteen, FITR included (500 MB). The reply is a comment under the clip everywhere; no drawing, scrubbing or pinned moment anywhere","<span class=tick>Keep, sharpen</span>. See below"),
("Per-client progress: adherence, loads, personal bests","Standard. PB tracking is what My PT Hub calls gamification; Hevy sends a live PR notification","<span class=tick>Keep</span>. The PR moment deserves a screen"),
("Push for a scheduled workout; a nudge after a miss","Standard, and TrainerFu's coach-side 'streaks broken' alert shows the trainer wants to know too","<span class=tick>Keep</span>. Add the trainer's view of who missed"),
("Accessibility from the first screen","Not marketed by any platform, and ratings of 2.5–3.0 on two of them say app quality is uneven","<span class=tick>Keep</span>. A quiet advantage"),
])}</table>
<div class="grid2" style="margin-top:3mm"><div><h3 style="margin-top:3mm">Add, or bring forward</h3>
<p class="small" style="color:#4B5766"><b>The reply lands on a moment.</b> A timestamp on the trainer's note, a tap that jumps there, and a mark of approval. This is the whole difference between RepGarden's video and FITR's, and it is cheap. Design it now, not in phase two.</p>
<p class="small" style="color:#4B5766"><b>A habit checklist.</b> Nine of fourteen have one; it is the cheapest mechanic in the market and the natural first thing a garden grows from. Not for the MVP, but the data model should expect it.</p>
<p class="small" style="color:#4B5766"><b>Check-ins: photos and body metrics.</b> On six or more platforms. Agreed in; the detail is scoped with Benji.</p>
<p class="small" style="color:#4B5766"><b>The trainer's inbox of sets.</b> A list of clips waiting for a reply, oldest first. Nobody shows this well, and it is what makes the review feature survive.</p></div>
<div><h3 style="margin-top:3mm">Leave out, confirmed</h3>
<p class="small" style="color:#4B5766"><b>Messaging.</b> Every platform has it, and Benji's clients still use WhatsApp. Everfit's per-exercise comment threads are the one idea worth noting, and the reply-on-a-set covers it.</p>
<p class="small" style="color:#4B5766"><b>Payments.</b> Nobody bills clients through the app; everyone collects on the web via Stripe. Out now, web-only later.</p>
<p class="small" style="color:#4B5766"><b>Nutrition, AI form analysis, localisation, bookings, a marketplace.</b> Nothing in the research argues for any of them in a first version. Everfit's camera-counted push-up challenge is the only AI feature with any novelty, and it is a stunt.</p>
<p class="small" style="color:#4B5766"><b>Remove: nothing.</b> The list was already short; the research argues for keeping it that way and spending the saved effort on the reply and on the calendar's empty days.</p></div></div>'''
grow_out=f'''<div class="mono eb">Outcome 2 · Growth</div><h2>How RepGarden finds its trainers.</h2>
<p class="lead">The trainer is the customer and the client is a guest. Eleven of fourteen platforms acquire the trainer first; the client pays nothing and arrives by invitation. That settles where the effort goes.</p>
<div class="grid2"><div>
<h3>What this means now</h3>
<p><b>The marketing website is the product's front door,</b> and it speaks to trainers. Its job is to make a trainer want to move their clients onto RepGarden; the store listing exists to get approved and to be the thing the invited client taps.</p>
<p><b>Benji is the first face.</b> Kahunas puts eighteen coaches with their Instagram handles on its homepage; Playbook fronts named creators with their earnings; TrainHeroic sells named strength coaches. The honest version of that is one real trainer whose clients use the app, saying what changed.</p>
<p><b>Lead with the two things nobody else has,</b> in this order: the reply that lands on the moment in a client's set, then the garden. Across 318 active Meta ads from eight platforms, not one leads with form review, video feedback or technique; every one sells a free trial and less admin. Everything else on the feature page is a tick in a column every competitor can also tick.</p></div>
<div><h3>Channels, when there are trainers to send</h3>
<table><tr><th>Channel</th><th>Precedent</th><th>For RepGarden</th></tr>{"".join(f"<tr><td><b>{a}</b></td><td class=small>{b}</td><td class=small>{c}</td></tr>" for a,b,c in [
("Referral","10–25% recurring is the norm; FITR has none","An opening against FITR; set up once a second trainer exists"),
("Gyms","FITR gives PureGym's trainers a 90-day trial; Kahunas shows the same logo","Benji's own gym first; the chain later"),
("Certification bodies","NASM, Precision Nutrition, CIMSPA deals on five platforms","CIMSPA is the UK route"),
("Search","FitBudd runs 60 'alternative to X' pages; Everfit publishes an llms.txt","'RepGarden vs FITR' and one page per competitor, written honestly"),
("Events","FITR and HYROX","Benji's sport, if he has one"),
("Social and ads","Eight platforms run 318 Meta ads between them, all at trainers, every one selling a free trial; Hevy buys nothing and has the biggest following","Not yet. When there is a trainer to sell to, lead with the thing no ad mentions: the video reply")])}</table>
<div class="call" style="margin-top:4mm"><b>One warning.</b> Hevy has 17 million consumer users and a coach product bolted on. If Benji's clients already log workouts in Hevy or Strong, RepGarden is competing with a free logger they like, and the trainer loop — the reply, the programme, the garden — has to be visibly better than what they lose.</div></div></div>'''
watch=f'''<div class="mono eb">Outcome 3 · Risks, and the business</div><h2>Things to watch out for.</h2>
<div class="grid2"><div>
<p><b>Fitr already has the upload.</b> Benji's complaint on the first call was that Fitr is clunky to use, and Fitr's own pages confirm the feature exists: 500 MB per file, coach comments, a push on reply. So the contest is on the review experience, not the upload. Filming a set and getting a reply has to feel light, and the reply has to land on the moment.</p>
<p><b>Video storage is the one cost that grows.</b> FITR allows 500 MB per file. The proposed rule — delete seven days after the trainer has viewed it, thirty days regardless, keep the data and a poster frame — needs deciding before the first upload, and the client needs one line telling them.</p>
<p><b>User-generated content rules.</b> Both stores treat a client's clip as UGC even when only the trainer sees it: report and block, terms before the first upload, published contact details. These are in the scope already; they must not slip.</p>
<p><b>Price is not a moat.</b> Trainerize starts at $9, Everfit is free for five clients, and every platform runs a 14–30 day trial. A trainer can leave for almost nothing. The reason to stay has to be the clients liking the app.</p>
<p><b>App quality is uneven and noticed.</b> Kahunas is at 2.5 stars on Play from 257 reviews, FITR at 3.0, and TrainerFu's iOS app has not shipped since May 2025. Clients rate the app they are made to use. A client app that is simply pleasant is itself a selling point to trainers.</p>
<p><b>Some trainers distrust game mechanics.</b> CoachRx sells "depth over volume, a relationship not a transaction" and hides its own streak counter. The garden must read as coaching made visible, not a toy bolted onto a logger.</p></div>
<div><h3>Is this a business?</h3>
<p>Not the main point, since the decision to build is made, but the research says something about it.</p>
<p>Money has moved in this category for six years: EverCommerce paid $11.7m for My PT Hub in 2020 and Jonas bought it in 2024; ABC bought Trainerize in 2020; Daxko bought Exercise.com in October 2025; Garmin bought TrainHeroic in July 2026. FITR, the UK independent nearest to RepGarden, raised £1.5m in December 2025 and is profitable. Everfit funds a free tier and an engineering team from per-client subscriptions. The model — a trainer paying $15–30 a month at entry, rising with clients, no cut on their payments — is proven on eleven platforms.</p>
<p>It is also crowded and cheap in the middle, where a UK trainer choosing between FITR, My PT Hub and Trainerize is choosing on feel. A new entrant does not win there on features. It wins with one reason to switch that can be said in a sentence, and with trainers who bring other trainers. The research gives RepGarden the sentence; Benji and the build series are the first trainers.</p>
<div class="call"><b>The viability test for later</b> is not revenue. It is whether a second trainer, one Benji did not bring, moves their clients onto RepGarden and keeps them there past the first month. Until then it is a product for one trainer, which is what it was scoped to be.</div></div></div>'''
gam_out=f'''<div class="mono eb">Outcome 4 · The second phase</div><h2>What the market calls gamification.</h2>
<p class="lead">Fourteen platforms were checked for nine mechanics, from the simplest to the kind that makes an app a game. The count falls off a cliff after the fourth rung.</p>
<div class="grid2" style="grid-template-columns:1.15fr 1fr"><div>
<h3>Platforms with each mechanic, of 14</h3>
{hbar([(n,v,False) for n,v,_ in ladder], 14, w=330, label_w=128, fmt=lambda v: f"{v}")}
<p class="small">Hevy's consumer app, which Hevy Coach's clients use, has a weekly streak and a follower leaderboard of its own; it is not counted above. "Challenges" on My PT Hub and PT Distinction are names for marketing programmes, not mechanics, and are not counted.</p></div>
<div><h3>What each one actually is</h3><table><tr><th>Mechanic</th><th>In plain words</th></tr>{"".join(f"<tr><td><b>{n}</b></td><td class=small>{d}</td></tr>" for n,_,d in ladder)}</table></div></div>
<h3>What the three "real" layers are made of</h3>
<p class="small" style="color:#4B5766"><b>Trainerize</b>: streaks and badges on habits, leaderboard and threshold challenges where clients "earn points by working out, achieving personal bests, completing habits", groups, high-fives in messages. <b>Everfit</b>: eleven leaderboard types, streak insights on habits (current, best, daily average), challenges behind a paid add-on, and a push-up challenge counted by the phone camera. <b>TrainHeroic</b>: team leaderboards on any exercise, a global percentile called StackUp, weekly streaks, virtual fist bumps, and a badge for lifting a million pounds in total.</p>
<div class="call"><b>The finding, in one sentence:</b> the whole market's idea of a game is a scoreboard: a number that goes up, a list that ranks you, a chain you must not break. Nothing has a character, a place, or anything that grows and can be tended. Those are the mechanics that make people open an app when nobody is making them, and in this market they are untouched.</div>'''
