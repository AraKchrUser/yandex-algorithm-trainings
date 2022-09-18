def temp(t_room, t_cond, mode):
    if mode == 'freeze':
        if not (t_cond >= t_room):
            return t_cond
    elif mode == 'heat':
        if not (t_room >= t_cond):
            return t_cond
    elif mode == 'auto':
        return t_cond
    return t_room


t_room, t_cond = list(map(int, input().split()))
mode = input()
print(temp(t_room, t_cond, mode))
