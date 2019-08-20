#SWEA 6019
import sys
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    D,A,B,F = map(int,input().split())
    t= A+B

    time = D/t
    result = 20 * time
    print("#{0} {1}".format(T+1, result))
