from pypdf import PdfReader
import pyttsx3
import speech_recognition as sr



# INITIALIZING PYTTSX----------------------------------------------------------------------------------------------------------------------------

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 210)
engine.setProperty('volume', 10.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# SPEAK FUNCTION FOR JARVIS-----------------------------------------------------------------------------------------------------------------------

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# TAKE COMMAND FUNCTION FOR JARVIS-----------------------------------------------------------------------------------------------------------------

def takeCommand():
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




def pdf_reader():
    reader = PdfReader('English Quran 2.pdf', 'rb')
    number_of_pages = len(reader.pages)
    speak(f'Total number of pages in this book {number_of_pages}')
    speak('Sir Please enter the page number')
    pg = int(input("Enter page number : "))
    page = reader.pages[pg]
    text = page.extract_text()
    speak(text)



    # book = open('English Quran 2.pdf', 'rb')
    # pdffReader = PyPDF2.PdfReader(book)
    # pages = len(pdffReader.pages)
    # for num in range(7, pages):
    #     page = pdffReader.pages[num]
    #     text = page.extract_text
    #     speak(text)
    # book = open('English Quran 2.pdf', 'rb')
    # pdfReader = PyPDF2.PdfReader(book)
    # PaGeS = len(pdfReader.pages)
    # speak(f'Total number of pages in this book {PaGeS}')
    # # speak('Sir Please enter the page number')
    # # pg = int(input("Enter page number : "))
    # # page = pdfReader.pages[pg]
    # text = extractText()
    # speak(text)
