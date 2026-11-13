import json,sys,re,pathlib,collections
S=pathlib.Path(sys.argv[1]); sys.path.insert(0,str(S/"tools"))
def words(t):
    t=t.lower().replace("’","'").replace("\n"," "); t=re.sub(r"[^a-z0-9' ]+"," ",t).replace("'",""); return t
STOP={"a","an","the","b","c","d","i","ii","iii","iv","v","s","1","2","3","4","or","and","of"}
SUB=[(r"title ix or this part","this policy"),(r"this part","this policy"),(r"postsecondary institutions?","university"),(r"recipients?","university"),
     (r"institutions?","university"),(r"victims?","complainant"),(r"universitys","university"),(r"persons","person"),(r"their","person"),(r"individuals?","person")]
def toks(t):
    for a,b in SUB: t=re.sub(rf"\b{a}\b",b,t)
    return [w for w in t.split() if w not in STOP]
def g(w,n=6): return {" ".join(w[i:i+n]) for i in range(len(w)-n+1)}
fed=set()
for f in ["reg2020.txt","reg2025.txt","clery_subD.txt","eeoc.txt"]: fed|=g(toks(words((S/f).read_text())))
C=json.load(open(S/"clusters_C.json")); res=collections.Counter(); rows=[]
for i,c in enumerate(C):
    gg=g(toks(c["text"])); f=len(gg&fed)/len(gg) if gg else 0
    cat="federal" if f>=0.5 else ("partial" if f>0 else "none")
    res[(c["n_schools"]>=3, cat)]+=1; rows.append(dict(i=i,n=c["n_schools"],fed=round(f,2),cat=cat,schools=c["schools"],words=c["words"],text=c["text"]))
json.dump(rows,open(S/"attrib_C.json","w"),indent=1)
for k,v in sorted(res.items()): print(("3+" if k[0] else "2 "),k[1],v)
print("words by cat:", {cat:sum(r["words"] for r in rows if r["cat"]==cat) for cat in ["federal","partial","none"]})
for r in rows:
    if r["cat"]!="federal" and r["n"]>=3: print(r)
