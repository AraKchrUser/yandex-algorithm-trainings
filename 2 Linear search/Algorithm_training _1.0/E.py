n = int(input())
seq = list(map(int, input().split()))
ind = -1
mx_v = 0
max_ind = 0
k = 0

for i in range(1, n):
    if seq[max_ind] < seq[i]:
        max_ind = i


for i in range(n - 1):
    if max_ind < i and seq[i] % 10 == 5 and seq[i] > seq[i + 1]:
        if seq[i] > mx_v:
            mx_v = seq[i]
            ind = i

for i in range(n):
    if seq[ind] < seq[i]:
        k += 1

if ind == -1:
    print(0)
else:
    print(k + 1)
