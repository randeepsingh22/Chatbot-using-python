from tkinter import *
from pygame import mixer
from PIL import ImageTk, Image
import wikipedia
import webbrowser
import datetime
import pyttsx3
import speech_recognition as rs
import random
import tkinter.messagebox as msg
import os



voice = pyttsx3.init('sapi5')
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[0].id)


def musicPlayer(audio):
    mixer.init()
    mixer.music.load(audio)
    mixer.music.set_volume(0.7)
    mixer.music.play()


def speak(audio):  # Speaks sentences which is given to this function
    voice.say(audio)
    voice.runAndWait()


def TakeCommand():  # take speech from user as input
    speech = rs.Recognizer()

    with rs.Microphone() as source:
        textarea.insert(END, "Listening....\n")
        speech.pause_threshold = 1
        audio = speech.listen(source)
    try:
        textarea.insert(END, "Recogonizing...\n")
        query = speech.recognize_google(audio, language="en-in").lower()
        textarea.insert(END, f"                     User Said: {query}.\n")
    except Exception:
        textarea.insert(END, "Please! Say Again")
        return "None"
    return query


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour < 12 and hour >= 1:

        speak("Good Morning, Sir")
    elif hour >= 12 and hour < 18:

        speak("Good Afternoon sir")
    elif hour >= 18 and hour < 21:

        speak("Good Evening Sir")
    else:

        speak("Good Night Sir")


def askBySpeaking():

    speak("how can i help you Sir")
    randomNumber = random.randint(1, 3)
    query = TakeCommand()

    if "google" in query:
        textarea.insert(END, "Opening Google\n")
        webbrowser.open("google.com")
            
    elif "name" in query:
        textarea.insert(END, "I am Randeep's Personal assistant\n")
        speak("I am randeeps personal assistant")
    elif "exit" in query:
        permission = msg.askquestion("Exit", "Do you want to Exit ?")
        if (permission == "yes"):
            root.destroy()
                
    elif "wikipedia" in query:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        textarea.insert(END, results)
        speak(results)
            
    elif "song" in query:
        textarea.insert(END, "Playing Song\n")
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
        textarea.insert(END, "Opening Youtube\n")
        webbrowser.open("youtube.com")
            
    elif "hello" in query:
        textarea.insert(END, "Hello! Sir\n")
        speak("Hello sir")
            
    elif "date" in query:
        textarea.insert(END, f"Todays Date is {datetime.date.today()}\n")
        speak(f"Todays Date is {datetime.date.today()}")
            
    elif "code" in query:
        os.startfile(
            r"C:\Users\akash\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            
    elif "time" in query:
        textarea.insert(END, f"Time is {datetime.datetime.now()}\n")
        speak(f"Time is {datetime.datetime.now().hour} o Clock")
            


def askByWriting():
    
    global takecommand
    randomNumber = random.randint(1, 3)
    query = takecommand.get()

    if "google" in query:
        textarea.insert(END, "Opening Google\n")
        webbrowser.open("google.com")
    elif query == "":
        msg.showinfo("Type Error","Please Type Something in Text area?")  
    elif "name" in query:
        textarea.insert(END, "I am Randeep's Personal assistant\n")
        
    elif "exit" in query:
        permission = msg.askquestion("Exit", "Do you want to Exit ?")
        if (permission == "yes"):
            root.destroy()
            
    elif "wikipedia" in query:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        textarea.insert(END, results)
        
        
    elif "song" in query:
        textarea.insert(END, "Playing Song\n")
       

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
            textarea.insert(END, "Opening Youtube\n")
            webbrowser.open("youtube.com")
        
    elif "hello" in query:
        textarea.insert(END, "Hello! Sir\n")
        
        
    elif "date" in query:
        textarea.insert(END, f"Todays Date is {datetime.date.today()}\n")
        
        
    elif "code" in query:
        os.startfile(
                r"C:\Users\akash\AppData\Local\Programs\Microsoft VS Code\Code.exe")
        
    elif "time" in query:
        textarea.insert(END, f"Time is {datetime.datetime.now()}\n")
    takecommand.set("")
        


root = Tk()

takecommand = StringVar()

root.title("Chat Bot | Developed By Randeep")
root.iconbitmap("messages.ico")
root.geometry("700x590")
root.maxsize(700, 590)
root.minsize(700, 590)
color = "#567437"
f1 = Frame(root, background=color)
f1.pack(fill="x", pady=5)

f2 = Frame(f1)
f2.pack(padx=200)
image_open = Image.open("message.png")
resized = image_open.resize((50, 50), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized)

lbl = Label(f2, image=img)
lbl.grid(row=0, column=0)

lbl = Label(f2, text="ChatBot ®Randeep", font="Lucida 15 bold", fg="#567437")
lbl.grid(row=0, column=1)

f3 = Frame(root)
f3.place(x=25, y=75)

textarea = Text(f3, background="white",
                font="helvatica 11 bold", pady=5)

textarea.insert(END, "Welcome to Randeep Singh's Computer.\n  ")
textarea.grid(row=0, column=0, columnspan=2)



lbl = Label(f3, text="Type here", font="Helvati",
            fg=color).grid(row=1, column=0)

textEntry = Entry(f3, font="helvatica 10",
                  textvariable=takecommand,width=50).grid(row=1, column=1)

btn = Button(f3, text="Ask By Speaking", font="helvatica 12 bold", command=askBySpeaking,
             width=25, background="#006622", fg="white").grid(row=2, column=0, pady=5)

btn = Button(f3, text="Ask By Typing", font="helvatica 12 bold", width=25,
             background="#006622", fg="white", command=askByWriting).grid(row=2, column=1, pady=5)

root.mainloop()
