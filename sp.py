
import speech_recognition as sr
import pyaudio
import pyttsx
import os

#initialising text to speech
engine = pyttsx.init()

#to speak
os.system("espeak 'Hello Siddharth I am Jarvis'")
os.system("espeak 'Say Something'")
#engine.say('Say Something')
#engine.runAndWait()

# obtain audio from the microphone
r = sr.Recognizer()
engine.setProperty('rate',150)
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
	
# recognize speech using Sphinx
try:
    print("Jarvis thinks you said " + r.recognize_google(audio,language ="en-US"))
    engine.say("Jarvis thinks you said")
    engine.say(r.recognize_google(audio))
    engine.runAndWait()
except sr.UnknownValueError:
    print("Jarvis could not understand audio")
except sr.RequestError as e:
    print("Jarvis error; {0}".format(e))


