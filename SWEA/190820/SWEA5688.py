# SWEA5688

import sys
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    N = int(input())
    n = round(N**(1/3))+1
    result = -1
    for i in range(1,n):
        if i**3 == N:
            result = i
    print("#{0} {1}".format(T+1,result))
    # n = round(N**(1/3))
    # print(n)