gen1 = input()
gen2 = input()
gen1_list = []
gen2_set = set()
for i in range(len(gen1) - 1):
    gen1_list.append(gen1[i: i + 2])
for i in range(len(gen2) - 1):
    gen2_set.add(gen2[i: i + 2])
summ = 0
for gen in gen1_list:
    if gen in gen2_set:
        summ += 1
print(summ)
