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
t=t.replace("# The apps personal trainers use to coach their clients.","# The apps personal trainers use to coach their clients\n\nMarkdown twin of `report.pdf`, generated from the same source by `report/gen.py` and `report/tomd.py` on 26 October 2026. The charts in the PDF are tables here; the data behind every figure is in `platforms.json`, and every claim's source is in `findings.md`.",1)
t=t.replace("### US App Store ratings on the client app, 26 October 2026\n","### US App Store ratings on the client app, 26 October 2026\n\n| Platform | US ratings |\n|---|---|\n| Hevy (consumer app) | 100,098 |\n| ABC Trainerize | 34,300 |\n| TrueCoach | 7,100 |\n| Everfit | 2,700 |\n| My PT Hub | 2,300 |\n| TrainHeroic | 1,836 |\n| Playbook | 1,100 |\n| Kahunas | 600 |\n| PT Distinction | 450 |\n| TrainerFu | 300 |\n| CoachRx | 100 |\n| FitBudd | 60 |\n| FITR | 25 |\n| Hevy Coach | 4 |\n",1)
t=t.replace("### Platforms with each mechanic, of 14\n","### Platforms with each mechanic, of 14\n\n| Mechanic | Platforms |\n|---|---|\n| Habit checklist | 9 |\n| Leaderboards | 5 |\n| Challenges | 5 |\n| Streaks | 4 |\n| Badges | 2 |\n| Points | 1 |\n| Levels or XP | 0 |\n| Avatars, a character | 0 |\n| A world that grows | 0 |\n",1)
open(sys.argv[2],"w").write(t)
