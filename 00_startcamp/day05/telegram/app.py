from flask import Flask, render_template,request
import requests
from pprint import pprint
from decouple import config
import random
import os
import sys
app = Flask(__name__)
token = config('TELEGRAM_TOKEN')


# homepage
@app.route('/')
def home():
    return render_template('home.html')

# task1 msg send
# @app.route('/send')
# def send():
    
#     #chat_id를 가져오는 코드 
#     # 1. getUpdates 메소드로 요청 보내기 
#     # 2. 받아온 응답(json)에서 dictionary로 바꿔서 
#     # 3. 첫 메세지 보낸 유저의 id가져오기
#     base = 'https://api.telegram.org'
#     method = "sendMessage"
#     method_id = "getUpdates"
#     url_id = f'{base}/{token}/{method_id}'
#     res = requests.get(url_id)
#     dict_id = res.json()
#     chat_id = dict_id.get("result")[0].get("message").get("from").get("id")
    
#     #home에서 보낸 msg를 받아 telegram api를 통해 메세지 전송 
#     msg = request.args.get('msg')
#     url = f"{base}/{token}/{method}?chat_id={chat_id}&text={msg}"
#     requests.get(url)
    
#     return render_template('send.html', msg = msg)


# WEBHOOK : 정보 노출되지 않아야할 때, 'POST'라는 방식으로 요청 
# POST : 비밀번호 등 보안 필요할 때 
# 요청방식 : get, post 

@app.route(f'/{token}', methods=['POST'])
def webhook():
    # 1. 메아리 챗봇
    #   (1) webhook 통해 telegram 보낸 요청 안에 있는 메세지를 가져와
    #   (2) 그대로 전송 
    #https://api.telegram.org/<token>?url=<url>/<token>

    res = request.get_json()
    msg = res.get('message').get('text')
    chat_id = res.get('message').get('chat').get('id')

    base = 'https://api.telegram.org'
    method ="sendMessage"
    

    # 입력값에 따른 다른 반응 
    # 1. 입력값이 파일인지 아닌지 판명 
    # 2. 아니라면,
    #   2-1 lotto입력시 로또번호 추천
    #   2-2 /번역 +"텍스트" : 텍스트 파파고 번역 

    # 입력이 파일이라면 다운받고 유명인 얼굴인식 하기  
    if res.get("message").get("photo") is not None:
        file_id = res.get("message").get("photo")[-1].get('file_id')
        file_res = requests.get(f"{base}/bot{token}/getFile?file_id={file_id}")
        file_path = file_res.json().get('result').get('file_path')
        file_url = f"{base}/file/bot{token}/{file_path}"

        #파일 다운
        image = requests.get(file_url, stream=True)

        #유명인 얼굴인식 
        url = "https://openapi.naver.com/v1/vision/celebrity"

        #헤더 
        headers = {
            'X-Naver-Client-Id': config('NAVER_ID'),
            'X-Naver-Client-Secret': config('NAVER_SECRET')
        }

        # 받아온 파일 넣기 
        files = {
            'image': image.raw.read()
        }

        #clova API 로 요청
        clova_res = requests.post(url,headers=headers, files=files)
        val = clova_res.json().get('faces')[0].get('celebrity').get('value')
        cof = clova_res.json().get('faces')[0].get('celebrity').get('confidence')
        msg = f"{val}을 {float(cof)*100}%만큼 닮았습니다. "
    else:
        #로또 번호 추천 
        if msg == 'lotto':
            msg = str(sorted(random.sample(range(1,46),6)))
        # /번역 +"텍스트" : 텍스트 파파고 번역 
        elif msg[0:3] == "/번역":
            # papago로 네이버 번역결과 알려줌 
            url = "https://openapi.naver.com/v1/papago/n2mt"

            headers = {
                'X-Naver-Client-Id': config('NAVER_ID'),
                'X-Naver-Client-Secret': config('NAVER_SECRET')
            }

            data = {
                'source':'ko',
                'target':'en',
                'text':res.get('message').get('text')[3:]
            }

            res = requests.post(url, headers=headers, data=data).json()
            msg = res.get('message').get('result').get('translatedText')
    
    # 봇이 출력할 메세지 
    url = f"{base}/bot{token}/{method}?chat_id={chat_id}&text={msg}"
    requests.get(url)

    return '', 200


# EZ server Run / 개발환경세팅 
if __name__ == "__main__":
    app.run(debug=True)

