fname = input('Please enter file name:')
han = open(fname) #otvorí .txt súbor
count = 0

for line in han:
    line = line.rstrip() # oreže entre (prázdne riadky)
    words = line.split() # odsplituje každu vetu na slová
    # Guardian command
    # if len(words) < 3:
        # continue
    # Guardian compound statement
    #if line == '' or len(words) < 3:
    #    continue
    # Guardian in a compound statement (Guardian before! - short circuit evaluation)
    if len(words) < 3 or words[0] != 'From': # ak prvé slovo začína slovom From tak...
        continue
    count = count + 1
    print(words[1])
print(count)

