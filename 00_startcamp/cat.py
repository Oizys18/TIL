import requests
from pprint import pprint as pp
response = requests.get(url="https://api.thecatapi.com/v1/images/search")
pp(response.json()[0]['url'])
