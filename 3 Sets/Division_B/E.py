m = int(input())
seq1 = [input() for _ in range(m)]
n = int(input())
seq2 = [input() for _ in range(n)]
max_cnt = 0
for i in range(n):
    count = 0
    for j in range(m):
        if not len(set(seq1[j]) - set(seq2[i])):
            count += 1
    if count > max_cnt:
        max_cnt = count
for i in range(n):
    count = 0
    for j in range(m):
        if not len(set(seq1[j]) - set(seq2[i])):
            count += 1
    if count == max_cnt:
        print(seq2[i])
