from pathlib import Path
import subprocess
import numpy as np
import torch
import soundfile as sf
from demucs.pretrained import get_model
from demucs.apply import apply_model
import imageio_ffmpeg
P=Path(__file__).resolve().parent/'reference-style';P.mkdir(exist_ok=True)
subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-y','-v','error','-i','/Users/sudarshan/Downloads/VIDEO-2026-07-15-16-00-57.mp4','-vn','-ar','44100','-ac','2',str(P/'reference-stereo.wav')],check=True)
x,sr=sf.read(P/'reference-stereo.wav',dtype='float32');w=torch.from_numpy(x.T.copy());ref=w.mean(0);mean=ref.mean();std=ref.std();w=(w-mean)/std
torch.set_num_threads(6)
print('Loading music separation model',flush=True)
model=get_model('htdemucs');model.cpu();model.eval()
with torch.no_grad():out=apply_model(model,w[None],device='cpu',shifts=0,split=True,overlap=.25,progress=True)[0]*std+mean
sources={name:out[i].numpy().T for i,name in enumerate(model.sources)}
music=sum(a for name,a in sources.items() if name!='vocals')
sf.write(P/'reference-music.wav',music,sr,subtype='PCM_24');sf.write(P/'reference-vocals.wav',sources['vocals'],sr,subtype='PCM_24')
print('Separated reference music and narration',flush=True)
