# 10개 수 입력, 가장 큰 수 출력 
# 내 코드 ㅠ 
T = int(input())
t1 = input().split(' ')
t2 = input().split(' ')
t3 = input().split(' ')
tl = [t1,t2,t3]
rl = [[],[],[]]
for i in range(0,3):
    for j in tl[i]:
        rl[i].append(int(j))

for i in range(0,T):
    print(f'#{i+1} ',end='')
    print(max(rl[i]))

# 코드 길이 짧은 것 

# 나랑 다른 점 : 
# 1. map() 함수로 int()와 max()를 반복
# 2. int(input())을 range로 받아서 반복횟수 조절 
for i in range(int(input())):
    print(f'#{i+1} {max(map(int,input().split()))}')

