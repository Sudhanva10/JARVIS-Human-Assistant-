from signal import signal, SIGTERM, SIGHUP
from rpi_lcd import LCD
import time
import sys
import multiprocessing
lcd = LCD()

def long_string(display, text='', num_line=1, num_cols=16):
    if len(text) > num_cols:
        display.text(text[:num_cols], num_line)
        time.sleep(0.1)
    for i in range(len(text) - num_cols + 1):
        text_to_print = text[i:i+num_cols]
        display.text(text_to_print, num_line)
        time.sleep(0.3)

    else:
        display.text(text, num_line)

def read(k):
    for x in range (0,10):
        print("fnerede {k}")
    try:
        while True:
            t1=multiprocessing.Process(target=long_string,args=(lcd,"how is going onddddddd",1)).start()
            t2=multiprocessing.Process(target=long_string,args=(lcd,"how is going on sdlkfl",2)).start()
    except KeyboardInterrupt:
        pass
    finally:
        lcd.clear()