import smtplib   # pip install pyttsx3
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtpd
import webbrowser as wb
import os
import pyautogui
import psutil     # pip install psutil
import pyjokes

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(time)


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
    time()
    date()git add Cortana.py data.txt
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternonn sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening sir!")
    else:
        speak("Good night sir!")
    speak("Cortana at youre service,Please tell me how cane i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please!")

        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail',587)
    server.ehlo()
    server.starttls()
    server.login('123@gmail.com','123')
    server.sendmail('123@gmail.com', to,content)
    server.close

def screenshot():
    img = pyautogui.screenshot()
    img.save(r'C:\Users\Desktop\Music')


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()
    speak("Your battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'Time' in query:
            time()

        elif 'Date' in query:
            date()

        elif 'Wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'Send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = '1234@gmail.com'
                #sendEmail(to,content)
                speak("content")
            except Exception as e:
                print(e)
                speak("Unable to send the mail!")

        elif 'Search in chrome' in query:
            speak("What should i search?")
            chromepath = 'C:/Program Files(x86)/Google/Chrome/Application/chrome.exe %s' #Add path to Chrome directory
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'Logout' in query:
            os.system("shutdown -1")

        elif 'Shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'Restart' in query:
            os.system("shutdown /r /t 1")

        elif 'Play songs' in query:
            songs_directory = r'C:\Users\Desktop\Music'
            songs = os.listdir(songs_directory)
            os.startfile(os.path.join(songs_directory,songs[0]))

        elif 'Remember that' in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("You said me to remember that" + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'Do you know anything' in query:
            remember = open('data.txt','r')
            speak("You said me to remember that" + remember.read())

        elif 'Take screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()


        elif 'offline' in query:
            quit()

