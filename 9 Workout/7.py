def h2s(h, m, s):
    return h * 3600 + m * 60 + s


def s2h(s):
    s %= (24 * 3600)
    h = s // 3600
    m = s % 3600 // 60
    s = s % 3600 % 60
    return h, m, s


def format(h, m, s):
    return f'{h:02}:{m:02}:{s:02}'


h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
h3, m3, s3 = map(int, input().split(':'))
eps = 1e-10
if h1 > h3:
    h3 += 24
dist = round((h2s(h3, m3, s3) - h2s(h1, m1, s1)) / 2 + eps)
time = dist + h2s(h2, m2, s2)
time = s2h(time)
print(format(*time))
