def main():
    queue = []
    head = tail = 0
    while (command := input()) != 'exit':
        if command[:4] == 'push':
            n = int(command.split()[-1])
            queue.append(n)
            tail += 1
            print('ok')
        elif command == 'pop':
            if head == tail:
                print('error')
                continue
            print(queue[head])
            head += 1
        elif command == 'front':
            if head == tail:
                print('error')
                continue
            print(queue[head])
        elif command == 'size':
            print(tail - head)
        elif command == 'clear':
            while head < tail:
                head += 1
            print('ok')
    print('bye')


main()
