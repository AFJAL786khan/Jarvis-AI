from Body.Listen import Listen
from Body.Speak import speak
from Features.WISH_ME import wishme
from Features.LOCATION import My_location
from Features.WIKIPEDIA import wiki
from Features.WHATSAPP import sendMessage
from Features.EMAIL import sendEmail
from Features.pdf_reader import pdf_reader
from Features.Calculator import Calco
from Features.temperature import Temp
from Features.Alarm import alarm
from Brain.AI import QuestionAnswer
from Brain.Learner_AI import ReplyBrain
# __________________________________________________________________________________________#
import time
import os
import pyautogui
from datetime import datetime
from requests import get
import webbrowser
import pywhatkit
import sys
import pyjokes
import instaloader
import psutil
import speedtest
import cv2
import urllib.request
import numpy as np




# Task Execution--------------------------------------------------------------------------------------------------------------------------------------------

def TaskExecution():
    print(">> Starting The Jarvis : Wait For Some Seconds.")
    print(">> Starting The Jarvis : Wait For Some Seconds More.")

# Wish Me Function RUN :-
    print("")
    print("")
    wishme()
    print("")

    while True:
        query = Listen().lower()

# Answers Question (USING OPEN AI)
        if "what is" in query or "where is" in query or "question" in query or "answer" in query:
            Reply = QuestionAnswer(query)
            speak(Reply)

# OPEN MOBILE CAMERA
        elif 'open mobile camera' in query:
            URL = "http://192.168.66.62:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('Camera', img)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            cv2.destroyAllWindows()

# Setting Alarm
        elif 'alarm' in query:
            speak("Sir please tell me the time to set alarm")
            tt = Listen()
            tt = tt.replace("set alarm to", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            alarm(tt)


# Control Volume
        elif 'volume up' in query:
            pyautogui.press("vloumeup")
        elif 'volume down' in query:
            pyautogui.press("volumedown")
        elif 'volume mute' in query:
            pyautogui.press("vloumemute")

# OPEN CAMERA
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                raise Exception("Could not open video device")
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                cv2.imshow("Camera", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

            cap.release()
            cv2.destroyAllWindows()

# Tells battery percentage
        elif 'how much power left' in query or 'how much power we have' in query or 'battery percentage' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our system have {percentage} percent battery")

# Check Internet Speed
        elif 'internet speed' in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir we have {dl} bit per secong downloading speed and {up} bit per second uploading speed.")

# Tells the current Location
        elif 'my location' in query:
            My_location()

# Tells the current Time
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

# Tell the user IP Adress
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is  {ip}")

# Search Anything on Google
        elif 'open google' in query:
            speak("Sir, What should I search")
            cm = Listen().lower()
            webbrowser.open(f"{cm}")

# Play Any song on Youtube
        elif 'play song on youtube' in query:
            speak("Which song do you want to listen")
            songName = Listen()
            pywhatkit.playonyt(f'{songName}')

# Open Any Program Online/Offline
        elif 'open' in query:
            query = query.replace("open", "")
            query = query.replace("jarvis", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            # pyautogui.sleep(2)
            pyautogui.press("enter")

# Open and close CMD
        elif 'open cmd' in query:
            os.system('start cmd')
        elif 'close cmd' in query:
            os.system("taskkill /f /im cmd.exe")

# Play selected Music
        elif 'play music' in query:
            music_dir = 'D:\\Desktop\\temp\\video.mp4'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

# Search anything on wikipedia
        elif 'wikipedia' in query:
            wiki(query)

# Automate Message on Whatsapp
        elif "message on whatsapp" in query:
            sendMessage()

# Tells the latest News
        # elif 'tell me news' in query:
        #     speak("Please wait Sir, fetching the latest news")
        #     listen_news()

# Send Automated Email
        elif 'send email' in query:
            sendEmail()

# Set Alarm
        # elif 'set alarm' in query:
        #     nn = int(datetime.now().hour)
        #     if nn==22:
        #         music_dir = 'D:\\Desktop\\temp\\video.mp4'
        #         songs =  os.listdir(music_dir)
        #         os.startfile(os.path.join(music_dir, songs[0]))

# Tells a Joke
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

# open instagram profile and download profile picture
        elif 'instagram profile' in query:
            speak("Sir please Enter the username Correctly.")
            name = input("Enter Username Here : ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak("Sir here is the profile of the user")
            time.sleep(5)
            speak("Sir would you like to download profile picture of this account")
            condition = Listen()

            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done Sir, Profile picture is saved in our main folder.")
            else:
                pass

# Take screenshot of current window
        elif 'take screenshot' in query:
            speak("Sir, Please tell me the name for this screenshot file")
            name_screenshot = Listen()
            speak("Please Sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name_screenshot}.png")
            speak("I am done Sir, The screenshot is saves in our main folder.")

# Read PDF
        elif 'read pdf' in query:
            pdf_reader()

# Do Calculation
        elif "calculate" in query:
            Calco(query)
            # from Calculator import WolfRam
            # from Calculator import Calco
            # Calco(query)

# Tells Temperature
        elif 'temperature' in query:
            Temp(query)
            # from temperature import Temp
            # Temp(query)

# Sleep Jarvis
        elif 'you can sleep now' in query:
            speak("Okay Sir, I am going to sleep you can call me anytime")
            break

# Activate ADVANCE AI mode
        else:
            Reply = ReplyBrain(query)
            speak(Reply)
#

TaskExecution()
#
# #--------------------------------------------------------#
#
# # if __name__ == "__main__":
# #     while True:
# #         permission = Listen().lower()
# #
# #
# #         if 'wake up jarvis' in permission:
# #             TaskExecution()
# #
# #         elif "goodbye jarvis" in permission:
# #             sys.exit()
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
#
#
#
#
#
#
#
#
#
