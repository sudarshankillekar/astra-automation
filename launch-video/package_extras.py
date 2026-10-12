from pathlib import Path
import json
P=Path(__file__).resolve().parent
scenes=json.loads((P/'script.json').read_text())
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}'
srt=[];idx=1
for start,end,_,_,text,_ in scenes:
 words=text.split();chunks=[' '.join(words[i:i+8]) for i in range(0,len(words),8)]
 for j,chunk in enumerate(chunks):
  a=start+.18+j*(end-start-.3)/len(chunks);b=start+.18+(j+1)*(end-start-.3)/len(chunks)
  srt.append(f'{idx}\n{stamp(a)} --> {stamp(b)}\n{chunk}\n');idx+=1
(P/'captions.srt').write_text('\n'.join(srt))
(P/'voiceover-script.txt').write_text('\n\n'.join(s[4] for s in scenes))
(P/'posting-copy.txt').write_text('Introducing Astra Automation.\n\nWe build your growth online—with websites, e-commerce stores, business automation, custom web applications, restaurant and booking systems, and influencer marketing.\n\nReady to build your next chapter? Let’s talk.\nhttps://astra-automation.vercel.app/\n\n#AstraAutomation #BusinessAutomation #WebDevelopment #Ecommerce #InfluencerMarketing\n')
(P/'README.md').write_text('''# Astra Automation — launch video

Both MP4 exports are exactly 60 seconds, 24 fps, with H.264 video, AAC audio, and embedded open captions.

- astra-launch-vertical.mp4: 1080 × 1920, 9:16; Instagram Reels, YouTube Shorts, and vertical LinkedIn posts.
- astra-launch-widescreen.mp4: 1920 × 1080, 16:9; YouTube and widescreen LinkedIn posts.
- voiceover.wav: isolated English narration.
- original-music.wav: original programmatically composed electronic instrumental.
- captions.srt: optional subtitle sidecar matching the on-screen phrase timing.
- posting-copy.txt: suggested post text.
- voiceover-script.txt: full narration.

Narration uses Microsoft’s en-IN-PrabhatNeural synthetic voice with slightly relaxed pacing. It is not a recording of a human actor. Brand marks are the supplied Astra assets. Illustrations are original schematic service demonstrations, not customer results. Music and sound design were synthesized for this video; no third-party song was sampled.

The Vercel address is used because the custom domain failed its HTTPS check during production. Files are prepared for the user to post; no social accounts were posted to.

Rebuild: install pillow, numpy, imageio-ffmpeg, and edge-tts in a Python environment, then run produce.py. The script uses Arial fonts from macOS. Internet access is needed only for narration generation when narration files are missing.
''')
