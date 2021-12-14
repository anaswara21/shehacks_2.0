import pyttsx3 as p
import speech_recognition as sr
from pyaudio import *
import pyjokes
import datetime
import webbrowser
import requests
import json
import wikipedia

'''
project:-personal assistant
1) use "open" comment to open youtube,google,facebook
   ex:-open youtube
2) use "search" comment to search anything in browser
   ex:-search python
3) use "exit" comment to exit from the assistant
4)other features 
   a)update date,time and weather
   b)say joke

'''

def say(text1):
    engine.say(text1)
    engine.runAndWait()

def say_print(x):
    engine.say(x)
    print(x)
    engine.runAndWait()
    
def joke():
    joke=pyjokes.get_joke()
    say_print(joke)

def date():
    d=datetime.datetime.now().date()
    say_print(d)
    say_print(d.strftime('%A'))

def time():
    d=datetime.datetime.now().time()
    if d.hour<12:
        d1=str(d.hour)+":"+str(d.minute)+"AM"
        say_print(d1)
    elif d.hour<13:
        d1=str(d.hour)+":"+str(d.minute)+"PM"
        say_print(d1)
        
    else:
        d1=str(d.hour-12)+":"+str(d.minute)+"PM"
        say_print(d1)
        
def good():
    d1=datetime.datetime.now().time()
    if d1.hour<12:
        say_print("good morning sir")
        
    elif d1.hour<17:
        say_print("good afternoon sir")
        
    else:
        say_print("good evening sir") 
        
     
def weather():
    say("please say your city name")
    with sr.Microphone() as source:
        print("Listening...")
        audio=r1.listen(source)
    
        text=r1.recognize_google(audio)
        text=text.lower()
        print(text) 
        city=text
    
        api="a0433d43c30daac5a7856979a2718538"
        base="http://api.openweathermap.org/data/2.5/weather?"
        url=base+"appid="+api+"&q="+city
        response=requests.get(url)
        
        data=response.json()
        if data["cod"]!=404:
            y=data["main"]
            t=y["temp"]
            p=y["pressure"]
            h =y["humidity"]
            temperature="temperature is "+str(t)+" kelvin"
            pressure="pressure is "+str(p)+" mb"
            humidity="humidity is  " +str(h)+"%"
            
            say_print(temperature)
            say_print( pressure)
            say_print(humidity)
    
engine =p.init()
v=engine.getProperty('voices')
engine.setProperty('voice',v[1].id)
r=engine.getProperty('rate')
engine.setProperty('rate',170)
good()
say_print("hey i am rubi your personal assistant")


r1=sr.Recognizer()
r1.energy_threshold=600

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio=r1.listen(source)
        try:
            text=r1.recognize_google(audio)
            text=text.lower()
            print(text) 
        
            
            list=["hello","hai","hi","hey"]
            list1=["fine","good","great"]

            if any(x in text for x in list):
                say_print("hello sir how are you")

            elif any(x in text for x in list1):   
                say_print("how can i help you sir")

            elif 'what about you' in text:
                say_print("i am good sir.how can i help you sir")

            elif 'joke' in text:
                joke()
                
            elif 'date' in text:
                date()

            elif 'time' in text:
                time()

            elif 'open youtube' in text:
                
                webbrowser.open("youtube.com")

            elif 'open google' in text:
                webbrowser.open("google.com")

            
            elif 'open facebook' in text:
                webbrowser.open("facebook.com")

            elif 'weather'  in text:
                weather()

            elif 'search' in text:
                say_print("searching")
                text=text.replace("search","")
                result=wikipedia.summary(text,sentences=2)
                say_print(result)

            elif 'exit' in text:
                say_print("have a nice day sir")
                break
        
            else:
                say(" i couldn't get it ,can you please repeat this")
        except Exception as e:
            print("say again")







