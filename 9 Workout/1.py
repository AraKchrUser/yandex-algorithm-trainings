with open('input.txt') as file:
    text = file.read()
text = ''.join(text.split())
cnt = {}
for symb in text:
    cnt[symb] = cnt.get(symb, 0) + 1
text = sorted(set(text))
for row in range(max(cnt.values()), 0, -1):
    for symb in text:
        if cnt[symb] >= row:
            print('#', end='')
        else:
            print(' ', end='')
    print()
print(''.join(text))
