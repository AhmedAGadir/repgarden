import json, re, urllib.request, time, os
OUT=os.path.dirname(os.path.abspath(__file__))
meta=json.load(open(f"{OUT}/store-meta.json"))
def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
    return urllib.request.urlopen(req,timeout=60).read()
for slug,m in meta.items():
    for i,u in enumerate(m["shot_urls"][:6]):
        v=re.sub(r"/\d+x\d+bb\.", "/1500x1500bb.", u)   # longest side 1500, keeps aspect
        fn=f"{OUT}/shots/{slug}-{i+1}.jpg"
        try:
            open(fn,"wb").write(get(v))
            old=f"{OUT}/shots/{slug}-{i+1}.png"
            if os.path.exists(old): os.remove(old)
        except Exception as e: print("fail",slug,i,e)
    m["shots"]=[f"{slug}-{i+1}.jpg" for i in range(len(m["shot_urls"][:6]))]
    time.sleep(0.2)
json.dump(meta,open(f"{OUT}/store-meta.json","w"),indent=1,ensure_ascii=False)
print("done")
