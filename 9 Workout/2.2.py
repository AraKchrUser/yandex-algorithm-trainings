import string
k, sequence = int(input()), input()
n, max_ = len(sequence), -1
for char in string.ascii_lowercase:
    summ_ = 1
    last = 0
    for i in range(n):
        while last < n and sequence[i] == char and last + 1 - i - summ_ <= k:
            max_ = max(min(summ_ + k, n), max_)
            last += 1
            summ_ += sequence[last] == char if last < n and last != i else 0
        summ_ -= (sequence[i] == char) if summ_ > 1 else 0
print(max_)
