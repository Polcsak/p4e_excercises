# Dictionaries

# What is a collection?

ccc = dict()
ccc['priemer'] = 55
ccc['hustota'] = 100
print(ccc)

# assign value (55) to key (priemer)

# if statement (counting names from a list)

counts = dict()
names = ['Jacob', 'Michael', 'Trevor', 'Jacob']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts) 