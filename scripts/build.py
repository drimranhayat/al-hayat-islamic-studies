"""Regenerate the browser data from the eight source content files."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
config=[('aqeedah','عقیدہ و ایمانیات','بنیادِ فکر اور ایمانی شعور','Aqeedah', '#126e61','shield'),('quran','علومِ قرآن','وحی، متن اور قرآنی علوم','Quran_Sciences','#24679a','book'),('tafsir','تفسیر و اصولِ تفسیر','معنی، منہج اور تفسیری روایت','Tafsir_Usul','#7460a7','layers'),('hadith','حدیث و علومِ حدیث','روایت، درایت اور حجیت','Hadith','#ad7234','sun'),('fiqh','فقہ و اصولِ فقہ','استنباط اور عملی رہنمائی','Fiqh','#387c86','scale'),('seerah','سیرت و تاریخِ اسلام','اسوۂ نبوی اور تاریخی شعور','Seerah','#a85753','globe'),('thought','اسلامی فکر و فلسفہ','علم، عقل اور فکری مکالمہ','Islamic_Thought','#5c68a6','spark'),('religions','ادیان و مکاتبِ فکر','تقابل، تنوع اور علمی گفتگو','Religions','#7a7540','compass')]
subjects=[]
for sid,title,subtitle,prefix,color,icon in config:
 files=list((root/'dist/data').glob(prefix+'*.json'))
 assert len(files)==1,(prefix,files)
 raw=json.loads(files[0].read_text());questions=[];groups=[]
 for g in raw['groups']:
  gids=[]
  for t in g['topics']:
   for q in t['questions']:
    n=len(questions)+1;uid=q.get('learning_id') or sid+'-'+str(n).zfill(3)
    questions.append({'id':uid,'sourceId':q.get('id'),'order':n,'title':q.get('title') or t['title'],'q':q['q'],'a':q['a'],'groupId':sid+'-'+g['id'],'groupTitle':g['title'],'topic':t['title'],'further_reading':q.get('further_reading',[]),'references':q.get('references',[]),'arabic_spans':q.get('arabic_spans',[])})
    gids.append(uid)
  groups.append({'id':sid+'-'+g['id'],'title':g['title'],'questionIds':gids})
 subjects.append({'id':sid,'title':title,'subtitle':subtitle,'color':color,'icon':icon,'groups':groups,'questions':questions,'bibliography':raw.get('urdu_bibliography',raw.get('bibliography',[])),'sourceFile':files[0].name,'referenceNote':raw.get('reference_note','')})
(root/'dist/data.js').write_text('window.STUDY_DATA = '+json.dumps(subjects,ensure_ascii=False,separators=(',',':'))+';\n')
print(f'Built {len(subjects)} subjects / {sum(len(s["questions"]) for s in subjects)} questions. Bundled answers match source JSON.')
