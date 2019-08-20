# SWEA5549.py
# 홀수 짝수 판별 프로그램

import sys
sys.stdin = open('input.txt','r')


for T in range(int(input())):
    N = int(input())
    if N%2:print("#{0} Odd".format(T+1))
    else:print("#{0} Even".format(T+1))

