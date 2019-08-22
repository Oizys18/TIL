# array의 부분집합의 합이 0인 경우를 모두 찾아내는 코드 
# 유용

arr = [1,-1,2,-5,3,6]
cnt = 0

# << 비트연산 
# 1<<n : 2^^n 부분집합 갯수
for i in range(1, 1 << len(arr)):
    k = []
    for j in range(len(arr)):
        if i & (1 << j):
            k.append(arr[j])
    if sum(k) ==0:
        cnt += 1
        print(cnt, k)