import asyncio
import time
import RPi.GPIO as GPIO
from datetime import datetime
import requests

data = []
backup_data = []
upload_url = "https://script.google.com/a/macros/ds.musashino-u.ac.jp/s/AKfycbyaK_FZYseENhrpYYZ_qsXGSe39tQ4Ws_frMTflMms0Uey220Kh_kdy2o1rfAiHGfo2/exec"
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

async def loop():
    print("start")
    while True:
        dis = distance()
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
        data.append(dt_string + ',%.2f' % dis)
        backup_data.append(dt_string + ',%.2f' % dis)
        print(dt_string + ', Distance: %.2f' % dis)

        if len(data) > 9:
            url = (
                upload_url
                + "?data1=" + data[0]
                + "&data2=" + data[1]
                + "&data3=" + data[2]
                + "&data4=" + data[3]
                + "&data5=" + data[4]
                + "&data6=" + data[5]
                + "&data7=" + data[6]
                + "&data8=" + data[7]
                + "&data9=" + data[8]
                + "&data10=" + data[9]
            )

            await asyncio.to_thread(requests.get, url)
            data.clear()

        await asyncio.sleep(1)

def save_csv():
    with open("ultra_sonic.csv", mode="w")as file:
        for i in range(len(backup_data)):
            file.writelines(backup_data[i] + '\n')

def destroy():
    GPIO.cleanup()

async def main():
    setup()
    try:
        await loop()
    except KeyboardInterrupt:
        save_csv()
        destroy()

if __name__ == "__main__":
    asyncio.run(main())
