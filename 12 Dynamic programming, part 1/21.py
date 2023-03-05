n = int(input())
fibb = [0, 1, 1]
for i in range(3, n + 3):
    fibb.append(fibb[i - 1] + fibb[i - 2] + fibb[i - 3])
print(fibb[-1])
