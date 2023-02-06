def get_stem(arr, even):
    ans = 0
    flag = False
    for i in range(len(arr)):
        if arr[i] >= l // 2 and not flag:
            ans = i
            flag = not flag
    if (not even and arr[ans] == l // 2) or ans == 0:
        return str(arr[ans])
    return str(arr[ans - 1]) + ' ' + str(arr[ans])


l, k = [*map(int, input().split())]
arr = [*map(int, input().split())]
even = l % 2 == 0
print(get_stem(arr, even))
