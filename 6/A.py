n, k = list(map(int, input().split()))
arr1, arr2 = list(map(int, input().split())), list(map(int, input().split()))


def binsearch(ind, arr):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] >= ind:
            r = m
        else:
            l = m + 1
    return l


if __name__ == '__main__':
    for i in arr2:
        print('YES' if i == arr1[binsearch(i, arr1)] else 'NO')
