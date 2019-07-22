# 하나의 자연수를 입력받아 각 자릿수의 합을 계산하는 프로그램
# 입력 : 자연수 N, 1 =< N =< 9999
# 출력 : 각 자릿수의 합

n = input()
nl = []
for i in n:
    nl.append(int(i))
print(sum(nl))
