import openai
from dotenv import load_dotenv


fileopen = open("D:\Documents\Codeing\JARVIS - Basic\Data\Api.txt", "r")
API = fileopen.read()
fileopen.close()


openai.api_key = API
load_dotenv()
completion = openai.Completion()

def QuestionAnswer(question, chat_log = None):
    FileLog = open("D:\Documents\Codeing\JARVIS - Basic\DataBase\chat_log.txt", "r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}Question : {question}\nAnswer : '
    response = completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f'\nQuestion : {question} \nAnswer : {answer}'
    FileLog = open("D:\Documents\Codeing\JARVIS - Basic\DataBase\chat_log.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer


# kk = Listen()
# speak(QuestionAnswer(kk))

# while True:
#     kk = input("Enter Here :")
#     print(QuestionAnswer(kk))


















# import openai
# import pyttsx3
# import speech_recognition as sr
#
#
# # Initializing pyttsx3
# engine = pyttsx3.init('sapi5')
#
# # Set Rate
# engine.setProperty('rate', 190)
#
# # Set Volume
# engine.setProperty('volume', 1.0)
#
# # Set Voice (Female)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
#
# # FUNCTIONS :--
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
#
# def takeCommand():
#     # It takes microphone input from the user and returns string output
#
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
#         print(f"User said: {query}\n")  # User query will be printed.
#
#     except Exception as e:
#         # print(e)
#         print("Say that again please...")  # Say that again will be printed in case of improper voice
#         return "None"  # None string will be returned
#     return query
#
#
#
# openai.api_key = "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"
# completion = openai.Completion()
#
#
#
# # while True:
#
#
# def Reply(question):
#         prompt = f'Afzal: {question}\n Jarvis: '
#         response = completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Afzal'], max_tokens=200)
#         answer = response.choices[0].text.strip()
#         return answer
#     #
#     # ques = takeCommand()
#     # ans = Reply(ques)
#
#
#     # if ques == 'no thanks':
#     #     break
#     # speak(ans)
#
#
#
#
#
#
#
#
#
#
#
#
