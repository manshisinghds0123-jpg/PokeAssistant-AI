import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import pyjokes
import requests
import urllib.parse
from openai import OpenAI
from datetime import datetime

# Initialize voice engine
try:
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

except Exception:
    engine = None

def speak(text):
    print("Assistant:", text)

    if engine:
        engine.say(text)
        engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception:
        speak("Sorry, I didn't understand.")
        return ""

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(question):
    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=question
        )

        answer = response.output_text
        speak(answer)

    except Exception:
        speak("Sorry, I could not connect to AI.")

def weather():

    API_KEY = "YOUR_API_KEY"

    CITY = "Delhi"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    try:
        data = requests.get(url).json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        speak(f"The temperature is {temp} degree Celsius with {desc}")

    except:
        speak("Unable to get weather.")




def main():
    speak("Hello Mansi. Welcome to PokeAssist AI.")
    speak("I am ready. Please tell me a command.")

    while True:

        
        command = take_command()

        if command == "":
            continue


        if command in ["exit", "stop", "goodbye"]:
          speak("Goodbye Mansi. Have a nice day.")
          break


        if "hey poke" not in command:
           continue

        command = command.replace("hey poke", "").strip()
        
        

        if "hello" in command:
            speak("Hello Mansi. Nice to see you.")

        elif "open chrome" in command:
            speak("Opening Google Chrome")
            os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open chatgpt" in command or ("chat" in command and "gpt" in command):
            speak("Opening ChatGPT")
            webbrowser.open("https://chatgpt.com")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open gmail" in command:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com")

        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        elif "open calculator" in command:
            speak("Opening Calculator")
            os.system("calc")

        elif "open paint" in command:
            speak("Opening Paint")
            os.system("mspaint")

        elif "open command prompt" in command:
            speak("Opening Command Prompt")
            os.system("start cmd")

        elif "open vs code" in command or "open v s code" in command:
            speak("Opening Visual Studio Code")
            os.system("code")

       

        elif "what time is it" in command or "tell me the time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speak("The time is " + current_time)
        elif command.startswith("search "):
            query = command.replace("search ", "")
            speak("Searching Google for " + query)
            webbrowser.open("https://www.google.com/search?q=" + query)
        elif "tell me the date" in command or "what is today's date" in command:
            today = datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + today)
        
        
        elif "open documents" in command:
            speak("Opening Documents")
            os.startfile(r"C:\Users\91965\Documents")

        elif "open downloads" in command:
            speak("Opening Downloads")
            os.startfile(r"C:\Users\91965\Downloads")

        elif "open desktop" in command:
            speak("Opening Desktop")
            os.startfile(os.path.join(os.environ["USERPROFILE"], "Desktop"))

        elif command.startswith("play "):
            song = command.replace("play ", "")
            speak("Playing " + song)
            query = urllib.parse.quote(song)
            webbrowser.open("https://www.youtube.com/results?search_query=" + query)

        elif "tell me the date" in command or "what is today's date" in command:
            today = datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + today)

        elif "what day is today" in command:
            day = datetime.now().strftime("%A")
            speak("Today is " + day)

        elif "tell me a joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif command.startswith("repeat "):
            message = command.replace("repeat ", "")
            speak(message)

        elif command.startswith("calculate "):
            try:
                expression = command.replace("calculate ", "")
                result = eval(expression)
                speak("The answer is " + str(result))
            except:
                speak("Sorry, I could not calculate that.")

        elif command.startswith("ai "):
            question = command.replace("ai ", "")
            speak("Thinking...")
            ask_ai(question)

        elif "weather" in command:
            weather()
       

        # -------------------------
        # Lock Computer
        # -------------------------

        elif "lock computer" in command or "lock pc" in command:
            speak("Locking your computer.")
            os.system("rundll32.exe user32.dll,LockWorkStation")

        # -------------------------
        # Sleep Computer
        # -------------------------

        elif "sleep computer" in command or "sleep pc" in command:
            speak("Putting your computer to sleep.")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # -------------------------
        # Restart Computer
        # -------------------------

        elif "restart computer" in command or "restart pc" in command:
            speak("Restarting your computer.")
            os.system("shutdown /r /t 5")

        # -------------------------
        # Shut Down Computer
        # -------------------------

        elif "shut down computer" in command or "shutdown computer" in command:
            speak("Shutting down your computer.")
            os.system("shutdown /s /t 5")

        # -------------------------
        # Cancel Shutdown or Restart
        # -------------------------

        elif "cancel shutdown" in command:
            os.system("shutdown /a")
            speak("Shutdown cancelled.")
        
        elif "exit" in command or "stop" in command or "goodbye" in command:
            speak("Goodbye Mansi. Have a nice day.")
            break

        else:
            speak("Sorry, I don't know that command yet.")
        
if __name__ == "__main__":
    main()
