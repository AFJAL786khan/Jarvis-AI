import pyttsx3

def speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.setProperty('rate', 200)
    print(f"Jarvis : {Text}.")
    engine.say(Text)
    engine.runAndWait()

# speak('Hello I am jarvis Sir , How are you')

