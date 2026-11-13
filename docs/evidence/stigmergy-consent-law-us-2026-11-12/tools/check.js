const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({userAgent:'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'});
  for (const u of process.argv.slice(2)) { const p = await ctx.newPage();
    try { const r = await p.goto(u,{waitUntil:'domcontentloaded',timeout:45000}); await p.waitForTimeout(2500);
      const t = (await p.evaluate(()=>document.body.innerText)).replace(/\s+/g,' '); const i=t.search(/Current as of/);
      console.log(r.status(), i>=0? t.slice(i, i+130) : 'NO-CURRENT '+t.slice(0,80), '<-', u);
    } catch(e){ console.log('ERR', u); } await p.close(); }
  await b.close(); })();
