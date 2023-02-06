max_n = int(input())
set_no = set()
set_yes = set(range(1, max_n - 1))
while (sequence := input()) != 'HELP':
    sequence = set(map(int, sequence.split()))
    if input() == 'YES':
        set_yes.intersection_update(sequence)
    else:
        set_no.update(sequence)
print(*sorted([item for item in set_yes.difference(set_no)]))
