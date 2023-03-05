n = int(input())
nmax = 5001
dp = [0] * 3 + [0] * n
a = [nmax] * 3 + [0] * n
b = [nmax] * 3 + [0] * n
c = [nmax] * 3 + [0] * n
for i in range(n):
    a_i, b_i, c_i = map(int, input().split())
    a[i + 3], b[i + 3], c[i + 3] = a_i, b_i, c_i
for i in range(3, n + 3):
    dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i - 1], dp[i - 3] + c[i - 2])
print(dp[-1])
