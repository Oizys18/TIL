# SWEA 4843

import sys
sys.stdin = open('input3.txt', 'r')

for num in range(int(input())):
    N = int(input())
    T = list(map(int, input().split()))
    print("#{0}".format(num+1),end=' ')
    for i in range(5):
        print(max(T), end=' ')
        T.remove(max(T))
        print(min(T), end =' ')
        T.remove(min(T))
    print('')

