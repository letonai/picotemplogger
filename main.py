
import network
import time
import machine
import urequests
import json
import gc
from pimoroni import RGBLED
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4

led = RGBLED(6, 7, 8)
led.set_rgb(1,0,0)
wlan = network.WLAN(network.STA_IF)
board_led = machine.Pin("LED", machine.Pin.OUT)
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)
sensor_temp = machine.ADC(4)
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)
display.set_backlight(.3)
display.set_font("serif")

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
sheetURL="https://script.google.com/macros/s/AKfycbwr12k7DzDAM5Woy-jNo7ZvXdSrL6Ekqb_Bk7-gF0xRcP2UzZ3jMBA9JS2WJE-w_vlqxA/exec?temp="
timeURL="https://timeapi.io/api/Time/current/zone?timeZone=America/Vancouver"


def getTime():
    res=urequests.get(url=timeURL)
    time=json.loads(res.text)["dateTime"]
    res.close()
    return time
# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(BLACK)
    display.clear()


def getTemp():
    print(str(sensor_temp.read_u16()*3.3/65535))
    #conversion_factor = 3.3033 / (65535)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 17 - (reading - 0.710) / 0.001721
    return "{:.1f}".format(temperature)+"C"

def connectWifi():
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect('<SSID>', '<PASSWD>')
        while not wlan.isconnected() and wlan.status() >= 0:
            print("Waiting to connect:")
            time.sleep(1)
            board_led.off()
        board_led.on()
        print(wlan.ifconfig())
    else:
        print("Wifi already connected...")
        print(getTime())
    
    
def sendToSpreadsheet(wifi):
    try:
        led.set_rgb(1,1,0)
        print(sheetURL+wifi)
        res=urequests.get(url=sheetURL+wifi)
        res.close()
        gc.collect()
        
        led.set_rgb(0,0,1)
    except NameError:
        led.set_rgb(5,0,0)
        print("Error..."+NameError)

connectWifi()   
led.set_rgb(0,1,0)
wlan.active(True)
    
def tela():
    display.set_pen(WHITE)            
    display.text(getTemp(),10,40,2,1)
    display.update()
    
running=True
lastrun=359
while True:
    time.sleep(1)
    lastrun+=1
    if running:
        clear()
        tela()
        
    if button_a.read() and running:
        running=False
        led.set_rgb(1,0,0)
    elif button_b.read() and not running:
        running=True
        led.set_rgb(0,1,0)
    elif button_x.read():
        sendToSpreadsheet(str(getTime()+","+getTemp()))
        
    if lastrun>360:
        sendToSpreadsheet(str(getTime()+","+getTemp()))
        lastrun=0




