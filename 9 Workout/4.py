def check(var_1, var_2, row):
    if var_1 > n and var_2 < 1:
        return (-1,)
    row_1 = var_1 // 2 + var_1 % 2
    row_2 = var_2 // 2 + var_2 % 2
    if row_1 - row <= row - row_2 and var_1 <= n:
        return row_1, 2 if var_2 % 2 == 0 else 1
    elif var_2 >= 1:
        return row_2, 2 if var_2 % 2 == 0 else 1
    return (-1,)


n = int(input())
var_all = int(input())
row = int(input())
side = int(input())
var = row * 2 - (1 if side == 1 else 0)
var_1 = var + var_all
var_2 = var - var_all
print(*check(var_1, var_2, row))
