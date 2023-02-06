n, k = list(map(int, input().split()))
arr1, arr2 = list(map(int, input().split())), list(map(int, input().split()))


def rbinsearch(ind, arr):
    l, r = 0, len(arr) - 1

    while l < r:
        m = (l + r + 1) // 2
        if arr[m] <= ind:
            l = m
        else:
            r = m - 1

    return l


if __name__ == '__main__':
    for i in arr2:

        rv = rbinsearch(i, arr1)
        if abs(arr1[rv + 1 if len(arr1) - 1 > rv else 0] - i) >= abs(arr1[rv] - i):
            print(arr1[rv])
        else:
            print(arr1[rv + 1])
