from flask import Flask, render_template, request
from faker import Faker
import random
import requests 
from bs4 import BeautifulSoup

fake = Faker('ko_KR')
app = Flask(__name__)

# task1 : fakesearch
@app.route('/')
def home():
    return render_template('home.html')

# task2 : 전생
@app.route('/pastlife')
def pastlife():
    return render_template('pastlife.html')

DicFake={ } #밖으로 빼줘야 매번 실행마다 딕셔너리 초기화 안함 
@app.route('/result')
def result():
    name = request.args.get('name')
    # 1. 우리 데이터에 해당하는 이름이 있는지 없는지 확인
    if name in DicFake:
        # 3. 있다면 => DicFake에 저장된 직업 보여줌 
        job = DicFake[name] 
        
    # 2. 없다면 => 랜덤으로 fake 직업 보여줌, DicFake 저장    
    else: 
        job = fake.job()
        # fname = fake.name()
        DicFake[name] = job

    return render_template('result.html', job = job, name = name)
   
 
# task3 궁합보기
@app.route("/goonghap")
def goonghap():
    return render_template('goonghap.html')


# babos = {'babo':{'you':hap,'c':50}, 's':{'d':20,'x':30}}
babos = {}
@app.route("/destiny")
def destiny():
    babo = request.args.get('babo')
    you = request.args.get('you')

    # #방법1 : 이름 + 이름으로 저장 

    # if babo + you in babos:
    #     hap = babos[babo + you]
    # else:
    #     hap = random.randint(51,101)
    #     babos[babo + you] = hap


    #방법2 : 리스트 속 리스트 
        #1. babo가 딕셔너리 안에 있음
    if babo in babos:
        if you in babos[babo]: 
            hap = babos[babo][you]
        else:
            hap = random.randint(50,100)
            babos[babo][you] = hap

        #2. babo가 딕셔너리 안에 없음 
    else:
        hap = random.randint(50,100)     # 새로 궁합 값을 생성 
        babos[babo] = {}                 #새로운 딕셔너리를 넣어줌 
        babos[babo][you] = hap           #방금 만든 딕셔너리에 값을 넣어줌 
     
    return render_template('destiny.html',babo = babo, you = you,hap=str(hap))


# task4 관리자페이지
@app.route('/admin')
def admin():
    # for babo in babos:
    #     print(babo)
    babobabo = babos
    return render_template('admin.html',babobabo = babobabo)


# task 5 opgg
@app.route('/opgg')
def opgg():    
    return render_template('opgg.html')

# task 5 search
@app.route('/search')
def search():
    userName = request.args.get('userName')
    # 1. op.gg에 요청을 보낸다. 
    url = 'https://www.op.gg/summoner/'+userName
    # 2. html 응답을 받아서
    res = requests.get(url)
    # 3. html 안에 있는 정보를 출력
    doc = BeautifulSoup(res.text,'html.parser')
    win = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins').text
    # 승 
    win = win.replace("W","승")
    #print(win[:3]+"승")
    lose = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses').text
    lose = lose.replace("L","패")

    return render_template('search.html', user = userName, win =win, lose = lose)

# 상시적용
if __name__ == "__main__":
    app.run(debug=True)
