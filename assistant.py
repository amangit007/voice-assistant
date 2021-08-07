import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import smtplib
import requests
from urllib.request import urlopen
import os
import ctypes
import subprocess
import winshell
from ecapture import ecapture as ec
from forex_python.converter import CurrencyRates
import assistant_name


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text) :
    engine.say(text)

    engine.runAndWait()


def set_name(myname="alexa") :
    return myname


def take() :
    try :
        with sr.Microphone() as source :
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            name = assistant_name.set_name()
            if name in command :
                command = command.replace(name, '')
                print(command)

    except :
        pass
    return command


def take_mid() :
    try :
        with sr.Microphone() as source :
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)

    except :
        pass
    return command


def sendEmail(to, content) :
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()


def run() :
    command = take()
    print(command)
    if 'play' in command :
        song = command.replace('play', '')

        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command :
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk(time)
        print(time)

    elif 'search on wikipedia' in command :
        person = command.replace('search on wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command :
        data = pyjokes.get_joke()
        print(data)
        talk(data)

    elif 'open youtube' in command :
        talk("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif 'search' in command :
        rio = command.replace('search', '')
        talk('here you go...')
        pywhatkit.search(rio)

    elif 'give me info of' in command :
        jio = command.replace('give me info of', '')
        jim = pywhatkit.info(jio, 1)
        print(jim)



    elif 'send a mail' in command :
        try :
            talk("What should I say?")
            content = take_mid()
            talk("whom should i send")
            to = input()
            sendEmail(to, content)
            talk("Email has been sent successfully !")
            print("Email has been sent successfully !")
        except Exception as e :
            print(e)
            talk("I am not able to send this email")

    elif 'send mail to deepika' in command :
        try :
            talk("What should I say?")
            content = take_mid()

            to = 'email to send'
            sendEmail(to, content)
            talk("Email has been sent successfully !")
            print("Email has been sent successfully !")
        except Exception as e :
            print(e)
            talk("I am not able to send this email")

    elif "weather" in command :
        try :
            # Google Open weather website
            # to get API of Open weather

            talk(" City name ")
            print("City name : ")
            city = take_mid()

            response = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,
                                                                                                          "YOUR API KEY"))
            x = response.json()

            if x["cod"] != "404" :
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature=current_temperature-273
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in celsius unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(
                    weather_description))

            else :
                talk(" City Not Found ")


        except Exception as e :

            print(str(e))
    elif 'news' in command :

        try :
            main_url = "https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=YOUR API KEY"

            # fetching data in json format
            open_news = requests.get(main_url).json()

            # getting all articles in a string article
            article = open_news["articles"]
            # empty list which will
            # contain all trending news
            results = []

            for ar in article :
                results.append(ar["title"])

            for i in range(len(results)) :
                # printing all trending news
                print(i + 1, results[i])
                talk(results[i])

        except Exception as e :

            print(str(e))
            # for internal files ,use exe files to launch any app
    elif 'open file' in command :
        codePath = r"C:\\11n.png"
        os.startfile(codePath)
    elif 'lock window' in command :
        talk("locking the device")
        ctypes.windll.user32.LockWorkStation()
    elif 'shutdown system' in command :
        talk("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif 'empty recycle bin' in command :
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        talk("Recycle Bin Recycled")

    elif "where is" in command :
        query = command.replace("where is", "")
        location = query
        talk("User asked to Locate")
        talk(location)
        webbrowser.open("https://www.google.nl/maps/place/" + location + "")

    elif "camera" in command or "take a photo" in command :
        try :
            ec.capture(0, "Jarvis Camera ", "img.jpg")
        except :
            pass



    elif "restart" in command :
        subprocess.call(["shutdown", "/r"])

    elif "thank you" in command:
        talk("Thank you for giving me you time")
        print("thank you for giving me your time")
        exit()

    elif "write a note" in command :
        talk("What should i write, sir")
        note = take_mid()
        file = open('helloman.txt', 'w')

        if file.write(note) :
            print("File is written succesfuly")


    elif "show note" in command :
        talk("Showing Notes")
        file = open("helloman.txt", "r")
        print(file.read())
        talk(file.read(6))

    elif "change you name" in command :
        talk("ok,what should be my name")
        new_name = take_mid()
        if set_name(new_name) :
            talk("my new name" + new_name + "is set succesfully")



    elif 'exchange rate' in command :

        c = CurrencyRates()
        v=c.get_rate('USD', 'INR')
        print(v)
        talk("current rate is")
        talk(v)

while True:
    run()
