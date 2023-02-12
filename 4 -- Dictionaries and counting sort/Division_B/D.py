with open('input.txt') as file:
    lines = file.readlines()
dct = {}
all_summ = 0
order = []
for line in lines:
    split = line.split()
    name, summ = ' '.join(split[:-1]), int(split[-1])
    dct[name] = summ
    all_summ += summ
    order.append(name)
first_private = all_summ / 450
places = {}
resuds = []
for name in order:
    div = dct[name] // first_private
    places[name] = div
    resuds.append((- dct[name] / first_private + div, dct[name], name))
dist = 450 - sum(places.values())
if dist > 0:
    place = 0
    for _, _, name in sorted(resuds):
        if place < dist:
            places[name] += 1
        place += 1
for name in order:
    print(name, int(places[name]))
