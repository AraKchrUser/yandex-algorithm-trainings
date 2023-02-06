def calculate_intermidate(n, i, j):
    if j < i:
        j, i = i, j
    interm_st1 = j - i - 1
    interm_st2 = n - j + i - 1
    if interm_st2 < interm_st1:
        return interm_st2
    return interm_st1


n, i, j = map(int, input().split())
print(calculate_intermidate(n, i, j))
