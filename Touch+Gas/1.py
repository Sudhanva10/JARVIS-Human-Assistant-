import os
import time
import wiringpi as wiringpi
from time import sleep
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

time.sleep(0.100)
import random
import RPi.GPIO as GPIO
wiringpi.wiringPiSetupGpio()
lcd=LCD()

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)

def safe_exit(signum, frame):
    exit(1)
wiringpi.pinMode(25,0)
count=0

while True:
    #my_input=wiringpi.analogRead(25)
    my_input=wiringpi.digitalRead(25)
    if ((GPIO.input(21) == True) and (my_input)):
        lcd.text("Touch Detected",1)
        print(my_input)
        lcd.text("NoAlchohol",2)
        time.sleep(0.5);
    elif((GPIO.input(21) == True) and (my_input==0)):
        lcd.text("Touch Detected",1)
        print(my_input)
        lcd.text("AlchoholDetected",2)
        time.sleep(0.5);
    elif((GPIO.input(21) == False) and (my_input)):
        lcd.text("NoTouchDetected",1)
        print(my_input)
        lcd.text("NoAlchohol",2)
        time.sleep(0.5);
    else:
        #((GPIO.input(21) == False) and (my_input==0)):
        lcd.text("NoTouchDetected",1)
        print(my_input)
        lcd.text("AlchoholDetected",2)
        time.sleep(0.5);
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP ,safe_exit)
    pause()
except KeyboardInterrupt:
    pass