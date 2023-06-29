import RPi.GPIO as GPIO
import time
from datetime import datetime
import requests

upload_url = "自分のURLを貼り付け"

TRIG = 16
ECHO = 18

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    print("setup OK")

def distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        a = 0
    time1 = time.time()
    while GPIO.input(ECHO) == 1:
        a = 1
    time2 = time.time()
    during = time2 - time1
    return during * 340 / 2 * 100

def loop():
    print("start")
    while True:
        try:
            dis = distance()
            now = datetime.now()
            dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
            upload_data = dt_string + ', Distance: %.2f' % dis
            url = upload_url + "?data1=" + upload_data
            print(upload_data)
            requests.get(url)
            time.sleep(10)
        except Exception as e:
            print("An error occurred: ", str(e))

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("\nProgram stopped by user")
