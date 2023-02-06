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



def Calco(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")
    Term = Term.replace("into", "*")

    final = str(Term)

    try:

        result = WolfRam(final)
        print(result)
        speak(f'{result}')

    except:

        speak("The Value is Not Answerable")


#
# def WolfRamAlpha(query):
#     apikey = "T92W27-VVX4L9E2TP"
#     requester = wolframalpha.Client(apikey)
#     requested = requester.query(query)
#
#     try:
#         answer = next(requested.results).text
#         return answer
#     except:
#         speak("The value is not answerable")
#
# def Calc(query):
#     Term = str(query)
#     Term = Term.replace("jarvis","")
#     Term = Term.replace("multiply","*")
#     Term = Term.replace("plus","+")
#     Term = Term.replace("minus","-")
#     Term = Term.replace("divide","/")
#
#     Final = str(Term)
#     try:
#         result = WolfRamAlpha(Final)
#         print(f"{result}")
#         speak(result)
#
#     except:
#         speak("The value is not answerable")
