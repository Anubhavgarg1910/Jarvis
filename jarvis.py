import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


engine = pyttsx3.init()

voices = engine.getProperty('voices')                 
engine.setProperty('voice', voices[2].id)

newVoiceRate = 140
engine.setProperty('rate', newVoiceRate)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    # time()
    # date()
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    elif hour>=18 and hour<=24:
        speak("Good evening")
    else:
        speak("Good night") 
    speak("I am Jarvis. How can I help you?")
# wishme()

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognising")
#         query = r.recognize_google(audio, 'en=US')
#         print(query)
#     except Exception as e:
#         print(e)
#         speak("Say that again please...")
#         return "None"
#     return query 
# takeCommand()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising...")
            # print (r.recognize_google(audio,language = 'en-in'))
            query = r.recognize_google(audio,language = 'en-in')
        except Exception as e:
            print("Error :  " + str(e))
            speak("Repeat the speech again")
            return "None"
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
        return query
# takeCommand()

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("utkarsh191020@gmail.com","utkarshgarg")
    server.sendmail("utkarsh191020@gmail.com",to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("/home/anubhav/Downloads/shot.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)
        if "time" in query:
            time()

        elif "date" in query:
            date()
        
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            speak(result)

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                # sendmail(to,content)
                speak(content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = "/usr/bin/google-chrome-stable /usr/share/man/man1/google-chrome-stable.1.gz %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "logout" in query:
            os.system("shutdown - 1")
        
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        
        elif "play songs" in query:
            songs_directory= " "
            songs = os.listendir(songs_directory)
            os.startfile(os.path.join(songs_directory,songs[0]))

        
        elif "remember that" in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You told me to remember "+ data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember= open("data.txt","r")
            speak("You told me to remember that" +remember.read())
            remember.close()

        elif "screenshot" in query:
            screenshot()
            speak("Screenshot captured")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()

        elif "offline" in query:
            quit()





