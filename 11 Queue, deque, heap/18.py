def main():
    n_max = 100
    deque = [0] * n_max
    head = tail = n_max // 2  #
    while (command := input()) != 'exit':
        if command[:10] == 'push_front':

            if head < 0:
                n_max *= 2
                new = [0] * n_max
                for i in range(head, tail):
                    new[i + n_max // 2] = deque[i]
                deque = new.copy()
                head += n_max // 2
                tail += n_max // 2

            n = int(command.split()[-1])
            head -= 1
            deque[head] = n
            print('ok')
        elif command[:9] == 'push_back':

            if tail >= n_max:
                n_max *= 2
                new = [0] * n_max
                for i in range(head, tail):
                    new[i] = deque[i]
                deque = new.copy()

            n = int(command.split()[-1])
            deque[tail] = n
            tail += 1
            print('ok')
        elif command[:9] == 'pop_front':
            if tail == head:
                print('error')
                continue
            print(deque[head])
            deque[head] = 0
            head += 1
        elif command[:8] == 'pop_back':
            if tail == head:
                print('error')
                continue
            print(deque[tail - 1])
            deque[tail - 1] = 0
            tail -= 1
        elif command == 'front':
            if tail == head:
                print('error')
                continue
            print(deque[head])
        elif command == 'back':
            if tail == head:
                print('error')
                continue
            print(deque[tail - 1])
        elif command == 'size':
            print(tail - head)
        elif command == 'clear':
            while head < tail:
                deque[head] = 0
                head += 1
            print('ok')
    print('bye')
    return


main()
