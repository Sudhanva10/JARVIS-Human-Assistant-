import wiringpi as wiringpi
from time import sleep
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

wiringpi.wiringPiSetupGpio()
lcd=LCD()
def safe_exit(signum, frame):
    exit(1)
wiringpi.pinMode(25,0)
count=0
while(True):
    #my_input=wiringpi.analogRead(25)
    my_input=wiringpi.digitalRead(25)
    if(my_input):
        lcd.text("NoAlchohol",2)
    else:
        lcd.text("AlchoholDetected",2)
    sleep(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP ,safe_exit)
    pause()
except KeyboardInterrupt:
    pass