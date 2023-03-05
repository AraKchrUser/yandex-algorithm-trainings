arr = [*map(int, input().split())]
m_min = 0
for i in range(len(arr)):
    if arr[i] != 1:
        continue
    n_min = 1000
    for j in range(len(arr)):
        if arr[j] == 2:
            len_n = abs(j - i)
            if len_n < n_min:
                n_min = len_n
    if n_min > m_min:
        m_min = n_min
print(m_min)
