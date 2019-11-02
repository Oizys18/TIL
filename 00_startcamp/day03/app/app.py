"""
Flask app
"""
from flask import Flask #플라스크 패키지 중 Flask를 사용했음. 
import random #/lotto /menu
import requests #/kospi
import bs4 #/kospi
from datetime import datetime #/newyear, #datetime패키지 중 datetime만 사용

app = Flask(__name__) 

# 1. 주문 받는 방식 (어떻게?)
@app.route("/")
# 2. 무엇을 제공할지 (무엇?)
def hello():
    return "Hello World!"

#주문서 작성
@app.route("/hi")
def hi():                           
    return "Hi there stranger!" 
#localhost:5000/hi 작성시 return 출력


# task1, 이름 출력 
@app.route("/name")
def prname():
    return "YANG CHAN WOO"

# task2, 
@app.route("/hello/john")
def hello2():
    return "hello, john"

# task3, variable routing <>사용. 변수를 넣어서 활용가능 
@app.route("/hello/<person>")
def hello3(person):
    return f"Hello, {person}"
    # return "Hello, " + person
    
#task4, 세제곱 함수
# /cube/1 => 1
# /cube/2 => 8
# /cube/3 => 27
@app.route("/cube/<num>")
def cube(num):
    result = int(num)**3
    return str(result)
# Internal server error : 
# 1. <num>으로 받은 것은 str인데 int 안해서 에러
# 2. return 값은 str,dict, tuple, Response instance, or WSG여야만 한다. 
# 따라서, 입력 받은 값을 int하고 계산후 결과값을 str해야함 

# task5, 점심메뉴추천
@app.route("/menu")
def menu():
    MenuList = ['순두부','제육','오삼']
    result = random.choice(MenuList)
    return result

# task6, 랜덤로또번호추천
@app.route("/lotto")
def lotto():
    # NumList = range(1,46)
    # NumRes = random.choices(NumList,k=6)
    # result = ''
    # for i in NumRes:
    #     result = result + str(i) + ' '
    # return result
    return str(sorted(random.sample(range(1,46),6))) #선생님 코드.. ㅠ One-liner

# task7, 현재 네이버 코스피 
@app.route("/kospi")
def kospi():
    url = "https://finance.naver.com/sise/"
    response = requests.get(url).text
    document = bs4.BeautifulSoup(response, 'html.parser')
    kospi = document.select_one('#KOSPI_now').text
    return "현재 코스피 지수는 : " + kospi

#task8, 새해 
@app.route("/newyear")
def newyear():
    #그냥 import datetime만 했다면 datetime.datetime.now().day 이런 식으로
    day = datetime.now().day 
    month = datetime.now().month
    #만약 오늘이 1월 1일이면 
    if month == 1 and day == 1:
        return "<h1>예<h1>" 
    else:
        return f"<h1>아니요, 오늘은 {str(month)}월 {str(day)}일입니다.<h1>"
    #html 사용, 볼드처리 
    
# task9, index
@app.route("/index")
def index():
    return "<html><head></head><body><h1>홈페이지</h1><p>이건내용</p></body></html>"
    #html로 씀