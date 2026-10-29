import json, os, urllib.request, time
from apps import APPS
OUT=os.path.dirname(os.path.abspath(__file__))
meta={}
def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
    return urllib.request.urlopen(req,timeout=60).read()
for slug,name,aid,grp in APPS:
    d=json.loads(get(f"https://itunes.apple.com/lookup?id={aid}&country=gb"))
    r=d["results"][0]
    icon=r["artworkUrl512"].replace("512x512bb","1024x1024bb")
    open(f"{OUT}/icons/{slug}.png","wb").write(get(icon))
    shots=r.get("screenshotUrls",[])[:6]
    files=[]
    for i,u in enumerate(shots):
        fn=f"{OUT}/shots/{slug}-{i+1}.png"
        try: open(fn,"wb").write(get(u)); files.append(os.path.basename(fn))
        except Exception as e: print("shot fail",slug,i,e)
    meta[slug]={"name":name,"id":aid,"group":grp,"track_name":r["trackName"],"seller":r["sellerName"],"rating":r.get("averageUserRating"),"count":r.get("userRatingCount"),"price":r.get("formattedPrice"),"released":r.get("releaseDate","")[:10],"current_version_date":r.get("currentVersionReleaseDate","")[:10],"genres":r.get("genres"),"shots":files,"icon_url":icon,"shot_urls":shots}
    print(slug, r["trackName"], r.get("userRatingCount"), len(files))
    time.sleep(0.4)
json.dump(meta,open(f"{OUT}/store-meta.json","w"),indent=1,ensure_ascii=False)
