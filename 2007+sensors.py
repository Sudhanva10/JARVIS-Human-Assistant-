import signal
from signal import SIGTERM
from signal import SIGHUP
from signal import pause
from gtts import gTTS
import sys
import math
import time
import spidev
import os
import random
from rpi_lcd import LCD
import RPi.GPIO as GPIO
time.sleep(0.100)

D7 = 17
D6 = 27
D5 = 22
D4 = 5
D3 = 6
D2 = 13
D1 = 19
D0 = 26

TRIG=21
ECHO=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(D7,GPIO.IN)
GPIO.setup(D6,GPIO.IN)
GPIO.setup(D5,GPIO.IN)
GPIO.setup(D4,GPIO.IN)
GPIO.setup(D3,GPIO.IN)
GPIO.setup(D2,GPIO.IN)
GPIO.setup(D1,GPIO.IN)
GPIO.setup(D0,GPIO.IN)

spi_ch = 0

# Enable SPI
spi = spidev.SpiDev(0, spi_ch)
spi.max_speed_hz = 1200000

def close(signal, frame):
    sys.exit(0)
signal.signal(signal.SIGINT, close)

def get_adc(channel):

    # Make sure ADC channel is 0 or 1
    if channel != 0:
        channel = 1

    # Construct SPI message
    #  First bit (Start): Logic high (1)
    #  Second bit (SGL/DIFF): 1 to select single mode
    #  Third bit (ODD/SIGN): Select channel (0 or 1)
    #  Fourth bit (MSFB): 0 for LSB first
    #  Next 12 bits: 0 (don't care)
    msg = 0b11
    msg = ((msg << 1) + channel) << 5
    msg = [msg, 0b00000000]
    reply = spi.xfer2(msg)

    # Construct single integer out of the reply (2 bytes)
    adc = 0
    for n in reply:
        adc = (adc << 8) + n

    # Last bit (0) is not part of ADC value, shift to remove it
    adc = adc >> 1

    # Calculate voltage form ADC value
    # considering the soil moisture sensor is working at 5V
    voltage = (5 * adc) / 1024

    return voltage

lcd=LCD()
def safe_exit(signum, frame):
    exit(1)
GPIO.setmode(GPIO.BCM)

if __name__ == '__main__':
    # Report the channel 0 and channel 1 voltages to the terminal
    try:
        while True:
            adc_0 = get_adc(0)
            rs0=((5-2.05)/2.05)
            ro0=rs0/9.8
            b0=1.3102
            m0=-0.3733
            y0=rs0/ro0
            rs0=((5-adc_0)/adc_0)
            
            adc_1 = get_adc(1)
            rs1=((5-2.05)/2.05)
            ro1=rs1/9.8
            b1=1.2506
            m1=-0.4548
            y1=rs1/ro1
            rs1=((5-adc_1)/adc_1)
            if (adc_0 > 3.10):
                print("MQ-3:", adc_0, "V MQ-3:", 10**((math.log10(rs0/0.40311)-b0)/m0), "ppm")
                a=round(10**((math.log10(rs0/0.40311)-b0)/m0),1)
                lcd.text(str(a)+"ppm,Alcohol",2)
                
            elif (adc_1 > 3.26 and adc_1 < 4.3):
                print("MQ-2:", adc_1, "V MQ-2:", 10**((math.log10(rs1/0.40311)-b1)/m1), "ppm")
                b=round(10**((math.log10(rs1/0.40311)-b1)/m1),2)
                lcd.text(str(b)+"ppm,Smoke",2)
                
            elif (adc_1 > 2.80 and adc_1 < 3.25):
                adc_0 = get_adc(0)
                rs2=((5-2.05)/2.05)
                ro2=rs0/9.8
                b2=1.61785
                m2=-0.4434
                y2=rs2/ro2
                rs2=((5-adc_1)/adc_1)
                print("MQ-2:", adc_1, "V MQ-2:", 10**((math.log10(rs2/0.40311)-b2)/m2), "ppm")
                c=round(10**((math.log10(rs2/0.40311)-b2)/m2),2)
                lcd.text(str(c)+"ppm,LPG",2)
                
            elif (adc_0 > 2.8 and adc_1 > 3.26 and adc_1 < 4.3):
                lcd.text("LPG & Alcohol Found",2)
                print("MQ-3:", adc_0, "V MQ-3:", 10**((math.log10(rs0/0.40311)-b0)/m0), "ppm","MQ-2:", adc_1, "V MQ-2:", 10**((math.log10(rs1/0.40311)-b1)/m1), "ppm")
                
            elif (adc_0 > 2.8 and adc_1 > 2.80 and adc_1 < 3.25):
                lcd.text("Smoke & Alcohol Found",2)
                print("MQ-3:", adc_0, "V MQ-3:", 10**((math.log10(rs0/0.40311)-b0)/m0), "ppm","MQ-2:", "MQ-2:", adc_1, "V MQ-2:", 10**((math.log10(rs2/0.40311)-b2)/m2), "ppm")
                
            else:
                lcd.text("I smell nothing",2)            
            signal.signal(signal.SIGTERM,safe_exit)
            signal.signal(signal.SIGHUP,safe_exit)
            #pause()
            
            if (GPIO.input(21) == True):
                lcd.text("No Touch Detected",1)
            else:
                print("Distance measurement in Progress")
                GPIO.output(TRIG,False)
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
                distance=round(distance,1)
                print("Distance",distance,"cm")
                time.sleep(0.5)
                if (distance >0 and distance <=10):
                    lcd.text("Object at "+str(distance)+"cm",1)
                elif (distance >10 and distance <=20):
                    lcd.text("Object at "+str(distance)+"cm",1)
                else:
                    lcd.text("No Object Found",1)
            
            if GPIO.input(D0) and not GPIO.input(D2) and not GPIO.input(D1) and not GPIO.input(D3):
                print("1")
                os.system('mpg123 Name.mp3 &')
                break
                
            elif GPIO.input(D1) and not GPIO.input(D0) and not GPIO.input(D2) and not GPIO.input(D3):
                print("2")
                os.system('mpg123 SIT.mp3 &')
                break
                
            elif GPIO.input(D1) and GPIO.input(D0) and not GPIO.input(D2) and not GPIO.input(D3):
                print("3")
                os.system('mpg123 Characteristics.mp3 &')
                break
                
            elif GPIO.input(D2) and not GPIO.input(D1) and not GPIO.input(D0) and not GPIO.input(D3):
                print("4")
                os.system('mpg123 Creation.mp3 &')
                break
                
            elif GPIO.input(D2) and GPIO.input(D0) and not GPIO.input(D1) and not GPIO.input(D3) and not GPIO.input(D4) and not GPIO.input(D5) and not GPIO.input(D6) and not GPIO.input(D7):
                print("5")
                if (adc_0 > 3.10):
                    os.system('mpg123 Alcohol.mp3 &')
                    break
                elif (adc_1 > 3.26 and adc_1 < 4.3):
                   os.system('mpg123 LPG.mp3 &')
                   break
                elif (adc_1 > 2.8 and adc_1 < 3.25):
                    os.system('mpg123 FragnanceStick.mp3 &')
                    break
                else:
                    os.system('mpg123 NoGasDetected.mp3 &')
                    break
                
            elif GPIO.input(D2) and GPIO.input(D1) and not GPIO.input(D0) and not GPIO.input(D3) and not GPIO.input(D4) and not GPIO.input(D5) and not GPIO.input(D6) and not GPIO.input(D7):
                print("6")
                if (distance >0 and distance <=20): 
                    os.system('mpg123 Object.mp3 &')
                    break
                
            elif GPIO.input(D2) and GPIO.input(D1) and GPIO.input(D0) and not GPIO.input(D3) and not GPIO.input(D4) and not GPIO.input(D5) and not GPIO.input(D6) and not GPIO.input(D7):
                print("7")
                os.system('mpg123 Uses.mp3 &')
                break
                
            elif not GPIO.input(D2) and not GPIO.input(D1) and not GPIO.input(D0) and GPIO.input(D3):
                print("8")
                os.system('mpg123  Cost.mp3 &')
                break
                
            elif not GPIO.input(D2) and not GPIO.input(D1) and GPIO.input(D0) and GPIO.input(D3):
                print("9")
                os.system('mpg123 Date.mp3 &')
                break
                
            elif not GPIO.input(D2) and GPIO.input(D1) and not GPIO.input(D0) and GPIO.input(D3):
                print("10")
                os.system('mpg123 Parts.mp3 &')
                break
        
    except KeyboardInterrupt:
        pass
        GPIO.cleanup()