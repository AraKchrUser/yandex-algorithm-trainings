
def symmseq(n, array):

    if array[:n // 2] == array[n // 2 + n % 2:][::-1]:
        return 0

    s = max = 0
    ind = -1
    for i in range(n - 2, 0, -1):
        one = array[i + 1:]
        two = array[i - len(one): i][::-1]
        if one == two:
            s = len(one)
        if max < s:
            max = s
            s = 0
            ind = i

    s = max1 = 0
    ind1 = -1
    for i in range(n - 2, 0, -1):
        one = array[i + 1:]
        two = array[i - len(one) + 1: i + 1][::-1]
        if one == two:
            s = len(one)
        if max1 < s:
            max1 = s
            s = 0
            ind1 = i

    if ind != -1 or ind1 != -1:
        if max < max1:
            ind = ind1 + 1
            max = max1
        return len(array[:ind - max][::-1]), array[:ind - max][::-1]

    l = 1
    if array[-1] == array[-2]:
        l += 1
    array1 = []
    for i in range(n - l):
        array1.insert(0, array[i])
    return n - l, array1


n = int(input())
array = list(map(int, input().split()))
ans = symmseq(n, array)
if ans == 0:
    print(0)
else:
    print(ans[0])
    print(*ans[1])
