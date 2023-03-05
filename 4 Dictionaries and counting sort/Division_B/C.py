with open('input.txt') as file:
    lines = file.readlines()
dct = {}
for line in lines:
    for word in line.split():
        if word not in dct:
            dct[word] = 0
        dct[word] += 1
for _, word in sorted([(-v, k) for k, v in dct.items()]):
    print(word)
