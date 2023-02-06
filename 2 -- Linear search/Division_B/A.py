arr = []
max_n = -1
while (n := int(input())) != 0:
    if n > max_n:
        max_n = n
    arr.append(n)
count = 0
for item in arr:
    if item == max_n:
        count += 1
print(count)
