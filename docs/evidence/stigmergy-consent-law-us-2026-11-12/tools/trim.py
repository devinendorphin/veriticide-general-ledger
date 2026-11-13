import re,sys,pathlib
T=pathlib.Path(sys.argv[1])
CUT={"DE":(r"§\s*761\.",r"§\s*7(8[1-9]|9\d)\."),"NV":(r"NRS\s*200\.364",r"NRS\s*200\.38"),"OR":(r"163\.305",r"163\.5\d\d"),
     "SC":(r"16-3-651",r"16-3-7\d\d"),"WA":(r"9A\.44\.010",r"9A\.44\.12[89]"),"WY":(r"6-2-301",r"6-2-4\d\d")}
for st,(a,b) in CUT.items():
    t=(T/f"{st}.txt").read_text(); best=""
    for m in re.finditer(a,t):
        e=re.search(b,t[m.end():]); seg=t[m.start(): m.end()+(e.start() if e else len(t)-m.end())]
        if len(seg)>len(best): best=seg
    (T/f"{st}.txt").write_text(best); print(st,len(t.split()),"->",len(best.split()), "|", best[:80].replace("\n"," "))
