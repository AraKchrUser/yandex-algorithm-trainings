def calc(n, k, m):
    iter1 = p = n
    iter2 = k
    s = 0
    if k // m == 0:
        return 0
    while p >= k:
        iter1 = p
        iter1 //= k
        p %= k
        s += k // m * iter1
        p += k % m * iter1
    return s


n, k, m = list(map(int, input().split()))
print(calc(n, k, m))
