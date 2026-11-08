from pathlib import Path
import shutil, subprocess, imageio_ffmpeg
from PIL import Image
r=Path('confctrl_website'); a=r/'static'
for name in ['teaser','method','baseline_comparison_eccv','zero_shot_poster']:
 im=Image.open(Path('pdf')/(name+'.png')).convert('RGB'); im.thumbnail((2000,2000)); im.save(a/'images'/(name+'.webp'),'WEBP',quality=90)
im=Image.open('poster.png').convert('RGB'); im.thumbnail((2000,2000)); im.save(a/'images/poster.webp','WEBP',quality=90)
shutil.copy2('3568_Yang_1400x1000mm.pdf',a/'pdfs/poster.pdf')
f=imageio_ffmpeg.get_ffmpeg_exe()
subprocess.run([f,'-hide_banner','-loglevel','error','-y','-ss','3','-i','ConfCtrl_video_template_eccv.mp4','-frames:v','1','-vf','scale=1280:-2',str(a/'images/video-poster.jpg')],check=True)
# Only the retained result clip is approved for this gallery.
# eccv/teddybear.mp4 and eccv/dl3dv.mp4 are not ConfCtrl results.
for name in ['inference_video_000']:
 subprocess.run([f,'-hide_banner','-loglevel','error','-y','-i',f'eccv/{name}.mp4','-vf','scale=960:-2','-c:v','libx264','-crf','25','-preset','fast','-an','-movflags','+faststart',str(a/'videos'/(name+'.mp4'))],check=True)
 subprocess.run([f,'-hide_banner','-loglevel','error','-y','-i',str(a/'videos'/(name+'.mp4')),'-frames:v','1',str(a/'images'/(name+'.jpg'))],check=True)
print('Website images, poster, and example videos prepared.')

# Clips explicitly selected by the user: Media76 and Media58, in that order.
for source, name in [('Media76.mp4', 'selected-media76'), ('Media58.mp4', 'selected-media58')]:
 src = Path('video_content/video_4_gif') / source
 out = a / 'videos' / (name + '.mp4')
 subprocess.run([f, '-v', 'error', '-y', '-i', str(src), '-c', 'copy', '-movflags', '+faststart', str(out)], check=True)
 subprocess.run([f, '-v', 'error', '-y', '-i', str(out), '-frames:v', '1', str(a / 'images' / (name + '.jpg'))], check=True)
