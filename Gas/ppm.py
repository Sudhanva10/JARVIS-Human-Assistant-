import signal
from signal import SIGTERM
from signal import SIGHUP
from signal import pause
import sys
import math
import time
import spidev
import os
import random
from rpi_lcd import LCD
import RPi.GPIO as GPIO
time.sleep(0.100)

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
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)

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
            if (adc_0 > 2.8):
                lcd.text("I smell Alcohol",2)
                print("MQ-3:", adc_0, "V MQ-3:", 10**((math.log10(rs0/0.40311)-b0)/m0), "ppm")
                
            elif (adc_1 > 3.26 and adc_1 < 4.3):
                lcd.text("I smell LPG",2)
                print("MQ-2:", adc_1, "V MQ-2:", 10**((math.log10(rs1/0.40311)-b1)/m1), "ppm")
                print(rs1/0.40311)
                
            elif (adc_1 > 2.80 and adc_1 < 3.25):
                adc_0 = get_adc(0)
                rs2=((5-2.05)/2.05)
                ro2=rs0/9.8
                b2=1.61785
                m2=-0.4434
                y2=rs2/ro2
                rs2=((5-adc_1)/adc_1)
                lcd.text("I smell Smoke",2)
                print("MQ-2:", adc_1, "V MQ-2:", 10**((math.log10(rs2/0.40311)-b2)/m2), "ppm")

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
                lcd.text("Touch Detected",1)

            else:
                #lcd.clear()
                lcd.text("NoTouch Detected",1)

    except KeyboardInterrupt:
        pass
        GPIO.cleanup()