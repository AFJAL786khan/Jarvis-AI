import pyttsx3
import smtplib
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


def sendEmail():

    try:
        speak("Whom do you want to send")
        to = input("Enter receievers Email : ")

        speak("What Should I Say ?")
        content = input("Enter a message")

        speak("Subject To Your Email !")
        subject = input("Enter Subject")

        sender_email = "afjalkhan17in@gmail.com"
        password = open("D:\Documents\Codeing\JARVIS - Basic\Data\password.txt", "r").read()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)

        message = f'Subject: {subject}\n\n{content}'
        server.sendmail(sender_email, to, message)
        server.close()
        speak("Email has Been Sent Successfully !")

    except Exception as e:
        speak("Sorry, There being an error to send email")
        print(e)

sendEmail()










