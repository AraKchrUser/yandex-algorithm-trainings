def lbinsearch(w, h, n):

    l, r = 0, min(w * n, h * n)

    while l < r:
        m = (l + r) // 2
        if (m // w) * (m // h) >= n:
            r = m
        else:
            l = m + 1

    return l


if __name__ == '__main__':
    w, h, n = list(map(int, input().split()))
    print(lbinsearch(w, h, n))
