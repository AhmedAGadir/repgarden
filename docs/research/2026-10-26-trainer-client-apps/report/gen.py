import json, os, re
P=os.path.dirname(os.path.abspath(__file__)); L="file://"+P+"/logos"
F="file:///Users/ahmed/dev/gadirlabs-console/assets/brand/fonts/"
D=json.load(open("/Users/ahmed/dev/repgarden/docs/research/2026-10-26-trainer-client-apps/platforms.json"))
PL={p["name"]:p for p in D["platforms"] if p["name"]!="Sidekick"}
INK,VIO,LIT,MUTED,LINE,PAPER,RED,LIVE="#141B24","#6D28D9","#A78BFA","#7A8694","#D6DCE3","#F4F6F8","#B23A3A","#2E7D5B"
LOGO={"ABC Trainerize":"trainerize","TrueCoach":"truecoach","Everfit":"everfit","My PT Hub":"my-pt-hub","TrainHeroic":"trainheroic","Playbook":"playbook","FITR":"fitr","PT Distinction":"pt-distinction","TrainerFu":"trainerfu","Kahunas":"kahunas","Hevy Coach":"hevy-coach","CoachRx":"coachrx","FitBudd":"fitbudd","Exercise.com":"exercise-com"}
ORDER=["ABC Trainerize","TrueCoach","Everfit","My PT Hub","TrainHeroic","Playbook","FITR","PT Distinction","TrainerFu","Kahunas","Hevy Coach","CoachRx","FitBudd","Exercise.com"]
def logo(n,s=28): return f'<img src="{L}/{LOGO[n]}.png" style="width:{s}px;height:{s}px;border-radius:{s*0.22:.0f}px;vertical-align:middle;margin-right:8px">'
CSS=f'''
@font-face{{font-family:"Bricolage Grotesque";src:url("{F}BricolageGrotesque-Variable.ttf");font-weight:200 800}}
@font-face{{font-family:"IBM Plex Mono";src:url("{F}IBMPlexMono-Medium.ttf");font-weight:500}}
@font-face{{font-family:"Source Serif 4";src:url("{F}SourceSerif4-Variable.ttf");font-weight:200 900}}
@font-face{{font-family:"Source Serif 4";src:url("{F}SourceSerif4-Italic-Variable.ttf");font-weight:200 900;font-style:italic}}
@page{{size:A4;margin:0}} *{{box-sizing:border-box}} html,body{{margin:0;background:#fff}}
body{{font-family:"Source Serif 4",Georgia,serif;color:{INK};font-size:11pt;line-height:1.45;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.pg{{width:210mm;height:297mm;padding:18mm 18mm 16mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}}
.pg:last-child{{page-break-after:auto}}
h1,h2,h3,.disp{{font-family:"Bricolage Grotesque",sans-serif;font-weight:700;letter-spacing:-.025em;line-height:1.05;font-optical-sizing:none;font-variation-settings:"opsz" 96;margin:0}}
h1{{font-size:34pt}} h2{{font-size:22pt;margin-bottom:6mm}} h3{{font-size:13pt;margin:6mm 0 2mm}}
.mono{{font-family:"IBM Plex Mono",monospace;font-weight:500;letter-spacing:.08em;text-transform:uppercase;font-size:8pt;color:{MUTED}}}
.eb{{margin-bottom:3mm;color:{VIO}}}
p{{margin:0 0 3mm}} .lead{{font-size:12.5pt;line-height:1.4}}
.foot{{position:absolute;left:18mm;right:18mm;bottom:9mm;display:flex;justify-content:space-between;font-family:"IBM Plex Mono",monospace;font-size:7.5pt;color:{MUTED};letter-spacing:.06em;text-transform:uppercase}}
.wm{{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:11pt;letter-spacing:-.03em;color:{INK};text-transform:none}} .wm b{{color:{VIO}}}
table{{border-collapse:collapse;width:100%;font-size:9pt;line-height:1.3}} th{{text-align:left;font-family:"IBM Plex Mono",monospace;font-weight:500;font-size:7.5pt;letter-spacing:.06em;text-transform:uppercase;color:{MUTED};padding:0 6px 4px 0;border-bottom:1.5px solid {INK};vertical-align:bottom}}
table.dense td{{padding:3px 5px 3px 0;font-size:8.5pt}} table.dense th{{font-size:7pt}} table.nw td:first-child{{white-space:nowrap}} td{{padding:5px 6px 5px 0;border-bottom:1px solid {LINE};vertical-align:top}} td.c,th.c{{text-align:center}}
.tick{{color:{LIVE};font-weight:700}} .no{{color:{RED};font-weight:700}} .dash{{color:{MUTED}}}
.call{{background:{PAPER};border-left:4px solid {VIO};padding:4mm 5mm;margin:4mm 0;font-size:10.5pt}}
.grid3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm}} .grid2{{display:grid;grid-template-columns:1fr 1fr;gap:6mm}}
.card{{background:{PAPER};border-radius:3mm;padding:4mm}} .card .n{{font-family:"Bricolage Grotesque",sans-serif;font-weight:700;font-size:11pt;display:flex;align-items:center}} .card .d{{font-size:9pt;color:#4B5766;margin-top:2mm}}
.big{{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:30pt;letter-spacing:-.03em;color:{VIO};line-height:1}}
small,.small{{font-size:8.5pt;color:{MUTED}}}
'''
def page(body, n, section): return f'<div class="pg">{body}<div class="foot"><span>RepGarden · market research · 26 October 2026 · {section}</span><span class="wm">gadirlabs<b>.</b></span><span>{n}</span></div></div>'
def hbar(rows, maxv, w=520, label_w=150, unit="", color=VIO, fmt=lambda v: f"{v:,}"):
    h=22; out=[f'<svg width="{w}" height="{len(rows)*h+6}" font-family="IBM Plex Mono" font-size="9">']
    for i,(name,v,hollow) in enumerate(rows):
        y=i*h; bw=max(2,(v/maxv)*(w-label_w-70))
        fill = "none" if hollow else color; stroke = f'stroke="{color}" stroke-dasharray="3,3"' if hollow else ""
        out.append(f'<text x="{label_w-8}" y="{y+15}" text-anchor="end" fill="{INK}" font-family="Bricolage Grotesque" font-weight="600" font-size="10">{name}</text>')
        out.append(f'<rect x="{label_w}" y="{y+4}" width="{bw:.1f}" height="14" rx="3" fill="{fill}" {stroke}/>')
        out.append(f'<text x="{label_w+bw+6:.1f}" y="{y+15}" fill="{MUTED}">{fmt(v)}{unit}</text>')
    out.append("</svg>"); return "".join(out)
# ---------- data ----------
ios={n:(PL[n]["ios"] or {}).get("us_count") for n in ORDER}
ios["Hevy (consumer app)"]=100098
scale_rows=sorted([(n,v,False) for n,v in ios.items() if v],key=lambda r:-r[1])
play={"ABC Trainerize":"1m+","TrueCoach":"100k+","Everfit":"100k+","My PT Hub":"100k+","TrainHeroic":"500k+","Playbook":"500k+","FITR":"50k+","PT Distinction":"—","TrainerFu":"50k+","Kahunas":"100k+","Hevy Coach":"10k+","CoachRx":"10k+","FitBudd":"5k+","Exercise.com":"—"}
entry={"ABC Trainerize":(9,"$","Grow, 2 clients"),"TrueCoach":(26.34,"$","5 clients, annual rate"),"Everfit":(0,"$","5 clients, free forever"),"My PT Hub":(20,"£","3 clients"),"PT Distinction":(19.90,"$","3 clients"),"TrainHeroic":(9.99,"$","1 athlete"),"FITR":(14.99,"£","+ £3 per client"),"Hevy Coach":(25,"$","1–10 clients"),"Kahunas":(35,"$","25 clients"),"FitBudd":(15,"$","2 clients"),"TrainerFu":(29,"$","10 clients"),"CoachRx":(29,"$","1–5 clients")}
fifty={"TrueCoach":(136.99,"$",False),"My PT Hub":(59,"£",False),"PT Distinction":(89.90,"$",False),"TrainHeroic":(74.99,"$",False),"FITR":(164.99,"£",False),"Hevy Coach":(90,"$",False),"Kahunas":(69,"$",False),"FitBudd":(139,"$",False),"TrainerFu":(79,"$",True),"CoachRx":(79,"$",False),"ABC Trainerize":(100,"$",True),"Everfit":(100,"$",True)}
rate={"£":1.30,"$":1.0}
# ---------- pages ----------
exec(open(f'{P}/social.py').read())

exec(open(f'{P}/outcomes.py').read())

cover=f'''<div style="height:100%;display:flex;flex-direction:column;justify-content:space-between">
<div><div class="mono eb">Research · 26 October 2026</div>
<h1 style="font-size:42pt;max-width:150mm">The apps personal trainers use to coach their clients.</h1>
<p class="lead" style="margin-top:8mm;max-width:140mm">Fourteen platforms, read from their own pages and store listings on one day: who is big, what they charge, which ones are games, how a client films a set, and how each one finds its trainers. Written for the RepGarden build, and for Benji.</p></div>
<div style="display:flex;flex-wrap:wrap;gap:3mm;max-width:150mm">{"".join(logo(n,38).replace("margin-right:8px","margin:0") for n in ORDER)}</div>
<div><div class="mono">Prepared by</div><div class="wm" style="font-size:18pt">gadirlabs<b>.</b></div><div class="small">Ahmed Gadir · gadirlabs.io · Every figure is from a page read on 26 October 2026; company marketing figures are marked as such; anything that could not be confirmed is marked not verified.</div></div></div>'''
summary=f'''<div class="mono eb">Summary</div><h2>Three things the market tells us.</h2>
<div class="grid3" style="margin-bottom:6mm">
<div class="card"><div class="big">5<span style="font-size:14pt">of 14</span></div><div class="n" style="margin-top:2mm">let a client film a set</div><div class="d">TrueCoach, Everfit, PT Distinction, TrainHeroic and FITR. <b>None</b> let the trainer mark the video up: no drawing, no frame-by-frame, no reply pinned to a moment. The market leader, Trainerize, has no client upload at all.</div></div>
<div class="card"><div class="big">3<span style="font-size:14pt">of 14</span></div><div class="n" style="margin-top:2mm">have a real game layer</div><div class="d">Everfit, Trainerize and TrainHeroic: streaks, badges, leaderboards, challenges. Eight have essentially nothing. <b>No platform has points, levels or avatars.</b></div></div>
<div class="card"><div class="big">0<span style="font-size:14pt">of 14</span></div><div class="n" style="margin-top:2mm">bill clients through Apple</div><div class="d">Every trainer-side platform collects on the web, nearly always Stripe. Rakes run from nothing (Hevy Coach, Kahunas) to 5.99% (FITR).</div></div></div>
<p>The market splits into three kinds of business that look alike from the outside. The largest group is <b>trainer-side software</b>: the coach pays, invites their own clients, and the clients use the platform's app for free — Trainerize, TrueCoach, Everfit, My PT Hub, PT Distinction, FITR, Hevy Coach, Kahunas, FitBudd, TrainerFu and CoachRx all work this way, at every price from $9 to $700 a month. The second group <b>sells distribution rather than software</b>: TrainHeroic and Playbook acquire consumers and take a cut when a coach sells to them. The third is <b>gym management software</b> that includes coaching, where Exercise.com now sits.</p>
<p>The last two years have been consolidation: Garmin bought TrainHeroic in July 2026, Daxko bought Exercise.com, My PT Hub changed hands twice, and Trainerize and TrueCoach belong to larger groups. FITR, PT Distinction, Hevy, Kahunas, FitBudd and CoachRx are the independents left.</p>
<div class="call"><b>What it means for RepGarden.</b> Filming a set is table stakes among strength-focused tools; the review of that video is an open gap, and that is where "watch a set, reply" should be better than a chat thread. Gamification is a differentiator rather than hygiene, and the field is open for the mascots. Payments stay off the app, as everyone's do. And since eleven of fourteen acquire the trainer first, the marketing website is what sells RepGarden; the store listing is secondary.</div>
'''
whos=f'''<div class="mono eb">Who's who</div><h2>Fourteen platforms, three kinds of business.</h2>
<h3>Trainer-side software — the coach pays, the client is invited</h3>
<div class="grid2" style="gap:3mm 6mm">{"".join(f'<div style="display:flex;gap:3mm;align-items:flex-start;border-bottom:1px solid {LINE};padding:2mm 0"><div>{logo(n,30)}</div><div><b style="font-family:Bricolage Grotesque,sans-serif">{n}</b> <span class="small">· {PL[n]["audience"]}</span><div class="small" style="color:#4B5766">{d}</div></div></div>' for n,d in [
("ABC Trainerize","The biggest. Owned by ABC Fitness since 2020. Every feature as a paid add-on; no client video upload."),
("TrueCoach","Solo online trainers. Owned by Xplor. Video upload attached to the exercise; flat 5% on client billing."),
("Everfit","The strongest game layer and a free tier for five clients. Video comments tagged per exercise."),
("My PT Hub","UK-rooted, unlimited clients for £59. No game layer. Owned by Jonas Software since 2024."),
("FITR","Benji's tool. UK, CrossFit and HYROX lean, profitable, small store footprint. See page 15."),
("PT Distinction","Independent, every feature on every tier, video upload included. Sells from the trainer's own site."),
("Hevy Coach","Built on the 17m-user Hevy consumer app. No client billing, no game layer of its own."),
("Kahunas","Branded-app play, creator-fronted, no commission. 2.5 stars on Play from 257 reviews."),
("FitBudd","Sells the trainer their own store listing. 60 'alternative to X' pages. $3.4m seed."),
("TrainerFu","Simple and cheap. iOS app not updated since May 2025."),
("CoachRx","By OPEX; sells depth over volume; a $5,995 certificate includes the software."),
])}</div>
<h3>Distribution businesses — the consumer comes first</h3>
<div class="grid2" style="gap:3mm 6mm">{"".join(f'<div style="display:flex;gap:3mm;align-items:flex-start;border-bottom:1px solid {LINE};padding:2mm 0"><div>{logo(n,30)}</div><div><b style="font-family:Bricolage Grotesque,sans-serif">{n}</b><div class="small" style="color:#4B5766">{d}</div></div></div>' for n,d in [("TrainHeroic","Strength coaches and teams; a marketplace that takes 30% on sales it sources. Bought by Garmin, 22 July 2026."),("Playbook","Creators with audiences, not 1:1 trainers; keeps 20% of everything. Consumer pays $14.99 a month.")])}</div>
<h3>Gym software with coaching in it</h3>
<div style="display:flex;gap:3mm;align-items:flex-start;padding:2mm 0"><div>{logo("Exercise.com",30)}</div><div><b style="font-family:Bricolage Grotesque,sans-serif">Exercise.com</b><div class="small" style="color:#4B5766">Gyms and studios, each shipping its own branded app. Quote-only, no trial. Bought by Daxko, October 2025.</div></div></div>
<p class="small" style="margin-top:4mm">Also checked: <b>Sidekick</b> does not exist as a product; its domain is parked and for sale.</p>'''
scale=f'''<div class="mono eb">Scale</div><h2>How big each one really is.</h2>
<p>Companies' own trainer counts are not reliable — Everfit claims 380,000 coaches on 2,700 App Store ratings, Trainerize's "400,000+" has not changed since 2022, and TrueCoach's count has gone down. The honest signal is how many people have rated the client app, which only happens when a real client uses it.</p>
<h3>US App Store ratings on the client app, 26 October 2026</h3>
{hbar(scale_rows, 100098, w=560, label_w=160)}
<p class="small">Hevy's consumer app is shown because Hevy Coach's clients use it; Hevy Coach's own app has 4 ratings. PT Distinction has no Play listing; Exercise.com has no consumer scale by design. Social following tells a different story: TrainHeroic has the largest Instagram in the set and TrueCoach and Everfit both beat Trainerize (page 14).</p>
<h3>Google Play install bands</h3>
<div style="display:flex;flex-wrap:wrap;gap:2mm">{"".join(f'<div style="display:flex;align-items:center;background:{PAPER};border-radius:2mm;padding:1.5mm 3mm 1.5mm 2mm;font-size:9pt">{logo(n,18)}{n.replace("ABC ","")} <b style="margin-left:5px;font-family:IBM Plex Mono,monospace;color:{VIO}">{play[n]}</b></div>' for n in ORDER)}</div>
<div class="call" style="margin-top:6mm">Two platforms are a different size from what their numbers suggest. <b>TrainHeroic</b> has 500k+ Play installs on 1,836 iOS ratings because athletes come in through its marketplace, not through coaches. <b>FITR</b> claims 120,000 clients and £53m processed, but has 50k+ Play installs at 3.0 stars and fewer than 25 iOS ratings worldwide — its scale, if real, is not visible in the stores.</div>'''
pr_rows=[(n,round(entry[n][0]*rate[entry[n][1]],2),False) for n in entry]; pr_rows.sort(key=lambda r:r[1])
f_rows=[(n,round(fifty[n][0]*rate[fifty[n][1]],2),fifty[n][2]) for n in fifty]; f_rows.sort(key=lambda r:r[1])
prices=f'''<div class="mono eb">Prices</div><h2>What a trainer pays.</h2>
<p>Almost everyone charges the trainer a monthly subscription that rises with the number of clients, and gives the client the app free. Sterling prices are shown in dollars at $1.30 for comparison; the originals are on the next table. Free trials are universal — 14 or 30 days — and Everfit's free tier is the only permanent one with real function.</p>
<div class="grid2"><div><h3>Cheapest paid tier, per month</h3>{hbar(pr_rows, 40, w=270, label_w=105, fmt=lambda v: f"${v:g}")}</div>
<div><h3>At around 50 clients, per month</h3>{hbar(f_rows, 220, w=270, label_w=105, fmt=lambda v: f"${v:g}")}<div class="small">Dotted bars are estimates where the price at that step is not published.</div></div></div>
<table class="dense nw" style="margin-top:4mm"><tr><th>Platform</th><th>Model</th><th>Published prices</th><th class=c>Trial</th><th>Cut on client payments</th></tr>
{"".join(f"<tr><td>{logo(n,18)}<b>{n}</b></td><td>{m}</td><td>{p}</td><td class=c>{t}</td><td>{c}</td></tr>" for n,m,p,t,c in [
("ABC Trainerize","Per client band","Free (1) · $9 (2) · Pro from $23 · $248 (500). Add-ons $10–45/mo each","30 d","Stripe add-on $10/mo; % not verified"),
("TrueCoach","Per client band","$26 (5) · $58 (20) · $137 (50), annual rates","14 d","Flat 5%"),
("Everfit","Per client band","Free (5) · Pro $16–242 · Studio $88–358","30 d","3.15% + $0.30, plus $9/mo"),
("My PT Hub","Flat above entry","£20 (3) · £59 unlimited · £199 all add-ons","30 d","Stripe; % not stated"),
("PT Distinction","Base + per client","$19.90 (3) · $59.90 (25) · $89.90 (50)","1 mo","None — trainer's own Stripe or PayPal"),
("TrainHeroic","Per athlete band","$9.99 (1) → $399.99 (1,000)","14 d","No 1:1 billing; marketplace 30% or $1/client"),
("FITR","Per active client","£14.99 + £3.00 per client; unlimited option","14 d","5.99% plus Stripe's fees"),
("Hevy Coach","Per client band","$25 (1–10) → $700 (501–1,000)","30 d","No client billing"),
("Kahunas","Three tiers","$35 (25) · $69 (50) · $99 unlimited","14 d","None"),
("FitBudd","Base + per client","$15 (2) · $79 (20) · $149 + setup fees","30 d","Web, or Apple IAP on Super Pro"),
("TrainerFu","Per client band","$29 (10) → $250 (250); branded app +$75","14 d","Not named"),
("CoachRx","Three tiers","$29 (5) · $79 (50) · $199 (150)","14 d","Stripe")][:-1]
)}</table><p class="small" style="margin-top:2mm">Playbook charges the trainer nothing and keeps 20% of what their followers pay ($14.99 a month each, 7-day trial). Exercise.com publishes no prices and offers no trial.</p>'''
MSG={"ABC Trainerize":"1:1, group, video messages","TrueCoach":"1:1 in-app","Everfit":"1:1, per-exercise threads","My PT Hub":"1:1, community feed","TrainHeroic":"team chat","Playbook":"community threads","FITR":"1:1, community, bulk","PT Distinction":"1:1 and group","TrainerFu":"1:1","Kahunas":"1:1, video messages","Hevy Coach":"1:1","CoachRx":"1:1 with video","FitBudd":"1:1 with video","Exercise.com":"1:1, group"}
BILL={"ABC Trainerize":"web, Stripe add-on","TrueCoach":"web, Stripe, 5%","Everfit":"web, Stripe, 3.15%+$0.30","My PT Hub":"web, Stripe","TrainHeroic":"marketplace, 30%","Playbook":"platform keeps 20%","FITR":"web, FITR's Stripe, 5.99%","PT Distinction":"trainer's own Stripe/PayPal","TrainerFu":"web, not named","Kahunas":"web, no commission","Hevy Coach":"none","CoachRx":"web, Stripe","FitBudd":"web; Apple IAP on top tier","Exercise.com":"own processing"}
T=lambda b: '<span class="tick">✓</span>' if b is True else ('<span class="no">✕</span>' if b is False else '<span class="dash">?</span>')
feat=f'''<div class="mono eb">Features</div><h2>What they do, side by side.</h2>
<p>Read from each platform's own feature pages and help centres. A question mark means it could not be confirmed either way on 26 October 2026, which for several smaller platforms is itself informative.</p>
<table class="dense nw"><tr><th>Platform</th><th class=c>Client films<br>a set</th><th class=c>Trainer marks<br>the video up</th><th class=c>Programme →<br>workout → exercise</th><th class=c>Client<br>calendar</th><th class=c>Progress<br>dashboards</th><th class=c>Push</th><th>Messaging</th><th>Client payments</th></tr>
{"".join(f"<tr><td>{logo(n,18)}<b>{n}</b></td><td class=c>{T(PL[n]['features'].get('client_video_upload_of_sets'))}</td><td class=c>{T(PL[n]['features'].get('coach_video_annotation'))}</td><td class=c>{T(bool(PL[n]['features'].get('structure')))}</td><td class=c>{T(PL[n]['features'].get('client_calendar'))}</td><td class=c>{T(PL[n]['features'].get('progress_dashboards'))}</td><td class=c>{T(PL[n]['features'].get('push_notifications'))}</td><td class=small>{MSG[n]}</td><td class=small>{BILL[n]}</td></tr>" for n in ORDER)}</table>
<div class="call" style="margin-top:5mm"><b>The column that matters is the third one.</b> Nobody has a verified way for a trainer to annotate a client's video — draw on it, scrub it frame by frame, or pin a note to a moment. Where video review exists it is a comment thread under the clip. That is the feature RepGarden can own.</div>'''
G=lambda n,k: T(PL[n]["gamification"].get(k))
gam=f'''<div class="mono eb">Gamification</div><h2>Who has turned training into a game.</h2>
<p>Three have a genuine layer, several have one mechanic sitting unused, and eight have essentially nothing. Trainerize is the only one with points; nowhere in the market are levels, XP or avatars confirmed to exist.</p>
<table class="dense nw"><tr><th>Platform</th><th class=c>Game<br>layer</th><th class=c>Streaks</th><th class=c>Badges</th><th class=c>Points</th><th class=c>Leader-<br>boards</th><th class=c>Challenges</th><th class=c>Levels</th><th class=c>Avatars</th><th>What it actually looks like</th></tr>
{"".join(f"<tr><td>{logo(n,18)}<b>{n}</b></td><td class=c>{G(n,'has_game_layer')}</td><td class=c>{G(n,'streaks')}</td><td class=c>{G(n,'badges')}</td><td class=c>{G(n,'points')}</td><td class=c>{G(n,'leaderboards')}</td><td class=c>{G(n,'challenges')}</td><td class=c>{G(n,'levels')}</td><td class=c>{G(n,'avatars')}</td><td class=small>{d}</td></tr>" for n,d in [
("ABC Trainerize","Streaks, badges, milestones, leaderboard and threshold challenges with points, groups, high-fives"),("TrueCoach","Milestone badges and habits only"),("Everfit","Eleven leaderboard types, an AI push-up challenge that counts reps by camera, streak insights — challenges behind the paid Autoflow add-on"),("My PT Hub","Personal bests and a social feed"),("TrainHeroic","Team leaderboards on any exercise, a global StackUp percentile, weekly streaks, a million-pound club"),("Playbook","Community features only"),("FITR","Challenge leaderboards, habit progress bars; no streaks, points or badges"),("PT Distinction","None"),("TrainerFu","Habit challenges, one leaderboard"),("Kahunas","Habits, a login streak, a water tracker"),("Hevy Coach","Nothing of its own; the consumer app has a weekly streak and a follower leaderboard"),("CoachRx","One unmarketed streak counter"),("FitBudd","Challenges and leaderboards, Elite tier only"),("Exercise.com","Leaderboards and challenges")])}</table>
<div class="call" style="margin-top:5mm">Everfit is the one to study: eleven leaderboard types and a camera-counted challenge show what a well-funded team thought was worth building. Notice what none of them built — a character, a world, a sense of growing something. That is the vegetable garden's opening.</div>'''
video=f'''<div class="mono eb">The video of a set</div><h2>Where the gap is.</h2>
<div class="grid2"><div><h3>Five let a client film a set and send it</h3>
{"".join(f'<div style="display:flex;gap:3mm;padding:2mm 0;border-bottom:1px solid {LINE}"><div>{logo(n,26)}</div><div><b style="font-family:Bricolage Grotesque,sans-serif">{n}</b><div class="small" style="color:#4B5766">{d}</div></div></div>' for n,d in [("TrueCoach","200 MB, about a minute of phone video, attached to the exercise, not to chat"),("Everfit","Video comments during a workout, each tagged to its exercise; the coach replies in the same thread"),("PT Distinction","Billed on every tier: clients video their technique and it goes straight to the trainer"),("TrainHeroic","'Video review' is a headline coach feature"),("FITR","500 MB per file, attached to a training performance; coach comments trigger a push notification")])}</div>
<div><h3>And then it stops</h3><p>On every one of the five, the trainer's reply is a comment under the clip. None has a verified way to draw on the video, step through it frame by frame, slow it down, or pin a note to the second where the knee caves in. Third-party reviews mention slow-motion on TrueCoach; TrueCoach's own pages do not.</p>
<p>The market leader does not have the upload at all. ABC Trainerize's ideas portal shows the request "Allow clients to upload video of their form" marked <b>Closed</b> by staff on 4 June 2020: "this can already be done in the app by sending video messages."</p>
<p>Six more platforms — My PT Hub, Kahunas, FitBudd, Hevy Coach, TrainerFu, CoachRx — could not be confirmed as having it. All of them move video through chat.</p>
<div class="call"><b>So the upload is table stakes, and the review is the product.</b> If a client films a set, the thing that keeps them filming is what comes back. A reply that lands on the moment, not under the clip, is a feature nobody in this market has shipped.</div></div></div>'''
grow=f'''<div class="mono eb">How they grow</div><h2>The trainer first, always.</h2>
<p>On eleven of the fourteen the trainer is acquired first: the trainer pays, the client pays nothing, and the client cannot get in without an invitation or a purchase. TrueCoach's App Store listing puts it bluntly — "If you are downloading this app, you are a client of a trainer who has chosen to level up and subscribe." Hevy is the one consumer-first case with 17 million users, and it deliberately declines to sell coaches to them. Playbook and TrainHeroic are the two that transact with consumers and take a cut.</p>
<div class="grid2"><div><h3>Referral and affiliate schemes</h3><table><tr><th>Platform</th><th>What they pay</th></tr>{"".join(f"<tr><td>{logo(n,16)}{n}</td><td class=small>{d}</td></tr>" for n,d in [("ABC Trainerize","15% recurring, no cap, via PartnerStack; open to influencers"),("Everfit","10% of the referred coach's revenue for two years"),("My PT Hub","Up to 25% per sale; 10% monthly, 25% annual"),("TrueCoach","Up to $1,000 in credit, never cash; a hidden cash affiliate elsewhere"),("FitBudd","$50 bonus + 15% recurring for 12 months"),("Kahunas","$49 per coach after 60 days, plus a separate affiliate tier"),("CoachRx","$50 per signup, since April 2026"),("TrainHeroic","$100 finder's fee; coaches run their own affiliate links"),("Exercise.com","10%, net 60"),("FITR","None — 'no formal coach referral scheme at the moment'"),("TrainerFu","None")])}</table></div>
<div><h3>Faces, partnerships, channels</h3><p class="small" style="color:#4B5766"><b>Creators front the platform</b> at Playbook (named creators with revenue figures, staff who are themselves influencers), Kahunas (18 coaches with Instagram handles on the homepage) and TrainHeroic (named strength coaches in its marketplace — revenue-shared, not sponsored). FITR borrows athlete credibility through its investors: Mat Fraser and HWPO on the board.</p>
<p class="small" style="color:#4B5766"><b>Certification bodies</b> are a real channel for five: Trainerize with NASM and Precision Nutrition, TrueCoach with NASM, My PT Hub with CIMSPA and UK providers, CoachRx by selling its own certificate, TrainHeroic through NSCA pro deals.</p>
<p class="small" style="color:#4B5766"><b>Gyms and events</b>: FITR has PureGym (370+ sites, 90-day free trial for its trainers) and HYROX. Kahunas shows a PureGym logo too.</p>
<p class="small" style="color:#4B5766"><b>Search</b> is the universal channel, and FitBudd takes it furthest with 4,300 pages, sixty of them "alternative to X". Two platforms now optimise for AI assistants — Everfit publishes an llms.txt and FitBudd's pricing page offers "get an unbiased answer from ChatGPT".</p>
<p class="small" style="color:#4B5766"><b>Money</b>: Garmin bought TrainHeroic (22 Jul 2026); Daxko bought Exercise.com (23 Oct 2025); Jonas bought My PT Hub (Mar 2024, after EverCommerce paid $11.7m in 2020); ABC bought Trainerize (2020). FITR raised $1.2m (2022) and £1.5m (Dec 2025) and is profitable. Playbook raised $12.3m by 2020; FitBudd $3.4m in 2022.</p></div></div>'''
fitr=f'''<div class="mono eb">Benji's current tool</div><h2>{logo("FITR",40)}FITR, in detail.</h2>
<div class="grid2"><div>
<p><b>What it is.</b> A UK platform (Fitr. Holdings Limited, incorporated 2015, Stevenage registered office), now at coachwithfitr.com under the line "where your business works out". Founder Leon Cassidy. Investors include Maven and the five-time CrossFit Games champion Mat Fraser; a £1.5m round in December 2025 came with the note that it is already profitable.</p>
<p><b>Size.</b> Claims 120,000 clients and £53m processed. The stores say less: 50k+ Play installs at 3.0 stars from 74 reviews, and fewer than 25 App Store ratings across eight countries. 408 YouTube subscribers.</p>
<p><b>Price.</b> £14.99 a month plus £3 per active client, or an unlimited plan; 14-day trial; annual saves 20%. Client payments run through FITR's Stripe at <b>5.99%</b>. A custom app with its own store listing is $199.99 a month.</p>
<p><b>Getting in.</b> Invite-only and purchase-first: "Sign up to a program with your coach first, then download the Fitr Client app." There is no public marketplace and never was — the only way to see the client app without buying is Benji's invite.</p></div>
<div><h3>What it does</h3><table><tr><th>Feature</th><th>FITR</th></tr>{"".join(f"<tr><td>{a}</td><td class=small>{b}</td></tr>" for a,b in [("Programmes","Program → training day → sets & reps → exercise; tracks within a programme; supersets of up to ten"),("Exercise videos","Preloaded library; 'hundreds' on one page, '1,000+' on another"),("Client films a set","<b>Yes</b> — up to 500 MB, attached to a performance, with coach comments and a push on reply"),("Calendar","Yes"),("Progress","Personal records over time, body metrics, charts, challenge history"),("Push","Yes"),("Messaging","1:1, community, bulk; no voice notes, no WhatsApp"),("Habits","Lifestyle goals with reminders and a coach view of who needs a nudge"),("Nutrition","Macros set by the coach"),("Game layer","Challenge leaderboards and habit bars only — no streaks, points, badges, levels or avatars"),("Growth","No referral scheme; PureGym and HYROX partnerships; athlete investors")])}</table>
<div class="call" style="margin-top:4mm">Benji's complaint on the first call was that Fitr is clunky, not that it lacks features: the set upload exists, with coach comments and a push on reply. That sets the bar for RepGarden: the same loop, made light, with the reply landing on the moment.</div></div></div>'''
means=f'''<div class="mono eb">Method</div><h2>Where the numbers come from.</h2>
<div class="grid2"><div>
<p><b>What was read.</b> Fourteen platforms' own websites, pricing pages, help centres and blogs; their App Store and Google Play listings; Companies House and press releases for ownership and funding; the Internet Archive where a page had changed. All on 26 October 2026, by an agent working from a written brief, with every claim recorded against its source URL.</p>
<p><b>What counts as verified.</b> A feature is marked present only where the platform's own pages or help centre describe it. "Not verified" means it could not be found on 26 October, not that it does not exist; for the smaller platforms the absence of a help article is itself a finding. Third-party review sites were read but are not used as evidence of a feature.</p>
<p><b>Scale.</b> App Store rating counts are the US storefront on the day. Google Play gives install bands, not counts. Company figures for trainers and clients are reported as the company's own claims and are not relied on.</p>
<p><b>Prices.</b> As published on the day, monthly, in the platform's own currency. Where a chart compares them, sterling is converted at $1.30. Estimated points are drawn dotted.</p></div>
<div><p><b>Limits.</b> Nothing here comes from using the client apps; three are invite-only and could not be entered. Social follower counts and ad-library figures were read through the ScrapeCreators API on the same day; there is no TikTok ad library, so paid activity covers Meta, Google and LinkedIn only. A single day's reading of pricing pages will date; the platforms change their tiers often.</p>
<p><b>Platforms checked.</b> {", ".join(ORDER)}. Also checked and excluded: Sidekick, whose domain is parked.</p>
<p><b>The full record.</b> A 1,300-line findings document with a source for every claim, and a structured data file of all fourteen platforms, in the RepGarden repository at <span class="mono" style="text-transform:none;letter-spacing:0;color:{INK}">docs/research/2026-10-26-trainer-client-apps/</span>. This report is a reading of that record; where the two disagree, the record wins.</p>
<p><b>Decisions this report fed.</b> The MVP scope, the invite-only decision, the no-payments decision and the second-phase gamification direction are recorded in <span class="mono" style="text-transform:none;letter-spacing:0;color:{INK}">docs/mvp-scope.md</span> in the same repository, which is the one place they are kept current.</p>
<div class="call" style="margin-top:4mm"><b>Prepared by</b> Ahmed Gadir, GadirLabs, for the RepGarden build. gadirlabs.io</div></div></div>'''
pages=[cover]+[page(b,i+2,s) for i,(b,s) in enumerate([(goals,"Why this report"),(feat_out,"Outcome 1 · the app"),(grow_out,"Outcome 2 · growth"),(watch,"Outcome 3 · risks"),(gam_out,"Outcome 4 · the second phase"),(whos,"Who's who"),(scale,"Scale"),(prices,"Prices"),(feat,"Features"),(gam,"Gamification"),(video,"The video of a set"),(grow,"How they grow"),(social,"Social and paid reach"),(fitr,"FITR"),(means,"Method")])]
pages[0]=f'<div class="pg">{cover}</div>'
HTML=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
if os.environ.get("BLUR"):
    NAMES=["ABC Trainerize","Trainerize","TrueCoach","Everfit","My PT Hub","TrainHeroic","Playbook","FITR","Fitr","PT Distinction","TrainerFu","Kahunas FZC","Kahunas","Hevy Coach","Hevy","CoachRx","FitBudd","Exercise.com","Sidekick","Strong","Garmin","Daxko","Jonas Software","Jonas","EverCommerce","ABC Fitness","ABC","Xplor","PureGym","HYROX","OPEX","Mat Fraser","HWPO","Leon Cassidy","coachwithfitr.com","Fitr. Holdings Limited","Stevenage","AI Sky US Bidco Inc","StackUp","Autoflow","trainerize.me","NASM","Precision Nutrition","CIMSPA","PartnerStack","Maven","Optimum Performance Training LLC","openGym","Pond5"]
    pat=re.compile(r"\b("+"|".join(re.escape(n) for n in sorted(NAMES,key=len,reverse=True))+r")\b")
    def blur_html(seg): return pat.sub(lambda m: f'<span class="blur">{m.group(1)}</span>', seg)
    out=[]; insvg=False
    for part in re.split(r"(<[^>]+>)", HTML):
        if part.startswith("<"):
            if part.startswith("<svg"): insvg=True; part=part+'<defs><filter id="blurf"><feGaussianBlur stdDeviation="2.2"/></filter></defs>'
            elif part.startswith("</svg"): insvg=False
            elif part.startswith("<img "): part=part.replace("<img ",'<img class="lg" ',1)
            elif insvg and part.startswith("<text"): part=part[:-1]+' data-t="1">'
            out.append(part)
        else:
            if insvg:
                if pat.search(part):
                    # mark the preceding <text> for an SVG filter
                    for i in range(len(out)-1,-1,-1):
                        if out[i].startswith("<text"): out[i]=out[i].replace(' data-t="1">',' filter="url(#blurf)">'); break
                out.append(part)
            else: out.append(blur_html(part))
    HTML="".join(out).replace("</style>",".blur{filter:blur(4px)} img.lg{filter:blur(6px)}</style>",1)
open(f"{P}/../report.html","w").write(HTML)
print("html written,", len(pages), "pages")
