fname = input("Enter file name: ")  #zadanie vstupu
fh = open(fname)  # spojenie so suborom
data=[] # vytvorenie prazdneho zoznamu
for line in fh:   # pre každú vetu v texte...
    words=line.split()  # rozdeliť vetu na slová
    for word in words:
        if word not in data:
            data.append(word)
print(sorted(data))