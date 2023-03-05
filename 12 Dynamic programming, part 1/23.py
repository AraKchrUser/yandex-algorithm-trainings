n = int(input())
dp = [0] * (n + 1)
for i in range(2, n + 1):
    min_ = dp[i - 1] + 1
    if not i % 2:
        min_ = min(min_, dp[i // 2] + 1)
    if not i % 3:
        min_ = min(min_, dp[i // 3] + 1)
    dp[i] = min_
trace = []
i = n
while i != 1:
    trace.append(i)
    if dp[i] == dp[i - 1] + 1:
        i -= 1
    elif i % 2 == 0 and dp[i] == dp[i // 2] + 1:
        i //= 2
    elif i % 3 == 0 and dp[i] == dp[i // 3] + 1:
        i //= 3
trace.append(1)
print(dp[-1])
print(*trace[::-1])
