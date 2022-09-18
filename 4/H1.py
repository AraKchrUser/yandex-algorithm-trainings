# bad solution

def entry():
    def counter(seq):
        dischard_list = [0] * (ord('z') + 1)
        for s in seq:
            dischard_list[ord(s)] += 1
        return dischard_list

    def equal(x, y):
        return x == y

    count = 0
    g_n, S_n = list(map(int, input().split()))
    g, S = counter(input()), input()

    for i in range(S_n - g_n + 1):
        if equal(counter(S[i: i + g_n]), g):
            count += 1

    return count


print(entry())
