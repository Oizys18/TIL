from flask import Flask, render_template
from datetime import datetime #/newyear, #datetime패키지 중 datetime만 사용
import random
import requests 
import bs4 

app = Flask(__name__) 

# task1
@app.route("/")
def home():
    return render_template('home.html')

# task2
@app.route('/hello/<name>')
def hello(name):
    # name에는 /hello/이름/활용가능
    return render_template('hello.html', username=name) 
    #hello.html에서 name 사용가능하도록 설정(jinja + flask)

# task3
    #랜덤으로 음식 메뉴 추천, 
    #해당 음식 사진 보여주는 기능 구현

@app.route("/menu")
def menu():
    #랜덤으로 음식 메뉴 추천
    MenuList = ['순두부','제육','오삼','냉수','인도커리','감자핫도그']
    result = random.choice(MenuList)
    
    #해당 음식 사진 보여주는 기능 구현
    # 이미지 링크
    a = "https://i.ytimg.com/vi/iCRj9VWDCt4/maxresdefault.jpg"
    b = "http://recipe1.ezmember.co.kr/cache/recipe/2015/05/27/38013d1dfd8fa46a871b9cda074b26341.jpg"
    c = 'http://recipe1.ezmember.co.kr/cache/recipe/2017/02/07/585ddeee0b70b6b9bf53b77b37f2499a1.jpg'
    d = 'https://pbs.twimg.com/profile_images/793816437399838721/ZFogcGnQ.jpg'
    e = 'http://file2.nocutnews.co.kr/newsroom/image/2018/06/08/20180608072916866618_0_1100_1100.jpg'
    f = 'https://img.insight.co.kr/static/2017/12/24/700/744bwizcpc9d24hwh4z6.jpg'
    menudic = {'순두부':a,'제육':b,'오삼':c,'냉수':d,'인도커리':e,'감자핫도그':f}
    image = menudic[result]
    return render_template('menu.html', menu = result, image = image)



@app.route("/lotto")
def lotto():
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
    res = requests.get(url)
    #json 파일 -> python dictionary로 바꿈 
    dict_lotto = res.json() # 이건 Json을 통해 딕셔너리로 변경됨
    # 당첨 번호 
    winner = []
    for i in range(1,7):
        winner.append(dict_lotto[f'drwtNo{i}'])
    
    winner.sort
    MyNum = sorted(random.sample(range(1,46),6))
    count = len(set(winner) & set(MyNum))
    if count == 6 :
        grade = "1등"
    elif count == 5 :
        grade ="3등"
    elif count == 4 :
        grade ="4등"
    elif count == 4 :
        grade ="5등"
    else:
        grade ="꽝"
    return render_template('lotto.html', Num = MyNum, winner = winner, count = count, grade = grade )


#변동 시 서버 재접속 필요없도록 
# 방법 1 
if __name__ == "__main__":
    app.run(debug=True)

# flask run 명령어로 바로 flask application 실행가능한 이유 
# python 파일 이름을 default 'app.py'로 했기 때문 
