# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램
# 0 =< a,b =< 10000

# for i in range(int(input())):
#     print(f'#{i+1}',end=' ')
#     a = list(map(int,input().split(' '))) 
#     if a[0] > a[1]:
#         print('>')
#     elif a[0] < a[1]:
#         print('<')
#     elif a[0] == a[1]:
#         print('=')

for i in range(int(input())):
    a, b = map(int,input().split(' '))
    print(f"#{i+1} {a>b and '>' or a<b and '<' or '='}")
