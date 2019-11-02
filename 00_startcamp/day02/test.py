"""
코딩 예제 1

"""

# 1. problem.txt 파일 생성 후, 다음과 같은 내용 작성
0
1
2
3

with open('problem.txt','w') as f:
    for i in range(0,4):
        f.write(str(i)+"\n")


# 2. problem.txt의 파일 내용을 다음과 같이 변경 
3
2
1
0

with open('problem.txt','w') as f:
    for i in range(0,4):
        f.write(str(3-i)+"\n")


# 3. `reverse.txt`라는 파일에 `problem.txt` 파일의 내용물을 
# 다시 다음과 같은 역순으로 바꾸는 코드를 작성 
# (조건 : writelines() 함수(메소드)를 활용 / reverse() 메소드 활용)  

with open('problem.txt','r') as f:
    lines = f.readlines()
    lines.reverse()
    with open('reverse.txt','w') as e:
        e.writelines(lines)    

