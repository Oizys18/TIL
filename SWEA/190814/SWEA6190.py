# #SWEA 6190
import sys
sys.stdin = open('input.txt','r')
#     # 1. list <- Ai * Aj 
#     # 2. danjo ?? 
#     # 2-2 result = -1
#     # 3. if danjo: result <- danjo 
#     # 4.    다음 danjo가 result 보다 크면 danjo에 저장 
#     # 5. result 출력 


for T in range(int(input())):
    N = int(input())
    case = list(map(int,input().split()))
    result = -1
    for i in range(N-1,1,-1):
        for j in range(i-1,0,-1):
            number = case[i] * case[j]

    
            if number > result:
                set_num = list(set(str(number)))
                if set_num == sorted(set_num):
                    if str(number) == ''.join(sorted(str(number))):
                        result = number

                # for w in range(len(str(number))-1):
                #     if str(number)[w] > str(number)[w+1]:
                #         danjo = 0
                # if danjo:
                #     result = number
    print("#{0} {1}".format(T+1,result))


# 2 
    # for i in range(N-1,0,-1):
    #     for j in range(i-1,0,-1):
    #         number = str(case[i] * case[j])
    #         if number == ''.join(sorted(list(number))):
    #             result = number
    #             break
    # print("#{0} {1}".format(T+1,result))

# # 3
    # for l in range(N-1):
    #     number = str(case[l] * case[l+1])
    #     if int(number) > result:
    #         for m in range(len(number)-1):
    #             if int(number[m]) >= int(number[m+1]):
    #                 danjo = 0
    #                 continue
    #         if danjo:
    #             result = int(number)
    #         # if number == int(''.join(sorted(list(str(number))))):
    # print("#{0} {1}".format(T+1,result))


#     for l in range(N-1):
#         number = case[l] * case[l+1]
# a = '12341'
# b = sorted(a)
# print(b)

# for T in range(int(input())):
#     N = int(input())
#     case = list(map(int,input().split()))
#     result = -1
#     for l in range(N,1,-1):
#         number = case[l] * case[l-1]
#         if number > result:
#             if number == int(''.join(sorted(str(number)))):
#                 result = number
#     print("#{0} {1}".format(T+1,result))

