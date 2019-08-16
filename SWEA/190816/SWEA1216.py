#SWEA 1216

import sys
sys.stdin = open('input.txt','r')

#1 회문검사 : 반으로 나눠서 앞뒤비교 
#2 zip 안쓰기
#3 회문발견시 break 

def palin(word, wl):
    for a in range(wl//2):
        if word[a] != word[wl-1-a]:
            return False
    return True

def rotate(mat):
    rotMat = [''.join([mat[j][i] for j in range(len(mat))]) for i in range(len(mat))]
    return rotMat

def maxP(mat1,mat2,wl):
    for idx in range(100):
        for pos in range(101-wl):
            word1 = mat1[idx][pos:pos+wl]
            word2 = mat2[idx][pos:pos+wl]
            if palin(word2,wl):
                return  len(word2)
            if palin(word1,wl):
                return  len(word1)
    return False


for case in range(10):
    matrix = []
    input()
    result = 0
    for _ in range(100):
        matrix.append(input())
    rotMat = rotate(matrix)

    for wl in range(100,1,-1):
        result = maxP(matrix,rotMat,wl)
        if result:
            break
            
    print("#{0} {1}".format(case+1,result))


