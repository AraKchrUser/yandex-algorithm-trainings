def bsearch(N, x, y):
    l, r = 0, min(x, y) * (N - 1)

    while l < r:
        m = (l + r) // 2
        if m // x + m // y >= N - 1:
            r = m
        else:
            l = m + 1

    return l + min(x, y)


if __name__ == "__main__":
    N, x, y = list(map(int, input().split()))
    print(bsearch(N, x, y))
