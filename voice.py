import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime

#Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_commands():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing....")
        command = recognizer.recognize_google(audio)
        print("You said:",command) 
        return command.lower()
    except Exception:
        print("sorry, please say that again..")
        return ""
    
def wish_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning \n I am your virtual Assitance")
    elif hour < 18:
        speak("Good Afternoon \n I am your virtual Assitance")
    else:
        speak("Good evening \n I am your virtual Assitance")
wish_user()

while True:
    command = take_commands()
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %P")
        speak(f"The time is {time}")
        
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")    
 
    elif "Who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(command, 2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("Goodbye")
        break
        














        
        
