# 8자리 날짜 입력 -> 날짜 유효하면 YYYY/MM/DD로 출력 
# 유효하지 않으면 -1출력 
from datetime import datetime, date
T = int(input())
t1 = input()
t2 = input()
t3 = input()
t4 = input()
t5 = input()
tc = [t1,t2,t3,t4,t5]
#t3,t4,t5
#.strftime('%Y/%m/%d')
#int(a[0:4]),int(a[4:6]),int(a[6:])
def d(a):
    while True:
        try:
            return (date(int(a[0:4]),int(a[4:6]),int(a[6:])).strftime('%Y/%m/%d'))
        except ValueError:
            return -1
            
for j in range(0,T):
    print(f'#{j+1}',end=' ')
    print(d(tc[j]))
