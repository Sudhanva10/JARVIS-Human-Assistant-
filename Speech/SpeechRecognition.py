import speech_recognition as sr
from gtts import gTTS
import os
ear = sr.Recognizer()
with sr.Microphone() as inputs:
    x = ''
    while x!='q':
        print("Please speak now")
        listening = ear.listen(inputs)
        print("Analysing...")
        try:
            print("Did you say: "+ear.recognize_google(listening,language = "kn-IN"))
            ent = (ear.recognize_google(listening,language = "kn-IN"))
        except:
             print("please speak again")
        finally:
            x = input("Press any key to continue, 'q' to quit : ")
            if x=='q':
                print("Exiting now...............")
text = str(ent)
#Define the language of text
language = 'kn'
#Defining the speech 
speech = gTTS(text = text, lang = language, slow = False)
#Saving the speech
speech.save("text.mp3")
#playing the speech
os.system("cvlc text.mp3")