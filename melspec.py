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
n_mels = 320


def scale_minmax(X, min=0.0, max=1.0):
	X_std = (X - X.min()) / (X.max() - X.min())
	X_scaled = X_std * (max - min) + min
	return X_scaled


#audioname = input("Which name did you put in your audio file? ")
data, sr = librosa.load("files/sr.wav")
mel_spec = librosa.feature.melspectrogram(y=data, sr=sr, n_mels= n_mels)
mel_db = (librosa.power_to_db(mel_spec, ref=np.max) + 40)/40
np.save("files/sr.npy", mel_db)
smel = np.load("files/sr.npy")
img = scale_minmax(smel, 0, 255).astype(np.uint8)
img = np.flip(img, axis=0) # put low frequencies at the bottom in image
img = 255-img # invert. make black==more energy
im = Image.fromarray(img)
img_path = "files/sr.png"
im.save(img_path)
