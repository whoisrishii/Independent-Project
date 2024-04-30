import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import os

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


# Function to speak out text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to recognize speech from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if 'open chrome' in query:
            # Locate and double click on Chrome icon
            img = pyautogui.locateCenterOnScreen('Screenshot1.png')
            pyautogui.doubleClick(img)
            time.sleep(1)

            # Maximize the window
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
            time.sleep(1)

            # Click on specific location for Google search
            img1 = pyautogui.locateCenterOnScreen('screenshot2.png')
            pyautogui.click(img1)
            time.sleep(2)

            # Click on search bar and type the query
            img2 = pyautogui.locateCenterOnScreen('screenshot3.png')
            pyautogui.click(img2)
            time.sleep(1)
            pyautogui.typewrite('How To Manual', 0.1)
            pyautogui.press('enter')
            time.sleep(1)

            # Close search bar
            pyautogui.press('esc')

            # Click on specific location to close Chrome
            img3 = pyautogui.locateCenterOnScreen('screenshot4.png')
            pyautogui.click(img3)

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
