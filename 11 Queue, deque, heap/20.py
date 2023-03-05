def heapsort(sequence, n):
    for i in range(n):
        heapify(sequence, i, n)
        sequence[0], sequence[(n - 1) - i] = sequence[(n - 1) - i], sequence[0]
    return


def heapify(sequence, i, n):
    curr_pos = (n - i) - 1
    parent_pos = (curr_pos - 1) // 2
    for j in range(parent_pos, -1, -1):
        screening(sequence, j, curr_pos)
    return


def screening(sequence, _pos, curr_pos):
    pos = _pos
    while pos * 2 + 1 <= curr_pos:  #
        if pos * 2 + 2 <= curr_pos:
            left, right = pos * 2 + 1, pos * 2 + 2
            max_pos = max((sequence[left], left), (sequence[right], right), key=lambda x: x[0])[1]
        else:
            max_pos = pos * 2 + 1
        if sequence[max_pos] > sequence[pos]:
            sequence[max_pos], sequence[pos] = sequence[pos], sequence[max_pos]
            pos = max_pos
        else:
            break


n = int(input())
sequence = [*map(int, input().split())]
heapsort(sequence, n)
print(*sequence)
