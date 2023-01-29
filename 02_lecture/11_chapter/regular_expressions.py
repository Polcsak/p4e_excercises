import re

hand = open('/DATA/SynologyDrive/p4e_excercises/02_lecture/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)