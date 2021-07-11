import datetime
import webbrowser
from pygame import mixer
import random
import pyttsx3
import speech_recognition as rs
import wikipedia
import os

voice = pyttsx3.init('sapi5')
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[0].id)


def speak(audio):  # Speaks sentences which is given to this function
    voice.say(audio)
    voice.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour < 12 and hour >= 1:
        speak("Good Morning, Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
    elif hour >=18 and hour < 21:
        speak("Good Evening Sir")
    else:
        speak("Good Night, Sir")


def TakeCommand():  # take speech from user as input
    speech = rs.Recognizer()

    with rs.Microphone() as source:
        print("Listening....")
        speech.pause_threshold = 1
        audio = speech.listen(source)
    try:
        print("Recognizing...")
        query = speech.recognize_google(audio, language="en-in").lower()
        print(f"User Said: {query}.")
    except Exception:
        print("Please! Say Again")
        return "None"
    return query


def musicPlayer(audio):
    mixer.init()
    mixer.music.load(audio)
    mixer.music.set_volume(0.7)
    mixer.music.play()


if __name__ == "__main__":
    wishme()
    print("Welcome to Randeep Singh's computer.  ")

    speak("Welcome to Randeep Singh's computer. Hello Sir ")
    speak("how my I help you ")
    while True:
        randomNumber = random.randint(1, 3)
        query = TakeCommand()

        if "google" in query:
            webbrowser.open("google.com")
        elif "what is your name" in query:
            speak("I am randeeps personal assistant")
        elif "exit" in query:
            break
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif "song" in query:
            speak("playing song")

            if randomNumber == 1:
                musicPlayer(
                    "C:\\Users\\akash\\OneDrive\\Desktop\\2020\\Aditya_Karan_Aujla_Mp3_Song_Download-(NewDjRemixSong).mp3")
            elif randomNumber == 2:
                musicPlayer(
                    "C:\\Users\\akash\\OneDrive\\Desktop\\2020\\Jhanjran - (amlijatt.in).mp3")
            elif randomNumber == 3:
                musicPlayer(
                    "C:\\Users\\akash\\OneDrive\\Desktop\\2020\\Shadow - Singga (DjPunjab.Com).mp3")
        elif "youtube" in query:
            webbrowser.open("youtube.com")
        elif "hello" in query:
            speak("Hello sir")
        elif "date" in query:
            print(f"Todays Date is {datetime.date.today()}")
            speak(f"Todays Date is {datetime.date.today()}")
        elif "code" in query:
            os.startfile(r"C:\Users\akash\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code")
        elif "time" in query:
            print(f"Time is {datetime.datetime.now()}")
            speak(f"Time is {datetime.datetime.now().hour - 12}")
