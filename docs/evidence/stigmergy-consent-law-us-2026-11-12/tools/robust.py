import json,sys,itertools,random,statistics as st,re,pathlib
L=json.load(open(sys.argv[1])); T=pathlib.Path(sys.argv[2]); random.seed(7); S=L["jurisdictions"]
X={m:[int(s in v["states"]) for s in S] for m,v in L["prevalence"].items() if v["kept"] and v["family"]!="UN"}
fam={m:L["prevalence"][m]["family"] for m in X}
def phi(a,b):
    n=len(a); n11=sum(x&y for x,y in zip(a,b)); n1=sum(a); m1=sum(b); d=(n1*(n-n1)*m1*(n-m1))**.5; return (n*n11-n1*m1)/d if d else 0.0
def t1(ms, rows=None):
    rows = rows if rows is not None else list(range(len(S)))
    ms=[m for m in ms if 2<=sum(X[m][i] for i in rows)<len(rows)]
    P={(a,b):phi([X[a][i] for i in rows],[X[b][i] for i in rows]) for a,b in itertools.combinations(ms,2)}
    def stat(lab):
        w=[v for k,v in P.items() if lab[k[0]]==lab[k[1]]]; b=[v for k,v in P.items() if lab[k[0]]!=lab[k[1]]]
        return (st.mean(w) if w else 0)-(st.mean(b) if b else 0)
    lab={m:fam[m] for m in ms}; o=stat(lab); ls=list(lab.values()); ge=0
    for _ in range(5000):
        random.shuffle(ls); ge+= stat(dict(zip(ms,ls)))>=o
    return dict(n_markers=len(ms), n_states=len(rows), diff=round(o,3), p=round((ge+1)/5001,4))
allm=list(X); res={}
res["primary"]=t1(allm)
for f in sorted(set(fam.values())): res[f"drop family {f}"]=t1([m for m in allm if fam[m]!=f])
res["collapse NY incapacity trio to one"]=None
trio=["physically helpless","mentally incapacitated","mentally disabled/defective"]
X["NY incapacity trio (any)"]=[int(any(X[m][i] for m in trio)) for i in range(len(S))]; fam["NY incapacity trio (any)"]="NY"
res["collapse NY incapacity trio to one"]=t1([m for m in allm if m not in trio]+["NY incapacity trio (any)"])
res["drop markers in >50% of states"]=t1([m for m in allm if sum(X[m])<=len(S)/2])
D={s:(T/f"{s}.txt").read_text().lower() for s in S}
defrows=[i for i,s in enumerate(S) if re.search(r"definitions?\b",D[s])]
res["only states whose text includes a definitions section"]=t1(allm, defrows); res["  (states lacking one)"]=[s for i,s in enumerate(S) if i not in defrows]
json.dump(res,open(sys.argv[3],"w"),indent=1); [print(k,v) for k,v in res.items()]
