from pathlib import Path
from PIL import Image,ImageDraw
import cv2, zipfile, hashlib, xml.etree.ElementTree as E
r=Path('video_content/video_4_gif'); files=sorted(r.glob('*.mp4'),key=lambda p:int(p.stem[5:]))
sheet=Image.new('RGB',(1200,((len(files)+7)//8)*120),'white'); d=ImageDraw.Draw(sheet)
for i,p in enumerate(files):
 c=cv2.VideoCapture(str(p)); c.set(cv2.CAP_PROP_POS_FRAMES,int(c.get(cv2.CAP_PROP_FRAME_COUNT)//2));ok,frame=c.read();c.release()
 if ok:
  im=Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB));im.thumbnail((145,95));x=(i%8)*150;y=(i//8)*120;sheet.paste(im,(x,y+20));d.text((x+3,y+2),p.stem,fill='black')
sheet.save('confctrl_website/result-candidates.jpg')
z=zipfile.ZipFile('ConfCtrl_video_template.pptx'); hashes={hashlib.sha256(p.read_bytes()).hexdigest():p.name for p in files}
matched={n:hashes[hashlib.sha256(z.read(n)).hexdigest()] for n in z.namelist() if n.endswith('.mp4') and hashlib.sha256(z.read(n)).hexdigest() in hashes}
for n in z.namelist():
 if n.startswith('ppt/slides/_rels/') and n.endswith('.rels'):
  hits=[matched['ppt/'+e.attrib['Target'].replace('../','')] for e in E.fromstring(z.read(n)) if 'ppt/'+e.attrib.get('Target','').replace('../','') in matched]
  if hits:
   slide='ppt/slides/'+Path(n).name.replace('.rels',''); text=' | '.join(E.fromstring(z.read(slide)).itertext()); print(slide, hits, text[:2500])
