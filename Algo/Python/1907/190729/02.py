# SW.EA D2 1986. 지그재그 숫자
# 1~N의 숫자 중 홀수는 더하고 짝수는 뺏을 때 최종누적값 

for i in range(int(input())):
    N = int(input())
    print(f"#{i+1} {sum([-x if x%2==0 else x if x%2 else 0 for x in range(1,N+1)])}")

