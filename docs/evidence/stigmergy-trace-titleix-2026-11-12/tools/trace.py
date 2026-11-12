import re, json, sys, itertools, collections, pathlib
S = pathlib.Path(sys.argv[1]); N = 12
DOCS = {"Illinois":"illinois","Indiana":"indiana","Iowa":"iowa3","Michigan":"michigan_emp","Minnesota":"minnesota",
        "Nebraska":"nebraska","Northwestern":"northwestern2","Ohio State":"ohiostate","Rutgers":"rutgers","Washington":"washington"}
def words(t):
    t = t.lower().replace("’","'").replace("‘","'")
    t = re.sub(r"[^a-z0-9' ]+"," ",t.replace("\n"," ")); t = t.replace("'","")
    return t.split()
def grams(w): return [" ".join(w[i:i+N]) for i in range(len(w)-N+1)]
r20 = set(grams(words((S/"reg2020.txt").read_text()))); r25 = set(grams(words((S/"reg2025.txt").read_text())))
rule = r20 | r25
clery = set(grams(words((S/"clery.txt").read_text())))
W = {k: words((S/"text"/f"{v}.txt").read_text()) for k,v in DOCS.items()}
G = {k: grams(w) for k,w in W.items()}; GS = {k:set(g) for k,g in G.items()}
out = {"n_schools":len(DOCS),"per_school":{}}
for k in DOCS:
    s = GS[k]; out["per_school"][k] = dict(words=len(W[k]), shingles=len(s),
        pct_rule2020=round(100*len(s&r20)/len(s),1), pct_rule2025=round(100*len(s&r25)/len(s),1),
        pct_either=round(100*len(s&rule)/len(s),1), pct_clery=round(100*len(s&clery)/len(s),1))
cnt = collections.Counter(g for s in GS.values() for g in s)
shared = {g for g,c in cnt.items() if c>=2 and g not in rule}
out["shared_nonmandated_shingles"] = len(shared)
out["shared_in_clery"] = len(shared & clery)
pair = {}
for a,b in itertools.combinations(DOCS,2):
    pair[f"{a}|{b}"] = len((GS[a]&GS[b])-rule)
out["pairs"] = dict(sorted(pair.items(), key=lambda x:-x[1]))
# runs and clusters
parent = {}
def find(x):
    while parent.setdefault(x,x)!=x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
def union(a,b): parent[find(a)]=find(b)
runs = []
for k,g in G.items():
    i=0
    while i < len(g):
        if g[i] in shared:
            j=i
            while j+1<len(g) and g[j+1] in shared: j+=1
            runs.append((k,i,j)); 
            for x in range(i,j): union(g[x],g[x+1])
            i=j+1
        else: i+=1
cl = collections.defaultdict(lambda: {"schools":set(),"shingles":set(),"best":""})
for k,i,j in runs:
    root = find(G[k][i]); c = cl[root]; c["schools"].add(k); c["shingles"].update(G[k][i:j+1])
    txt = " ".join(W[k][i:j+N]); 
    if len(txt)>len(c["best"]): c["best"]=txt
clusters = []
for c in cl.values():
    sh=c["shingles"]; clusters.append(dict(n_schools=len(c["schools"]), schools=sorted(c["schools"]),
        words=len(c["best"].split()), clery_frac=round(len(sh&clery)/len(sh),2), text=c["best"]))
clusters.sort(key=lambda c:(-c["n_schools"],-c["words"]))
out["n_clusters"]=len(clusters)
out["clusters_by_breadth"]=dict(collections.Counter(c["n_schools"] for c in clusters))
json.dump(out, open(sys.argv[2],"w"), indent=1)
json.dump(clusters, open(sys.argv[3],"w"), indent=1)
print(json.dumps({k:v for k,v in out.items() if k!="pairs"}, indent=1)); print("top pairs", list(out["pairs"].items())[:12])
