# pip install SpeechRecognition
# pip install pyttsx3
# pip install pywhatkit
# pip install wikipedia

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

r=sr.Recognizer()

phone_nos={"aryan":6353930898,"vasu":873546413,"satyam":8765093164,"darshit":3631987654,"vinayak":7823974365}

def speak(command):
    engine=pyttsx3.init()  # Created object for this library
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)  # Use female voice
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            r.adjust_for_ambient_noise(source, duration=1)  # Calibrate the mic
            print("Listening...")
            audioin = r.listen(source, timeout=5)  # Listen with a timeout
            print("Processing audio...")
            query = r.recognize_google(audioin)
            query = query.lower()
            print(f"Recognized text: {query}")
            # speak(query)

            if "exit" in query or "stop" in query or "quit" in query or "goodbye" in query:
                speak("Goodbye! Have a great day.")
                return "exit" 
            
            # ask to play song
            if 'play' in query:
                song = query.replace('play', '')
                speak(f"Playing {song}")
                pywhatkit.playonyt(song)  # to play the song on youtube we are using pywahtkit

            # ask date
            elif 'date' in query:
                speak("Today's date is:")
                now = datetime.datetime.now()
                speak(now.strftime("%Y-%m-%d"))

            # ask time
            elif 'time' in query:
                speak("Current time is:")
                now = datetime.datetime.now()
                speak(now.strftime("%H:%M:%S"))

            # ask details about any person
            elif "who is" in query:
                person = query.replace("who is", "")
                speak(f"According to Wikipedia, {person} is a {wikipedia.summary(person, 1)}")
            
            elif "tell about " in query:
                place = query.replace("tell about", "")
                speak(f"According to Wikipedia, {place} is a {wikipedia.summary(place, 1)}")

            # ask phone numbers
            elif "phone number" in query:
                names=list(phone_nos)
                print(names)
                for name in names:
                    if name in query:
                        print(name + " phone number is " + str(phone_nos[name]))
                        speak(name + " phone number is " + str(phone_nos[name]))

            elif "name" in query:
                speak("My name is cap")

            elif "hello" in query:
                speak("Hello dude, How can i help you?")

            else:
                print("Sorry, I didn't catch that")



            # ask bank account no.

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the recognition service: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

# Run the assistant
speak("Welcome! I am ready to assist you.")

while True:
    result = commands()
    if result == "exit":
        break  # Exit the loop

