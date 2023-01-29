handle = open('mbox-short.txt')
di = dict() # create empty dictionary to save extracted  words from "mbox-short.txt

for line in handle:
    line=line.rstrip()
    words = line.split() # odsplituje slova vo vete
    #for word in words:
    if len(words) < 3 or words[0] != 'From': # ak je slovo dlžka slova kratšia ako 3 alebo sa slovo !=0 tak pokračuj
        continue

    print(words[5]) # ak nie tak vytlač slová