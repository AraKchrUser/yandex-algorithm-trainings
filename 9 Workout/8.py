k = int(input())
x = [0] * k
y = [0] * k
for i in range(k):
    x[i], y[i] = map(int, input().split())
x.sort()
y.sort()
print(x[0], y[0], x[-1], y[-1], sep=' ')
