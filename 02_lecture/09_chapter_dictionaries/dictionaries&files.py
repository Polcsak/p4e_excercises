# Counting Pattern - spočita jednotlive slova vo vete

counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

# Retrieving lists of Keys and Values

jjj = {'chuck' : 1, 'Fred' : 48, 'Jozef' : 150}
print(list(jjj))
