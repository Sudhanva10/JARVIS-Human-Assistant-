import os
import time
time.sleep(0.100)
import random

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    if (GPIO.input(21) == True):
        print("Touch Detected")
        time.sleep(0.5);
    else:
        print("No Touch Detected")
        time.sleep(0.5);