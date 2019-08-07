import sys
sys.stdin = open('input.txt', 'r')


class Snail:

    def __init__(self,x,y):
        self.x, self.y = x, y

    def move(self,dx, dy):
        self.x += dx
        self.y += dy

charlie = Snail(0,0)




# input 값을 5*5행렬로 받는다.
mat = []
for i in range(5):
    mat.append(list(map(int, (input().split()))))

# 값을 저장할 result 배열을 만든다.
result = [[0]*5 for i in range(5)]









print(result)

