const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
const plan=JSON.parse(fs.readFileSync(process.argv[2])); const out=process.argv[3];
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'});
  const log=[];
  for (const [st,[pre,secs]] of Object.entries(plan)) { fs.mkdirSync(path.join(out,st),{recursive:true}); let txt='';
    for (const s of secs) { const u=`https://codes.findlaw.com/${pre}${s}/`; const p=await ctx.newPage(); let rec={st,s,u};
      try { const r=await p.goto(u,{waitUntil:'domcontentloaded',timeout:60000}); await p.waitForTimeout(2500);
        const html=await p.content(); fs.writeFileSync(path.join(out,st,`${s}.html`),html);
        const t=(await p.evaluate(()=>document.body.innerText)).replace(/[ \t]+/g,' ');
        const cur=(t.match(/Current as of ([A-Za-z]+ \d{1,2}, \d{4})/)||[])[1]||null;
        let i=t.search(/Updated by Find[Ll]aw Staff/); let body=i>=0? t.slice(i).replace(/^Updated by Find[Ll]aw Staff/,''):'';
        const j=body.search(/FindLaw Codes may not reflect|Read this complete|Was this helpful|Cite this article/); if(j>0) body=body.slice(0,j);
        rec.status=r.status(); rec.current_as_of=cur; rec.words=body.split(/\s+/).filter(Boolean).length; txt+=body+'\n';
      } catch(e){ rec.error=e.message.split('\n')[0]; }
      log.push(rec); console.log(JSON.stringify(rec)); await p.close(); }
    fs.writeFileSync(path.join(out,`${st}.txt`),txt); }
  fs.writeFileSync(path.join(out,'fetch_log.json'),JSON.stringify(log,null,1)); await b.close(); })();
