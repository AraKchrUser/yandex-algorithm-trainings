a, k, b, m, x = map(int, input().split())
l, r = 0, 10**19
while l < r:
    day = (l + r) // 2
    if (a + b) * day - (day // k * a + day // m * b) >= x:
        r = day
    else:
        l = day + 1
print(l)
