import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i in range(0,20):
	print(voices[i].id)
engine.setProperty('voice', voices[16].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Groot! How may I help you?")

if __name__ == "__main__":
    wishMe()
