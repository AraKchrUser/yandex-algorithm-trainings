N = int(input())
seq = list(map(int, input().split()))
nb = int(input())
max = seq[0]
diff = abs(max - nb)
for i in range(1, N):
    if abs(seq[i] - nb) < diff:
        max = seq[i]
        diff = abs(seq[i] - nb)
print(max)
