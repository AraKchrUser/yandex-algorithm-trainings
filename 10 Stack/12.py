stack = []
sequence = input()
opening = {']': '[', ')': '(', '}': '{'}
flag = True
for bracket in sequence:
    if bracket in opening.values():
        stack.append(bracket)
    elif not stack or stack.pop() != opening[bracket]:
        flag = False
if flag and not stack:
    print('yes')
else:
    print('no')
