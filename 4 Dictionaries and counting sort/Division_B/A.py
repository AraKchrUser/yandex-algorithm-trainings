n = int(input())
dct = {}
i = 0
while i < n:
    key, val = map(int, input().split())
    if key not in dct:
        dct[key] = 0
    dct[key] += val
    i += 1
for key in sorted(dct.keys()):
    print(key, dct[key])
