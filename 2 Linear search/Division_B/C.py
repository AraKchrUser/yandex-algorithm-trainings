in_string = input()
n = 0
for index in range(len(in_string) // 2):
    if in_string[index] != in_string[len(in_string) - 1 - index]:
        n += 1
print(n)
