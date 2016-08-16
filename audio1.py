import pyaudio
import wave
import sys

CHUNK = 1024

wavefile = wave.open("sin440.wav", "rb")

audio = pyaudio.PyAudio()

stream = audio.open(
    format=audio.get_format_from_width(wavefile.getsampwidth()),
    channels=wavefile.getnchannels(),
    rate=wavefile.getframerate(),
    output=True
)

data = wavefile.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wavefile.readframes(CHUNK)

stream.stop_stream()
stream.close()

audio.terminate()
