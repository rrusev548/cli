"""Render the fire story to MP4 with Python + ffmpeg.
Requires: ffmpeg installed on PATH. The HTML preview remains available without it.
"""
from pathlib import Path
import subprocess, shutil
ROOT=Path(__file__).parent
if not shutil.which('ffmpeg'):
    raise SystemExit('ffmpeg is required to render MP4; open fire_story.html for the browser preview.')
# Convert each SVG scene to PNG, hold 10 seconds, then mux narration.
frames=ROOT/'rendered_frames'; frames.mkdir(exist_ok=True)
for i in range(1,19):
    subprocess.run(['rsvg-convert','-w','1280','-h','720',str(ROOT/f'fire_story_frames/frame_{i:02d}.svg'),'-o',str(frames/f'{i:02d}.png')],check=True)
subprocess.run(['ffmpeg','-y','-framerate','1/10','-i',str(frames/'%02d.png'),'-vf','fps=30,format=yuv420p','-t','180','-c:v','libx264','-movflags','+faststart',str(ROOT/'fire_story.mp4')],check=True)
subprocess.run(['ffmpeg','-y','-i',str(ROOT/'fire_story.mp4'),'-i',str(ROOT/'narration_part_1.mp3'),'-i',str(ROOT/'narration_part_2.mp3'),'-filter_complex','[1:a][2:a]concat=n=2:v=0:a=1[a]','-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-shortest',str(ROOT/'fire_story_final.mp4')],check=True)
print(ROOT/'fire_story_final.mp4')
