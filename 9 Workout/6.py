m = int(input())
n = int(input())
sections = []
nsections = n
for _ in range(n):
    a, b = map(int, input().split())
    sections.append([a, b, 0])
for i in range(1, n):
    for j in range(i):
        item_last = sections[j]
        item_curr = sections[i]
        if not item_last[-1]:
            if item_curr[0] > item_last[1] or item_last[0] > item_curr[1]:
                continue
            else:
                item_last[-1] = 1
                nsections -= 1
print(nsections)
