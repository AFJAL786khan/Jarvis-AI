import pyttsx3
import wikipedia
import speech_recognition as sr


# Initializing pyttsx3
engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# FUNCTIONS :--
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query







def wiki(query):
    query = query.replace("on wikipedia", "")
    query = query.replace("wikipedia", "")
    query = query.replace("search", "")
    speak(f"searching {query} on wikipedia")
    results = wikipedia.summary(query, sentences=2)
    speak("here are the results")
    print(results)
    speak(results)


