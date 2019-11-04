import os
import sys
import requests
from decouple import config

client_id = config('NAVER_ID')
client_secret = config('NAVER_SECRET')

# url = "https://openapi.naver.com/v1/vision/face" // 얼굴감지
url = "https://openapi.naver.com/v1/vision/celebrity" #유명인 얼굴인식
files = {'image': open('1414.png', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)