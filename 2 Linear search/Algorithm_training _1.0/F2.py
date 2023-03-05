# Решить перебором

n = int(input())
array = list(map(int, input().split()))
s = 0
while array != array[::-1]:
    array.insert(n, array[s])
    s += 1
print(s)
if s != 0:
    print(*array[-s:])
