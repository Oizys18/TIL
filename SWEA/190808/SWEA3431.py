# SWEA 3431
# 운동하는 준환이 

for T in range(int(input())):
    L,U,X = map(int,input().split())
    if X < L: 
        result = L-X 
    elif X > L:
        if X < U : 
            result = 0
        else:
            result = -1
    print("#{0} {1}".format(T+1,result))
    