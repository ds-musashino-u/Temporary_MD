import asyncio
from datetime import datetime
import requests

data = []
backup_data = []
upload_url = "https://script.google.com/a/macros/ds.musashino-u.ac.jp/s/AKfycbyaK_FZYseENhrpYYZ_qsXGSe39tQ4Ws_frMTflMms0Uey220Kh_kdy2o1rfAiHGfo2/exec"
u_size = 9
TRIG = 16
ECHO = 18

def setup():
    print("setup OK")

def distance():
    return 100

async def loop():
    print("start")
    while True:
        dis = distance()
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
        data.append(dt_string + ',%.2f' % dis)
        backup_data.append(dt_string + ',%.2f' % dis)
        print(dt_string + ', Distance: %.2f' % dis)
        await asyncio.sleep(1)
       
        if len(data) > 10:
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
            
        requests.get(url)
        print("deta送信完了")
        data.clear()
        

def save_csv():
    with open("ultra_sonic.csv", mode="w")as file:
        for i in range(len(backup_data)):
            file.writelines(backup_data[i] + '\n')

def destroy():
    pass

if __name__ == "__main__":
    setup()
    try:
        asyncio.run(loop())
        
    except KeyboardInterrupt:
        save_csv()
        destroy()
