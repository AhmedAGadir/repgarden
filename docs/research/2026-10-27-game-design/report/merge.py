# merge the three lanes' apps.json into ../apps.json, keyed by slug, with store-meta attached
import json, glob, os, re, sys
P=os.path.dirname(os.path.abspath(__file__))
LANES=sys.argv[1] if len(sys.argv)>1 else "/private/tmp/claude-501/-Users-ahmed-dev-gadirlabs-console/bd209fed-b6d1-47d3-b3e5-922d6cc1ed38/scratchpad/gamedesign/lanes"
META=json.load(open(f"{P}/store-meta.json"))
KEY={"stardew":["stardew"],"hayday":["hay day"],"farmville2":["farmville"],"township":["township"],"gardenscapes":["gardenscapes"],"pocketcamp":["pocket camp","animal crossing"],"neko":["neko"],"tamagotchi":["tamagotchi"],"growagarden":["grow a garden"],
"finch":["finch"],"forest":["forest"],"flora":["flora"],"plantnanny":["plant nanny"],"habitica":["habitica"],"focusfriend":["focus friend"],"brainrot":["brainrot"],
"pikmin":["pikmin"],"pokemongo":["pokémon go","pokemon go"],"zombiesrun":["zombies"],"duolingo":["duolingo"],"walkr":["walkr"],"sweatcoin":["sweatcoin"]}
def slug_of(name):
    n=name.lower()
    for s,ks in KEY.items():
        if any(k in n for k in ks): return s
    return None
out={}
for lane in sorted(glob.glob(f"{LANES}/*/apps.json")):
    for a in json.load(open(lane)):
        s=slug_of(a["name"])
        if not s: print("unmatched", a["name"]); continue
        a["slug"]=s; a["lane"]=os.path.basename(os.path.dirname(lane)); a["store"]=META.get(s,{})
        out[s]=a
json.dump(out,open(f"{P}/../apps.json","w"),indent=1,ensure_ascii=False)
print("merged", len(out), sorted(out))
