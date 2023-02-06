n = int(input())
arr = [*map(int, input().split())]
summ = 0
mmax = 0
for i in range(n):
    summ += arr[i]
    if arr[i] > arr[mmax]:
        mmax = i
print(summ - arr[mmax])
