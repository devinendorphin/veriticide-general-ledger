import re, json, sys, itertools, collections, pathlib
S = pathlib.Path(sys.argv[1]); N = 12
DOCS = {"Illinois":"illinois","Indiana":"indiana","Iowa":"iowa3","Michigan":"michigan_emp","Minnesota":"minnesota",
        "Nebraska":"nebraska","Northwestern":"northwestern2","Ohio State":"ohiostate","Rutgers":"rutgers","Washington":"washington"}
NAMES = {"Illinois":["university of illinois urbana champaign","university of illinois","illinois"],
 "Indiana":["indiana university","iu"],"Iowa":["university of iowa"],"Michigan":["university of michigan","u m"],
 "Minnesota":["university of minnesota"],"Nebraska":["university of nebraska"],"Northwestern":["northwestern university","northwestern"],
 "Ohio State":["the ohio state university","ohio state university","ohio state"],"Rutgers":["rutgers the state university of new jersey","rutgers university","rutgers"],
 "Washington":["university of washington","uw"]}
def words(t):
    t = t.lower().replace("’","'").replace("‘","'").replace("\n"," ")
    t = re.sub(r"[^a-z0-9' ]+"," ",t).replace("'","")
    return " ".join(t.split())
def norm(t, school=None):
    if school:
        for n in NAMES[school]: t = re.sub(rf"\b{n}\b","university",t)
    for a,b in [(r"title ix or this part","this policy"),(r"this part","this policy"),(r"postsecondary institutions?","university"),
                (r"recipients?","university"),(r"institutions?","university"),(r"victims?","complainant"),(r"the university university","the university")]:
        t = re.sub(rf"\b{a}\b",b,t)
    return t
def grams(s): w=s.split(); return [" ".join(w[i:i+N]) for i in range(len(w)-N+1)], w
R = lambda f: words((S/f).read_text())
def run(level):
    nb = level in "BC"
    rule = set()
    srcs = ["reg2020.txt","reg2025.txt"] + (["clery_subD.txt","eeoc.txt"] if level=="C" else [])
    for f in srcs: rule |= set(grams(norm(R(f)) if nb else R(f))[0])
    G,W = {},{}
    for k,v in DOCS.items():
        t = R(f"text/{v}.txt"); G[k],W[k] = grams(norm(t,k) if nb else t)
    GS = {k:set(g) for k,g in G.items()}
    cnt = collections.Counter(g for s in GS.values() for g in s)
    shared = {g for g,c in cnt.items() if c>=2 and g not in rule}
    per = {k: dict(pct_mandated=round(100*len(GS[k]&rule)/len(GS[k]),1),
                   pct_shared_nonmandated=round(100*len(GS[k]&shared)/len(GS[k]),2)) for k in DOCS}
    parent={}
    def find(x):
        while parent.setdefault(x,x)!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    runs=[]
    for k,g in G.items():
        i=0
        while i<len(g):
            if g[i] in shared:
                j=i
                while j+1<len(g) and g[j+1] in shared: j+=1
                runs.append((k,i,j))
                for x in range(i,j): parent[find(g[x])]=find(g[x+1])
                i=j+1
            else: i+=1
    cl=collections.defaultdict(lambda:{"schools":set(),"sh":set(),"best":""})
    for k,i,j in runs:
        c=cl[find(G[k][i])]; c["schools"].add(k); c["sh"].update(G[k][i:j+1])
        t=" ".join(W[k][i:j+N]); c["best"]=max(c["best"],t,key=len)
    C=sorted([dict(n_schools=len(c["schools"]),schools=sorted(c["schools"]),n_shingles=len(c["sh"]),words=len(c["best"].split()),text=c["best"]) for c in cl.values()],
             key=lambda c:(-c["n_schools"],-c["words"]))
    return dict(level=level, sources=srcs, shared_nonmandated_shingles=len(shared), n_clusters=len(C),
                clusters_by_breadth=dict(sorted(collections.Counter(c["n_schools"] for c in C).items())),
                words_in_clusters_3plus=sum(c["words"] for c in C if c["n_schools"]>=3), per_school=per), C
out={}
for L in "ABC":
    s,C = run(L); out[L]=s; json.dump(C,open(S/f"clusters_{L}.json","w"),indent=1)
    print(L, {k:v for k,v in s.items() if k!="per_school"})
json.dump(out,open(S/"trace_levels.json","w"),indent=1)
print(json.dumps({k:(out["A"]["per_school"][k]["pct_mandated"],out["C"]["per_school"][k]["pct_mandated"],out["C"]["per_school"][k]["pct_shared_nonmandated"]) for k in DOCS}))
