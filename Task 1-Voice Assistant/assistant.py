import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    r.pause_threshold = 1

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You:", query)
    except:
        print("Say that again...")
        return "none"

    return query.lower()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")


def run_assistant():
    while True:
        query = take_command()

        if "hello" in query or "hi" in query:
            speak("Hello, how can I help you")

        elif "time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak("Current time is " + time)

        elif "date" in query:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + date)

        elif "who is" in query or "what is" in query:
            try:
                speak("Searching Wikipedia...")
                result = wikipedia.summary(query, sentences=1)
                speak(result)
            except:
                speak("Sorry, I couldn't find that")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "exit" in query or "stop" in query or "bye" in query:
            speak("Goodbye")
            break

        elif query == "none":
            continue

        else:
            speak("I didn't understand, please say again")

wish()
run_assistant()