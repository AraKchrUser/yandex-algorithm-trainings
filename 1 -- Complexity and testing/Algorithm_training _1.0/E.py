k1, m, k2, p2, n2 = list(map(int, input().split()))
if k2 < m * p2 and p2 != 1:
    n1 = -1
    p1 = -1
elif k2 != 1 and n2 != 1:
    numk = (k2 - 1) // (n2 - 1)
    n1 = (k1 // numk + 1) % m
    p1 = (k1 // numk + 1) // m + 1
else:
    if m != 1:
        n1 = 0
    else:
        n1 = 1
    if abs(k1 - k2) < m:
        p1 = p2
    else:
        p1 = 0
print(p1, n1)
