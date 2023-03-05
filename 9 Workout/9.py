n, m, k = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for idx, item in enumerate(map(int, input().split())):
        matrix[i][idx] = item
prefix = [[0] * m for _ in range(n)]
prefix[0][0] = matrix[0][0]
for i in range(1, m):
    prefix[0][i] = prefix[0][i - 1] + matrix[0][i]
for i in range(1, n):
    prefix[i][0] = prefix[i - 1][0] + matrix[i][0]
for i in range(1, n):
    for j in range(1, m):
        prefix[i][j] = prefix[i][j - 1] + \
                       prefix[i - 1][j] - prefix[i - 1][j - 1] + matrix[i][j]
for _ in range(k):
    x_1, y_1, x_2, y_2 = map(lambda x: int(x) - 1, input().split())
    print(prefix[x_2][y_2] -
          (prefix[x_1 - 1][y_2] if x_1 else 0) -
          (prefix[x_2][y_1 - 1] if y_1 else 0) +
          (prefix[x_1 - 1][y_1 - 1] if x_1 and y_1 else 0))
