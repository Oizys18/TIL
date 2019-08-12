# SWEA 7675 통역사 성경이
"""
1. T = testcase
2. N = 문장의 갯수 
3. list(문장.split(' .?!')) :: 공백, .?! 구두점 
3-1 list 중 대문자로 시작하는 단어 찾기 (element[0] isupper==True) 
3-2 


>> 
for * T
    N = int(input()) : N 문장갯수 받기 
    input() 문장받기 : 구두점별로 나눠서 넣기 
    for * N : 리스트의 N번째 문장에서, 
        count = 0
        첫글자가 대문자로 시작하는 단어 찾기 -> 첫글자 빼고 리스트에 추가 
    판별리스트에서 모든 글자가 isalpha, islower True면 count+=1 
        count 출력, end=' '
"""


for T in range(int(input())):
    N = int(input())
    talk = input().split('.?!')
    count = 0
    for i in range(N):
        word_li = []
        if talk[i][0].isupper == True:
            word_li.append(talk[i][1:])
    for j in word_li:
        for k in j:
            if not k.isalpha or k.isupper:
                word_li.remove(j)
                count += 1 
    print("#{0} {1}".format(T+1,count))
