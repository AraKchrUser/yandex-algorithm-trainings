n, k, m = list(map(int, input().split()))
iter1 = n
s = 0
flag = True
if m > k:
    flag = False
while iter1 >= k and flag:
    iter1 -= k
    iter2 = k
    while iter2 >= m:
        iter2 -= m
        s += 1
    iter1 += iter2 % m
print(s)
