import RPi.GPIO as GPIO
import time
from datetime import datetime

data = []
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
        dis = distance() 
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
        data.append (dt_string +', Distance: %.2f' % dis)
        print (dt_string + ', Distance: %.2f' % dis)
        time.sleep(1)

def save_csv():
    with open("ultra_sonic.csv",mode="w") as file:
        for i in range(len(data)):
            file.writelines(data[i] + '\n')

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        save_csv()
        destroy()

