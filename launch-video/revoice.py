from pathlib import Path
import asyncio,json,subprocess,wave
import numpy as np
import edge_tts
import produce as v
ORIGINAL=v.P
OUT=ORIGINAL/'reference-style'
OUT.mkdir(exist_ok=True)
async def generate():
 for i,s in enumerate(v.SCENES):
  f=OUT/f'vo-{i}.mp3'
  if not f.exists():await edge_tts.Communicate(s[4],'en-IN-NeerjaExpressiveNeural',rate='-2%',pitch='+1Hz').save(str(f))
  print('New voice',i,flush=True)
def build_voice():
 sr=48000;n=60*sr;voice=np.zeros(n,dtype=np.float32);report=[]
 for i,(start,end,_,_,s,_) in enumerate(v.SCENES):
  a=v.decode(OUT/f'vo-{i}.mp3');nz=np.flatnonzero(np.abs(a)>.002);a=a[max(0,nz[0]-int(.04*sr)):min(len(a),nz[-1]+int(.1*sr))]
  avail=end-start-.4;speed=max(1,len(a)/sr/avail)
  if speed>1:
   v.wav(OUT/'temp.wav',a);subprocess.run([v.FF,'-y','-v','error','-i',str(OUT/'temp.wav'),'-af',f'atempo={speed}',str(OUT/'fitted.wav')],check=True);a=v.decode(OUT/'fitted.wav')
  pos=int((start+.18)*sr);voice[pos:pos+len(a)]+=a
  report.append({'scene':i,'seconds':len(a)/sr,'tempo':speed})
 voice*=.77/max(.01,np.max(np.abs(voice)));v.wav(OUT/'voiceover.wav',voice)
 (OUT/'audio-report.json').write_text(json.dumps(report,indent=2));print(report,flush=True)
if __name__=='__main__':
 asyncio.run(generate());build_voice()
