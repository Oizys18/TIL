"""

KOSPI 주가를 자동으로 스크랩하는 프로그램
외장 requests 함수 + Beautiful Soup

"""

import requests
import bs4

#서버 요청 
url = "https://www.howmanypeopleareinspacerightnow.com/"
CurUrl = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8"

#응답 저장 
response = requests.get(url).text
response2 = requests.get(CurUrl).text

#파싱 Parsing 
#feature를 html 파서로 입력
document = bs4.BeautifulSoup(response, 'html.parser')
document2 = bs4.BeautifulSoup(response2, 'html.parser')

#페이지 -> 원하는 정보 '요소검사' -> 복사 -> CSS 선택자

# #코스피 지수 찾아서 출력 #KOSPI_now 
# kospi = document.select_one('#KOSPI_now').text
# print("현재 코스피 지수는 : " + kospi)

#코스닥 #KOSDAQ_now
kosdaq = document.select_one('#top > h1').text
print("현재 코스닥 지수는 : " + kosdaq)

#환율 .spt_con > strong:nth-child(2)
currency = document2.select_one('.spt_con > strong:nth-child(2)').text
print("현재 원-달러 환율은 : " + currency)
