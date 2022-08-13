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
            if (ent=="ನಿನ್ನ ಹೆಸರೇನು"):
                text = "ನನ್ನ ಹೆಸರು ಜಾರ್ವಿಸ್"
                language = 'kn'
                speech = gTTS(text = text, lang = language, slow = False)
                speech.save("text.mp3")
                os.system("cvlc text.mp3")
            elif (ent=="ಏನು ಮಾಡುತ್ತಿರುವೆ"):
                text = "ನಾನು ನಿಮ್ಮೊಂದಿಗೆ ಮಾತನಾಡುತ್ತಿರುವೆ"
                language = 'kn'
                speech = gTTS(text = text, lang = language, slow = False)
                speech.save("text.mp3")
                os.system("cvlc text.mp3")
            elif (ent=="ನಿನ್ನ ಬಗ್ಗೆ ಹೇಳು"):
                text = "ನನ್ನ ಹೆಸರು ಜಾರ್ವಿಸ್, ನಾನು ರೋಬೋಟ್, ನನ್ನನ್ನು ಮಾಡಲು ರಾಸ್ಪ್ಬೆರಿಪೈಯನ್ನು ಬಳಸಿರುವರು"
                language = 'kn'
                speech = gTTS(text = text, lang = language, slow = False)
                speech.save("text.mp3")
                os.system("cvlc text.mp3")
            elif (ent=="ಸಿದ್ದಗಂಗಾ ತಾಂತ್ರಿಕ ಮಹಾವಿದ್ಯಾಲಯದ ಬಗ್ಗೆ ಹೇಳು"):
                text = "ಸಿದ್ದಗಂಗಾ ತಾಂತ್ರಿಕ ಮಹಾವಿದ್ಯಾಲಯವನ್ನು 1963 ರಲ್ಲಿ ಸ್ಥಾಪಿಸಲಾಯಿತು.ಈ ವಿದ್ಯಾಲಯವು 13 ಪದವಿಪೂರ್ವ ಕಾರ್ಯಕ್ರಮಗಳು ಮತ್ತು 12 ಸ್ನಾತಕೋತ್ತರ ಕಾರ್ಯಕ್ರಮಗಳನ್ನು ನೀಡುತ್ತಿದೆ.ಪ್ರಸ್ತುತ ಸಂಸ್ಥೆಯಲ್ಲಿ 4000 ಕ್ಕೂ ಹೆಚ್ಚು ವಿದ್ಯಾರ್ಥಿಗಳು ತಮ್ಮ ಅಧ್ಯಯನವನ್ನು ಮುಂದುವರಿಸುತ್ತಿದ್ದಾರೆ.ಸಂಸ್ಥೆಯ 15 ವಿಭಾಗಗಳು ಬೆಳಗಾವಿಯ ವಿಶ್ವೇಶ್ವರಯ್ಯ ತಾಂತ್ರಿಕ ವಿಶ್ವವಿದ್ಯಾಲಯದಿಂದ ಸಂಶೋಧನಾ ಕೇಂದ್ರಗಳಾಗಿ ಗುರುತಿಸಲ್ಪಟ್ಟಿವೆ ಮತ್ತು 2007-2008ರ ಶೈಕ್ಷಣಿಕ ವರ್ಷದಿಂದ ಬೆಳಗಾವಿಯು ಈ ಸಂಸ್ಥೆಗೆ ಸ್ವಾಯತ್ತ ಸ್ಥಾನಮಾನವನ್ನುನೀಡಿದೆ.ಹೆಚ್ಚಿನ ವಿವರಗಳಿಗೆ wwwಡಾಟ್ಎಸ್ಐಟಿಡಾಟ್ಎಸಿಡಾಟ್ಇನ್ ಗೆ ಭೇಟಿ ನೀಡಿ"
                language = 'kn'
                speech = gTTS(text = text, lang = language, slow = False)
                speech.save("text.mp3")
                os.system("cvlc text.mp3")
            
            elif (ent=="ನಿನ್ನ ವೈಶಿಷ್ಟ್ಯಗಳ ಬಗ್ಗೆ ಹೇಳು"):
                text = "ನಾನು ಜಾರ್ವಿಸ್, ನನ್ನನ್ನು ಮಾಡಲು ರಾಸ್ಪ್ಬೆರಿಪೈಯನ್ನು ಬಳಸಿರುವರು, ನಾನು ಮಾತನಾಡಬಲ್ಲೆ, ನೀವು ಹೇಳುವುದನ್ನು ಕೇಳಬಲ್ಲೆ, ಹಾಗು ನಾನು ವಿವಿದ ಅನಿಲಗಳನ್ನು ಗುರುತಿಸಬಲ್ಲೆ"
                language = 'kn'
                speech = gTTS(text = text, lang = language, slow = False)
                speech.save("text.mp3")
                os.system("cvlc text.mp3")
                
            elif (ent=="ನಿನ್ನನ್ನು ಸೃಷ್ಟಿ ಮಾಡಿದವರಾರು"):
                text = "ನನ್ನನು ೬ನೇ ಸೆಮ್ ಎಂಜಿನಿಯರಿಂಗ್ ವಿದ್ಯಾರ್ಥಿಗಳಾದ ಸುಧನ್ವ , ಜೀವನ್ , ಕಾಂತರಾಜು, ಸುಪ್ರಿಯಾ ರವರು ಡಾಕ್ಟರ್.ಆರ್.ಕುಮಾರಸ್ವಾಮಿ ಅವರ ಮಾರ್ಗದರ್ಶನದಲ್ಲಿ ಸೃಷ್ಟಿಮಾಡಲಾಯಿತು"
                language = 'kn'
                speech = gTTS(text = text, lang = language, slow = False)
                speech.save("text.mp3")
                os.system("cvlc text.mp3")       
                
            elif (ent=="ನೀನು ಹೇಳುವುದು ನಿಜವೇ"):
                text = "ಸಂಶಯವಿದ್ದಲ್ಲಿ ಗೂಗಲ್ ಮಾಡಿ ನೋಡಿ"
                language = 'kn'
                speech = gTTS(text = text, lang = language, slow = False)
                speech.save("text.mp3")
                os.system("cvlc text.mp3")
            
            elif (ent=="ನಿನ್ನ ಜೊತೆ ಮಾತನಾಡಿ ನನಗೆ ಸಂತೋಷವಾಯಿತು"):
                text = "ವಂದನೆಗಳು,ನನಗು ನಿಮ್ಮಜೊತೆ ಮಾತನಾಡಲು ಬಹಳ ಇಷ್ಟವಾಯಿತು"
                language = 'kn'
                speech = gTTS(text = text, lang = language, slow = False)
                speech.save("text.mp3")
                os.system("cvlc text.mp3")
                
            else:
                text = str(ent)
                language = 'kn'
                speech = gTTS(text = text, lang = language, slow = False)
                speech.save("text.mp3")
                os.system("cvlc text.mp3")
                
        except:
             print("please speak again")
