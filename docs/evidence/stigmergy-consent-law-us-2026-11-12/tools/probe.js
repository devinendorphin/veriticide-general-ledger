const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36' });
  const urls = process.argv.slice(2);
  for (const u of urls) {
    const p = await ctx.newPage();
    try {
      const r = await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await p.waitForTimeout(6000);
      const t = await p.evaluate(() => document.body ? document.body.innerText : '');
      console.log((r ? r.status() : 'noresp'), t.split(/\s+/).length, 'words |', t.replace(/\s+/g,' ').slice(0,160), '<-', u);
    } catch (e) { console.log('ERR', e.message.split('\n')[0], '<-', u); }
    await p.close();
  }
  await b.close();
})();
