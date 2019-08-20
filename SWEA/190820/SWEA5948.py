#SWEA5948
# 서로다른 7개의 정수 중 3개의 합으로 수를 구하기 
# 3개의 합으로 수를 만든 후 5번째로 큰 수를 구하기 

# 테스트 케이스만큼 반복
# 7개의 정수 int해서 list로 받기 
# 3개씩 골라서 합하기  -> 리스트로 저장 
# sort 
# 5번째 선택 
# 출력 

import sys
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    N = list(map(int,input().split()))
    result = []
    for i in range(len(N)):
        for j in range(i+1,len(N)):
            for k in range(j+1,len(N)):
                result.append(N[i]+N[j]+N[k])
    result = sorted(set(result))
    print("#{0} {1}".format(T+1,result[len(result)-5]))
    # print(result[4])
    # print(sorted(result)[4])
