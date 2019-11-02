
"""
',' 구분 숫자Input -> 홀수값을 ','구분 출력
리스트 내포 기능을 이용한 프로그램
"""

# a = '1, 2, 3, 4, 5'
# a = a.split(', ')
# b = []
# for i in a:
#     b.append(int(i))

# for j in b:
#     if j %2 !=0 and j != 5:
#         print(f'{j}, ',end='')
#     elif j == 5:
#         print(str(j))



"""
주어진 튜플 앞 뒤 절반씩 나눠 출력
"""
# a = (1,2,3,4,5,6,7,8,9,10)
# print(a[0:5])
# print(a[5:])

"""
리스트 내포 기능을 이용해 [5, 6, 77, 45, 22, 12, 24]에서 
짝수를 제거한 후 리스트를출력하는 프로그램을 작성하십시오.
"""
# TheList = [5, 6, 77, 45, 22, 12, 24]
# for num in TheList:
#     if num % 2 == 0:
#         TheList.remove(num) #오류발생, 12 삭제 X 
#         print(num)

# @app.route("/lotto/<num>")
# def lotto(num):
#     NumList = range(1,46)
#     NumRes = random.choices(NumList,k=6)
#     for i in NumRes:
#         result = result + str(i) + ' '
#     return result
import random

def menu():
    #랜덤으로 음식 메뉴 추천, 
    #해당 음식 사진 보여주는 기능 구현
    MenuList = {'순두부','제육','오삼'}
    MenuName = random.choice(MenuList)
    return MenuName

menu()
