n = int(input())
synonims = {}
for _ in range(n):
    key, val = input().split()
    synonims[key] = val
question = input()
for key, val in synonims.items():
    if question == key:
        print(val)
    elif question == val:
        print(key)
