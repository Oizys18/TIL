import os

# print(os.listdir())
"""
Git Bash, 파일이름 바꾸기
mv 현재파일명 바꿀파일명  

"""

# os함수 이용해 파일명 바꾸기
# os.rename('bye.py','hello.py')
# print(os.listdir())


# os함수 이용해 파일 생성 및 삭제
"""
os.system('ls') #system함수 사용하면 터미널에 사용하는 명령어 바로 사용가능 
os.system('touch a.txt') #a.txt 생성
os.system('rm a.txt') #a.txt 삭제
"""
os.chdir('TestFolder') #파일 실행 디렉토리 변경 

# 파일 100번 반복 생성
# for i in range(200):
    # os.rename(f'samsung_report{i}.txt',f'ssafy_report{i}.txt') # 이름 바꾸기
    #  os.system('touch report{0}.txt'.format(str(i))) #format 함수
""" 
# 다른 방법 1 
files = os.listdir()
for name in files:
    os.rename('samsung_'+name, name)
"""

""" 
# 다른 방법2

files = os.listdir()
for i in files:
    os.rename(i, i.replace('ssafy','samsung'))

"""



#open('파일명','Action')
#파이썬 읽고쓰기 r : read // w : write //a : append

#Write
"""
f = open('ssafy.txt','w')
for i in range(0,5):
    f.write('Hell SsAfY \n')
f.close() #open()하고나서 꼭 close()해야됨 
"""

#Write, with 사용
#그냥 open했을 때 값을 f에저장해준 것과 달리, 
#with에선 as 를 사용해서 코드 사용 중 저장할 곳을 지정 
"""
with open('ssafy.txt','w', encoding='utf-8') as f:
    for i in range(0,5):
        f.write('HeLlO SsAfY 헬 싸 피\n')
"""

#Read
# read() // readlines() 한줄씩 읽기 (리스트화) // 
"""
with open('ssafy.txt', 'r', encoding = 'utf-8') as f:
    result = f.readlines()
    print(result)
"""


