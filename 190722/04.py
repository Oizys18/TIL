# 중간값 프로그램 
# 입력 : n개의 정수
# 출력 : 중간값 

n = int(input())
nl = input().split(' ')
li = []
for i in nl:
    li.append(int(i))    
li = sorted(li)
print(divmod(5,2))
print(li[divmod(n,2)])
