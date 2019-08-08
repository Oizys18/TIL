#SWEA 4837
import sys
sys.stdin = open('input2.txt', 'r')
arr = [1,2,3,4,5,6,7,8,9,10,11,12]

for T in range(int(input())):
    N, K = map(int,input().split())
    cnt = 0
    for i in range(1, 1 << len(arr)):
        li = []
        for j in range(len(arr)):
            if i & (1 << j):
                li.append(arr[j])
        if len(li)== N and sum(li) == K:
            cnt += 1
    print("#{0} {1}".format(T+1,cnt))