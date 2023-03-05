def check_1(sequence, m, x):
    return sequence[m] >= x


def check_2(sequence, m, x):
    return sequence[m] > x


def binsearch(sequence, n, x, check, right=False):
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if check(sequence, m, x):
            r = m
        else:
            l = m + 1
    if right:
        l -= 1
    if l >= n or sequence[l] != x:
        return 0
    return l + 1


n = int(input())
sequence = [*map(int, input().split())]
m = int(input())
queries = [*map(int, input().split())]
for query in queries:
    l, r = binsearch(sequence, n, query, check_1), binsearch(sequence, n, query, check_2, True)
    print(l, r)
