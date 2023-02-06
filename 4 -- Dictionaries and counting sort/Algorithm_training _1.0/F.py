import sys

database = {}
text = sys.stdin.readlines()
for row in text:
    name, item, count = row.strip().split()
    if name not in database:
        database[name] = {}
    if item not in database[name]:
        database[name][item] = 0
    database[name][item] += int(count)
for name in sorted(database.keys()):
    print(name, ':', sep='')
    for item in sorted(database[name].keys()):
        print(item, database[name][item])
