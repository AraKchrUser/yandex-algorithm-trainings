def binsearch(n, a, b, w, h):
    l, r = 0, min(w, h)

    while l < r:
        m = (l + r + 1) // 2
        if (w // (a + 2 * m)) * (h // (b + 2 * m)) >= n or (h // (a + 2 * m)) * (w // (b + 2 * m)) >= n:
            l = m
        else:
            r = m - 1

    return l


if __name__ == '__main__':
    n, a, b, w, h = list(map(int, input().split()))
    res = binsearch(n, a, b, w, h)
    print(res)
