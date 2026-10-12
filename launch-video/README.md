# Astra Automation — launch video

Both MP4 exports are exactly 60 seconds, 24 fps, with H.264 video, AAC audio, and embedded open captions.

- astra-launch-vertical.mp4: 1080 × 1920, 9:16; Instagram Reels, YouTube Shorts, and vertical LinkedIn posts.
- astra-launch-widescreen.mp4: 1920 × 1080, 16:9; YouTube and widescreen LinkedIn posts.
- voiceover.wav: isolated English narration from the original Astra cut.
- reference-style/voiceover.wav: revised narration with the reference-video delivery style.
- reference-style/reference-music.wav: music separated from the user-provided reference video and extended with crossfades.
- captions.srt: optional subtitle sidecar matching the on-screen phrase timing.
- posting-copy.txt: suggested post text.
- voiceover-script.txt: full narration.

The current MP4s use Microsoft’s en-US-AndrewMultilingualNeural synthetic voice with relaxed conversational pacing and the music bed from the user-provided reference video, extended to the full minute. The voice is not a recording of a human actor. Use the reference music only if you own it or have permission to reuse it. Brand marks are the supplied Astra assets. Illustrations are original schematic service demonstrations, not customer results.

The Vercel address is used because the custom domain failed its HTTPS check during production. Files are prepared for the user to post; no social accounts were posted to.

Rebuild: install pillow, numpy, imageio-ffmpeg, and edge-tts in a Python environment, then run produce.py. The script uses Arial fonts from macOS. Internet access is needed only for narration generation when narration files are missing.
