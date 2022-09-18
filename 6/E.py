def lbinsearch(a, b, c):
    l, r = 0, 10 ** 18

    while l < r:
        m = (l + r) // 2
        if (2 * a + 3 * b + c * 4 + 5 * m) >= 3.5 * (a + b + c + m):
            r = m
        else:
            l = m + 1

    return l


if __name__ == '__main__':
    a, b, c = int(input()), int(input()), int(input())
    print(lbinsearch(a, b, c))
