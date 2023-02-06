n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]

count = 0

j = 0
for i in range(len(prefix)):

    while j < len(prefix) and abs(prefix[i] - prefix[j]) == k:
        count += 1
        j += 1



    # for j in range(i + Complexity and testing, len(prefix)):
    #     if abs(prefix[i] - prefix[j]) == k:
    #         count += Complexity and testing
    #         break
    # i = j

print(count)
