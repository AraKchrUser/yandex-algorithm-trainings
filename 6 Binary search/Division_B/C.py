def eq(x, a, b, c, d):
    val = a * (x ** 3) + b * (x ** 2) + c * x + d
    if a > 0:
        return val > 0
    return val < 0


a, b, c, d = map(int, input().split())
eps = 1e-10
l, r = -1e10, 1e10
while r - l > eps:
    x = (l + r) / 2
    if eq(x, a, b, c, d):
        r = x
    else:
        l = x
print(l)
