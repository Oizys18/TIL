# Algo 
# Delta 
# 2차 배열 탐색

import sys
sys.stdin = open('input.txt', 'r')
oriMat = []
resMat = [[0]*5 for i in range(5)]
for i in range(5):
    oriMat.append(list(map(int,(input().split()))))

print(oriMat)
# print(resMat)

cur_x = 0
cur_y = 0
# def isWall(a):
#   len(a) = 5 (0~4)
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
dx = 1
dy = 0
# print(len(oriMat))
# print(len(oriMat[0]))
for y in range(len(oriMat)): # 0 1 2 3 4 
    for x in range(len(oriMat[y])): # 0 1 2 3 4
        # print(x)
        # print(dx,dy)
        cur_x = cur_x + dx
        cur_y = cur_y + dy
        # print(cur_x, cur_y)
        # print(cur_x,cur_y)
        print(oriMat[cur_y][cur_x]) # 
        if cur_x == len(oriMat[y])-1 and cur_y == len(oriMat)-1:
            dx = -1
            dy = 0
            # print('hi',dx,dy)
            continue
        if cur_x == 0 and cur_y == len(oriMat)-1:
            dx = 0
            dy = -1
        if cur_x == len(oriMat[y])-1:
            dy = 1 
            dx = 0

        #     continue
        # if x == len(oriMat)-1 and y == len(oriMat[x])-1:
        #     dx = -1
        #     dy = 0 
        #     continue
        # if x == 0 and y == len(oriMat)-1:
        #     dx = 0
        #     dy = -1
        #     continue
        
        # if x == len(oriMat[y])-1:
        #     dy = 1
        #     dx = 0
        


# def move(a):
