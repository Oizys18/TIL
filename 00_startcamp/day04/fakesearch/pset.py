'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1-1 ====')
# result = 0 
# for i in score:
#     result += score[i] 
# print(result)

# 쌤
print(sum(score.values())/len(score.values()))

# 2. 반 평균을 구하시오. -> 전체 평균(a&b반 각각)
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2-1 ====')
#쌤

for i in scores:
    print(sum(scores[i].values())/len(list(scores[i].values())))

print(sum(scores['a'].values()) / len(scores['b'].values()))

#나
# resulta=0
# resultb=0
# for i in scores:
#     if i == 'a':
#         for j in scores[i]:
#             resulta = resulta + scores[i][j]
#         resulta = resulta / len(list(scores[i].keys()))
#     else:
#         for j in scores[i]:
#             resultb = resultb + scores[i][j]
#         resultb = resultb / len(list(scores[i].keys()))
# print(f'a반평균 : {resulta}, b반평균 :{resultb}')



# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
# CT = []
# for i in city:
#     # i : 딕셔너리 keys
#     num = 0
#     for j in city[i]: 
#        num = num + j
#     num = num / len(city[i])
#     CT.append(num)
# print(CT)
print('==== Q3-1 ====')
#쌤
for temp in city.values():
    print(sum(temp)/len(temp))

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
#쌤

# 이런 방법 있음 
# numpy 등의 외장함수 나중에 사용 
maxes = []
mins = []

for temp in city.values():
    maxes.append(max(temp))
    mins.append(min(temp))

high = max(maxes)
low = min(mins)

for key, values in city.items():
    if high in values:
        print(key)

for key, values in city.items():
    if low in values:
        print(key)

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
print(2 in city['서울'])
