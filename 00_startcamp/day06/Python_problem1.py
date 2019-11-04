"""
상승장? 하락장? : EX01
최고가와 최저가의 차이를 변동폭으로 정의할 때 
(시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 
그렇지 않은 경우 "하락장" 문자열을 출력하라.
"""
import requests
from pprint import pprint
url = "https://api.bithumb.com/public/ticker/btc"
data = requests.get(url).json()['data']

# 데이터 딕셔너리 작성 
stock = {'opeing_price':data.get('opening_price'),
        'closing_price':data.get('closing_price'),
        'min_price':data.get('min_price'),
        'max_price':data.get('max_price')}


# 변동폭 및 시가 
BDP = abs(int(stock.get('max_price'))-int(stock.get('min_price')))
siga = int(data.get('buy_price'))

# 조건문으로 출력 
if siga + BDP > int(stock.get('max_price')):
    print('상승장')
else: 
    print('하락장')


"""
모음제거 : EX02
"""

my_str = "Life is too short, you need python"
new_str = ''
vowel = 'aeiou'
for i in list(my_str):
    if i not in vowel:
        new_str = new_str + i
print(new_str)

"""
my_str = "Life is too short, you need python"
vowels = 'aeiou'
result = ''
for char in my_str:
    if char not in vowels:
        result +=char
print(result)

# 만약 대문자도 구분하려면 vowel = 'aeiouAEIOU'
# 아님 str.replace()해도 ㄱㅊ 
"""
"""

my_str = "Life is too short, you need python"
new_str = ''
vowel = 'aeiou'



""" 





"""
개인정보 보호
"""
phone = input()

if len(phone) == 11:
    if phone[0:3] == '010':
        print('*'*7 + phone[7:11])
    else:
        print('핸드폰 번호를 입력하세요')
else:    
    print('핸드폰 번호를 입력하세요')


"""
정중앙
"""

text = input()

# 홀짝
def isEven(num):
    tl = int(len(text)/2)
    if num % 2 == 0:
        print(text[tl-1:tl+1]) 
    else:
        print(text[tl:tl+1])


