import json, os, re, html
P=os.path.dirname(os.path.abspath(__file__)); R="file://"+P
F="file:///Users/ahmed/dev/gadirlabs-console/assets/brand/fonts/"
INK,VIO,LIT,MUTED,LINE,PAPER,RED,LIVE="#141B24","#6D28D9","#A78BFA","#7A8694","#D6DCE3","#F4F6F8","#B23A3A","#2E7D5B"
META=json.load(open(f"{P}/store-meta.json"))
DATE="27 October 2026"
SHORT={"stardew":"Stardew Valley","hayday":"Hay Day","farmville2":"FarmVille 2","township":"Township","gardenscapes":"Gardenscapes","pocketcamp":"Pocket Camp","neko":"Neko Atsume","tamagotchi":"Tamagotchi","growagarden":"Grow a Garden",
"finch":"Finch","forest":"Forest","flora":"Flora","plantnanny":"Plant Nanny","habitica":"Habitica","focusfriend":"Focus Friend","brainrot":"Brainrot",
"pikmin":"Pikmin Bloom","pokemongo":"Pokémon GO","zombiesrun":"Zombies, Run!","walkr":"Walkr","sweatcoin":"Sweatcoin","duolingo":"Duolingo","fruitninja":"Fruit Ninja","chess":"Chess.com"}
FARM=["growagarden","stardew","hayday","farmville2","township","gardenscapes","pocketcamp","neko","tamagotchi"]
HABIT=["finch","forest","flora","plantnanny","habitica","focusfriend","brainrot"]
FIT=["pikmin","pokemongo","zombiesrun","walkr","sweatcoin","duolingo"]
ALL=FARM+HABIT+FIT
def icon(slug,s=28,mr=8):
    return f'<img src="{R}/icons/{slug}.png" style="width:{s}px;height:{s}px;border-radius:{s*0.22:.0f}px;vertical-align:middle;margin-right:{mr}px;flex:none">'
def shot(slug,n=1,h=70,radius=2.5):
    """a phone/landscape screenshot framed; h in mm"""
    return f'<img src="{R}/shots/{slug}-{n}.jpg" style="height:{h}mm;border-radius:{radius}mm;border:1px solid {LINE};display:block">'
def named(slug,s=22): return f'<span style="display:inline-flex;align-items:center;white-space:nowrap">{icon(slug,s,6)}<b style="font-family:Bricolage Grotesque,sans-serif">{SHORT[slug]}</b></span>'
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
h1{{font-size:34pt}} h2{{font-size:22pt;margin-bottom:5mm}} h3{{font-size:12.5pt;margin:5mm 0 2mm}}
.mono{{font-family:"IBM Plex Mono",monospace;font-weight:500;letter-spacing:.08em;text-transform:uppercase;font-size:8pt;color:{MUTED}}}
.eb{{margin-bottom:3mm;color:{VIO}}}
p{{margin:0 0 3mm}} .lead{{font-size:12.5pt;line-height:1.4}}
.foot{{position:absolute;left:18mm;right:18mm;bottom:9mm;display:flex;justify-content:space-between;font-family:"IBM Plex Mono",monospace;font-size:7.5pt;color:{MUTED};letter-spacing:.06em;text-transform:uppercase}}
.wm{{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:11pt;letter-spacing:-.03em;color:{INK};text-transform:none}} .wm b{{color:{VIO}}}
table{{border-collapse:collapse;width:100%;font-size:9pt;line-height:1.3}} th{{text-align:left;font-family:"IBM Plex Mono",monospace;font-weight:500;font-size:7.5pt;letter-spacing:.06em;text-transform:uppercase;color:{MUTED};padding:0 6px 4px 0;border-bottom:1.5px solid {INK};vertical-align:bottom}}
table.dense td{{padding:3px 5px 3px 0;font-size:8.5pt}} table.dense th{{font-size:7pt}} table.xd td{{padding:2.5px 4px 2.5px 0;font-size:8pt;line-height:1.25}} table.nw td:first-child{{white-space:nowrap}} td{{padding:5px 6px 5px 0;border-bottom:1px solid {LINE};vertical-align:top}} td.c,th.c{{text-align:center}}
.tick{{color:{LIVE};font-weight:700}} .no{{color:{RED};font-weight:700}} .dash{{color:{MUTED}}} .warn{{color:#B7791F;font-weight:700}}
.call{{background:{PAPER};border-left:4px solid {VIO};padding:4mm 5mm;margin:4mm 0;font-size:10.5pt}}
.grid3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm}} .grid2{{display:grid;grid-template-columns:1fr 1fr;gap:6mm}} .grid4{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}} .grid6{{display:grid;grid-template-columns:repeat(6,1fr);gap:3mm}}
.card{{background:{PAPER};border-radius:3mm;padding:4mm}} .card .n{{font-family:"Bricolage Grotesque",sans-serif;font-weight:700;font-size:11pt;display:flex;align-items:center}} .card .d{{font-size:9pt;color:#4B5766;margin-top:2mm}}
.big{{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:30pt;letter-spacing:-.03em;color:{VIO};line-height:1}}
small,.small{{font-size:8.5pt;color:{MUTED}}} .dim{{color:#4B5766}}
.q{{font-style:italic;font-size:9.5pt;line-height:1.35;color:#2A3440}} .q .who{{font-style:normal;font-family:"IBM Plex Mono",monospace;font-size:7pt;letter-spacing:.06em;text-transform:uppercase;color:{MUTED};display:block;margin-top:1mm}}
.chip{{display:inline-flex;align-items:center;background:{PAPER};border-radius:2mm;padding:1mm 2.5mm 1mm 1.5mm;font-size:8.5pt;margin:0 1.5mm 1.5mm 0;white-space:nowrap}}
.tag{{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:7pt;letter-spacing:.06em;text-transform:uppercase;padding:.6mm 1.8mm;border-radius:1.2mm;background:{PAPER};color:{MUTED};vertical-align:middle}}
.tag.v{{background:#EDE9FE;color:{VIO}}} .tag.g{{background:#E3F2EA;color:{LIVE}}} .tag.r{{background:#F8E5E5;color:{RED}}} .tag.y{{background:#FBF1DC;color:#B7791F}}
.fig{{font-family:"IBM Plex Mono",monospace;font-size:7.5pt;color:{MUTED};margin-top:1.5mm;line-height:1.3}}
'''
def page(body, n, section): return f'<div class="pg">{body}<div class="foot"><span>RepGarden · game design research · {DATE} · {section}</span><span class="wm">gadirlabs<b>.</b></span><span>{n}</span></div></div>'
def hbar(rows, maxv, w=520, label_w=150, unit="", color=VIO, fmt=lambda v: f"{v:,}", h=22):
    out=[f'<svg width="{w}" height="{len(rows)*h+6}" font-family="IBM Plex Mono" font-size="9">']
    for i,(name,v,hollow) in enumerate(rows):
        y=i*h; bw=max(2,(v/maxv)*(w-label_w-70))
        fill = "none" if hollow else color; stroke = f'stroke="{color}" stroke-dasharray="3,3"' if hollow else ""
        out.append(f'<text x="{label_w-8}" y="{y+15}" text-anchor="end" fill="{INK}" font-family="Bricolage Grotesque" font-weight="600" font-size="10">{name}</text>')
        out.append(f'<rect x="{label_w}" y="{y+4}" width="{bw:.1f}" height="14" rx="3" fill="{fill}" {stroke}/>')
        out.append(f'<text x="{label_w+bw+6:.1f}" y="{y+15}" fill="{MUTED}">{fmt(v)}{unit}</text>')
    out.append("</svg>"); return "".join(out)
T=lambda b: '<span class="tick">✓</span>' if b is True else ('<span class="no">✕</span>' if b is False else ('<span class="warn">~</span>' if b=="~" else '<span class="dash">?</span>'))
