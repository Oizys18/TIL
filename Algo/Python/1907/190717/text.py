"""
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.
"""

# def solution(x):
#     hap = 0
#     for i in str(x):
#         hap = hap + int(i)
#     print(hap)
#     if x%hap==0:
#         answer = True
#     else:
#         answer = False
#     return answer

# print(solution(18))


"""임의의 정수 n에 대해, n이 어떤 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
n은 1이상, 50000000000000 이하인 정수입니다.
"""
def solution(n):
    answer = 0
    for i in range(1,round(n/2)):
        if i**2 != n :
            answer = -1
            continue
        elif i**2 == n:
            answer = (i+1)**2
            break
    return answer
