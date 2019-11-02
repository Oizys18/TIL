# # 최빈수 출력
# y = []
# for i in range(int(input())):
#     k = list(map(int,input()))
#         print(f"#{i+1} {y.append()}")

li=[]
for i in range(int(input())):
    tn = input()
    li = list(map(int,input().split(' ')))
    
    print(f'#{tn} {max(list(set([li.count(i) for i in li])))}')


