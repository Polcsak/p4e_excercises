#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words
#  using the split() method. The program should build a list of words. For each word on each line check to 
# see if the word is already in the list and if not append it to the list. When the program completes, 
# sort and print the resulting words in python sort() order as shown in the desired output.
 
fname = input("Enter file name: ")  #zadanie vstupu
fh = open(fname)  # spojenie so suborom
data=[] # vytvorenie prazdneho zoznamu
for line in fh:   # pre každú vetu v texte...
    words=line.split()  # rozdeliť vetu na slová
    for word in words:  # pre každé slovo v slovách
        if word not in data: # ak sa slovo nenachádza v texte
            data.append(word) # priradiť slovo do zoznamu
print(sorted(data))

#


