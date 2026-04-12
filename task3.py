lst = [3, 1, 1, 1, 2, 2]
dct = {}

for i in lst:
    son = lst.count(i)
    dct[i] = son
print(len(set(dct.values()))==len(list(dct.values())))