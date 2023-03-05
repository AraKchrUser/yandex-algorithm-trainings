def func(a, b, n, m):
    min1 = (n - 1) * a + n
    min2 = (m - 1) * b + m

    max1 = (n + 1) * a + n
    max2 = (m + 1) * b + m

    if max1 < min2 or min1 > max2:
        return -1

    return max(min1, min2), min(max1, max2)


a = int(input())
b = int(input())
n = int(input())
m = int(input())

ans = func(a, b, n, m)
if ans != -1:
    print(*ans)
else:
    print(-1)
