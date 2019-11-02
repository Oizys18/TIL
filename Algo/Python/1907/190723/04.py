# 10개 수 입력받아 홀수 출력 
for i in range(int(input())):
    print(f"#{i+1} {sum([x for x in list(map(int,input().split())) if x%2!=0])}")