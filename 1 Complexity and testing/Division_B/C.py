def check(x, y):
    if x > 12:
        return 1
    if y > 12:
        return 1
    if x == y:
        return 1
    return 0


x, y, _ = [*map(int, input().split())]
print(check(x, y))
