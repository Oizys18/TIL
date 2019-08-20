#SWEA5431

import sys
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    N, K = map(int,input().split())
    sl = [x for x in range(1,N+1)]
    pl = list(map(int,input().split()))
    for p in pl:
        sl.remove(p)
    print("#{0}".format(T+1),end=' ')
    for i in sl:
        print(i,end=' ')
    print()
