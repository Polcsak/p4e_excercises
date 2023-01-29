# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number
#  of mail messages. The program looks for 'From ' lines and takes the second word of those lines
#  as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
#  they appear in the file. After the dictionary is produced, the program reads through the dictionary 
# using a maximum loop to find the most prolific committer.

counts = dict()

handle = open('mbox-short.txt')
for line in handle:
    line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words)
    
    counts[words[1]] = counts.get(words[1],0) + 1
# print(counts)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

