from pathlib import Path
import asyncio, json, math, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import edge_tts, imageio_ffmpeg
P=Path(__file__).resolve().parent
FF=imageio_ffmpeg.get_ffmpeg_exe()
SCENES=[
(0,5,'THE NEXT CHAPTER','Your business.\nReady for more?', 'Your business deserves more than busy days and missed opportunities.','hook'),
(5,10,'INTRODUCING','Astra\nAutomation','Meet Astra Automation. We build your growth online.','brand'),
(10,17,'01 / WEBSITE DEVELOPMENT','Make your first\nimpression count.','Fast, mobile-friendly websites and landing pages that make a powerful first impression.','web'),
(17,24,'02 / E-COMMERCE','Turn browsing\ninto buying.','Online stores with product catalogues, payments, and connected order and inventory management.','shop'),
(24,32,'03 / BUSINESS AUTOMATION','Less busywork.\nMore possibility.','Automate orders, billing, customer management, notifications, and reporting. Less busywork. More time to grow.','network'),
(32,40,'04 / CUSTOM APPLICATIONS','Built around\nyour business.','Custom web applications. Restaurant solutions, bookings, dashboards, inventory systems, and customer portals. Built around you.','apps'),
(40,48,'05 / INFLUENCER MARKETING','Get seen.\nBuild connections.','Influencer marketing. Creator discovery, campaign strategy, content planning, brand collaborations, and performance tracking.','creator'),
(48,54,'ONE CONNECTED VISION','Build smarter.\nGrow stronger.','Your first website. Your next big launch. Bring it together with Astra.','summary'),
(54,60,'LET’S BUILD WHAT’S NEXT','Your next chapter\nstarts here.','Astra Automation. We build your growth online. Let’s build your next chapter.','cta')]
(P/'script.json').write_text(json.dumps(SCENES,indent=2))
async def voices():
 for i,(_,_,_,_,s,_) in enumerate(SCENES):
  f=P/f'vo-{i}.mp3'
  if not f.exists():
   await edge_tts.Communicate(s,'en-IN-PrabhatNeural',rate='-3%',pitch='-1Hz').save(str(f))
  print('Narration',i,flush=True)
def decode(f):
 b=subprocess.check_output([FF,'-v','error','-i',str(f),'-f','f32le','-ac','1','-ar','48000','pipe:1'])
 return np.frombuffer(b,dtype=np.float32).copy()
def wav(f,a):
 with wave.open(str(f),'wb') as w:
  w.setnchannels(1 if a.ndim==1 else a.shape[1]);w.setsampwidth(2);w.setframerate(48000);w.writeframes((np.clip(a,-1,1)*32767).astype('<i2').tobytes())
def audio():
 sr=48000;n=60*sr;voice=np.zeros(n,dtype=np.float32);report=[]
 for i,(start,end,_,_,s,_) in enumerate(SCENES):
  a=decode(P/f'vo-{i}.mp3'); a=a[np.argmax(np.abs(a)>.002):]; last=np.flatnonzero(np.abs(a)>.002);a=a[:last[-1]+int(.12*sr)]
  available=end-start-.4;speed=max(1,len(a)/sr/available)
  if speed>1:
   wav(P/'tmp.wav',a);subprocess.run([FF,'-y','-v','error','-i',str(P/'tmp.wav'),'-af',f'atempo={speed}',str(P/'fit.wav')],check=True);a=decode(P/'fit.wav')
  pos=int((start+.18)*sr);voice[pos:pos+len(a)]+=a
  report.append({'scene':i,'seconds':len(a)/sr,'tempo':speed})
 voice=voice/max(np.max(np.abs(voice)),.01)*.75
 music=np.zeros((n,2),dtype=np.float32);rng=np.random.default_rng(27);beat=60/112
 def add(signal,at,gain=1,pan=0):
  ix=int(at*sr);size=min(len(signal),n-ix)
  if ix<0 or size<=0:return
  music[ix:ix+size,0]+=signal[:size]*gain*(1-pan*.5);music[ix:ix+size,1]+=signal[:size]*gain*(1+pan*.5)
 def tone(hz,dur):
  t=np.arange(int(dur*sr))/sr
  return t
 chords=[[146.83,174.61,220,261.63],[116.54,146.83,174.61,220],[130.81,164.81,196,246.94],[110,130.81,164.81,196]]
 for bar in range(29):
  at=bar*4*beat;ch=chords[bar%4];dur=4*beat+.3;t=tone(1,dur);env=np.minimum(t/.35,1)*np.minimum((dur-t)/.6,1)
  for j,hz in enumerate(ch):
   sig=(np.sin(2*np.pi*hz*t)+.25*np.sin(2*np.pi*hz*2.004*t))*env
   add(sig,at,.032,(-1)**j*.5)
  for k in range(8):
   tt=tone(1,.42);hz=ch[k%4]*4;sig=np.sin(2*np.pi*hz*tt)*np.exp(-tt*11)*np.minimum(tt/.007,1)
   add(sig,at+k*beat/2,.047,math.sin(k*1.7));add(sig,at+k*beat/2+.23,.018,-math.sin(k*1.7))
 for b in range(112):
  at=b*beat
  t=tone(1,.22);kick=np.sin(2*np.pi*(48*t+9*(1-np.exp(-t*24))))*np.exp(-t*22)
  add(kick,at,.20 if at>5 else .1)
  t=tone(1,.33);bass=np.sin(2*np.pi*chords[(b//4)%4][0]/2*t)*np.minimum(t/.008,1)*np.exp(-t*8)
  add(bass,at,.085)
  if b%2:
   t=tone(1,.14);noise=rng.normal(0,1,len(t));sn=(noise-np.roll(noise,1))*.4*np.exp(-t*30)
   add(sn,at,.065)
  for off in [0,.5]:
   t=tone(1,.06);noise=rng.normal(0,1,len(t));hat=(noise-np.roll(noise,1))*np.exp(-t*80)
   add(hat,at+off*beat,.017,(-1)**b*.6)
 # transition risers
 for at in [5,10,17,24,32,40,48,54]:
  t=tone(1,.6);noise=rng.normal(0,1,len(t));sig=np.convolve(noise,np.ones(20)/20,mode='same')*np.sin(np.pi*t/.6)**2
  add(sig,at-.45,.085)
 fade=np.minimum(np.arange(n)/sr/1.4,1)*np.minimum((60-np.arange(n)/sr)/1.4,1)
 music*=fade[:,None]
 # Broad ducking keeps the voice foregrounded throughout each spoken scene.
 mix=voice[:,None]+music*.42
 peak=np.max(np.abs(mix));mix*=.9/max(.9,peak)
 wav(P/'voiceover.wav',voice);wav(P/'original-music.wav',music);wav(P/'mix.wav',mix)
 (P/'audio-report.json').write_text(json.dumps(report,indent=2));print(report,flush=True)
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
fonts={}
def font(n,b=False):
 key=(int(n),b)
 if key not in fonts:fonts[key]=ImageFont.truetype(BOLD if b else FONT,int(n))
 return fonts[key]
BLUE=(125,197,255);WHITE=(242,247,255);MUTED=(152,170,198);PINK=(199,72,121);MINT=(97,227,189)
def draw_frame(t,wide=False):
 W,H=(1920,1080) if wide else (1080,1920)
 # background with static radial glow, moving grid, orbit and particles
 im=BACK[wide].copy();d=ImageDraw.Draw(im)
 for x in range(-100,W+100,90):d.line((x+int(t*9)%90,0,x+int(t*9)%90,H),fill=(17,28,45),width=1)
 for y in range(0,H,90):d.line((0,y,W,y),fill=(17,28,45),width=1)
 cx,cy=(W*.78,H*.51) if wide else (W*.5,H*.60)
 for r in [220,335,440]:
  d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=(27,44,68),width=2)
  a=t*.3+r;px=cx+r*math.cos(a);py=cy+r*math.sin(a);d.ellipse((px-5,py-5,px+5,py+5),fill=BLUE)
 for j in range(24):
  px=(j*193.73+t*(5+j%3))%W;py=(j*313.21-t*7)%H;d.ellipse((px,py,px+2,py+2),fill=(76,109,148))
 i=next((i for i,s in enumerate(SCENES) if s[0]<=t<s[1]),8);st,en,eyebrow,title,spoken,kind=SCENES[i];u=t-st
 ease=1-(1-min(1,u/.8))**3;dy=(1-ease)*45
 # header lockup retains supplied mark unchanged
 logo=LOGO.copy();im.alpha_composite(logo,(64,65));d=ImageDraw.Draw(im)
 d.text((152,78),'ASTRA AUTOMATION',font=font(25,True),fill=WHITE)
 d.text((152,113),'WE BUILD YOUR GROWTH ONLINE',font=font(13),fill=MUTED)
 d.rounded_rectangle((W-211,79,W-64,120),20,fill=(20,40,54),outline=(50,93,108));d.ellipse((W-191,95,W-183,103),fill=MINT);d.text((W-171,89),'INTRODUCING',font=font(14,True),fill=MINT)
 tx=90;ty=(265 if wide else 300)+dy
 d.text((tx,ty),eyebrow,font=font(22,True),fill=BLUE)
 # A crisp animated accent makes each scene change legible without competing
 # with the headline or caption.
 reveal=min(1,u/.65)
 accent_w=int((170+90*math.sin(t*2.4)**2)*reveal)
 d.rounded_rectangle((tx,ty+34,tx+accent_w,ty+40),3,fill=MINT)
 size=80 if wide else 82
 if kind=='brand':size=100 if wide else 120
 for j,line in enumerate(title.split('\n')):d.text((tx,ty+58+j*(size+12)),line,font=font(size,True),fill=WHITE if j==0 else BLUE)
 if kind=='cta':
  d.text((tx,ty+270),'astra-automation.vercel.app',font=font(32,True),fill=MINT)
 # illustration region
 x,y,w,h=(1040,255,770,570) if wide else (90,760,900,670)
 bob=math.sin(t*1.8)*7;y+=bob
 def panel(xx,yy,ww,hh):d.rounded_rectangle((xx,yy,xx+ww,yy+hh),24,fill=(15,25,42),outline=(49,72,103),width=2)
 def text(xx,yy,s,size=24,col=WHITE,b=True):d.text((xx,yy),s,font=font(size,b),fill=col)
 def bar(xx,yy,ww,hh=10,col=BLUE):d.rounded_rectangle((xx,yy,xx+max(1,ww),yy+hh),hh/2,fill=col)
 if kind in ['hook','network','summary']:
  ccx=x+w/2;ccy=y+h/2
  labels=['Website','Orders','Customers','Payments','Analytics','Automation']
  for j,label in enumerate(labels):
   a=j*math.pi/3-math.pi/2;nx=ccx+math.cos(a)*w*.34;ny=ccy+math.sin(a)*h*.37
   d.line((ccx,ccy,nx,ny),fill=(60,96,133),width=2)
   f=(t*.6+j*.16)%1;px=ccx+(nx-ccx)*f;py=ccy+(ny-ccy)*f;d.ellipse((px-5,py-5,px+5,py+5),fill=MINT)
   panel(nx-95,ny-35,190,70);text(nx-78,ny-11,label,21)
  pulse=105+int(7*math.sin(t*3.2)**2);d.ellipse((ccx-pulse,ccy-pulse,ccx+pulse,ccy+pulse),fill=(23,49,74),outline=BLUE,width=3)
  text(ccx-71,ccy-25,'ASTRA',39);text(ccx-65,ccy+24,'CONNECTED',17,MINT)
 elif kind in ['brand','cta']:
  sz=350 if wide else 460;lg=MARK.resize((sz,sz),Image.Resampling.LANCZOS);im.alpha_composite(lg,(int(x+(w-sz)/2),int(y+20)));d=ImageDraw.Draw(im)
  text(x+w/2-155,y+h-115,'IDEAS. SYSTEMS. GROWTH.',23,BLUE)
  if kind=='cta':
   panel(x+25,y+h-20,w-50,80);text(x+65,y+h+3,'Let’s build your growth online.',29)
 elif kind=='web':
  reveal=min(1,u/.8);panel(x,y,w,h);bar(x+25,y+22,10,10,PINK);bar(x+45,y+22,10,10,BLUE);bar(x+65,y+22,10,10,MINT)
  text(x+35,y+68,'YOUR BRAND',19,BLUE);text(x+35,y+136,'A better digital',42);text(x+35,y+190,'first impression.',42)
  for j in range(3):bar(x+35,y+270+j*25,(w*.43-j*30)*min(1,max(0,(u-j*.14)/.45)),9,(63,81,106))
  d.rounded_rectangle((x+35,y+379,x+285,y+439),12,fill=BLUE);text(x+58,y+395,'Let’s get started',23,(9,23,40))
  # responsive phone
  xx=x+w-220+int((1-reveal)*90);yy=y+115;panel(xx,yy,185,385);bar(xx+55,yy+18,75,6,MUTED)
  d.rounded_rectangle((xx+18,yy+58,xx+167,yy+201),12,fill=(36,65,98));text(xx+34,yy+106,'HELLO.',27)
  for j in range(4):bar(xx+20,yy+233+j*23,143-j*12,8,(74,99,129))
  text(x+35,y+h-61,'FAST  /  RESPONSIVE  /  SEO-FRIENDLY',19,MINT)
 elif kind=='shop':
  panel(x,y,w,h);text(x+35,y+33,'YOUR ONLINE STORE',25,BLUE)
  for j in range(3):
   appear=min(1,max(0,(u-j*.38)/.55));xx=x+30+j*(w-45)/3;ww=(w-100)/3;drop=int((1-appear)*65)
   d.rounded_rectangle((xx,y+102+drop,xx+ww,y+309+drop),18,fill=[(43,53,79),(66,38,61),(31,67,72)][j])
   # stylized product packaging
   d.rounded_rectangle((xx+ww*.25,y+143,xx+ww*.75,y+270),12,outline=WHITE,width=3);d.arc((xx+ww*.37,y+119,xx+ww*.63,y+170),180,360,fill=WHITE,width=3)
   text(xx,y+328+drop,['Discover','Add to cart','Checkout'][j],22)
   if j<2 and u>1.1+j*.55:d.ellipse((xx+ww-45,y+205+drop,xx+ww-29,y+221+drop),fill=MINT)
  for j,label in enumerate(['Payments connected','Orders organised','Inventory in sync']):
   text(x+42,y+405+j*48,'✓ '+label,25,MINT)
 elif kind=='apps':
  panel(x,y,w,h);text(x+35,y+35,'YOUR BUSINESS / CONNECTED',24,BLUE)
  tabs=['Restaurants','Bookings','Dashboards','Customer portals']
  for j,label in enumerate(tabs):
   appear=min(1,max(0,(u-j*.2)/.45));xx=x+30+(j%2)*(w/2-5);yy=y+105+(j//2)*145+int((1-appear)*30);panel(xx,yy,w/2-50,115)
   bar(xx+18,yy+20,34,5,[BLUE,MINT,PINK,BLUE][j]);text(xx+18,yy+47,label,24)
  text(x+36,y+431,'Designed for the way you work.',26)
  for j in range(12):
   ht=25+((j*29)%85)*(.75+.25*math.sin(t*2+j));bar(x+40+j*(w-85)/12,y+h-30-ht,(w-150)/12,ht,BLUE if j%3 else MINT)
 elif kind=='creator':
  for j in range(3):
   appear=min(1,max(0,(u-j*.3)/.55));xx=x+15+j*(w-20)/3+int((1-appear)*70);yy=y+55+(j%2)*45;ww=(w-65)/3
   panel(xx,yy,ww,390)
   d.ellipse((xx+ww*.2,yy+42,xx+ww*.8,yy+42+ww*.6),fill=[(71,52,84),(42,72,105),(80,39,61)][j],outline=[BLUE,MINT,PINK][j],width=3)
   text(xx+ww*.39,yy+68,['A','B','C'][j],55)
   text(xx+18,yy+240,['CREATE','CONNECT','AMPLIFY'][j],23,BLUE)
   for k in range(3):bar(xx+18,yy+290+k*19,ww-38-k*14,7,(70,89,115))
   if u>1.35+j*.3:d.ellipse((xx+ww-48,yy+18,xx+ww-30,yy+36),fill=PINK);text(xx+ww-44,yy+13,'+',18,WHITE)
  text(x+30,y+h-114,'The right creators. Your brand story.',26)
  text(x+30,y+h-67,'STRATEGY  /  CONTENT  /  PERFORMANCE',18,MINT)
 # captions: two/three short lines, synchronized by phrase chunks
 words=spoken.split();chunks=[];current=[]
 for word in words:
  current.append(word)
  if len(current)>=8:chunks.append(' '.join(current));current=[]
 if current:chunks.append(' '.join(current))
 active=min(len(chunks)-1,int(max(0,u-.18)/(en-st-.3)*len(chunks)))
 cap=chunks[active]
 capfont=font(30 if wide else 34)
 maxwidth=W-180
 # center compact caption box
 bb=d.textbbox((0,0),cap,font=capfont);tw=bb[2]
 if tw>maxwidth:
  ws=cap.split();mid=len(ws)//2;lines=[' '.join(ws[:mid]),' '.join(ws[mid:])]
 else:lines=[cap]
 by=H-(168 if wide else 315)
 for k,line in enumerate(lines):
  tw=d.textlength(line,font=capfont);d.rounded_rectangle(((W-tw)/2-19,by+k*48-8,(W+tw)/2+19,by+k*48+43),9,fill=(7,13,24));d.text(((W-tw)/2,by+k*48),line,font=capfont,fill=WHITE)
 # footer CTA / progressing timeline
 d.text((90,H-100),'astra-automation.vercel.app',font=font(23),fill=BLUE)
 d.text((W-205,H-100),f'{i+1:02d} / 09',font=font(21),fill=MUTED)
 bar(90,H-53,W-180,3,(32,48,70));bar(90,H-54,(W-180)*t/60,5,BLUE)
 # initial and scene cuts fade from dark, preserve momentum
 fade=min(1,u/.25,(60-t)/.5)
 if fade<1:im=Image.blend(Image.new('RGBA',(W,H),(7,12,22,255)),im,max(0,fade))
 return im.convert('RGB')
def init():
 global BACK,MARK,LOGO
 MARK=Image.open(P.parent/'public/astra-mark.png').convert('RGBA');LOGO=MARK.resize((72,72),Image.Resampling.LANCZOS)
 BACK={}
 for wide,(w,h) in [(False,(1080,1920)),(True,(1920,1080))]:
  yy,xx=np.mgrid[0:h,0:w];g=np.exp(-(((xx-w*.7)/(w*.6))**2+((yy-h*.53)/(h*.42))**2)*3)
  a=np.zeros((h,w,3),dtype=np.uint8)
  for c,(b,v) in enumerate([(7,10),(12,17),(22,26)]):a[:,:,c]=b+g*v
  BACK[wide]=Image.fromarray(a).convert('RGBA')
def render(wide):
 W,H=(1920,1080) if wide else (1080,1920);name='astra-launch-widescreen' if wide else 'astra-launch-vertical'
 cmd=[FF,'-y','-v','error','-f','rawvideo','-vcodec','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','24','-i','pipe:0','-i',str(P/'mix.wav'),'-c:v','libx264','-preset','medium','-crf','16','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-af','loudnorm=I=-16:TP=-1.5:LRA=9','-t','60','-movflags','+faststart',str(P/f'{name}.mp4')]
 proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
 for f in range(1440):
  proc.stdin.write(draw_frame(f/24,wide).tobytes())
  if f%240==0:print(name,f//24,'seconds rendered',flush=True)
 proc.stdin.close();assert proc.wait()==0
if __name__=='__main__':
 import sys
 if '--frames' in sys.argv:
  init()
  for wide in [False,True]:
   thumbs=[]
   for i,s in enumerate(SCENES):
    im=draw_frame(s[0]+2,wide);im.thumbnail((480,480));thumbs.append(im)
   cw,ch=thumbs[0].size;sheet=Image.new('RGB',(cw*3,ch*3))
   for i,im in enumerate(thumbs):sheet.paste(im,((i%3)*cw,(i//3)*ch))
   sheet.save(P/('storyboard-wide.jpg' if wide else 'storyboard-vertical.jpg'))
 else:
  asyncio.run(voices());audio();init();render(False);render(True)
