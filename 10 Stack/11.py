stack = []
while (command := input()) != 'exit':
    if command[:4] == 'push':
        stack.append(int(command.split()[1]))
        print('ok')
        continue
    if command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print('error')
        continue
    if command == 'back':
        if stack:
            print(stack[-1])
        else:
            print('error')
        continue
    if command == 'size':
        print(len(stack))
        continue
    if command == 'clear':
        while stack:
            stack.pop()
        print('ok')
        continue
print('bye')
