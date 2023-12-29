import IPython.display as ipd
import soundfile as sf

# Path to the recorded audio file
audio_path = "files/sr.wav"

# Load the audio file
audio, samplerate = sf.read(audio_path)

# Display the audio
ipd.Audio(audio, rate=samplerate)
