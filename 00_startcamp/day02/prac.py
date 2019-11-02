"""
네이버 실시간 검색 순위 출력
"""

import requests
import bs4

#서버 요청 
url = "https://www.naver.com/"

#응답 저장 
response = requests.get(url).text

#파싱 Parsing 
#feature를 html 파서로 입력
document = bs4.BeautifulSoup(response, 'html.parser')

#페이지 -> 원하는 정보 '요소검사' -> 복사 -> CSS 선택자


# 네이버 순위 1~10
# 소스 열어보면 span class="ah_k" ~~라고 적혀있음
# 문자열이 ah_k 에 있다는 뜻 

naver = document.select('.ah_k',limit=10)
for title in naver:
    print(title.text)

