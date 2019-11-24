# Algorithm 

 https://velog.io/@doontagi 

# Problem Solving

1. Brute force
2. 분할 정복
3. 동적계획법 DP 
4. 그래프

# Sample Code - Preset

- Python sample code 

## Bit

- 비트 체크를 통해 

- 부분집합 구하기 

```python
# array의 부분집합의 합이 0인 경우를 모두 찾아내는 코드 
# 유용

arr = [1,-1,2,-5,3,6]
cnt = 0

# << 비트연산 
# 1<<n : 2^^n 부분집합 갯수
for i in range(1, 1 << len(arr)):
    k = []
    for j in range(len(arr)):
        if i & (1 << j):
            k.append(arr[j])
    if sum(k) ==0:
        cnt += 1
        print(cnt, k)
```



## Combination / Permutation

## DFS / BFS 

```python
edges = {
    1:[2,3,4],
    2:[5,6],
    3:[7],
    4:[8],
    5:[9],
    6:[10],
    7:[],
    8:[],
    9:[],
    10:[11],
    11:[],
}

def DFS(node):
    if len(edges[node]) == 0:
        print(visit)
        return
    else:
        for i in edges[node]:
            visit.append(i)
            DFS(i)
            visit.pop()

for i in edges.keys():
    visit = [i]
    DFS(i)
    
```

## DisjointSets

## Dijkstra

## Prim

## Kruskal

