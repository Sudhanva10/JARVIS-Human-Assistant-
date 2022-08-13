import RPi.GPIO as GPIO
import time
from gtts import gTTS
import os
GPIO.setmode(GPIO.BCM)
D7 = 17
D6 = 27
D5 = 22
D4 = 5
D3 = 6
D2 = 13
D1 = 19
D0 = 26

GPIO.setup(D7,GPIO.IN)
GPIO.setup(D6,GPIO.IN)
GPIO.setup(D5,GPIO.IN)
GPIO.setup(D4,GPIO.IN)
GPIO.setup(D3,GPIO.IN)
GPIO.setup(D2,GPIO.IN)
GPIO.setup(D1,GPIO.IN)
GPIO.setup(D0,GPIO.IN)

while True:
    if GPIO.input(D0) and not GPIO.input(D2) and not GPIO.input(D1):
        print("1")
        text = "ನನ್ನ ಹೆಸರು ಜಾರ್ವಿಸ್"
        language = 'kn'
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("text.mp3")
        os.system("cvlc text.mp3")
        break
        
    elif GPIO.input(D1) and not GPIO.input(D0) and not GPIO.input(D2):
        print("2")
        text = "ಸಿದ್ದಗಂಗಾ ತಾಂತ್ರಿಕ ಮಹಾವಿದ್ಯಾಲಯವನ್ನು 1963 ರಲ್ಲಿ ಸ್ಥಾಪಿಸಲಾಯಿತು.ಈ ವಿದ್ಯಾಲಯವು 13 ಪದವಿಪೂರ್ವ ಕಾರ್ಯಕ್ರಮಗಳು ಮತ್ತು 12 ಸ್ನಾತಕೋತ್ತರ ಕಾರ್ಯಕ್ರಮಗಳನ್ನು ನೀಡುತ್ತಿದೆ. ಪ್ರಸ್ತುತ ಸಂಸ್ಥೆಯಲ್ಲಿ 4000 ಕ್ಕೂ ಹೆಚ್ಚು ವಿದ್ಯಾರ್ಥಿಗಳು ತಮ್ಮ ಅಧ್ಯಯನವನ್ನು ಮುಂದುವರಿಸುತ್ತಿದ್ದಾರೆ. ಸಂಸ್ಥೆಯ 15 ವಿಭಾಗಗಳು ಬೆಳಗಾವಿಯ ವಿಶ್ವೇಶ್ವರಯ್ಯ ತಾಂತ್ರಿಕ ವಿಶ್ವವಿದ್ಯಾಲಯದಿಂದ ಸಂಶೋಧನಾ ಕೇಂದ್ರಗಳಾಗಿ ಗುರುತಿಸಲ್ಪಟ್ಟಿವೆ ಮತ್ತು 2007-08ರ ಶೈಕ್ಷಣಿಕ ವರ್ಷದಿಂದ ಬೆಳಗಾವಿಯು ಈ ಸಂಸ್ಥೆಗೆ ಸ್ವಾಯತ್ತ ಸ್ಥಾನಮಾನವನ್ನುನೀಡಿದೆ. ಹೆಚ್ಚಿನ ವಿವರಗಳಿಗೆ wwwಡಾಟ್ಎಸ್ಐಟಿಡಾಟ್ಎಸಿಡಾಟ್ಇನ್ ಗೆ ಭೇಟಿ ನೀಡಿ"
        language = 'kn'
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("text.mp3")
        os.system("cvlc text.mp3")
        break
        
    elif GPIO.input(D1) and GPIO.input(D0) and not GPIO.input(D2):
        print("3")
        text = "ನಾನು ಜಾರ್ವಿಸ್, ನನ್ನನ್ನು ಮಾಡಲು ರಾಸ್ಪ್ಬೆರಿಪೈಯನ್ನು ಬಳಸಿರುವರು, ನಾನು ಮಾತನಾಡಬಲ್ಲೆ, ನೀವು ಹೇಳುವುದನ್ನು ಕೇಳಬಲ್ಲೆ, ಹಾಗು ನಾನು ವಿವಿದ ಅನಿಲಗಳನ್ನು ಗುರುತಿಸಬಲ್ಲೆ"
        language = 'kn'
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("text.mp3")
        os.system("cvlc text.mp3")
        break
        
    elif GPIO.input(D2) and not GPIO.input(D1) and not GPIO.input(D0):
        print("4")
        text = "ನನ್ನನು ೬ನೇ ಸೆಮ್ ಎಂಜಿನಿಯರಿಂಗ್ ವಿದ್ಯಾರ್ಥಿಗಳಾದ ಸುಧನ್ವ , ಜೀವನ್ , ಕಾಂತರಾಜು, ಸುಪ್ರಿಯಾ ರವರು ಡಾಕ್ಟರ್.ಆರ್.ಕುಮಾರಸ್ವಾಮಿ ಅವರ ಮಾರ್ಗದರ್ಶನದಲ್ಲಿ ಸೃಷ್ಟಿಮಾಡಲಾಯಿತು"
        language = 'kn'
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("text.mp3")
        os.system("cvlc text.mp3")
        break
        
    elif GPIO.input(D2) and GPIO.input(D0) and not GPIO.input(D1):
        print("5")
        text = str("ನನ್ನ ಹೆಸರು ಜಾರ್ವಿಸ್")
        language = 'kn'
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("text.mp3")
        os.system("cvlc text.mp3")
        break