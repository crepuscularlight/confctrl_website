from pathlib import Path
import subprocess, imageio_ffmpeg
root=Path(__file__).resolve().parent
source=root.parent/'ConfCtrl_video_template_eccv.mp4'
out=root/'static/videos/confctrl-introduction.mp4'
cmd=[imageio_ffmpeg.get_ffmpeg_exe(),'-hide_banner','-y','-i',str(source),'-vf','scale=1280:-2','-c:v','libx264','-preset','medium','-crf','25','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-movflags','+faststart',str(out)]
with (root/'compression.log').open('w') as log:
 subprocess.run(cmd,stdout=log,stderr=log,check=True)
print(f'Original: {source.stat().st_size:,} bytes; compressed: {out.stat().st_size:,} bytes',flush=True)
