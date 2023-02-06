def check_X(d, x, y):
    if 0 <= y <= d and 0 <= x <= d and y <= d - x:
        return 0
    a = x ** 2 + y ** 2
    b = (d - x) ** 2 + y ** 2
    c = x ** 2 + (d - y) ** 2
    if a <= b and a <= c:
        return 1
    if b <= c and b <= a:
        return 2
    return 3


d = int(input())
coords = [*map(int, input().split())]
print(check_X(d, *coords))
