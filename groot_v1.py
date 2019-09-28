from gtts import gTTS
from playsound import playsound
import datetime
import webbrowser
import wikipedia
import speech_recognition as sr

def speak(mytext):
    myobj = gTTS(text=mytext, lang='hi', slow=False)
    myobj.save("groot.mp3")
    playsound("groot.mp3")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0  and hour < 12:
        mytext = "Good Morning!"

    elif hour >= 12 and hour < 18:
        mytext = "Good Afternoon!"

    else:
        mytext = "Good Evening!"

    mytext = mytext + (" I am Groot, version 1.0,  How may I help you?")
    speak(mytext)


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
    while True:
        query = takeCommand().lower()

        if 'what is' in query:
            print("Searching wikipedia...")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedi...")
            # speak("Baba Bole...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("Opening YouTube...")
            webbrowser.open_new_tab("https://www.youtube.com/")

        elif 'open github' in query:
            print("Opening GitHub...")
            webbrowser.open_new_tab("https://github.com/")

        elif 'open google' in query:
            print("Opening Google...")
            webbrowser.open_new_tab("https://www.google.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
