from pathlib import Path
import subprocess, json, wave
import imageio_ffmpeg
P=Path(__file__).resolve().parent;ff=imageio_ffmpeg.get_ffmpeg_exe();report=[]
for name,wh in [('astra-launch-vertical',(1080,1920)),('astra-launch-widescreen',(1920,1080))]:
 p=P/(name+'.mp4');r=subprocess.run([ff,'-hide_banner','-i',str(p)],capture_output=True,text=True)
 info=r.stderr
 assert 'Duration: 00:01:00.00' in info,info
 assert f'{wh[0]}x{wh[1]}' in info,info
 assert 'aac' in info and 'h264' in info
 r=subprocess.run([ff,'-v','error','-i',str(p),'-f','null','-'],capture_output=True,text=True)
 assert r.returncode==0 and not r.stderr,r.stderr
 subprocess.run([ff,'-y','-v','error','-ss','56','-i',str(p),'-frames:v','1',str(P/(name+'-cover.jpg'))],check=True)
 report.append({'file':p.name,'duration_seconds':60,'dimensions':list(wh),'bytes':p.stat().st_size,'full_decode':'passed','audio':'AAC','video':'H.264'})
(P/'verification.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
