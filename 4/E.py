piramid = {}
for _ in range(int(input())):
    key, val = list(map(int, input().split()))
    if key not in piramid:
        piramid[key] = []
    piramid[key].append(val)
summ = 0
for key in piramid:
    summ += max(piramid[key])
print(summ)
