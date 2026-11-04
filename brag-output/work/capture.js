// usage: node capture.js stills t1,t2,... | node capture.js frames
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const dir = __dirname;
const html = fs.readFileSync(path.join(dir,'video.html'),'utf8')
  .replace('__HEADLINES__', fs.readFileSync(path.join(dir,'headlines.json'),'utf8'))
  .replace('__WAVE__', fs.readFileSync(path.join(dir,'wave.json'),'utf8'));
fs.writeFileSync(path.join(dir,'page.html'), html);
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await pg.goto('file://' + path.join(dir,'page.html'));
  await pg.evaluate(async () => { await document.fonts.ready; await Promise.all([...document.images].map(i => i.decode())); });
  const mode = process.argv[2];
  if (mode === 'stills') {
    fs.mkdirSync(path.join(dir,'stills'), { recursive: true });
    for (const t of process.argv[3].split(',').map(Number)) {
      await pg.evaluate(t => render(t), t);
      await pg.screenshot({ path: path.join(dir,'stills',`t${t.toFixed(2)}.png`) });
    }
  } else {
    fs.mkdirSync(path.join(dir,'frames'), { recursive: true });
    const [A, B] = mode === 'range' ? process.argv.slice(3).map(Number) : [0, 600];
    for (let f = A; f < B; f++) {
      await pg.evaluate(t => render(t), f / 30);
      await pg.screenshot({ path: path.join(dir,'frames',`f${String(f).padStart(4,'0')}.png`) });
    }
  }
  await b.close();
})();
