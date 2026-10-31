import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
const source=fs.readFileSync(new URL('../dist/app.js',import.meta.url),'utf8');
const scope={settings:{highlight:true},esc:t=>String(t).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;')};
vm.createContext(scope);
vm.runInContext(source.slice(source.indexOf('const TERMS='),source.indexOf('function refText')),scope);
const render=(text,spans=[])=>vm.runInContext(`rich(${JSON.stringify(text)},${JSON.stringify(spans)})`,scope);
assert.equal(render('روایتوں روایت روایتِ، ایمان ایماناً'),'روایتوں <mark>روایت</mark> <mark>روایتِ</mark>، <mark>ایمان</mark> ایماناً');
assert.equal(render('توحیدِ الوہیت، توحیدیں'),'<mark>توحیدِ الوہیت</mark>، توحیدیں');
assert.equal(render('<img> **عقیدہ**'),'&lt;img&gt; <strong><mark>عقیدہ</mark></strong>');
const quote='قُلْ هُوَ اللَّهُ أَحَدٌ';
assert.equal(render(quote,[quote]),`<strong class="arabic-quote" lang="ar" dir="rtl">${quote}</strong>`);
const reader=source.slice(source.indexOf('function reader('),source.indexOf('function toggleBookmark'));
assert.match(reader,/\$\{answerHTML\(q,false\)\}<div class="reader-pagination">/);
assert.ok(reader.indexOf('reader-pagination')<reader.indexOf('${referencePanel(q)}'));
assert.equal((reader.match(/class="reader-pagination"/g)||[]).length,1);
const data=JSON.parse(fs.readFileSync(new URL('../dist/data.js',import.meta.url),'utf8').replace(/^window.STUDY_DATA = /,'').replace(/;\s*$/,''));
const revision=JSON.parse(fs.readFileSync(new URL('../CONTENT_ENRICHMENT.json',import.meta.url),'utf8'));
for(const id of revision.updated_question_ids){
 const q=data.flatMap(s=>s.questions).find(q=>q.id===id);
 assert.ok(q&&q.a.includes('اس کا ترجمہ ہے:')&&q.arabic_spans.length,id);
 assert.ok(q.references.some(r=>typeof r==='object'&&/^https:\/\//.test(r.url)),id);
 for(const quote of q.arabic_spans){assert.ok(q.a.includes(quote),id);assert.ok(render(quote,q.arabic_spans).includes('lang="ar"'),id)}
}
console.log('PASS: whole-word highlighting, combining marks, safe markup, Arabic styling, answer-end navigation and all new evidence records.');
