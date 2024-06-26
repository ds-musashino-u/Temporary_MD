import time
from datetime import datetime
import requests

upload_url = "自分のURLを貼り付け"

def loop():
    print("start")
    while True:
        try:
            dis = 100
            now = datetime.now()
            dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
            upload_data = dt_string + ', Distance: %.2f' % dis
            url = upload_url + "?data1=" + upload_data
            print(upload_data)
            requests.get(url)
            time.sleep(10)
        except Exception as e:
            print("An error occurred: ", str(e))

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
