import requests 
from bs4 import BeautifulSoup
# 1. op.gg에 요청을 보낸다. 
url = 'https://www.op.gg/summoner/userName=cuzz'

# 2. html 응답을 받아서
res = requests.get(url)

# 3. html 안에 있는 정보를 출력
doc = BeautifulSoup(res.text,'html.parser')
win = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins').text
# 승 

print(win.replace("W","승"))
#print(win[:3]+"승")
    

#https://www.op.gg/summoner/