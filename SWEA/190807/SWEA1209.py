# SWEA 1209

for i in range(10):
    input()
    mat = []
    k1 = k2 = 0
    for j in range(100):
        mat.append(list(map(int, input().split())))
    col = list(map(sum, zip(*mat)))
    row = list(map(sum, mat))
    for k in range(100):
        k1 += mat[k][k]
        k2 += mat[k][99-k]

    print(max(max(row), max(col), k1, k2))