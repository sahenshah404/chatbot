import pyttsx3
import os
import datetime
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('rate',120)
engine.setProperty('voice',voices[2].id)


answers={
    "hi":"Hi how are you",
    "who are you" : "i am your personal assistant  sir, name is reaas",
    "what is your name":"my name is reaas ",
    "whats your name" : "my name is reaas "
}


def speak(text):
    engine.say(text)
    engine.runAndWait()

def start(name):
    os.startfile(name)

def wish():
    time=int(datetime.datetime.now().hour)
    

command=input()
command=command.lower()
if "open" in command:
    pos=command.find("open")
    command=command[pos:]
    command=command.replace("open ","")
    start(command)
#speak(answers.get(command,"i dont know this command sir"))
    
