import datetime
import operator
import os
import random
import smtplib
import sys
import time
import webbrowser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from tkinter import filedialog, Tk
import openai
import cv2
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
import genai

#api_key = "AIzaSyBplSb99OJbwHK8Q-AtH7WhWK-jvrzL6H0"
#model = genai.GenerativeModel(api_key, 'gemini-pro-vision')

#api_key = "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"
#client = openai.Client(api_key=api_key)


# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)

# Function to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Function to convert voice into text
def takecommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"Rishi said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


# Function to greet the user
def wish():
    hour = int(datetime.datetime.now().hour)
    time_str = time.strftime("%I:%M %p")

    if 0 <= hour < 12:
        speak(f"Good morning Rishi! It's {time_str}")
    elif 12 <= hour < 18:
        speak(f"Good afternoon Rishi ! It's {time_str}")
    else:
        speak(f"Good evening Rishi! It's {time_str}")
    speak("I am Ghost AI Sir. Please tell me how may I help you.")

# Function to fetch news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=a3e84416a7894d23a5369fe52c611095'
    main_page = requests.get(main_url).json()

    try:
        articles = main_page["articles"]
        headlines = []
        day = ["first", "second", "third", "fourth"]
        for article in articles:
            headlines.append(article["title"])
        for i in range(len(day)):
            speak(f"Today's {day[i]} news is: {headlines[i]}")
    except KeyError:
        speak("Sorry, I couldn't fetch the news at the moment. Please try again later.")

def check_password(password):
    correct_password = "rishi123"  # Set your password here
    return password == correct_password


def takeCommand():
    pass

def generate_content(prompt):
    response = openai.ChatCompletion.create(
        model="gemini-pro-vision",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message['content']


def generate_image(prompt):
    pass


if __name__ == "__main__":
        password_attempts = 3
        while password_attempts > 0:
            speak("Enter your password: ")
            password = input()

            if check_password(password):
                speak("Password correct. Access granted.")
                wish()
                break
            else:
                speak("Incorrect password. Please try again.")
                password_attempts -= 1
                if password_attempts == 0:
                    speak("Maximum attempts reached. Exiting program.")
                    sys.exit()

        while True:
            query = takecommand().lower()

            if 'open chrome' in query:
                os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')

            elif 'maximize this window' in query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('x')

            elif 'google search' in query:
                query = query.replace("google search", "")
                pyautogui.hotkey('alt', 'd')
                pyautogui.write(f"{query}", 0.1)
                pyautogui.press('enter')

            elif 'youtube search' in query:
                query = query.replace("youtube search", "")
                pyautogui.hotkey('alt', 'd')
                time.sleep(1)
                pyautogui.press(['tab', 'tab', 'tab', 'tab'])
                pyautogui.write(f"{query}", 0.1)
                pyautogui.press('enter')

            elif 'open new window' in query:
                pyautogui.hotkey('ctrl', 'n')

            elif 'open incognito window' in query:
                pyautogui.hotkey('ctrl', 'shift', 'n')

            elif 'minimise this window' in query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('n')

            elif 'open history' in query:
                pyautogui.hotkey('ctrl', 'h')

            elif 'open downloads' in query:
                pyautogui.hotkey('ctrl', 'j')

            elif 'previous tab' in query:
                pyautogui.hotkey('ctrl', 'shift', 'tab')

            elif 'next tab' in query:
                pyautogui.hotkey('ctrl', 'tab')

            elif 'close tab' in query:
                pyautogui.hotkey('ctrl', 'w')

            elif 'close window' in query:
                pyautogui.hotkey('ctrl', 'shift', 'w')

            elif 'clear browsing history' in query:
                pyautogui.hotkey('ctrl', 'shift', 'delete')

            elif 'close chrome' in query:
                os.system("taskkill /f /im chrome.exe")

            elif "open notepad" in query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
            elif 'hi' in query or 'hello' in query:
                speak('Hello sir, how may I help you?')
            elif "open adobe reader" in query:
                apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
                os.startfile(apath)
            elif "open command prompt" in query:
                os.system("start cmd")
            # Other elif conditions...

            elif "no thanks" in query:
                speak("Thanks for using me sir, have a good day.")
                sys.exit()

            elif "close notepad" in query:
                speak("Okay sir, closing Notepad.")
                os.system("taskkill /f /im notepad.exe")

            elif "set alarm" in query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music_dir = 'E:\\music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down system" in query:
                os.system("shutdown /s /t 5")

            elif "restart system" in query:
                os.system("shutdown /r /t 5")

            elif "sleep system" in query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif 'switch window' in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in query:
                speak("Please wait sir, fetching the latest news.")
                news()

            elif "email amber" in query:
                speak("Sir, what should I say?")
                content = takecommand().lower()
                print("Content:", content)  # Debug statement
                if any(keyword in content for keyword in ["send a file", "attach a file", "send the file"]):
                    try:
                        email = 'singhrishiraj1102cu@gmail.com'  # Your email
                        password = 'rishidps'  # Your email account password
                        send_to_email = 'ambershresth.10@gmail.com'  # Receiver's email address

                        # Create a multipart message
                        msg = MIMEMultipart()
                        msg['From'] = email
                        msg['To'] = send_to_email
                        msg['Subject'] = "Email Subject"  # Subject of the email

                        # Update the file location with the correct path to your file
                        file_location = "C:/Users/SANJAY KUMAR SINGH/Desktop/Atomic_Habits.pdf"
                        attachment = open(file_location, "rb")
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload((attachment).read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition',
                                        "attachment; filename= %s" % os.path.basename(file_location))

                        # Add attachment to the message
                        msg.attach(part)

                        # Send the message via SMTP server
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email, password)
                        text = msg.as_string()
                        server.sendmail(email, send_to_email, text)
                        server.quit()

                        speak("Email with attachment has been sent.")
                    except Exception as e:
                        speak("Sorry, I couldn't send the email. Please try again later.")
                        print("Error:", e)

            elif "sleep" in query:
                speak("Going to sleep,sir")
                exit()


            elif "close" in query:
                from Dictapp import closeappweb

                closeappweb(query)

            elif "remember that" in query:
                rememberMessage = query.replace("remember that", "")
                rememberMessage = rememberMessage.replace("jarvis", "")  # Fix: Replacing "query" with "rememberMessage"
                speak("You told me to remember that" + rememberMessage)
                remember = open("Remember.txt", "a")
                remember.write(rememberMessage + "\n")  # Adding a newline character to separate messages
                remember.close()

            elif "what do you remember" in query:
                try:
                    remember = open("Remember.txt", "r")
                    speak("You told me to remember these:")
                    remembered_messages = remember.readlines()
                    for msg in remembered_messages:
                        speak(msg.strip())  # Stripping newline characters from each message
                    remember.close()
                except FileNotFoundError:
                    speak("I don't have any messages saved yet.")

            elif "tired" in query:
                speak("Playing your favorite songs, sir")
                songs = [
                    "https://youtu.be/myh5xtfUG-I?si=fJioiAjd-KhPmUKe",
                    "https://youtu.be/Uce4YoxDAIE?si=MqJ-YGyyMPZboreL",
                    "https://youtube.com/shorts/5aAvwxtAf8w?si=STPIZzG6SY1qJCnf"
                ]
                song_to_play = random.choice(songs)
                webbrowser.open(song_to_play)

            elif 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.PageError:
                    speak("Sorry, I couldn't find any information on that.")
                except wikipedia.exceptions.DisambiguationError:
                    speak("There are multiple pages matching that query. Can you be more specific?")
                except Exception as e:
                    speak("An error occurred while searching Wikipedia.")


            elif 'search on youtube' in query:
                query = query.replace("search on youtube", "")
                webbrowser.open(f"www.youtube.com/results?search_query={query}")

            elif 'open youtube' in query:
                speak("What would you like to watch?")
                qrry = takecommand().lower()
                pywhatkit.playonyt(qrry)


            elif 'close chrome' in query:
                os.system("taskkill /f /im chrome.exe")

            elif 'close youtube' in query:
                os.system("taskkill /f /im msedge.exe")

            elif 'open google' in query:
                speak("what should I search ?")
                qry = takeCommand().lower()
                webbrowser.open(f"{qry}")
                try:
                    results = wikipedia.summary(qry, sentences=2)
                    speak(results)
                except wikipedia.exceptions.DisambiguationError:
                    speak("There are multiple pages matching that query. Can you be more specific?")
                except Exception as e:
                    speak("An error occurred while searching Wikipedia.")

            elif 'close google' in query:
                os.system("taskkill /f /im msedge.exe")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif "shut down the system" in query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in query:
                os.system("shutdown /r /t 5")

            elif "lock the system" in query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "close notepad" in query:
                os.system("taskkill /f /im notepad.exe")

            elif "open command prompt" in query:
                os.system("start cmd")

            elif "close command prompt" in query:
                os.system("taskkill /f /im cmd.exe")

            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "close camera" in query:
                cv2.destroyAllWindows()


            elif "go to sleep" in query:
                speak(' alright then, I am switching off')
                sys.exit()

            elif "take screenshot" in query:
                speak('tell me a name for the file')
                name = takeCommand().lower()
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("screenshot saved")

            elif "calculate" in query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("ready")
                    print("Listning...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)


                    def get_operator_fn(op):
                        return {
                            '+': operator.add,
                            '-': operator.sub,
                            'x': operator.mul,
                            'divided': operator.__truediv__,
                        }[op]


                    def eval_bianary_expr(op1, oper, op2):
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)


                    speak("your result is")
                    speak(eval_bianary_expr(*(my_string.split())))

            elif "what is my ip address" in query:
                speak("Checking")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    speak("your ip address is")
                    speak(ipAdd)
                except Exception as e:
                    speak("network is weak, please try again some time later")

            elif "volume up" in query:
                pyautogui.press("volumeup")

            elif "volume down" in query:
                pyautogui.press("volumedown")

            elif "mute" in query:
                pyautogui.press("volumemute")

            elif "refresh" in query:
                pyautogui.moveTo(1551, 551, 2)
                pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
                pyautogui.moveTo(1620, 667, 1)
                pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')

            elif "scroll down" in query:
                pyautogui.scroll(1000)

            elif "drag visual studio to the right" in query:
                pyautogui.moveTo(46, 31, 2)
                pyautogui.dragRel(1857, 31, 2)

            elif "rectangular spiral" in query:
                pyautogui.hotkey('win')
                time.sleep(1)
                pyautogui.write('paint')
                time.sleep(1)
                pyautogui.press('enter')
                pyautogui.moveTo(100, 193, 1)
                pyautogui.rightClick()
                pyautogui.click()
                distance = 300
                while distance > 0:
                    pyautogui.dragRel(distance, 0, 0.1, button="left")
                    distance = distance - 10
                    pyautogui.dragRel(0, distance, 0.1, button="left")
                    pyautogui.dragRel(-distance, 0, 0.1, button="left")
                    distance = distance - 10
                    pyautogui.dragRel(0, -distance, 0.1, button="left")

            elif "close paint" in query:
                os.system("taskkill /f /im mspaint.exe")

            elif "who are you" in query:
                print('My Name Is Ghost')
                speak('My Name Is Ghost')
                print('I can Do Everything that my creator programmed me to do')
                speak('I can Do Everything that my creator programmed me to do')

            elif "who created you" in query:
                #print('His Name Rishi, I created with Python Language, in Pycharm.')
                speak('His Name Rishi, I created with Python Language, in Pycharm.')

            elif "open notepad and write my  name" in query:
                pyautogui.hotkey('win')
                time.sleep(1)
                pyautogui.write('notepad')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write("How To Manual", interval=0.1)


            elif 'type' in query:
                query = query.replace("type", "")
                pyautogui.write(query)

            elif 'convert ppt to pdf' in query:
                speak("Sure, please select the PowerPoint file you want to convert.")
                root = Tk()
                root.withdraw()  # Hide the main window
                input_ppt = filedialog.askopenfilename(title="Select PowerPoint file",
                                                       filetypes=[("PowerPoint files", "*.pptx;*.ppt")])
                if not input_ppt:
                    speak("No PowerPoint file selected. Cancelling operation.")
                    sys.exit()

                # Ask the user to select the output PDF file
                output_pdf = filedialog.asksaveasfilename(title="Save PDF as", defaultextension=".pdf",
                                                          filetypes=[("PDF files", "*.pdf")])
                if not output_pdf:
                    speak("No output PDF file selected. Cancelling operation.")
                    sys.exit()

            elif "generate image" in query:
                speak("Sure, what do you want the image to be?")
                prompt = takecommand().lower()  # Assuming takecommand() retrieves the user's input
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                )
                image_url = response.data[0].url
                speak("Here is the generated image.")
                webbrowser.open(image_url)

            '''
            elif "generate image" in query:
                speak("Sure, what do you want the image to be?")
                prompt = takecommand().lower()  # Assuming takecommand() retrieves the user's input
                response = generate_image(prompt)
                speak("Here is the generated image.")
            '''



