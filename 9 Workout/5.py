n = int(input())
arr = [0] * n
sum_ = 0
arr[0] = int(input())
for i in range(1, n):
    arr[i] = int(input())
    sum_ += min(arr[i - 1], arr[i])
print(sum_)
