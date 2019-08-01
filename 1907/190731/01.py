# Algorithm / View

# output
# for i in range(int(input())):
#     T = int(input())
#     gn = list(map(int,(input().split())))
#     result = 0
#     print("#{0} {1}".format(i+1,sum([(gn[i]-max([gn[i-2],gn[i-1],gn[i+1],gn[i+2]])) for i in range(2,len(gn)-2) if max([gn[i-2],gn[i-1],gn[i],gn[i+1],gn[i+2]]) == gn[i]])))

# # i에서 

# for k in range(1,11):
#     T = int(input())
#     result = 0
#     B = list(map(int,input().split()))
#     for i in range(2,T-2):
#         B2 = [B[i-2],B[i-1],B[i+1],B[i+2]]
#         if B[i] > max(B2):
#             result += (B[i] - max(B2))
#     print("#{0} {1}".format(k,result))
#j j j j j 
#    i i i i i i 
#0 0 3 3 2 9 9 6 0 0
# T = 리스트


# def bubbleBig(a):
#     for i in range(len(a)-1,0,-1):
#         for j in range(0,i):
#             if a[j] > a[j+1]:
#                 a[j],a[j+1] = a[j+1],a[j]
#     return a[len(a)-1]

# result = 0
# for num in range(2):
#     length,T = int(input()),list(map(int,(input().split(' '))))
#     for i in range(2,length-3):
#         li = [T[i-2],T[i-1],T[i+1],T[i+2]]
#         if T[i] > bubbleBig(li):
#             result += (T[i]-bubbleBig(li))
#     print("#{0} {1}".format(num+1,result))


def bb(a):
    for i in range(len(a)-1,0,-1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return(a[len(a)-1])

for i in range(1,11):
    length = input()
    a = list(map(int,input().split()))
    result = 0
    for i in range(2,len(a)-2):
        near = [a[i-2],a[i-1],a[i+1],a[i+2]]
        if a[i] > bb(near):
            result += (a[i]-bb(near))
    print("#{0} {1}".format(i,result))
