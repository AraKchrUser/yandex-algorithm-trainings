N, n_list = int(input()), list(map(int, input().split()))
M, m_list = int(input()), list(map(int, input().split()))

mini = minj = 0
min_diff = max(n_list[-1], m_list[-1])
i, j = 0, 0
while i < N and j < M:
    if abs(n_list[i] - m_list[j]) < min_diff:
        min_diff = abs(n_list[i] - m_list[j])
        mini, minj = n_list[i], m_list[j]

    if n_list[i] > m_list[j]:
        j += 1
    else:
        i += 1
print(mini, minj)


mini = minj = 0
min_diff = max(n_list[-1], m_list[-1])
for i in n_list:
    for j in m_list:
        if abs(i - j) < min_diff:
            min_diff = abs(i - j)
            mini, minj = i, j
print(mini, minj)
