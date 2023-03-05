n, m = map(int, input().split())
n_seq = sorted([[value, index]
                for index, value in enumerate(map(int, input().split()))])
m_seq = sorted([[value, index]
                for index, value in enumerate(map(int, input().split()))])
max_ = 0
last = 0
ans = [0] * n
for first in range(n):
    while last < m and n_seq[first][0] >= m_seq[last][0]:
        last += 1
    if last != m:
        max_ += 1
        ans[n_seq[first][1]] = m_seq[last][1] + 1
        last += 1
print(max_)
for k in range(n):
    number = ans[k]
    print(number)
