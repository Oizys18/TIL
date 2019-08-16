# #SWEA 6190
import sys
sys.stdin = open('input.txt','r')
#     # 1. list <- Ai * Aj 
#     # 2. danjo ?? 
#     # 2-2 result = -1
#     # 3. if danjo: result <- danjo 
#     # 4.    다음 danjo가 result 보다 크면 danjo에 저장 
#     # 5. result 출력 


# 알고리즘 강사님 코드 
def solve1(x):
    str1 = str(x)
    for i in range(len(str1) - 1):
        if str1[i] > str1[i + 1] : return False
    return True
 
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    ans = -1
    for i in range(N - 1):
        for j in range(i + 1, N):
            num = arr[i] * arr[j]
            if solve1(num):
                if ans < num: ans = num
    print("#%d"%tc, ans)

#1 내 코드 ㅠ 쥬륵 
for T in range(1,int(input())+1):
    N = int(input())
    case = list(map(int,input().split()))
    result = -1
    num_li = [case[i] * case[j] for i in range(N) for j in range(i+1,N) ]
    for number in num_li:
        if number%10 ==0:
            continue
        if number > result:
            if str(number) == ''.join(sorted(list(str(number)))):
                result = number
                continue
    print("#{0} {1}".format(T,result))


# for T in range(int(input())):
#     N = int(input())
#     case = list(map(int,input().split()))
#     result = -1
#     # case = sorted(case)
#     num_li = [case[i] * case[j] for i in range(N-1,1,-1) for j in range(i-1,0,-1) ]
#     for number in num_li:
#         if number%10 ==0:
#             continue
#         if number > result:
#             if str(number) == ''.join(sorted(list(str(number)))):
#                 result = number
#                 continue
#     print("#{0} {1}".format(T+1,result))

# for T in range(int(input())):
#     N = int(input())
#     case = list(map(int,input().split()))
#     result = -1
#     for i in range(N-1,0,-1):
#             for j in range(i-1,0,-1):
#                 number = case[i] * case[j]
#                 if str(number) == ''.join(sorted(list(str(number)))):
#                     result = number
#                     continue
#                 # continue
#     print("#{0} {1}".format(T+1,result))

# srtNum = sorted(set(str(number)))
            # if str(srtNum) == ''.join(srtNum):
            # for w in range(len(str(number))-1):
            #     if str(number)[w] > str(number)[w+1]:
            #         result = -1
            #         continue
            #     result = number

# for T in range(int(input())):
#     N = int(input())
#     case = list(map(int,input().split()))
#     result = -1
#     num_li = [case[i] * case[j] for i in range(N-1,1,-1) for j in range(i-1,0,-1) ]
#     for number in num_li:
#         if number > result:
#             # set_num = list(set(str(number)))
#             # if set_num == sorted(set_num):
#             #     print('set_num:{0}'.format(set_num))

#             if number == ''.join(sorted(str(number))):
#                 result = number
#                 continue

                # print("result:{0}".format(result))
        
                # for w in range(len(str(number))-1):
                #     if str(number)[w] > str(number)[w+1]:
                #         danjo = 0
                # if danjo:
                #     result = number
    # print("#{0} {1}".format(T+1,result))


# 2 
    # for i in range(N-1,0,-1):
    #     for j in range(i-1,0,-1):
    #         number = case[i] * case[j]
    #         if number == ''.join(sorted(list(number))):
    #             result = number
            #     continue
            # continue

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

