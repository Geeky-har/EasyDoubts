import speech_recognition as sr
import moviepy.editor as mp
import re

vid1 = mp.VideoFileClip('static/osvid.mp4')
vid1.audio.write_audiofile('osvid.wav')

r = sr.Recognizer()
with sr.AudioFile('osvid.wav') as source:
    audio = r.record(source)

text = r.recognize_google(audio)

doubt = re.findall(r'\bd\w{6}k\b|\bm\w{5}\s\w{9}|\bh\w{3}\s\w{3}\s\w{4}|\bc\w{7}\s\w{4}|\bp\w{8}n\b|'
                   r'\br\w{3}\s\w{4}', text)

for i in doubt:
    print(i)

