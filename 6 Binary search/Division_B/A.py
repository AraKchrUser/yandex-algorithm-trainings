def check_1(sequence, m, x):
    return sequence[m] >= x


def check_2(sequence, m, x):
    return sequence[m] > x


def binsearch(sequence, n, x, check):
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if check(sequence, m, x):
            r = m
        else:
            l = m + 1
    return l


n = int(input())
sequence = sorted([*map(int, input().split())])
k = int(input())
for _ in range(k):
    l, r = map(int, input().split())
    ans = binsearch(sequence, n, r, check_2) - binsearch(sequence, n, l, check_1)
    print(ans, end=' ')
