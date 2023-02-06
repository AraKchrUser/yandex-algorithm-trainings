keyboard = {}
n = int(input())
for i, key in enumerate(map(int, input().split())):
    keyboard[i] = key
n = int(input())
for key in map(int, input().split()):
    keyboard[key-1] -= 1
print(*['YES' if keyboard[i] < 0 else 'NO' for i in keyboard], sep='\n')
