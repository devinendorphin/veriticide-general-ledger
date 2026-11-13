import re, json, sys, random, itertools, pathlib, statistics as st
T=pathlib.Path(sys.argv[1]); OUT=pathlib.Path(sys.argv[2]); random.seed(20261112); NPERM=10000
def norm(t): return " ".join(t.lower().replace("’","'").replace("“",'"').replace("”",'"').split())
D={p.stem: norm(p.read_text()) for p in sorted(T.glob("*.txt"))}
R=lambda p: (lambda t: re.search(p,t) is not None)
M={ # marker: (family, test)
 "gross sexual imposition":("MPC",R(r"gross sexual imposition")),
 "deviate sexual intercourse":("MPC",R(r"deviate sexual intercourse")),
 "compels ... to submit":("MPC",R(r"compels?\b.{0,60}\bto submit")),
 "substantially impaired ... power to appraise or control":("MPC",R(r"substantially impaired.{0,200}power to appraise or control|power to appraise or control.{0,200}substantially impaired")),
 "criminal sexual conduct":("MI",R(r"criminal sexual conduct")),
 "however slight":("MI",R(r"however slight")),
 "personal injury":("MI",R(r"personal injury")),
 "force or coercion":("MI",R(r"force or coercion")),
 "lack of consent results from":("NY",R(r"lack of consent results from")),
 "forcible compulsion":("NY",R(r"forcible compulsion")),
 "clearly expressed":("NY",R(r"clearly expressed")),
 "physically helpless":("NY",R(r"physically helpless")),
 "mentally disabled/defective":("NY",R(r"mentally (disabled|defective)")),
 "mentally incapacitated":("NY",R(r"mentally incapacitated")),
 "freely given agreement":("AFF",R(r"freely given agreement")),
 "words or overt actions":("AFF",R(r"words or overt actions")),
 "actual words or conduct":("AFF",R(r"actual words or conduct")),
 "manner of dress":("AFF",R(r"manner of dress")),
 "lack of verbal or physical resistance":("AFF",R(r"lack of verbal or physical resistance")),
 "withdraws consent":("AFF",R(r"withdraws consent")),
 "sexual act":("FED",R(r"sexual act\b")),
 "aggravated sexual abuse":("FED",R(r"aggravated sexual abuse")),
 "renders ... unconscious":("FED",R(r"renders?\b.{0,80}\bunconscious")),
 "knowingly engages":("FED",R(r"knowingly engages")),
 "carnal knowledge":("CL",R(r"carnal knowledge")),
 "against her/his/the will":("CL",R(r"against (her|his|the) will")),
 "ravish":("CL",R(r"\bravish")),
 "no matter how slight":("UN",R(r"no matter how slight")),
 "sexual battery":("UN",R(r"sexual battery")),
 "intimate parts":("UN",R(r"intimate parts")),
 "earnest/utmost resistance":("UN",R(r"(earnest|utmost) resistance")),
 "marital flag (read by hand)":("UN",R(r"spouse.{0,40}\b(not|exception|defense)\b|\b(not|exception|defense)\b.{0,40}spouse")),
}
S=list(D); X={m:[int(f(D[s])) for s in S] for m,(fam,f) in M.items()}
prev={m:sum(v) for m,v in X.items()}
keep=[m for m in M if 2<=prev[m]<len(S)]
def phi(a,b):
    n=len(a); n11=sum(x&y for x,y in zip(a,b)); n1=sum(a); m1=sum(b)
    d=(n1*(n-n1)*m1*(n-m1))**.5; return (n*n11-n1*m1)/d if d else 0.0
# Test 1
assigned=[m for m in keep if M[m][0]!="UN"]; fam={m:M[m][0] for m in assigned}
P={(a,b):phi(X[a],X[b]) for a,b in itertools.combinations(assigned,2)}
def stat(lab):
    w=[v for (a,b),v in P.items() if lab[a]==lab[b]]; bt=[v for (a,b),v in P.items() if lab[a]!=lab[b]]
    return (st.mean(w) if w else 0)-(st.mean(bt) if bt else 0), (st.mean(w) if w else None), (st.mean(bt) if bt else None), len(w), len(bt)
obs=stat(fam); labs=list(fam.values()); ge=0
for _ in range(NPERM):
    random.shuffle(labs); 
    if stat(dict(zip(assigned,labs)))[0]>=obs[0]: ge+=1
t1=dict(markers=len(assigned), within_pairs=obs[3], between_pairs=obs[4], mean_phi_within=round(obs[1],3), mean_phi_between=round(obs[2],3),
        diff=round(obs[0],3), p_one_sided=round((ge+1)/(NPERM+1),4))
# per-family within mean
t1["within_by_family"]={f:round(st.mean([v for (a,b),v in P.items() if fam[a]==fam[b]==f]),3) for f in sorted(set(labs)) if sum(1 for (a,b) in P if fam[a]==fam[b]==f)}
# Test 2 (curveball, rows=states, cols=kept markers)
rows=[{m for m in keep if X[m][i]} for i in range(len(S))]
def s2(rs): return sum(len(a&b)**2 for a,b in itertools.combinations(rs,2))
o2=s2(rows); cur=[set(r) for r in rows]; ge=0; null=[]
def curveball(rs,steps):
    for _ in range(steps):
        i,j=random.sample(range(len(rs)),2); a,b=rs[i],rs[j]; ua=list(a-b); ub=list(b-a)
        if not ua and not ub: continue
        pool=ua+ub; random.shuffle(pool); na=pool[:len(ua)]; nb=pool[len(ua):]
        rs[i]=(a&b)|set(na); rs[j]=(a&b)|set(nb)
curveball(cur,5000)
for _ in range(NPERM):
    curveball(cur,5*len(S)); v=s2(cur); null.append(v); ge+= v>=o2
t2=dict(statistic=o2, null_mean=round(st.mean(null),1), null_sd=round(st.pstdev(null),1), z=round((o2-st.mean(null))/st.pstdev(null),2), p_one_sided=round((ge+1)/(NPERM+1),4))
# Test 3 flags + dominant family
F3={"force":r"forcib|by force|physical force|forcible compulsion","resistance":r"resist"}
dom={}
for i,s in enumerate(S):
    c={}; 
    for m in assigned:
        if X[m][i]: c[fam[m]]=c.get(fam[m],0)+1
    mx=max(c.values()) if c else 0; top=[f for f,v in c.items() if v==mx]
    dom[s]= top[0] if len(top)==1 else ("none" if not c else "mixed:"+"/".join(sorted(top)))
t3={s:dict(dominant=dom[s], **{k:int(bool(re.search(p,D[s]))) for k,p in F3.items()}, marital_flag=X["marital flag (read by hand)"][S.index(s)]) for s in S}
out=dict(jurisdictions=S, n=len(S), prevalence={m:dict(family=M[m][0],n=prev[m],kept=m in keep,states=[S[i] for i,v in enumerate(X[m]) if v]) for m in M},
         test1=t1, test2=t2, test3=t3, phi_pairs={f"{a} | {b}":round(v,3) for (a,b),v in sorted(P.items(),key=lambda x:-x[1])})
json.dump(out,open(OUT,"w"),indent=1)
print("n",len(S)); [print(f"{M[m][0]:4s} {prev[m]:2d} {'K' if m in keep else '-'} {m}: {' '.join(out['prevalence'][m]['states'])}") for m in M]
print("T1",t1); print("T2",t2)
