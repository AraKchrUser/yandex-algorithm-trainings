sequence = input()
counter = {}
n = len(sequence)
for i, char in enumerate(sequence):
    if char not in counter:
        counter[char] = (n - i) * (i + 1)
    else:
        counter[char] += (n - i) * (i + 1)
chars = sorted(counter.keys())
for char in chars:
    print(f'{char}: {counter[char]}')
