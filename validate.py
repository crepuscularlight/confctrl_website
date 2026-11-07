from pathlib import Path
from html.parser import HTMLParser
import subprocess, imageio_ffmpeg, json, re
r=Path(__file__).resolve().parent
class Check(HTMLParser):
 def __init__(self): super().__init__(); self.refs=[]; self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  for k in ['src','href','poster']:
   if a.get(k):self.refs.append(a[k])
p=Check();p.feed((r/'index.html').read_text(encoding='utf-8-sig'))
assert len(p.ids)==len(set(p.ids)), 'Duplicate IDs'
for ref in p.refs:
 if ref.startswith('#'):assert not ref[1:] or ref[1:] in p.ids,ref
 elif not ref.startswith(('http:','https:')):assert (r/ref).is_file(),ref
ff=imageio_ffmpeg.get_ffmpeg_exe(); reports=[]
for video in (r/'static/videos').glob('*.mp4'):
 result=subprocess.run([ff,'-v','error','-i',str(video),'-f','null','-'],capture_output=True,text=True)
 assert result.returncode==0 and not result.stderr, result.stderr
 data=video.read_bytes(); assert data.find(b'moov')<data.find(b'mdat'), 'Missing faststart'
 reports.append({'file':video.name,'bytes':len(data),'full_decode':'passed','faststart':True})
report={'local_links':'passed','unique_ids':'passed','videos':reports,'browser_qa':'Unavailable: Windows browser runtime fails with CreateProcessWithLogonW error 1385.'}
(r/'validation.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
