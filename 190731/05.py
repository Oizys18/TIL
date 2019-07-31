# SWEA 1959 2개 숫자열

for t in range(int(input())):
    N,M = tuple(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if N > M:
        N,M = M,N
        A,B = B,A
    result = [0]*(M-N+1)
    for i in range(N):
        for j in range(M-N+1):
            result[j] += A[i] * B[i+j]
    print(f"#{t+1} {max(result)}")