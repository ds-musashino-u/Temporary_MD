import RPi.GPIO as GPIO
import time
from datetime import datetime

data = []
PIR = 17    # the pir connect to pin17

def setup():
    GPIO.setmode(GPIO.BCM)      # Set the GPIO modes to BCM Numbering
    GPIO.setup(PIR, GPIO.IN)    # Set pirPin to input

def loop():
    while True:
        pir_val = GPIO.input(PIR)
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
        if pir_val==GPIO.HIGH:
            print('Detected')
            data.append (dt_string + ',Detected')
        else :
            print('Not Detected')
            data.append (dt_string + ',Not Detected')
        time.sleep(1)

def destroy():
    GPIO.cleanup()    # Release resource

def save_csv():
    with open("IR.csv",mode="w") as file:
        for i in range(len(data)):
            file.writelines(data[i] + '\n')

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        save_csv()
        destroy()