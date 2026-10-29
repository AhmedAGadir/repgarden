import os, re, sys
from common import *
exec(open(f"{P}/front.py").read())
exec(open(f"{P}/evidence_fixed.py").read())
exec(open(f"{P}/evidence.py").read())
PAGES=[(goals,"Why this report"),(theme,"Why a theme"),(uitypes,"The screen")]+EVIDENCE+[(scale,"Scale"),(streaks,"Streaks"),(means,"Method")]
try:
    exec(open(f"{P}/outcomes.py").read()); exec(open(f"{P}/evidence.py").read())
    PAGES=[(goals,"Why this report"),(summary,"Summary"),(story,"Decision 1 · the story"),(unit,"Decision 2 · the unit of play"),(absence,"Decision 3 · absence"),(economy,"Decision 4 · the economy"),(uitypes,"Decision 5 · the screen"),(mechanics,"Decision 6 · mechanics"),(cut,"Decision 7 · the MVP cut"),(theme,"Why a theme")]+EVIDENCE+[(scale,"Scale"),(streaks,"Streaks"),(means,"Method")]
except FileNotFoundError as e: print("partial build:", e)
pages=[f'<div class="pg">{cover}</div>']+[page(b,i+2,s) for i,(b,s) in enumerate(PAGES)]
HTML=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
if os.environ.get("BLUR"):
    NAMES=sorted(set(list(SHORT.values())+[m["name"] for m in META.values()]+["Stardew","Supercell","Zynga","Playrix","Nintendo","Animal Crossing","Pocket Camp","Hit-Point","Bandai Namco","Seekrtech","AppFinca","Sparkful","HabitRPG","Hank Green","Smolworks","Niantic","Scopely","Six to Start","Duolingo","Roblox","The Garden Game","Halfbrick","Taito","ConcernedApe","Pikmin","Pokémon","Pokemon","Sweatcoin","Walkr","Fourdesire","Finch Care","Township","Hay Day","FarmVille","Gardenscapes","Neko Atsume","Tamagotchi","Habitica","Forest","Flora","Plant Nanny","Focus Friend","Brainrot","Zombies, Run!","Grow a Garden","Fruit Ninja","Chess.com","Space Invaders","Lose It","Insight Timer"]),key=len,reverse=True)
    pat=re.compile(r"(?<![\w])("+"|".join(re.escape(n) for n in NAMES)+r")(?![\w])")
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
                    for i in range(len(out)-1,-1,-1):
                        if out[i].startswith("<text"): out[i]=out[i].replace(' data-t="1">',' filter="url(#blurf)">'); break
                out.append(part)
            else: out.append(blur_html(part))
    HTML="".join(out).replace("</style>",".blur{filter:blur(4px)} img.lg{filter:blur(8px)}</style>",1)
open(f"{P}/../report.html","w").write(HTML); print("html written,", len(pages), "pages")
