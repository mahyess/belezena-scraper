import os

# url = """curl 'https://im.ge/json' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0' -H 'Accept: application/json' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: multipart/form-data; boundary=---------------------------1862835642000304411921308525' -H 'Origin: https://im.ge' -H 'Connection: keep-alive' -H 'Referer: https://im.ge/upload' -H 'Cookie: PHPSESSID=7em1n3rtevfl06f5a19m8eu53k; amplitude_id_476d446d2d57aa9a7764732a26466a97im.ge=eyJkZXZpY2VJZCI6ImNkMmZhNWFjLTU2NTYtNGYwNC04OTAzLWRmN2MwOWM3YjY0ZlIiLCJ1c2VySWQiOiJkZWExYzMxYy1mZDU2LTRiOTItOTljZC1lMDQ0ZDFkMmU0OTYiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2MzI1MDU1NTI1OTUsImxhc3RFdmVudFRpbWUiOjE2MzI1MDU1NTI2MDIsImV2ZW50SWQiOjMsImlkZW50aWZ5SWQiOjYsInNlcXVlbmNlTnVtYmVyIjo5fQ==' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' -H 'DNT: 1' -H 'Sec-GPC: 1' --data-binary $'-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data; name="source"\r\n\r\nhttps://res.cloudinary.com/beleza-na-web/image/upload/w_1500,f_auto,fl_progressive,q_auto:eco,w_800,h_800/v1/imagens/product/87579/6c802146-a960-4724-8ab2-df10665497b9-87579-pai-86814-86815-86819.jpeg\r\n-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data; name="type"\r\n\r\nurl\r\n-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data; name="action"\r\n\r\nupload\r\n-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data; name="timestamp"\r\n\r\n1632505608098\r\n-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data; name="auth_token"\r\n\r\n91b2035f81c114cf3c9ee57c4d775cd2bb2fb52e\r\n-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data; name="nsfw"\r\n\r\n0\r\n-----------------------------1862835642000304411921308525--\r\n'"""

# url = f"""curl 'https://im.ge/json' -X POST \
# -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0' \
# -H 'Accept: application/json' \
# -H 'Accept-Language: en-US,en;q=0.5' --compressed \
# -H 'Referer: https://im.ge/upload' \
# -H 'Content-Type: multipart/form-data; boundary=---------------------------211586313138283738522022639772' \
# -H 'Origin: https://im.ge' \
# -H 'Connection: keep-alive' \
# -H 'Cookie: PHPSESSID=7em1n3rtevfl06f5a19m8eu53k; amplitude_id_476d446d2d57aa9a7764732a26466a97im.ge=eyJkZXZpY2VJZCI6ImNkMmZhNWFjLTU2NTYtNGYwNC04OTAzLWRmN2MwOWM3YjY0ZlIiLCJ1c2VySWQiOiJkZWExYzMxYy1mZDU2LTRiOTItOTljZC1lMDQ0ZDFkMmU0OTYiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2MzI1MDI2MzU4ODIsImxhc3RFdmVudFRpbWUiOjE2MzI1MDI2OTQyOTcsImV2ZW50SWQiOjMsImlkZW50aWZ5SWQiOjUsInNlcXVlbmNlTnVtYmVyIjo4fQ==' \
# -H 'Sec-Fetch-Dest: empty' \
# -H 'Sec-Fetch-Mode: no-cors' \
# -H 'Sec-Fetch-Site: same-origin' \
# -H 'DNT: 1' \
# -H 'Sec-GPC: 1' \
# -H 'Pragma: no-cache' \
# -H 'Cache-Control: no-cache' \
# --data-binary $'-----------------------------211586313138283738522022639772\r\nContent-Disposition: form-data;
# name="source"\r\n\r\nhttps://res.cloudinary.com/beleza-na-web/image/upload/w_1500,f_auto,fl_progressive,q_auto:eco,w_800,h_800/v1/imagens/5/1902-tradition-lavande-perfume-unissex-eau-de-cologne-245ml-26280-902552048440593096.jpg\r\n-----------------------------211586313138283738522022639772\r\nContent-Disposition: form-data;
# name="type"\r\n\r\nurl\r\n-----------------------------211586313138283738522022639772\r\nContent-Disposition: form-data;
# name="action"\r\n\r\nupload\r\n-----------------------------211586313138283738522022639772\r\nContent-Disposition: form-data;
# name="timestamp"\r\n\r\n1632502739583\r\n-----------------------------211586313138283738522022639772\r\nContent-Disposition: form-data;
# name="auth_token"\r\n\r\n91b2035f81c114cf3c9ee57c4d775cd2bb2fb52e\r\n-----------------------------211586313138283738522022639772\r\nContent-Disposition: form-data;
# name="nsfw"\r\n\r\n0\r\n-----------------------------211586313138283738522022639772--\r\n'"""

# res = os.system(f"{url}")

# import json

# res = json.loads(res)
# print(res["status_code"])
# print(res)

import requests

cookies = {
    "PHPSESSID": "7em1n3rtevfl06f5a19m8eu53k",
    "amplitude_id_476d446d2d57aa9a7764732a26466a97im.ge": "eyJkZXZpY2VJZCI6ImNkMmZhNWFjLTU2NTYtNGYwNC04OTAzLWRmN2MwOWM3YjY0ZlIiLCJ1c2VySWQiOiJkZWExYzMxYy1mZDU2LTRiOTItOTljZC1lMDQ0ZDFkMmU0OTYiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2MzI1MDU1NTI1OTUsImxhc3RFdmVudFRpbWUiOjE2MzI1MDU1NTI2MDIsImV2ZW50SWQiOjMsImlkZW50aWZ5SWQiOjYsInNlcXVlbmNlTnVtYmVyIjo5fQ==",
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "multipart/form-data; boundary=---------------------------1862835642000304411921308525",
    "Origin": "https://im.ge",
    "Connection": "keep-alive",
    "Referer": "https://im.ge/upload",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "DNT": "1",
    "Sec-GPC": "1",
}

curl_data = '-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data;name="source"\r\n\r\n{{image_link}}\r\n-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data;name="type"\r\n\r\nurl\r\n-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data;name="action"\r\n\r\nupload\r\n-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data;name="timestamp"\r\n\r\n{{timestamp}}\r\n-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data;name="auth_token"\r\n\r\n91b2035f81c114cf3c9ee57c4d775cd2bb2fb52e\r\n-----------------------------1862835642000304411921308525\r\nContent-Disposition: form-data;name="nsfw"\r\n\r\n0\r\n-----------------------------1862835642000304411921308525--\r\n'
import csv, time
from datetime import datetime

with open("results/__all__.csv") as reader, open(
    "results/__all__ updated.csv", "w"
) as writer:
    reader = csv.DictReader(reader)
    writer = csv.DictWriter(writer, fieldnames=reader.fieldnames)
    writer.writeheader()
    for count, row in enumerate(reader):
        retry_count = 0
        while True:
            try:
                print(f"count: {count} starting")
                response = requests.post(
                    "https://im.ge/json",
                    data=curl_data.replace(
                        "{{image_link}}", row["photo"].replace('"', "")
                    )
                    .replace(
                        "{{timestamp}}",
                        str(int(time.time()*1000)),
                    )
                    .encode(),
                    headers=headers,
                    cookies=cookies,
                )
                print(f"count: {count} {response.status_code}")

                if response.status_code == 200:
                    # print(f"count: {count} 200 status")

                    response = response.json()
                    row["photo"] = response["image"]["url"]
                    writer.writerow(row)
                    break
            except Exception as e:
                print(e)
