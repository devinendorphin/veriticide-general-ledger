import sys,re,html,pathlib,json
O=pathlib.Path(sys.argv[1]); T=pathlib.Path(sys.argv[2]); T.mkdir(exist_ok=True); rep={}
for d in sorted(p for p in O.iterdir() if p.is_dir()):
    out=[]
    for f in sorted(d.glob("*.html")):
        s=f.read_text(errors="replace"); s=re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>',' ',s); t=html.unescape(re.sub(r'(?s)<[^>]+>',' ',s)); t=re.sub(r'\s+',' ',t)
        i=re.search(r'Updated by Find[Ll]aw Staff',t); 
        if not i: rep[f"{d.name}/{f.stem}"]="NO BODY"; continue
        b=t[i.end():]; j=re.search(r'Previous Part of Code|FindLaw Codes may not reflect|Back to Chapter List',b); b=b[:j.start()] if j else b
        out.append(b); rep[f"{d.name}/{f.stem}"]=len(b.split())
    (T/f"{d.name}.txt").write_text("\n".join(out))
print(json.dumps(rep))
