def binsearch(seq, x, n):
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if seq[m] >= x:
            r = m
        else:
            l = m + 1
    return l


n = int(input())
diegos = sorted(set(map(int, input().split())))
k = int(input())
collects = map(int, input().split())
for collect in collects:
    index = binsearch(diegos, collect, len(diegos))
    print(index)
