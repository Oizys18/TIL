# 10개 수 입력받아 평균값 출력 
for i in range(int(input())):
    print(f"#{i+1} {round(sum(list(map(int,input().split())))/10)}")