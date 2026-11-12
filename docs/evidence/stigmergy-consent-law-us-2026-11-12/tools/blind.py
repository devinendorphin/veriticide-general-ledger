import re,json,sys,itertools,collections,pathlib,random
T=pathlib.Path(sys.argv[1]); N=8; random.seed(3)
def w(t): t=re.sub(r"[^a-z0-9 ]+"," ",t.lower().replace("’","").replace("'","")); return t.split()
G={p.stem:set(" ".join(x[i:i+N]) for x in [w(p.read_text())] for i in range(len(x)-N+1)) for p in sorted(T.glob("*.txt"))}
c=collections.Counter(g for s in G.values() for g in s)
rare={g for g,k in c.items() if 2<=k<=4}   # shared by 2-4 jurisdictions: excludes near-universal boilerplate
pairs={(a,b):len(G[a]&G[b]&rare) for a,b in itertools.combinations(G,2)}
top=sorted(pairs.items(),key=lambda x:-x[1])[:20]
L=json.load(open(sys.argv[2])); dom={s:v["dominant"] for s,v in L["test3"].items()}
print("rare shared 8-grams:",len(rare)); 
for (a,b),k in top: print(f"{a}-{b} {k}  [{dom[a]} / {dom[b]}]")
# do pairs sharing a dominant family share more rare text than other pairs? permutation over state labels
same=lambda d:[k for (a,b),k in pairs.items() if d[a]==d[b] and not d[a].startswith(("none","mixed"))]
diff=lambda d:[k for (a,b),k in pairs.items() if not (d[a]==d[b] and not d[a].startswith(("none","mixed")))]
mean=lambda v:sum(v)/len(v)
obs=mean(same(dom))-mean(diff(dom)); keys=list(dom); vals=list(dom.values()); ge=0
for _ in range(10000):
    random.shuffle(vals); d=dict(zip(keys,vals)); ge+= (mean(same(d))-mean(diff(d)))>=obs
res=dict(n_rare=len(rare), mean_same_family_pairs=round(mean(same(dom)),1), mean_other_pairs=round(mean(diff(dom)),1), n_same=len(same(dom)), p=round((ge+1)/10001,4), top20=[[a,b,k] for (a,b),k in top])
json.dump(res,open(sys.argv[3],"w"),indent=1); print({k:v for k,v in res.items() if k!="top20"})
print("dominant:",dom)
