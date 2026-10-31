"""Check content integrity, IDs, references and required site assets."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1];dist=root/'dist'
s=(dist/'data.js').read_text();data=json.loads(s.removeprefix('window.STUDY_DATA = ').strip().removesuffix(';'))
assert len(data)==8
allids=[];total=0
for subject in data:
 source=json.loads((dist/'data'/subject['sourceFile']).read_text())
 originals=[q for g in source['groups'] for t in g['topics'] for q in t['questions']]
 assert len(originals)==len(subject['questions'])
 for original,q in zip(originals,subject['questions']):
  assert q['q']==original['q'] and q['a']==original['a'],q['id']
  assert q['references']==original.get('references',[])
  allids.append(q['id'])
  assert all(a in q['a'] for a in q.get('arabic_spans',[])),q['id']
 assert set(allids).issuperset(q for g in subject['groups'] for q in g['questionIds'])
 total+=len(originals)
assert total==470 and len(set(allids))==470
for name in ['index.html','app.js','style.css','sw.js','assets/icon.svg','assets/fonts/NotoNastaliqUrdu.ttf','assets/fonts/NotoSansArabic.ttf','assets/fonts/Amiri.ttf','assets/fonts/Amiri-Bold.ttf','assets/fonts/JameelNooriNastaleeq.woff2']:
 assert (dist/name).is_file(),name
assert not re.search(r'TODO|PLACEHOLDER|TBD',(dist/'index.html').read_text())
print('PASS: 8 subjects, 470 unique questions, source answers/references matched, required assets present.')
