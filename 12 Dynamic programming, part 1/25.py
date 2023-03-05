n = int(input())
sequence = sorted(map(int, input().split()))
nmax = 10 ** 6
dp = [0] * (n + 1)
dp[1] = nmax
for i in range(2, n + 1):
    dist = sequence[i - 1] - sequence[i - 2]
    dp[i] = min(dist + dp[i - 1], dist + dp[i - 2])
print(dp[-1])
