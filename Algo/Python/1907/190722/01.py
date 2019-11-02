# 알파벳을 숫자로 변환 

#딕셔너리 사용 
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphaDic = {}
for i in range(1,27):
    alphaDic[alpha[i-1]] = i

alin = input()
for bet in alin:
    print(alphaDic[bet],end=' ')

#ord() 사용하는 방법
a= input()
for i in a:
    print(ord(i)-64,end=' ')

