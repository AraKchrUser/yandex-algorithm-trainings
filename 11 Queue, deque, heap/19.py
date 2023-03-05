def push(heap, num):
    heap.append(num)
    pos = len(heap) - 1
    while pos > 0 and heap[pos] > heap[(pos - 1) // 2]:
        heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
        pos -= 1
        pos //= 2
    return


def pop(heap):
    max_num, heap[0] = heap[0], heap[-1]
    heap.pop()
    pos = 0
    while pos * 2 + 1 < len(heap):
        if pos * 2 + 2 < len(heap):
            left, right = pos * 2 + 1, pos * 2 + 2
            max_pos = max((heap[left], left), (heap[right], right), key=lambda x: x[0])[1]
        else:
            max_pos = pos * 2 + 1
        if heap[max_pos] > heap[pos]:
            heap[max_pos], heap[pos] = heap[pos], heap[max_pos]
        pos = max_pos
    return max_num


n = int(input())
heap = []
for _ in range(n):
    command = input()
    if command[0] == '0':
        num = int(command.split()[-1])
        push(heap, num)
    else:
        print(pop(heap))
