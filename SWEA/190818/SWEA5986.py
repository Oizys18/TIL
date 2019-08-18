# SWEA 5986 소수
# 홀수를 세 소수의 합으로 나타낼 수 있는 경우의 수를 구하기 
# N = x + y + z 
# import sys
# sys.stdin = open("input.txt", 'r')
sosuL = []
temp = []
for sosu in range(1,999):
    for n in range(1,sosu):
        if sosu % n != 0:
            temp.append(sosu)
        if sosu % n == 0: 
            temp = []
    sosuL += temp

print(sosuL)

# for T in range(int(input())):
#     N = int(input())
#     oddL = [i for i in range(1,N,2)]
#     print(oddL)
    # n = len(oddL)
    # for j in range(1<<n):
    #     for k in range(n+1):
    #         if j & (1<<k):

    #             print(oddL[k], end=", ")
    #     print()
    # print()    
