#SWEA 1966. 숫자 정렬
for t in range(int(input())):
    l = int(input())
    n = list(map(int,input().split()))
    for i in range(l-1,0,-1):
        for j in range(0,i):
            if n[j] > n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
    print(f"#{t+1} ",end='')
    for k in n:
        print(f'{k}',end=' ')
    print('')


# ver 2 
for t in range(int(input())):
    l = int(input())
    n = list(map(int,input().split()))
    for i in range(l-1,0,-1):
        for j in range(0,i):
            if n[j] > n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
    print(f"#{t+1} ",end='')
    for k in n:
        print(f'{k}',end=' ')
    print('')