n, k = map(int, input().split())
nfibb = [0, 1]
for i in range(n - 2):
    if i < k - 1:
        nfibb.append(sum(nfibb[-k:]) + 1)
    else:
        nfibb.append(sum(nfibb[-k:]))
print(nfibb[-1])
