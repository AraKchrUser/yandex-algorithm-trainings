dct = {}
with open('input.txt') as file:
    content = file.readlines()
for line in content:
    key, val = line.split()
    if key not in dct:
        dct[key] = 0
    dct[key] += int(val)
for key in sorted(dct.keys()):
    print(key, dct[key])
