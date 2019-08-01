# my_all(x) 만들기 
"""
def my_all(x):
    for i in x:
        if bool(i) != True :
            return False
    return True
"""

# my_any(x)

"""
def my_any(x):
    for i in x:
        if bool(i) == True:
            return True 
    return False
        
"""

# 소수 찾기 

# 아래에 코드를 작성하세요
"""
numbers = [26, 39, 51, 53, 57, 79, 85]
def my_sosu(numbers):
    insu ={}
    for i in numbers:
        insu[i] = []
        for j in range(1,i+1):
            if i % j == 0:
                insu[i].append(j)
        #소수가 아닐 때
        if len(insu[i]) != 2:
            print(f'{i}는 소수가 아닙니다. {insu[i][1]}는 {i}의 인수입니다.')
        # 소수일 때 
        else:
            print(f'{i}는 소수입니다.')

my_sosu(numbers)
"""


# 최대공약수, 최소공배수 
"""
def gcdlcm(x,y):
    insu ={}
    for i in [x,y]:
        insu[i] = []
        for j in range(1,i+1):
            if i % j == 0:
                insu[i].append(j)
    print(insu)
    insuset = list(set(insu[x]) & set(insu[y]))
    biggest = (insuset[len(insuset)-1])
    smallest = biggest * insu[y][(insu[y].index(biggest)+1)]
    
    return [biggest,smallest]
"""

def a():
    return 3,2
print(a())

