def cumsum(sequence):
    cumsumarr = [0] * (len(sequence) + 1)
    for i in range(1, len(cumsumarr)):
        cumsumarr[i] = sequence[i - 1] + cumsumarr[i - 1]
    return cumsumarr


def rsq(l, r, arr_cum_summ):
    return arr_cum_summ[r] - arr_cum_summ[l - 1]


n, q = map(int, input().split())
sequence = [*map(int, input().split())]
arr_cum_summ = cumsum(sequence)
for _ in range(q):
    l, r = map(int, input().split())
    print(rsq(l, r, arr_cum_summ))
