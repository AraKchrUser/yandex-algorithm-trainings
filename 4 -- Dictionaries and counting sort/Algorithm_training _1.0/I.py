def counter(dictionary):
    cnt = {}
    for i in dictionary:
        if i.lower() not in cnt:
            cnt[i.lower()] = set()
        cnt[i.lower()].add(i)
    return cnt


def isUpper(w):
    cnt = 0
    for c in w:
        if c.isupper():
            cnt += 1
        if cnt > 1:
            return 0
    if cnt == 0:
        return 0
    return 1


dictionary = counter([input() for _ in range(int(input()))])
text = input().split()
error = 0
# Прохождим по тексту и ищем ошибки в ударении
for w in text:
    if w.lower() in dictionary:
        if w not in dictionary[w.lower()]:
            error += 1
    else:
        if not isUpper(w):
            error += 1

print(error)
