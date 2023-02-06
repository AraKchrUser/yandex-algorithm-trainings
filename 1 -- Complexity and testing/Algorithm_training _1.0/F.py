a1, b1, a2, b2 = list(map(int, input().split()))
squares = []
if a1 > a2:
    a = a1
else:
    a = a2
squares.append((b1 + b2, a))

if a1 > b2:
    a = a1
else:
    a = b2
squares.append((b1 + a2, a))

if b1 > b2:
    b = b1
else:
    b = b2
squares.append((a1 + a2, b))

if b1 > a2:
    b = b1
else:
    b = a2
squares.append((a1 + b2, b))

ind = min(squares, key=lambda x: x[0] * x[1])
print(*ind)
