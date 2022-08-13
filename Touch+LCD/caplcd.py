import os
import time
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
time.sleep(0.100)
import random
import RPi.GPIO as GPIO
lcd=LCD()

def safe_exit(signum, frame):
    exit(1)
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)


while True:
    if (GPIO.input(21) == True):
        lcd.text("Touch Detected",1)
        time.sleep(0.5);
    else:
        #lcd.clear()
        lcd.text("NoTouch Detected",1)
        time.sleep(0.5);
try:
    signal(SIGTERM,safe_exit)
    signal(SIGHUP,safe_exit)
    pause()
except KeyboardInterrupt:
    pass