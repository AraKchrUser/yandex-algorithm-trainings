array = input().split()
allnum = set()
nonuique = set()
for item in array:
    if item not in allnum:
        allnum.add(item)
    else:
        nonuique.add(item)
print(' '.join([item for item in array if item not in nonuique]))
