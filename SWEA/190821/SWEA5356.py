# SWEA 5356

# 'A'~'Z'
# 'a'~'z'
# '0'~'9'

import sys
sys.stdin = open('input.txt','r')

# 축약
for T in range(int(input())):
    li = [list(input()) for _ in range(5)]
    a = max(map(len,li))
    for r in li:
        while len(r) < a:
            r.append('')
    re = ''.join([li[x][y] for y in range(a) for x in range(len(li))])
    print("#{0} {1}".format(T+1,re))



# # 첫 풀이
# for T in range(int(input())):
#     line = [list(input()) for _ in range(5)]
#     big = max([len(st) for st in line])
#     for r in line:
#         while len(r) < big:
#             r.append('@')

#     result = []
#     for y in range(big):
#         for x in range(len(line)):
#             result.append(line[x][y])
#     result = ''.join(result).replace('@','')
#     print("#{0} {1}".format(T+1,result))