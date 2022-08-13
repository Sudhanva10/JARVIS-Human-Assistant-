import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=21
ECHO=20
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
while True:
    print("Distance measurement in Progress")
    GPIO.output(TRIG,False)
    print("Waiting for Sensor to Settle")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print("Distance",distance,"cm")
    time.sleep(0.5)