# lotto api 사용, 최신 당첨번호 가져옴
import requests
import random
from flask import Flask, render_template

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
res = requests.get(url)
#json 파일 -> python dictionary로 바꿈 
json_lotto = res.text # 이건 STR  
dict_lotto = res.json() # 이건 Json을 통해 딕셔너리로 변경됨
# 당첨 번호 
winner = []
for i in range(1,7):
    winner.append(dict_lotto[f'drwtNo{i}'])
winner.sort


# 보너스번호 넣기 
# winner.append(dict_lotto['bnusNo'])
# check = []
# a = 0
# def lotto(): 
#     MyNum = sorted(random.sample(range(1,46),6))
#     for i in range(0,6):
#         if winner[i] == MyNum[i]:
#             check.append(i)
#     if len(check)==6:
#         print("1등 당첨!")
#         return False
#     elif len(check) == 5:
#         print("2등 당첨!")
#         return False
#     elif len(check) == 4:
#         print("3등 당첨!")
#         return False
#     else : 
#         print("꽝")
#         return True
# trynum = 0
# while lotto():
#     trynum = trynum + 1 
#     print(trynum)




# for i in winner:
#     for j in MyNum:
#         if i == j:
#             count = count + 1
MyNum = sorted(random.sample(range(1,46),6))
# set 집합함수를 사용, 동일한 숫자 갯수 세기

# count = 0
# count = len(set(winner) & set(MyNum)) 

# if count == 6 :
#     grade = "1등"
# elif count == 5 :
#     grade ="3등"
# elif count == 4 :
#     grade ="4등"
# elif count == 4 :
#     grade ="5등"
# else:
#     grade ="꽝"

trial = 0
while True:
    MyNum = sorted(random.sample(range(1,46),6))
    count = len(set(winner) & set(MyNum)) 
    if count == 6:
        print("1등입니다~!~!")
        break
    trial += 1
    print(trial)



app = Flask(__name__) 
# /lotto 랜덤 넘버 추천, 최신로또와 비교해 등수를 알려주는 기능 
@app.route("/lotto")
def lotto():
    MyNum = sorted(random.sample(range(1,46),6))
    count = len(set(winner) & set(MyNum))
    return f"추천 번호는 {MyNum}, 최신로또번호는 {winner}, 일치숫자는 {count}개 입니다."
