import pyttsx3

import speech_recognition as sr
import eel


def speak(text):

    engine = pyttsx3.init()

    voices = engine.getProperty("voices")
    engine.setProperty("rate", 175)
    engine.setProperty(
        "voice", voices[1].id
    )  # changing index, changes voices. 1 for female

    engine.say(text)
    engine.runAndWait()


@eel.expose
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        eel.displayMessage("I am listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 8)
        try:
            print("Recognizing...")
            eel.displayMessage("Recognizing...")
            query = r.recognize_google(audio, language="en-bn")
            eel.displayMessage(query)
            speak(query)
            eel.ShowHood()
        except Exception as e:
            print("Error: ", str(e), "\n")
            return "None"
        return query


@eel.expose
def takeAllCommand():
    pass
