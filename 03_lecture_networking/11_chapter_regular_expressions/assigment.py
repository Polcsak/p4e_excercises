# assigment

import re

handle = open('regex_sum_1708130.txt')
numlist = list()

for line in handle:
    words = line.rstrip()
    # print(words)
    y = re.findall('[0-9]+', words)
    # if len(y) != 1: continue
    for num_str in y:
        num = float(num_str)
        # num = float(word)
        numlist.append(num)
print(numlist)
print('Sum:', sum(numlist))
