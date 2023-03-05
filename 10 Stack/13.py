polish_notation = input().split()
stack = []
for oper in polish_notation:
    if oper == '+':
        stack.append(stack.pop() + stack.pop())
    elif oper == '-':
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 - num2)
    elif oper == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(oper))
print(stack[0])
