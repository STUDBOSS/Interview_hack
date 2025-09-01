# import whisper
# import numpy as np
# import tempfile
# import soundfile as sf

# # Load Whisper model once when the module is imported
# model = whisper.load_model("base")

# # def transcribe_audio(audio_data: np.ndarray, sample_rate: int = 16000) -> str:
# #     """
# #     Convert NumPy audio array to text using OpenAI's Whisper model.
    
# #     Args:
# #         audio_data (np.ndarray): Audio waveform data.
# #         sample_rate (int): Sampling rate of the audio data. Default is 16000 Hz.
        
# #     Returns:
# #         str: Transcribed text from the audio.
# #     """
# #     # Write audio to a temporary WAV file
# #     with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as tmpfile:
# #         sf.write(tmpfile.name, audio_data, sample_rate)
# #         result = model.transcribe(tmpfile.name)
# #         return result["text"].strip()

# def transcribe_audio(audio_data: np.ndarray, sample_rate: int = 16000) -> str:
#     import numpy as np
#     import tempfile
#     import soundfile as sf

#     if audio_data.size == 0:
#         raise ValueError("Received empty audio data.")

#     audio_data = audio_data.astype(np.float32)

#     with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
#         print(f"Writing audio to: {tmpfile.name}")
#         sf.write(tmpfile.name, audio_data, sample_rate)
#         result = model.transcribe(tmpfile.name)
#         return result["text"].strip()


# import whisper
# import tempfile
# import openai

# # Initialize OpenAI client with your API Key
# client = openai.OpenAI(
#     api_key=""
# )

# # Load Whisper model once
# model = whisper.load_model("base")

# def transcribe_audio(audio_path):
#     try:
#         result = model.transcribe(audio_path)
#         return result["text"]
#     except Exception as e:
#         print(f"[ERROR] Failed to transcribe audio: {e}")
#         return ""

# import sounddevice as sd
# import numpy as np
# import scipy.io.wavfile as wav
# import tempfile
# import os

# def record_audio(duration=5, fs=16000):
#     print("🎙️ Recording for {} seconds...".format(duration))
#     recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
#     sd.wait()
    
#     # Save recording to a temporary WAV file
#     tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
#     wav.write(tmpfile.name, fs, recording)
#     return tmpfile.name

# def transcribe_audio(audio_file_path):
#     # 🛠️ Use Whisper API OR your own code
#     # For now, dummy return (since you moved away from openai.whisper)
#     with open(audio_file_path, 'rb') as f:
#         data = f.read()
    
#     # You would send this to your Whisper endpoint or custom logic
#     print(f"Transcribing {audio_file_path}... (you can implement this)")
    
#     # 👇 TEMPORARY: simulate that transcription returns "Tell me about yourself."
#     return "Tell me about yourself."

# import sounddevice as sd
# import numpy as np
# import scipy.io.wavfile as wavfile
# import os
# import time

# SAMPLE_RATE = 16000  # 16 kHz
# DURATION = 5  # seconds
# OUTPUT_DIR = "recordings"

# if not os.path.exists(OUTPUT_DIR):
#     os.makedirs(OUTPUT_DIR)

# def record_audio(duration=DURATION):
#     print("🔴 Recording...")
#     recording = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype=np.int16)
#     sd.wait()

#     timestamp = int(time.time())
#     filename = f"{OUTPUT_DIR}/recording_{timestamp}.wav"
#     wavfile.write(filename, SAMPLE_RATE, recording)
    
#     print(f"✅ Audio recorded and saved to {filename}")
#     return filename

# def transcribe_audio(audio_path):
#     # ⚡ Dummy transcriber - only returns "Tell me about yourself."
#     # You can replace this later with actual Whisper or OpenAI API
#     print(f"📝 Transcribing audio from {audio_path}...")
    
#     # Simulate a recognized question
#     fake_questions = [
#         "Tell me about yourself.",
#         "What are your strengths and weaknesses?",
#         "Why do you want this job?",
#         "Describe a challenge you faced and how you overcame it.",
#         "Where do you see yourself in five years?"
#     ]
#     return np.random.choice(fake_questions)
