def check(L, k, m):
    s = 0
    for i in L:
        s += i // m
    return s < k


def rbinsearch(N, K, L):
    l, r = 0, 10**18

    while l < r:
        m = (l + r + 1) // 2
        if check(L, K, m):
            l = m
        else:
            r = m - 1

    return l


if __name__ == '__main__':
    N, K = tuple(map(int, input().split()))
    L = list()
    for i in range(N):
        L.append(int(input()))
    print(rbinsearch(N, K, L))
