# SWEA3316.py
"""
ABCD -> N일 간의 활동일정  -> 참여 or 불참
but 모두 불참 경우의 수는 X 
즉 15

첫째날 열쇠 : A
열쇠를 가진 사람은 내일 활동 무조건 해야함 

N일동안 각 날마다 활동 책임자 : 무조건 활동참여

N일 동안 동아리 활동을 할 수 있는 경우의 수를 출력 


"""


"""
logic 

A : B/C/D 

B : A/C/D

C : A/B/D

... 
D : 0 

1 : A / D  : AD ABD ACD ABCD  -> 첫날은 무조건 4가지 (앞/뒤가 정해지면)
2 : D / B  : DB DAB DCB DACB  -> n날도 무조건 4가지 (앞/뒤가 정해지면)
3 : B      : B BA BC BD BAC BCD BAD  ////마지막 : 뒤에 뭐가 와도 되니까 7가지 
/// BACD: 마지막 맨 앞에 누가 와도 됨
"""
import sys      
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    line = input()
