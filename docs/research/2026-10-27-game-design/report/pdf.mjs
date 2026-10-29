import {createRequire} from 'node:module'; import path from 'node:path'; import os from 'node:os';
const require=createRequire(import.meta.url);
const {chromium}=require(path.join(os.homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright'));
const [,, src, out]=process.argv;
const b=await chromium.launch({channel:'chrome',headless:true}); const p=await b.newPage();
await p.goto('file://'+src,{waitUntil:'load'}); await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:out, format:'A4', printBackground:true, preferCSSPageSize:true}); await b.close(); console.log('pdf ok');
