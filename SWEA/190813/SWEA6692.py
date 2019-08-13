# SWEA 6692 다솔쓰 월급상자


"""
T = testcase 
N = case 별 Num 
"""

import sys
sys.stdin = open('input.txt','r')


for T in range(int(input())):
    sum_li = 0
    for n in range(int(input())):
        li = list(map(float,input().split()))
        sum_li += li[0] * li[1]
    print("#{0} {1}".format(T+1,sum_li))