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
import sys
import re
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    N = int(input())
    talk = re.split('[.?!]',input())[0:N]
    print("#{0}".format(T+1),end=' ')
    for i in talk:
        cnt = 0
        for j in i.split():
            if j[0].isupper() and j.isalpha():
                if len(j)==1:
                    cnt += 1
                if j[1:].islower():
                    cnt += 1
        print(cnt, end=' ')
    print('')