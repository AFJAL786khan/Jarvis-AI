import pyttsx3
import speech_recognition as sr
import wolframalpha


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


def WolfRam(query):
    api_key = "T92W27-VVX4L9E2TP"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)



    try:
        answer = next(requested.results).text
        return answer

    except:
        speak("The Value is Not Answerable")

def Temp(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("temperature", "")
    Term = Term.replace("what is the", "")
    Term = Term.replace("in", "")
    Term = Term.replace("tell", "")
    Term = Term.replace("me", "")
    Term = Term.replace("the", "")
    Term = Term.replace("current", "")



    tem_query = str(Term)


    if 'outside' in tem_query:
        var1 = 'Temperature in dholpur'
        answer = WolfRam(var1)
        speak(f"{var1} is {answer}")

    else:
        var2 = "Temperature in" + tem_query
        ans = WolfRam(var2)
        speak(f"{var2} is {ans}")



