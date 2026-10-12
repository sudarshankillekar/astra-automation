from pathlib import Path
import numpy as np, soundfile as sf
from scipy.signal import resample_poly
from scipy.ndimage import uniform_filter1d
P=Path(__file__).resolve().parent
voice,sr=sf.read(P/'reference-style/voiceover.wav',dtype='float32'); music,sr2=sf.read(P/'reference-style/reference-music.wav',dtype='float32')
if sr2 != sr:
    music = resample_poly(music, sr, sr2, axis=0)
if voice.ndim==1: voice=voice[:,None]
if music.ndim==1: music=music[:,None]
# Keep the reference's stereo character and create a seamless 60s bed by repeating it with short crossfades.
target=60*sr
music=np.vstack([music, music, music[:int(20.2*sr)]])
music=music[:target]
fade=np.minimum(np.arange(target)/sr/1.2,1)*np.minimum((target-np.arange(target))/sr/1.5,1)
music*=fade[:,None]
# Reference narration loudness is moderate; keep Astra narration forward and music supportive.
voice=np.pad(voice,((0,max(0,target-len(voice))),(0,0)))[:target]
vrms=np.sqrt(np.mean(voice**2)); mrms=np.sqrt(np.mean(music**2))
# Voice-led ducking keeps the reference track audible in transitions and pauses,
# then gently lowers it whenever narration is present.
speech=uniform_filter1d(np.abs(voice.mean(axis=1)), size=int(.32*sr), mode='nearest')
speech_amount=np.clip((speech-.004)/.018, 0, 1)
music_gain=0.12*(1-0.58*speech_amount)
music=music*(music_gain[:,None]/max(mrms,1e-6))
mix=voice*(0.78/max(vrms,1e-6))*0.36 + music
peak=np.max(np.abs(mix));mix*=0.9/max(peak,0.9)
sf.write(P/'reference-style/mix-reference.wav',mix,sr,subtype='PCM_16')
print({'voice_rms':float(vrms),'music_rms':float(mrms),'duration':len(mix)/sr,'peak':float(peak)})
