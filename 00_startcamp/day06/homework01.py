# #1 
# import keyword
# print(keyword.kwlist)

# #2 
# import math
# a = 0.1 *3
# b = 0.3
# print(math.isclose(a,b))

# #3
# print('\\n은\n줄바꿈입니다')
# print('\\t는\t탭입니다.')
# print('\\는 \\입니다.')

# #4
# name = "철수"
# print(f'안녕, {name}야')

# #5
# 5

# n=5
# m=9

# print(('*'*n + '\n')*m)
# print('"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'')



#2차 방정식 
"""
import math
Line = str(input())

def CF(x):
    text_split = x.split('+' or '-')
    if text_split[0][0] != 'x':
        a = int(text_split[0][0])
        print(f'a={a}')
    else:
        a = 1
        print(f'a={a}')
    if text_split[1][0] != 'x':
        b = int(text_split[1][0])
        print(f'b={b}')
    else:
        b = 1
        print(f'b={b}')
    c = int(text_split[2])
    print(f'c={c}')

    if (b**2 - 4*a*c) < 0:
        x1 = complex(-b/2, math.sqrt(abs(b**2 - 4*a*c))/(2*a))
        x2 = complex(-b/2, -math.sqrt(abs(b**2 - 4*a*c))/(2*a))
    else :
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

    return (x1,x2)
print(CF(Line))
"""

# m = 9
# n = 5
# for j in range(0,9):
#     for i in range (0,5):
#         print('*',end='')
#     print('')
    

