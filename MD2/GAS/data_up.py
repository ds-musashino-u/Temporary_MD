import requests
import time

distance = 300
url = "https://script.google.com/a/macros/ds.musashino-u.ac.jp/s/AKfycbyaK_FZYseENhrpYYZ_qsXGSe39tQ4Ws_frMTflMms0Uey220Kh_kdy2o1rfAiHGfo2/exec?data1=" + str(distance)

upload_data = []
u_size = 9

while True:
    upload_data.append(url)
    time.sleep(1)

    if(len(upload_data) > u_size):
        for i in range(u_size):
            requests.get(url)
            print(url)

        upload_data.clear()
