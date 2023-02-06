array = list(map(int, input().split()))
cnt = 0
for i in range(1, len(array) - 1):
    if array[i - 1] < array[i] and array[i] > array[i + 1]:
        cnt += 1
print(cnt)
