arr = [*map(int, input().split())]
_set = set()
for item in arr:
    if item in _set:
        print('YES')
    else:
        print('NO')
    _set.add(item)
