array = list(map(int, input().split()))

max1 = array[0]
max2 = array[1]
max3 = array[2]
if max1 < max2:
    if max2 < max3:
        max1, max2, max3 = max3, max2, max1
    else:
        max1, max2, max3 = max2, max1, max3
else:
    if max2 < max3:
        max1, max2, max3 = max1, max3, max2

min1 = array[0]
min2 = array[1]
if min1 > min2:
    min1, min2 = min2, min1


for i in range(3, len(array)):
    if max1 < array[i]:
        max3 = max2
        max2 = max1
        max1 = array[i]
    elif max2 < array[i]:
        max3 = max2
        max2 = array[i]
    elif max3 < array[i]:
        max3 = array[i]

for i in range(2, len(array)):
    if min1 > array[i]:
        min2 = min1
        min1 = array[i]
    elif min2 > array[i]:
        min2 = array[i]


if min1 * min2 * max1 > max1 * max2 * max3:
    print(min1, min2, max1)
else:
    print(max3, max2, max1)
