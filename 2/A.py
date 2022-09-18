lst = list(map(int, input().split()))
flag = True
for i in range(1, len(lst)):
    if lst[i - 1] >= lst[i]:
        flag = False
        break
print('YES' if flag else 'NO')
