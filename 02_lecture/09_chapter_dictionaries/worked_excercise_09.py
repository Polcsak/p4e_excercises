fname = input('Enter file name:')
if len(fname) < 2 : fname = 'clown.txt'
handle = open(fname)

di = dict()
for line in handle:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for word in words:
        print(word)

# **harder way with if & else**

        #if word in di:
            #di[word] = di[word] + 1
            #print('Already existing...')

        #else:
            #di[word] = 1
            #print('**NEW**')
        #print(di[word])

# Method with get (harder one) (counts from zero!)

        #if word in words:
# if the key is not there the count is zero    
            #oldcount = di.get(word,0) 
            #print(word,'old',oldcount)

            #newcount = oldcount + 1
            #di[word] = newcount
            #print(word,'new',newcount)


# easier way with funcion "get":
# idiom: retrieve/create/update counter

        di[word] = di.get(word,0) + 1

print(di)

#now we want to find the most common word.
#maximum loop

largest = -1
largest_key = None

for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        largest_key = k #capture/remember the key that was largest

print('Done', largest_key, largest)