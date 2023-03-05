def verdict(r, i, c):
    if i == 0:
        return c if r == 0 else 3
    if i == 1:
        return c
    if i == 4:
        return 4 if r == 0 else 3
    if i == 6:
        return 0
    if i == 7:
        return 1
    return i


r = int(input())
i = int(input())
c = int(input())
print(verdict(r, i, c))
