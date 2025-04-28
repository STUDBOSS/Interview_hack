import sounddevice as sd
import numpy as np

def record_audio(duration=5, samplerate=16000):
    print("Recording...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    return audio
