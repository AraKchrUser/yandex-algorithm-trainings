n, m = list(map(int, input().split()))
an_set, bor_set = set(), set()
for _ in range(n):
    an_set.add(int(input()))
for _ in range(m):
    bor_set.add(int(input()))
print(len(an_set.intersection(bor_set)))
print(*sorted(an_set.intersection(bor_set)))
print(len(an_set.difference(bor_set)))
print(*sorted(an_set.difference(bor_set)))
print(len(bor_set.difference(an_set)))
print(*sorted(bor_set.difference(an_set)))
