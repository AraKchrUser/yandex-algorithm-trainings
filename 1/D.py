def solution(a, b, c):
    if a == 0:
        if b == c ** 2 and c >= 0:
            return 'MANY SOLUTIONS'
        else:
            return 'NO SOLUTION'
    x = (c ** 2 - b) // a
    if a * x + b < 0 or c < 0 or a * x + b != c ** 2:
        return 'NO SOLUTION'
    return x


a = int(input())
b = int(input())
c = int(input())
print(solution(a, b, c))
