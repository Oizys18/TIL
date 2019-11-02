# Algo 
# Delta 
# 2차 배열 탐색

import sys
sys.stdin = open('input.txt', 'r')

for m in range(int(input())):
    N = int(input())
    oriMat = []
    resMat = [[0]*N for i in range(N)]
    for i in range(N):
        oriMat.append(list(map(int,(input().split()))))

    def miniSelect(a):
        mini = a[0][0]
        m_i,m_j = 0, 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] < mini:
                    mini = a[i][j]
                    m_i, m_j = i, j 
        return mini, m_i, m_j

    def isWall(a,x,y,cur_dr):
        dx,dy = Move(cur_dr)
        if x+dx > len(a)-1 or y +dy > len(a)-1:
            return True
        else: 
            if a[y+dy][x+dx] != 0: return True
            else: return False

    def Move(cur_dr):
        dr = [(1,0),(0,1),(-1,0),(0,-1)]
        return dr[cur_dr]

    def printIt(a):
        for i in range(len(a)):
            print(a[i])

    #현재 x,y좌표, 현재 방향 
    cur_x,cur_y,cur_dr = 0, 0, 0
    for y in range(len(oriMat)): 
        for x in range(len(oriMat[y])): 
            #시작점 (0,0) 인쇄
            if x == 0 and y == 0:
                mini = miniSelect(oriMat)
                resMat[cur_y][cur_x] = mini[0]
                oriMat[mini[1]][mini[2]] = 99
                continue
            # 만약 다음 경로에 이미 숫자가 들어있거나 범위를 벗어날 경우
            if isWall(resMat,cur_x,cur_y,cur_dr):
                if cur_dr == 3:
                    cur_dr = 0
                else: 
                    cur_dr += 1
            dx,dy = Move(cur_dr)
            cur_x += dx
            cur_y += dy
            mini = miniSelect(oriMat)
            resMat[cur_y][cur_x] = mini[0]
            oriMat[mini[1]][mini[2]] = 99
    printIt(resMat)

