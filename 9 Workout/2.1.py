k = int(input())
sequence = input()
n = len(sequence)
max_ = -1
for char in set(sequence):
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        add = 1 if sequence[i - 1] == char else 0
        prefix[i] = prefix[i - 1] + add
    flag = False
    for i in range(n):
        for j in range(i + 1, n):
            item_1 = sequence[i]
            item_2 = sequence[j]
            if item_1 == item_2 == char:
                flag = True
                count_char = prefix[j + 1] - prefix[i]
                replace_count = j + 1 - i - count_char
                if replace_count <= k:
                    curr_max = min(count_char + k, n)
                    max_ = max(curr_max, max_)
    if not flag:
        replace_count = k
        curr_max = min(1 + k, n)
        max_ = max(curr_max, max_)
print(max_)
