def heapsort(sequence, n):
    parent_pos = (n - 1) // 2
    for i in range(parent_pos, -1, -1):
        heapify(sequence, i, n)
    for i in range(n):
        sequence[0], sequence[(n - 1) - i] = sequence[(n - 1) - i], sequence[0]
        heapify(sequence, 0, (n - 1) - i)
    return


def heapify(sequence, pos, size):
    pos = pos
    while pos * 2 + 1 < size:
        if pos * 2 + 2 < size:
            left, right = pos * 2 + 1, pos * 2 + 2
            max_pos = max((sequence[left], left), (sequence[right], right), key=lambda x: x[0])[1]
        else:
            max_pos = pos * 2 + 1
        if sequence[max_pos] > sequence[pos]:
            sequence[max_pos], sequence[pos] = sequence[pos], sequence[max_pos]
            pos = max_pos
        else:
            break
    return


n = int(input())
sequence = [*map(int, input().split())]
heapsort(sequence, n)
print(*sequence)
