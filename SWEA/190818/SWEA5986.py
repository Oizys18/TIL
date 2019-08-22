# SWEA 5986 소수
# 홀수를 세 소수의 합으로 나타낼 수 있는 경우의 수를 구하기 
# N = x + y + z 
# import sys
# sys.stdin = open("input.txt", 'r')
def sosu(N):
    if N < 2:
        return False
    # 소수 조건 넣기 
    if N == 2:
        return True
    if N % 2 == 0:
        return False
    squareRootN = round(N ** 0.5) +1
    for i in range(3,squareRootN,2):
        if N % i == 0:
            return False
    return True

# for T in range(int(input())):
#     N = int(input())
#     sosuL = [x for x in range(1, N+1) if sosu(x)]
#     temp = []
#     cnt = 0
#     for i in range(len(sosuL)):
#         for j in range(i,len(sosuL)):
#             for k in range(j,len(sosuL)):
#                 if sosuL[i]+ sosuL[j] + sosuL[k] == N:
#                     cnt += 1 
#     print("#{0} {1}".format(T+1,cnt))

    
print([x for x in range(1, 50000) if sosu(x)])