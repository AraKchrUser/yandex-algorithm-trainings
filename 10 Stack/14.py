n = int(input())
carriages = [*map(int, input().split())]
order = range(1, n + 1)
stack = []
i = 0
for carriage in order:
    if stack and stack[-1] == carriage:
        stack.pop()
        continue
    while i < n and carriages[i] != carriage:
        stack.append(carriages[i])
        i += 1
    i += 1
if stack:
    print('NO')
else:
    print('YES')
