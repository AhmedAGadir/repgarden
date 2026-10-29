import re, sys
from html.parser import HTMLParser
src=open(sys.argv[1]).read()
src=re.sub(r"<svg.*?</svg>","",src,flags=re.S); src=re.sub(r"<img[^>]*>","",src); src=re.sub(r"<style>.*?</style>","",src,flags=re.S)
class M(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.stack=[]; s.row=None; s.rows=None; s.cell=None; s.hdr=False; s.skip=0
    def sink(s): return s.cell if s.cell is not None else s.out
    def handle_starttag(s,t,a):
        a=dict(a); c=a.get("class","") or ""
        s.stack.append((t,c))
        if t=="div" and "foot" in c: s.skip+=1; return
        if s.skip: return
        if t=="h1": s.out.append("\n\n# ")
        elif t=="h2": s.out.append("\n\n## ")
        elif t=="h3": s.out.append("\n\n### ")
        elif t=="p": s.out.append("\n\n")
        elif t=="div" and "mono" in c and "eb" in c: s.out.append("\n\n*")
        elif t=="div" and "card" in c: s.out.append("\n\n- ")
        elif t=="div" and "call" in c: s.out.append("\n\n> ")
        elif t=="div" and c=="n": s.out.append("**")
        elif t=="div" and c=="d": s.out.append(" ")
        elif t=="div": s.out.append(" ")
        elif t=="b": s.sink().append("**")
        elif t=="table": s.rows=[]
        elif t=="tr": s.row=[]
        elif t in("td","th"): s.cell=[]; s.hdr=(t=="th")
        elif t=="br": s.sink().append(" ")
    def handle_endtag(s,t):
        c=""
        for i in range(len(s.stack)-1,-1,-1):
            if s.stack[i][0]==t: c=s.stack[i][1]; del s.stack[i:]; break
        if t=="div" and "foot" in c: s.skip-=1; return
        if s.skip: return
        if t=="div" and "mono" in c and "eb" in c: s.out.append("*")
        elif t=="div" and c=="n": s.out.append("**")
        elif t=="b": s.sink().append("**")
        elif t in("td","th"):
            txt=re.sub(r"\s+"," ","".join(s.cell)).strip().replace("|","/"); s.row.append(txt); s.cell=None
        elif t=="tr": s.rows.append((s.row,s.hdr)); s.row=None
        elif t=="table":
            if s.rows:
                width=max(len(r) for r,_ in s.rows); lines=[]
                if not s.rows[0][1]: s.rows.insert(0,([""]*width,True))
                for i,(r,h) in enumerate(s.rows):
                    r=r+[""]*(width-len(r)); lines.append("| "+" | ".join(r)+" |")
                    if i==0: lines.append("|"+"---|"*width)
                s.out.append("\n\n"+"\n".join(lines)+"\n")
            s.rows=None
    def handle_data(s,d):
        if s.skip: return
        s.sink().append(d)
m=M(); m.feed(src); txt="".join(m.out)
txt=txt.replace("✓","yes").replace("✕","no")
txt=re.sub(r"[ \t]+"," ",txt); txt=re.sub(r" *\n *","\n",txt); txt=re.sub(r"\n{3,}","\n\n",txt).strip()
open(sys.argv[2],"w").write(txt+"\n")
# --- fixed additions: title note and the two chart data tables ---
t=open(sys.argv[2]).read()
t=t.replace("# What the best growing games do, and what a gym app can borrow.","# What the best growing games do, and what a gym app can borrow\n\nMarkdown twin of `report.pdf`, generated from the same source by `report/gen.py` and `report/tomd.py` on 27 October 2026. Charts are tables here; the data behind every figure is in `apps.json` and `report/store-meta.json`, and every claim's source is in `findings.md`.",1)
t=t.replace("### GB App Store ratings, 27 October 2026\n","### GB App Store ratings, 27 October 2026\n\n"+'| Game | GB ratings | Average |\n|---|---|---|\n| Duolingo | 993,193 | 4.70 |\n| Township | 263,895 | 4.72 |\n| Gardenscapes | 249,729 | 4.67 |\n| Pokémon GO | 96,457 | 4.10 |\n| Flora | 84,985 | 4.76 |\n| Finch | 78,607 | 4.93 |\n| Hay Day | 73,814 | 4.67 |\n| Sweatcoin | 71,224 | 4.49 |\n| FarmVille 2 | 27,054 | 4.61 |\n| Forest | 20,506 | 4.79 |\n| Plant Nanny | 10,392 | 4.70 |\n| Stardew Valley | 6,206 | 4.80 |\n| Pikmin Bloom | 5,821 | 4.75 |\n| Zombies, Run! | 4,725 | 4.76 |\n| Tamagotchi | 3,336 | 4.44 |\n| Neko Atsume | 2,965 | 4.74 |\n| Brainrot | 2,573 | 4.37 |\n| Pocket Camp | 1,134 | 4.74 |\n| Focus Friend | 733 | 4.75 |\n| Walkr | 630 | 4.59 |\n| Habitica | 378 | 4.04 |\n',1)
open(sys.argv[2],"w").write(t)
