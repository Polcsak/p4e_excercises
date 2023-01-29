# Use words.txt as the file name

fname = open('C:/Users/jakub/Desktop/p4e_excercises/02_lecture/07_chapter/words.txt')
fstore = fname.read()
fstore = fstore.rstrip()
fstore = fstore.upper()
print(fstore)