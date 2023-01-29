counts = dict()
names = ['Jacob', 'Michael', 'Trevor', 'Jacob']
for name in names:
    counts[name] = counts.get(name, 0) + 1 # combination of if & else
print(counts)