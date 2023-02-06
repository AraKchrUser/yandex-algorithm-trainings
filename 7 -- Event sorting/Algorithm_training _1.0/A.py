# Другой подход:
# https://github.com/lakshinav/yandex-algorithm-trainings/blob/main/topic7/task_A.py

def student_cnt(events, students):
    visible = 0
    cnt = 0
    flg = 1

    for i in range(len(events)):
        if cnt > 0:
            visible += events[i][0] - events[i - 1][0]
            if flg:
                visible += 1
                flg = 0
        if events[i][1] == -1:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            flg = 1

    return students - visible


if __name__ == "__main__":
    n, m = tuple(map(int, input().split()))
    events = list()
    for _ in range(m):
        inp, outp = tuple(map(int, input().split()))
        events.append((inp, -1))
        events.append((outp, 1))
    events.sort()
    print(student_cnt(events, n))
