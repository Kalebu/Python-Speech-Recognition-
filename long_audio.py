import os 
from pydub import AudioSegment
import speech_recognition as sr
from pydub.silence import split_on_silence

recognizer = sr.Recognizer()

def load_chunks(filename):
    long_audio = AudioSegment.from_mp3(filename)
    audio_chunks = split_on_silence(
        long_audio, min_silence_len=1800,
        silence_thresh=-17
    )
    return audio_chunks

for audio_chunk in load_chunks('./sample_audio/long_audio.mp3'):
    audio_chunk.export("temp", format="wav")
    with sr.AudioFile("temp") as source:
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("Chunk : {}".format(text))
        except Exception as ex:
            print("Error occured")
            print(ex)

print("++++++")



