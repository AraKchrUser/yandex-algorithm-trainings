n = int(input())
average_cost = [[v, i, -1] for i, v in enumerate(map(int, input().split()))]
stack = []
ans = []
for item in average_cost:
    while stack and stack[-1][0] > item[0]:
        city = stack.pop()
        city[-1] = item[1]
        ans.append(city)
    else:
        stack.append(item)
ans += stack
ans.sort(key=lambda x: x[1])
print(' '.join([str(item[-1]) for item in ans]))
