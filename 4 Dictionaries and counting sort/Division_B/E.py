n = int(input())
dct = {}
for i in range(1, n + 1):
    number = int(input())
    if number == 0:
        dct[input()] = [i]
    else:
        for key in dct:
            if number in dct[key]:
                dct[key].append(i)
    _ = input()
max_len = -1
max_key = ''
for key in dct:
    len_key = len(dct[key])
    if len_key > max_len:
        max_len = len_key
        max_key = key
print(max_key)
