n = 4
nums = [input() for _ in range(n)]
for i in range(n):
    num = nums[i]
    if num[0] == '+':
        num = num[2:]
    elif num[0] == '8':
        num = num[1:]
    num = num.replace('(', '').replace(')', '').replace('-', '')
    if len(num) < 3 + 7:
        num = '495' + num
    nums[i] = num
for i in range(1, n):
    if nums[i] == nums[0]:
        print('YES')
    else:
        print('NO')
