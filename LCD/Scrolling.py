from RPLCD import *
from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)
lcd.cursor_pos = (0, 0)
lcd.write_string('Hello World')
framebuffer = [
        '',
        '',
        ]
def write_to_lcd(lcd, framebuffer, num_cols):
        """Write the framebuffer out to the specified LCD."""
        lcd.home()
        for row in framebuffer:
            lcd.write_string(row.ljust(num_cols)[:num_cols])
            lcd.write_string('\r\n')
def long_text(text):
        if len(text)<16:
            lcd.write_string(text)      
        for i in range(len(text) - 16 + 1):
            framebuffer[1] = text[i:i+16]
            write_to_lcd(lcd, framebuffer, 16)
            sleep(0.2)
lcd.cursor_pos = (0, 0)
long_text('This is a long Scrolling text')