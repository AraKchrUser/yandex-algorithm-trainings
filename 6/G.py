def binsearch(n, m, t):
    l, r = 0, min(n, m)

    while l < r:
        d = (l + r + 1) // 2

        if (2 * d * n) + (2 * d * (m - 2 * d)) <= t and m - 2 * d >= 0:
            l = d
        else:
            r = d - 1
    return l


if __name__ == '__main__':
    n, m, t = int(input()), int(input()), int(input())
    print(binsearch(n, m, t))
