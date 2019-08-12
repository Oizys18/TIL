# SWEA7728 다양성 측정
# 파이썬 문제가 아니라서 체크 못함 


for T in range(int(input())):
    word = input()
    set_w = set([int(w) for w in word])
    print("#{0} {1}".format(T+1,len(set_w)))

