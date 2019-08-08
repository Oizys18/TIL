# SWEA 1215 Palindrome
import sys
sys.stdin = open('input.txt','r')

for t in range(10):
    matrix = []
    N = int(input())
    for i in range(8):
        matrix.append(input())
    cnt = 0 
    for j in matrix:
        for k in range(8-N+1):
            word = j[0+k:N+k]
            if word == word[::-1]:
                cnt += 1
    for l in list(zip(*matrix)):
        for m in range(8-N+1):
            word = l[0+m:N+m]
            if word == word[::-1]:
                cnt += 1
    print("#{0} {1}".format(t+1,cnt))
