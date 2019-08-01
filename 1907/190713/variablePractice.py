# test
"""
c=int(input())
print(c + (10*c+c) + (100*c+10*c+c) + (1000*c+100*c+10*c+c))
"""

#예제 섭씨 화씨 변환
"""
섭씨(℃)를 화씨(℉)로 변환하는 프로그램을 작성하십시오.
이 때 물의 빙점은 화씨 32도이고 비등점은 화씨 212도(표준 기압에서)입니다.
물의 비등점과 빙점 사이에 정확하게 180도 차이가 납니다.
그러므로 화씨 눈금에서의 간격은 물의 빙점과 비등점 사이의 간격의 1/180입니다.
"""

"""
a = float(input())
print("{0:0.2f} ℃ =>  {1:0.2f} ℉".format(a,(a*1.8)+32))
"""


#예제 소금물 농도
"""
20% 농도의 소금물 100g과 물 200g을 혼합한 소금물의 농도(%)를 소수점 두 번째 자리까지 구하는 프로그램을 작성하십시오.
"""
"""
print("혼합된 소금물의 농도: {0:0.2f}%".format((100*0.2)/(80+200)*100))
"""



#예제 (변수에 조건에 따른 다른 값 저장)

"""
score = 90
result = "합격" 
    if score >= 50 else "불합격"

print(result)"""



#예제 인치 cm 변환
"""
b = float(input())
print("{0:0.2f} inch => {1:0.2f} cm".format(b,b*2.54))

"""

#예제 임의의 양의 정수 입력, 모든 약수 구하기

"""
d = 5

for i in range(1, d+1):
    if d%i == 0:
        print("{0}(은)는 {1}의 약수입니다.".format(i,d))
"""


# 소수일 경우 소수 표시
"""
sosu = []
for i in range(1, d+1):
    if d%i == 0:
        print("{0}(은)는 {1}의 약수입니다.".format(i,d))
        sosu.append(i)
        if len(sosu) == 2:
            print("{0}(은)는 {1}과 {2}로만 나눌 수 있는 소수입니다.".format(d,sosu[0],sosu[1]))

"""
# 입력 영어 알파벳 문자에 대해 대소문자를 구분

"""
char = str(input())

if char.isupper():
    print ("대문자")
else :
    print("소문자")
"""

#가위바위보 게임, 가위바위보 리스트 활용
"""
m1_input = str(input())
m2_input = str(input())

list1 = ["가위", "바위", "보"]

if m1_input == list1[0]:
    if m2_input == list1[0]:
        print("Result : Draw")
    elif m2_input == list1[1]:
        print("Result : Man2 Win!")
    elif m2_input == list1[2]:
        print("Result : Man1 Win!")
elif m1_input == list1[1]:
    if m2_input == list1[1]:
        print("Result : Draw")
    elif m2_input == list1[2]:
        print("Result : Man2 Win!")
    elif m2_input == list1[0]:
        print("Result : Man1 Win!")
elif m1_input == list1[2]:
    if m2_input == list1[2]:
        print("Result : Draw")
    elif m2_input == list1[0]:
        print("Result : Man2 Win!")
    elif m2_input == list1[1]:
        print("Result : Man1 Win!")
else:
    print("뭔가이상")
"""


# 알파벳 -> 대문자는 소문자, 소문자는 대문자  / 문자아니면 그냥 출력
"""
char = "D"

if char.isalpha():
    if char.isupper():
        charL = char.lower()
        print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(char,ord(char),charL,ord(charL)))

    else:
        charU = char.upper()
        print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(char, ord(char), charU, ord(charU)))
else:
    print(char)
"""

#1~200사이 정수, 7의 배수이면서 5의 배수는 아닌 모든 숫자를 찾아 콤마로 구성된 문자열로 출력
"""
1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.
"""
"""
list1 = []
result = ""
for i in range (1,201):
    if i%7 == 0 and i%5 != 0:
        list1.append(i)

for i in range(0,len(list1)):
    if i !=len(list1)-1:
        result = result + str(list1[i]) + ","
    else :
        result = result + str(list1[i])

print(result)

"""


#100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.
"""
list2 = []
result = ""
for i in range(100,300):
    if int(str(i)[0])%2==0:
        if int(str(i)[1])%2 ==0:
            if int(str(i)[2])%2 ==0:
                list2.append(i)



for i in range(0,len(list2)):
    if i != len(list2)-1:
        result = result + str(list2[i]) + ","
    else :
        result = result + str(list2[i])
print(result)
"""
"""
다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.
"""
"""
scores = {1:88, 2:30, 3:61, 4:55,5:95}

for i in range(1,6):
    if scores.get(i)>60:
        print("{0}번 학생은 {1}점으로 합격입니다.".format(i,scores.get(i)))
    else :
        print("{0}번 학생은 {1}점으로 불합격입니다.".format(i,scores.get(i)))
    i += 1
"""

#1부터 100까지의 숫자를 for 문과 range 함수를 이용해 출력하십시오.
"""
for i in range(1,101):
    print(i)
"""

#1부터 100사이의 숫자 중 짝수를 for 문을 이용해 다음과 같이 출력하십시오.
"""
for i in range(1,101):
    if i%2==0:
        print(i, end=" ")
"""
#1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.
"""
for i in range(1,101):
    if i%2 !=0:
        if i != 99:
            print(i,end=", ")
        else :
            print(i)
"""
#1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.
"""
sum = 0
for i in range(1,101):
    if i%3==0:
        sum += i
print("1부터 100사이의 숫자 중 3의 배수의 총합: %s"%sum)
"""


#다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
"""
['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.
"""

"""
BloodT = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
BA = 0
BB = 0
BAB = 0
BO = 0
for i in BloodT:
    if i =='A':
        BA += 1
    elif i =='B':
        BB += 1
    elif i =='O':
        BO += 1
    elif i =='AB':
        BAB += 1
print("{"+"'A': {0}, 'O': {1}, 'B': {2}, 'AB': {3}".format(BA,BO,BB,BAB)+"}")
"""


# 다음은 학생의 점수를 나타내는 리스트입니다.
"""
[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
"""
"""
scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum = 0
a = 0
while a < len(scores):
    if scores[a]>=80:
        sum += scores.pop(a)
    else :
        scores.pop(a)
print(sum)
"""


#while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
"""
i = 5
while i > 0:
    print("*" *i)
    i = i-1


i = 4
j = 0

while i >0 :
    print(" "*j+"*"*(2*i-1))
    i= i-1
    j= j+1
"""


#다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.

"""
num = 11
snum = str(num)
a = snum.count("0")
b = snum.count("1")
c = snum.count("2")
d = snum.count("3")
e = snum.count("4")
f = snum.count("5")
g = snum.count("6")
h = snum.count("7")
i = snum.count("8")
j = snum.count("9")
print("0 1 2 3 4 5 6 7 8 9")
print(a,b,c,d,e,f,g,h,i,j)
"""

#for문 별만들기
"""
j=4
for i in range(1,6):
    print(" "*j + "*"*i)
    j=j-1
"""
#10->2진수 변환
"""
num = 9
binum = str(bin(num))
print(binum[2:])
"""


#다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
#그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
"""
word = str(input())
def pal(word):
    return word[::-1]

print(pal(word))
if pal(word) == word:
    print("입력하신 단어는 회문(Palindrome)입니다.")
"""

#사용자 2명, 가위바위보
#가위바위보 함수 이용 승패 결과 값 출력
"""
p1 = input()
p2 = input()
p1p = input()
p2p = input()

def RCP(p1p,p2p):
    if p1p == p2p:
        return "비겼습니다!"
    elif (p1p=="가위" and p2p=="바위") or (p1p == "바위" and p2p == "가위"):
        return "바위가 이겼습니다!"
    elif (p1p=="가위" and p2p=="보") or (p1p == "보" and p2p == "가위"):
        return "가위가 이겼습니다!"
    elif (p1p == "바위" and p2p == "보") or (p1p == "보" and p2p == "바위"):
        return "보가 이겼습니다!"

print(RCP(p1p,p2p))
"""


#소수 검사 함수
#출력값
"""
num = int(input())
list1 =[]
def decimal(num):
    for i in range(1, num + 1):
        if num % i == 0:
            list1.append(i)
    if len(list1)==2:
        return "소수입니다"
    else:
        return "소수가 아닙니다."

print(decimal(num))
"""


#피보나치
"""
num = int(input())
Fibolist = [1,1]
def FiboNum(num):
    for i in range(2,num):
        Fibolist.append(Fibolist[i-1]+Fibolist[i-2])
    return Fibolist
print(FiboNum(num))
"""

#리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고
#이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하십시오.
"""
lst = [1, 2, 3, 4, 3, 2, 1]
print(lst)
def listdel(lst):
    i=0
    while i <len(lst):
        if lst.count(lst[i]) > 1:
            lst.remove(lst[i])
        else:
            i = i+1
    nlst = sorted(lst)
    return nlst

print(listdel(lst))
"""


#정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
#이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.
"""
list1 = [2,4,6,8,10]

def listf(listname,num):
    if listname.count(num) >0:
        return True
    else:
        return False

print(list1)
print("{0} => {1}".format(5,listf(list1,5)))
print("{0} => {1}".format(10,listf(list1,10)))
"""

#팩토리얼 구하는 함수, 입력숫자 팩토리얼값구하기
"""
def facto(num):
    i = 1
    fac = 1
    while i <= num:
        fac = fac*i
        i = i+1
    return fac

print(facto(5))
"""

#제곱함수
"""
def square(num):
    return num**2

a = str(input())
print("square({0}) => {1}".format(a[0],square(int(a[0]))))
print("square({0}) => {1}".format(a[3],square(int(a[3]))))
"""

#아스키코드값 입력받아 문자를 확인하는 코드
"""
code = input()

def transascii(word):
    print("ASCII {0} => {1}".format(code,chr(code)))
"""


#49차시, 1~10정수 리스트 객체에서 filter,람다식 이용해 짝수만 리스트로 반환
"""
list1 = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda x: x%2==0,list1)))

# 1~10 정수 리스트, map(), lambda 사용, 항목의 제곱값 갖는 리스트 반환
list1 = [1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda x: x**2, list1)))

"""

#1~10 정수, filter, lambda,
#짝수만 선택, map ,lambda 항목의 제곱값 반환


"""
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list(filter(lambda x: x%2==0,list1))
print(list(map(lambda x: x**2, list2)))
"""

# 가변형인자, 가장 큰 값 반환 정의
"""
a = 3,5,4,1,8,10,2

def maxnum(*args):
    list(args)
    return max(args)

print("max(3, 5, 4, 1, 8, 10, 2) => {0}".format(maxnum(*a)))
"""

#abcdef문자열의 각각문자가 키, 0~5사이의 정수를 값으로하는 딕셔너리 객체생성
#키와 값 정보 출력하는 프로그램 작성
"""
keys = 'abcdef'
values = 0,1,2,3,4,5
dic = {}
for i in range(0, 6):
    dic[keys[i]] = values[i]
for i in range(0,6):
    print("{0}: {1}".format(keys[i],values[i]))
"""

# 가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고,
# 단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.
"""
a= input()

def multi_num(*num):
    result = 1
    for i in num:
        if type(i) != type(str(i)):
            result = result * int(i)
        elif type(i) == type(str(i)):
            raise ValueError  ### error 상황 발생시 raise로 강제 예외 상황 발생, 예외로 빼내기
    return result

try:
    print(multi_num(*a))
except ValueError: #ValueError 발생
    print("에러발생")
"""