import IPython.display as ipd
import sounddevice as sd
import soundfile as sf
import librosa
import os
import numpy as np
from PIL import Image
import cv2

samplerate = 48000  
duration = 8 # seconds

print("start")
audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, blocking=True)
print("end")
sd.wait()
audio_path = "files/sr.wav"
sf.write(audio_path, audio, samplerate)

