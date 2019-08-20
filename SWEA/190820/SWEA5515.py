# #SWEA5515

import sys
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    m, d = map(int,input().split())
    day = [4,5,6,0,1,2,3]
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = 0
    for i in range(m-1):
        date += month[i]
    date += d
    print("#{0} {1}".format(T+1,day[(date%7)-1]))

