def linelen(n, m, events, line):
    cnt = 0

    for eventidx in range(len(events)):

        if events[eventidx][1] == -1:
            cnt += 1
        elif events[eventidx][1] == 1:
            cnt -= 1

        if events[eventidx][1] == 0:
            # line.append(cnt)
            addition = 0
            if eventidx > 0 and events[eventidx - 1][0] == events[eventidx][0] and events[eventidx - 1][1] == -1:
                addition += 1
            line.append((cnt + addition, events[eventidx][2]))

    return line


if __name__ == "__main__":
    n, m = tuple(map(int, input().split()))
    events = []
    for _ in range(n):
        t_in, t_out = tuple(map(int, input().split()))
        events.append((t_in, -1))
        events.append((t_out, 1))
    observs = list(map(int, input().split()))
    events.extend([(i, 0, nb) for nb, i in enumerate(observs)])
    # events = list(set(events))
    events.sort()
    line = list()
    print(*[i[0] for i in sorted(linelen(n, m, events, line), key=lambda x: x[-1])])
