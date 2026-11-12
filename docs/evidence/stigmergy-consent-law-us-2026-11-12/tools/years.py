import json,re,sys,pathlib
C=pathlib.Path(sys.argv[1]); L=json.load(open(C/"lineage49.json"))
MK={"criminal sexual conduct":r"criminal sexual conduct","personal injury":r"personal injury","force or coercion":r"force or coercion","however slight":r"however slight",
 "lack of consent results from":r"lack of consent results from","forcible compulsion":r"forcible compulsion","physically helpless":r"physically helpless",
 "mentally disabled/defective":r"mentally (disabled|defective)","mentally incapacitated":r"mentally incapacitated"}
NOTE=r"(History:|HISTORY:|Source: (SDC|SL|Laws)|\[L\.? ?\d{4}|\[\d{4} (\d+(st|nd|rd|th) ex\.s\. )?c|\(\d{4}, c\.|Laws \d{4}|P\.A\. \d{4}|P\.L\. \d{4}|En\. \d|Acts \d{4}|\d{4} Act No\.|\[\d{4} c\.\d|\(L\. \d{4}|Add\. \d{4})"
rows=[]
for m,p in MK.items():
    for s in L["prevalence"][m]["states"]:
        t=" ".join((C/"text3"/f"{s}.txt").read_text().split()); o=re.search(p,t,re.I)
        n=re.search(NOTE,t[o.end():]) if o else None
        if s=="AL":  # AL (FindLaw) puts the note before the section text
            back=list(re.finditer(r"Acts \d{4}[^)]*\)",t[:o.start()])); note=back[-1].group(0) if back else None
        else: note=t[o.end()+n.start(): o.end()+n.start()+260] if n else None
        yrs=sorted({int(y) for y in re.findall(r"\b(1[89]\d\d|20[0-2]\d)\b",note or "")})
        rows.append(dict(marker=m,state=s,first_year_in_note=yrs[0] if yrs else None,years=yrs[:8],note=(note or "")[:160]))
json.dump(rows,open(C/"years_raw.json","w"),indent=1)
for r in rows: print(f'{r["marker"][:22]:22s} {r["state"]} {str(r["first_year_in_note"]):5s} | {r["note"][:120]}')
