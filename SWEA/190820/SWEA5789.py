#SWEA5789
# N개의 상자 / 숫자 새길 수 있는데 default는 0 
#  

import sys
sys.stdin = open('input.txt','r')

# T 만큼 반복
# N Q : N길이의 0 리스트 : 
# Q만큼 색칠 반복 
# i 번째 : L:R i로 변경

for T in range(int(input())):
    N, Q = map(int,input().split())
    boxes = [0 for box in range(N)]
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for k in range(L-1,R):
            boxes[k] = i

    print("#{0}".format(T+1),end=' ')
    for x in boxes:
        print('{0}'.format(x),end=' ')
    print()