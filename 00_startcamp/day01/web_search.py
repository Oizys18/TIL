"""
다음에서 아이유,수지,아이린,슬기 검색 
"""

import webbrowser
url = "https://search.daum.net/search?q="
keyword = ["아이유","수지","아이린","슬기"]

#맨 앞 글자가 '아'일 경우 검색 
for j in range(0,5):
    if ord(keyword[j][0]) == 50500:
        webbrowser.open(url + keyword[j])


"""
#리스트 내용물 모두 검색 
for i in keyword:
    webbrowser.open(url + i)
"""
