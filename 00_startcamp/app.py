import requests
import bs4 #/kospi
from pprint import pprint as pp

url = "https://finance.naver.com/sise/"
response = requests.get(url).text

document = bs4.BeautifulSoup(response, 'html.parser')
pp(document)
# pp(response)