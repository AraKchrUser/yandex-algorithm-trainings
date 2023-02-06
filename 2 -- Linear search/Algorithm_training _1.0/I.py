n, m, k = list(map(int, input().split()))
field = [[0]*m for _ in range(n)]
for _ in range(k):
    i, j = list(map(int, input().split()))
    field[i - 1][j - 1] = '*'

for i in range(n):
    for j in range(m):
        if field[i][j] == '*':
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    if ((i + ii) in range(0, n)) and ((j + jj) in range(0, m)) and field[i + ii][j + jj] != '*':
                        field[i + ii][j + jj] += 1

for row in field:
    for item in row:
        print(item, end=' ')
    print()
