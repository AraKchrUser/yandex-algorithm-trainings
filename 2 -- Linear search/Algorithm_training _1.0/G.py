array = list(map(int, input().split()))

max1 = array[0]
max2 = array[1]
if array[0] < array[1]:
    max1, max2 = max2, max1
min1 = array[0]
min2 = array[1]
if array[0] > array[1]:
    min1, min2 = min2, min1

for i in range(2, len(array)):
    if max1 < array[i]:
        max2 = max1
        max1 = array[i]
    elif max2 < array[i]:
        max2 = array[i]

    elif min1 > array[i]:
        min2 = min1
        min1 = array[i]
    elif min2 > array[i]:
        min2 = array[i]

if max1 * max2 > min1 * min2:
    print(max2, max1)
else:
    print(min1, min2)
