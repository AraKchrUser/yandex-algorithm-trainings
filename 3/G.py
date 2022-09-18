n = int(input())
lst = []
for _ in range(n):
    lst.append(tuple(map(int, input().split())))
lst = set(lst)
summ = 0
for i, j in lst:
    if i + j == n - 1 and i >= 0 and j >= 0:
        summ += 1
print(summ)
