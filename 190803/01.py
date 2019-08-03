# SWEA 2007 패턴마디의 길이
# 테스트 케이스 T회 반복 
# 문자열의 최대 길이는 10 
# 각 문자열의 길이는 30
# str으로 받아서 하나씩 비교하기 ?

# import sys
# sys.stdin = open('input.txt',mode='r')

for t in range(int(input())):
    a = ''
    words = input()
    for i in range(0,30):
        if words[i] in a and a == words[i:i+len(a)]:
            print(f"#{t+1} {len(a)}")
        else: 
            a += words[i]
            temp = words[i:]