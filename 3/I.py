n = int(input())
lst = [set([input() for _ in range(int(input()))]) for _ in range(n)]
all_ = lst[0]
any_ = lst[0]
for i in range(1, len(lst)):
    all_ = all_.intersection(lst[i])
    any_ = any_.union(lst[i])
print(len(all_))
if len(all_):
    print(*all_, sep='\n')
print(len(any_))
if len(any_):
    print(*any_, sep='\n')
