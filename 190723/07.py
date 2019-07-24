# # N = 양양
# ##

# for i in range(int(input())):
#     cnt = 1
#     N = int(input())
#     li = []
#     while ['0','1','2','3','4','5','6','7','8','9'] not in li:
#         li = list(sorted(set(li + [x for x in str(cnt * N)]))):
#             print(N)
#             break
#         else:
#             cnt += 1
#             continue

# N = 92839829389
# a = list(sorted((set([x for x in str(N)]))))
# print(a)