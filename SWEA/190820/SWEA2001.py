#SWEA2001
# NxN배열, 각 칸은 파리 수 
# MxM 크기의 파리채를 내리쳐 최대한 많은 파리 죽이기 
# 죽은 파리 수 구하기 

# 파리채는 이미 있는 파리 matrix에서, 0,0 부터 N-M+1,N-M+1 까지 돌며 겹친 부분을 더함 
# 각 더한 부분을 리스트에 추가하고 가장 큰 값을 출력 

import sys
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    N,M = map(int,input().split())
    matN = []
    for n in range(N):
        matN.append(list(map(int,input().split())))
    pari = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = []
            for x in range(M):
                for y in range(M):
                    temp.append(matN[i+x][j+y])
            pari.append(sum(temp))
    print("#{0} {1}".format(T+1,max(pari)))
