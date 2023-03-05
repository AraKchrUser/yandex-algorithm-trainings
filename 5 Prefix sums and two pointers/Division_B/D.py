sequence = input()
k = 0
for index, item in enumerate(sequence):
    if item == '(' and index != len(sequence) - 1:
        k += 1
    elif index != 0:
        k -= 1
if k == 0:
    print('YES')
else:
    print('NO')
