from gtts import gTTS
from playsound import playsound
import datetime
import webbrowser
import wikipedia
import json, codecs, apiai
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
        user_query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {user_query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return user_query


if __name__ == "__main__":
    wishMe()

    CLIENT_ACCESS_TOKEN = "7f790c9c5d11467493162773c9196204 "
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.lang = 'en '
    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    while True:
        user_query = takeCommand().lower()

        if 'what is' in user_query:
            print("Searching wikipedia...")
            user_query = user_query.replace("what is", "")
            results = wikipedia.summary(user_query, sentences=2)
            speak("According to Wikipedi...")
            # speak("Baba Bole...")
            print(results)
            speak(results)

        elif 'open youtube' in user_query:
            print("Opening YouTube...")
            webbrowser.open_new_tab("https://www.youtube.com/")

        elif 'open github' in user_query:
            print("Opening GitHub...")
            webbrowser.open_new_tab("https://github.com/")

        elif 'open google' in user_query:
            print("Opening Google...")
            webbrowser.open_new_tab("https://www.google.com/")

        elif 'the time' in user_query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        else:
            request.query = user_query
            response = request.getresponse()
            obj = json.load(response)
            reply = obj['result']['fulfillment']['speech']
            speak(reply)
