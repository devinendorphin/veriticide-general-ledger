import re,html,sys,json,time,subprocess,urllib.parse,pathlib
OUT=pathlib.Path(sys.argv[1])
COURTS={"AR":"ark arkctapp","CO":"colo coloctapp","CT":"conn connappct","IN":"ind indctapp","KY":"ky kyctapp","MD":"md mdctspecapp","MS":"miss missctapp","PA":"pa pasuperct pacommwct"}
MK={"AR":["forcible compulsion","physically helpless","mentally defective","mentally incapacitated"],"CO":["physically helpless"],"CT":["physically helpless","mentally incapacitated"],
    "IN":["mentally defective","mentally disabled"],"KY":["lack of consent results from","forcible compulsion","physically helpless","mentally incapacitated"],
    "MD":["physically helpless","mentally incapacitated"],"MS":["physically helpless","mentally defective","mentally incapacitated"],"PA":["forcible compulsion"]}
res={}
for st,ms in MK.items():
    for m in ms:
        q=urllib.parse.urlencode({"q":f'"{m}" AND (rape OR "sexual intercourse" OR "sexual assault" OR sodomy)',"type":"o","order_by":"dateFiled asc","court":COURTS[st]})
        s=subprocess.run(["curl","-s","--max-time","60","-A","Mozilla/5.0 (X11; Linux x86_64) Chrome/120","https://www.courtlistener.com/?"+q],capture_output=True,text=True).stdout
        (OUT/f"cls_{st}_{m.replace(' ','_')}.html").write_text(s)
        s2=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',s)
        arts=re.findall(r'(?is)<article.*?</article>',s2)
        hits=[]
        for a in arts[:4]:
            t=re.sub(r'\s+',' ',html.unescape(re.sub(r'(?s)<[^>]+>',' ',a))).strip()
            d=re.search(r'Date Filed:\s*([A-Za-z]+\.? \d{1,2}(st|nd|rd|th)?,? \d{4})',t)
            hits.append(dict(date=d.group(1) if d else None,text=t[:420]))
        n=re.search(r'(\d[\d,]*) Results?',re.sub(r'<[^>]+>',' ',s))
        res[f"{st}|{m}"]=dict(n=n.group(1) if n else None,hits=hits); print(st,m,res[f"{st}|{m}"]["n"],[h["date"] for h in hits]); time.sleep(2)
json.dump(res,open(OUT/"cl_results_sex.json","w"),indent=1)
