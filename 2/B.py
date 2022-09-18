def define_seq():
    end = int(-2e9)
    seq = []
    n = int(input())

    while n != end:
        seq.append(n)
        n = int(input())

    # print(set(seq), *seq)
    if len(set(seq)) == 1:
        return "CONSTANT"

    asc = 0
    weasc = 0
    desc = 0
    wedesc = 0
    for i in range(1, len(seq)):
        if seq[i - 1] < seq[i]:
            asc += 1
        if seq[i - 1] <= seq[i]:
            weasc += 1
        if seq[i - 1] > seq[i]:
            desc += 1
        if seq[i - 1] >= seq[i]:
            wedesc += 1
    if asc == len(seq) - 1:
        return "ASCENDING"
    if weasc == len(seq) - 1:
        return "WEAKLY ASCENDING"
    if desc == len(seq) - 1:
        return "DESCENDING"
    if wedesc == len(seq) - 1:
        return "WEAKLY DESCENDING "
    return "RANDOM"


print(define_seq())
