import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# for i in range(0,20):
    # print(voices[i].id)
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

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recoginzing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    takeCommand()
