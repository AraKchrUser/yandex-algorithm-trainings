A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if D > E:
    D, E = E, D
if A > B:
    A, B = B, A

if D >= C:
    if A <= E or E >= B:
        print('YES')
else:
    print('NO')
