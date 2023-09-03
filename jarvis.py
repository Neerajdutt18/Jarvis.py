import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from time import time, ctime
import webbrowser
import os
import random
import sys
import ctypes
import pyjokes 
from pyautogui import click
from playsound import playsound
import requests
from bs4 import BeautifulSoup
import json
import winsound
import pyautogui
import requests


list = ['bye    sir' , 'closing   myself']
m = ['thank  you  sir', 'my   pleasure   sir']
k = ["I  am  good " , "I'm  well", "I'm  pretty   good "]



search = "temperature in jammu"
url = f"http://google.com/search?q={search}"
r = requests.get(url)
data = BeautifulSoup(r.text,"html.parser")
temp = data.find("div",class_="BNeawe").text

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    strTime = datetime.datetime.now().strftime("%I:%M:%p")
    speak(f"{strTime} " )


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)    

def wishMe():

    hour = int(datetime.datetime.now().hour)
      
    if hour>=0 and hour<12:
        speak("GOOD MORNING SIR!!! " f"its {temp} temperature" )
        print("GOOD MORNING SIR!!! " f"its {temp} temperature" )
        speak("!!!!! today is")
        date()
        speak("and current time is.......")
        time()
        extra()
       


    elif hour>=13 and hour<18:
      speak("GOOD AFTERNOON SIR!!!")
      print("GOOD AFTERNOON SIR")

    else:
      speak("GOOD EVENING SIR!!!"  ) 
      print("GOOD EVENING SIR"  ) 
     

def extra():

        speak("how are you ??")
        query = takeCommand().lower()

        if 'i am good' in query or 'i am fine' in query:        
            speak("that's  cool sir ")    
            speak("tell me what can i do for you?")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query    


def TaskExecution():   
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com/")
            
        elif 'open google' in query:
            speak("Opening google") 
            speak( "what should I search in google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        
        
        elif 'how are you' in query or 'how r u'  in query or 'how' in query:
            n = random.choice(k)
            speak(n) 
               
      
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%MM:%p")
            speak(f"Its {strTime} " )

        elif 'date today' in query:
            speak("Today is ")
            date()
            
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")    
        
        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")

        elif "open twitter" in query:
            webbrowser.open("https://www.twitter.com/")

        elif 'play music' in query or 'play song' in query or 'play songs' in query:
            n = random.randint(0,24)
            print(n)

            music_dir = 'C:\\Users\\neera\\Music\\fav'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[n]))  
        
        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")
            
        elif 'introduce yourself' in query or 'tell me about yourself' in query:
            playsound("D:/Jarvis/mp3/jarvis_introduction_.mp3")   

        elif 'stop the music' in query :
            speak("ok  sir")    
            os.system("taskkill /f /im os.music.exe")    
         
        elif 'open code' in query:
            speak("Opening Visual studio code")
            codePath  = "C:\\Users\\neera\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'close the code' in query or 'close code' in query:
            speak("closing the code")    
            os.system("taskkill /f /im code.exe")

        elif 'play' in query:
            song = query.replace('play','')
            speak('playing'+ song)     

        elif 'lock' in query or 'lock the system' in query:
            speak("Locking    the    system")
            ctypes.windll.user32.LockWorkStation()

        elif 'open si' in query or 'open c' in query:
            speak("opening c")
            codePath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)
     
        elif 'close the c' in query or 'close si' in query:
            speak("closing the code")    
            os.system("taskkill /f /im devcpp.exe")
      
        elif 'open photos' in query:
            speak("opening    photos")
            codePath = "C:\\Users\\neera\\OneDrive\\Pictures\\Camera Roll"
            os.startfile(codePath)

        elif 'close the photos' in query or 'close photos' in query:
            speak("closing the photos")    
            os.system("taskkill /f /im explorer.exe")
     

        elif 'open document' in query:
            speak("opening    documents")
            codePath = "C:\\Users\\neera\\OneDrive\\Documents"
            os.startfile(codePath)  

        elif 'close the documents' in query or 'close documents' in query:
            speak("closing the documents")    
            os.system("taskkill /f /im explorer.exe")
       

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif 'hello jarvis' in query or 'hello' in query or 'jarvis' in query or 'hey jarvis' in query:
            speak("yes   sir! tell     me     what     can    i    do    for     you")

        elif 'shutdown the window' in query or 'shutdown' in query or 'sleep' in query:
            os.system("shutdown /s /t 30")
            speak("window  is   going   to    be   shutdown   in     30 seconds! Bye  Sir  ! Have   a   good   day  ")
            sys.exit() 

        elif  'who is amazon alexa' in query or 'who is siri assistant' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to sources")
            print(results)
            speak(results)
            speak("!!!! but   she   is   less   intelligent   then    me  ")
            

        elif  'excellent' in query or 'fantastic' in query or 'superb' in query:
            n = random.choice(m)
            speak(n)


        elif 'temperature ' in query:
            search = "temperature in jaipur"
            url = f"http://google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"sir its {temp} temperature")
           
        elif 'open stack overflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("https://stackoverflow.com/users/16061157/neeraj-dutt")
                 
        elif "exit" in query or "close yourself" in query or "bye bye jarvis" in query or "quit" in query:
            playsound("D:/Jarvis/mp3/Jbl Shutdown - Sound Effect.mp3")
            sys.exit()    

if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "wake up" in permission:
            playsound("D:/Jarvis/mp3/Startup Sound.mp3")
            TaskExecution()
        elif "exit" in permission or "close yourself" in permission:
            playsound("D:/Jarvis/mp3/Jbl Shutdown - Sound Effect.mp3")
            sys.exit()    

                         
