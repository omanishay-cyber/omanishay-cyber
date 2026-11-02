// Render every .art block of art.html to PNG, light and dark, at scale 2, headless, and write the text boxes for the contrast check.
// Usage: node render.cjs <out folder> [id,id]
const path = require('path');
const fs = require('fs');
const { pathToFileURL } = require('url');
const pw = require('C:/Users/Anish/.claude/stryx/temp/perch-notch-harness/node_modules/playwright-core');
const out = process.argv[2];
const only = process.argv[3] ? process.argv[3].split(',') : null;

(async () => {
  const browser = await pw.chromium.launch({ channel: 'msedge', headless: true });
  fs.mkdirSync(out, { recursive: true });
  const boxes = {};
  for (const theme of ['dark', 'light']) {
    const page = await browser.newPage({ viewport: { width: 1100, height: 900 }, deviceScaleFactor: 2 });
    page.on('pageerror', (e) => console.log('pageerror', e.message));
    page.on('requestfailed', (r) => console.log('failed', r.url()));
    await page.goto(pathToFileURL(path.join(__dirname, 'art.html')).href + '?theme=' + theme);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(300);
    const ids = await page.$$eval('.art', (els) => els.map((e) => e.id));
    for (const id of ids) {
      if (only && !only.includes(id)) continue;
      const el = page.locator('#' + id);
      await el.screenshot({ path: path.join(out, `${id}-${theme}.png`), omitBackground: true });
      // the same block with its text hidden, and each text box, for the measured contrast
      const list = await el.evaluate((root) => {
        const r0 = root.getBoundingClientRect(); const res = [];
        const walk = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
        while (walk.nextNode()) {
          const n = walk.currentNode; if (!n.textContent.trim()) continue;
          const range = document.createRange(); range.selectNodeContents(n);
          const b = range.getBoundingClientRect(); const cs = getComputedStyle(n.parentElement);
          res.push({ t: n.textContent.trim().slice(0, 40), x: b.x - r0.x, y: b.y - r0.y, w: b.width, h: b.height, color: cs.color, px: parseFloat(cs.fontSize) });
        }
        root.dataset.hide = '1'; root.style.color = 'transparent';
        root.querySelectorAll('*').forEach((e) => { if (e.tagName !== 'svg' && !e.closest('svg')) e.style.setProperty('color', 'transparent', 'important'); });
        return res;
      });
      await el.screenshot({ path: path.join(out, `${id}-${theme}.bare.png`), omitBackground: true });
      await el.evaluate((root) => { root.style.color = ''; root.querySelectorAll('*').forEach((e) => { if (e.tagName !== 'svg' && !e.closest('svg')) e.style.removeProperty('color'); }); });
      boxes[`${id}-${theme}`] = list;
      console.log(id, theme);
    }
    await page.close();
  }
  fs.writeFileSync(path.join(out, 'boxes.json'), JSON.stringify(boxes));
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
