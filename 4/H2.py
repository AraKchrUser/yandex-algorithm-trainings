def entry():
    def counter(seq):
        cnt = {}
        for s in seq:
            if s not in cnt:
                cnt[s] = 0
            cnt[s] += 1
        return cnt

    def equal(x, y):
        match = 0
        for key in x:
            if key in y and x[key] == y[key]:
                match += 1
        return match

    def modify(_s, w, ch, mdf):
        ans = 0  # На сколько изменилось количество совпадющих букв
        if ch not in s:
            _s[ch] = 0
        if ch in w and _s[ch] == w[ch]:
            ans = -1
        s[ch] += mdf
        if ch in w and _s[ch] == w[ch]:
            ans = 1
        return ans

    count_word = 0
    g_n, S_n = list(map(int, input().split()))
    g, S = counter(input()), input()

    s = counter(S[:g_n])

    matches = equal(g, s)
    if matches == len(g):
        count_word += 1

    for i in range(g_n, S_n):
        matches += modify(s, g, S[i - g_n], -1)
        matches += modify(s, g, S[i], 1)
        if matches == len(g):
            count_word += 1

    return count_word


print(entry())
