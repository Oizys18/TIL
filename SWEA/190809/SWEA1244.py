#SWEA 1244 최대 상금 
import sys
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    c, turn = input().split()
    turn = int(turn)
    case = [int(num) for num in c]
    print(turn,case)

    cnt = 0 
    for i in range(len(case)):
        min = case[i]
        temp = case[::-1]
        max(temp)

