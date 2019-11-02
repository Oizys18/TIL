import requests
from decouple import config

base = 'https://api.telegram.org/'
token = config('TELEGRAM_TOKEN')
method = "sendMessage"
chat_id = ""
text = "우웩"
url = base + token + method + '?' + "chat_id=" + chat_id +"&"+ "text=" + text

res = requests.get(url)

