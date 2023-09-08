import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr 
import requests
import pyjokes
import pyautogui
import webbrowser as web
import time
import wikipedia
import wolframalpha

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

def currenttime():
    Time = datetime.datetime.now().strftime("%I hours %M minutes %S seconds") #I-hours, M-minutes, S-seconds 
    print("The current time is " + Time)
    speak("The current time is " + Time)

def month():
    Month = datetime.datetime.now().strftime("%B") #B-month as full name
    print("The current month is " + Month)
    speak("The current month is " + Month)

def day():
    Day = datetime.datetime.now().strftime("%A") #A-weekday as full name
    print("The current day is " + Day)
    speak("The current day is " + Day)
    
def date():
    Date = datetime.datetime.now().strftime("%d %B %Y, %A") #d-date, B-month, Y-year, A-weekday
    print("The current date is " + Date)
    speak("The current date is " + Date)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        print("Good Morning! LIZ at your service.")
        speak("Good Morning! LIZ at your service.")
    elif hour >= 12 and hour < 16:
        print("Good Afternoon! LIZ at your service.")
        speak("Good Afternoon! LIZ at your service.")
    elif hour >= 16 and hour < 23:
        print("Good Evening! LIZ at your service.")
        speak("Good Evening! LIZ at your service.")
    else:
        print("Good Night! LIZ at your service.")
        speak("Good Night! LIZ at your service.")

def username():
    print("What should I call you?")
    speak("What should I call you?")
    Username = takeCommandMIC()
    print("Welcome " + Username)
    speak("Welcome " + Username)

def wishme():
    greeting()
    username()
    print("Please Tell Me How may I Assist You?")
    speak("Please Tell Me How may I Assist You?")

def takeCommandCMD():
    query = input("Please Tell Me How may I Assist You? \n")
    return query

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. . .")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising. . .")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        print("sorry i did not get that, can you please repeat. . .")
        speak("sorry i did not get that, can you please repeat. . .")
        return "None"
    return query

def jokes():
    Joke = pyjokes.get_joke()
    print(Joke)
    speak(Joke)

def whatsappmsg(phone_no, message):
    Message = message
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    pyautogui.press('enter')

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommandMIC().lower()
        if 'time' in query:
            currenttime()

        elif 'date' in query:
            date()  

        elif 'weekday' in query:
            day()

        elif 'month' in query:
            month()

        elif 'message' in query:
            user_name = {
                'Anushka': '+91 9057290632'
            }
            try:
                print("To whom you want to send the WhatsApp message?")
                speak("To whom you want to send the WhatsApp message?")
                name = takeCommandMIC()
                phone_no = user_name[name]
                print("What's the Message?")
                speak("What's the Message?")
                message = takeCommandMIC()
                whatsappmsg(phone_no, message)
                print("The Message has been sent")
                speak("The Message has been sent")
            except Exception as e:
                print(e)
                print("Unable to send the message")
                speak("Unable to send the message")
        
        elif 'joke' in query or "jokes" in query:
            jokes()

        elif 'wikipedia' in query:
            print("According to Wikipedia. . .")
            speak("According to Wikipedia. . .")
            query = query.replace("wikipedia",  "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'youtube' in query:
            web.open_new_tab("https://www.youtube.com")
            print("Youtube is open now")
            speak("Youtube is open now")

        elif 'gmail' in query or 'google mail' in query or 'mail' in query:
           web.open_new_tab("https://www.gmail.com")
           print("Google Mail is open now")
           speak("Google Mail is open now")
        
        elif 'news' in query:
            news = web.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            print("Here are some headlines from The Time of India, Happy reading!")
            speak("Here are some headlines from The Time of India, Happy reading!")       

        elif 'who are you' in query or 'what can you do' in query:
            print("I am LIZ, your persnal assistant. I am programmed to do minor tasks like - opening google chrome, youtube, google mail, searching wikipedia, predict date, time and month, message someone on WhatsApp, get headlines from The Times of India and open weather reports, tell some jokes and you can ask me computational or geographical questions too!.")
            speak("I am LIZ, your persnal assistant. I am programmed to do minor tasks like - opening google chrome, youtube, google mail, searching wikipedia, predict date, time and month, message someone on WhatsApp, get headlines from The Times of India and open weather reports, tell some jokes and you can ask me computational or geographical questions too!.")      

        elif "who made you" in query or "who created you" in query or "who discovered you" in query or 'who build you' in query:
            print("I was built by Anushka")
            speak("I was built by Anushka")


        elif 'Google' in query or 'search' in query:
            web.open_new_tab("https://www.google.com")
            print("Google chrome is open now")
            speak("Google chrome is open now")
        
        elif 'weather' in query:
            web.open_new_tab("https://www.accuweather.com/en/in/india-weather")
            print("Enter the location and weather reports will be displayed")
            speak("Enter the location and weather reports will be displayed")

        elif 'ask' in query:
            print('I can answer to computational and geographical questions. You may please ask now!')
            speak('I can answer to computational and geographical questions. You may please ask now!')
            question=takeCommandMIC()
            app_id="T7WVAU-7HJ7E868RH"
            client = wolframalpha.Client('T7WVAU-7HJ7E868RH')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        elif "good bye" in query or "ok bye" in query or "stop" in query or "bye" in query:
            print('LIZ is shutting down, thanks for giving me your time. Have a good day!')
            speak('LIZ is shutting down, thanks for giving me your time. Have a good day!')
            quit()