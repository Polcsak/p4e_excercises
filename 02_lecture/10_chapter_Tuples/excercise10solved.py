fname = input ('Enter file:')
if len(fname) < 2 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

x = di.items() # change dictionary to list of tuples...

x = sorted(di.items())
# print(x[:5]) # print first 5 words (ABC...)

lst = list()
for k,v in di.items():
    #print (k,v)
    newtuple = (v,k)
    lst.append(newtuple)

lst = sorted(lst,reverse=True)
#print('Sorted', lst[:5])

for k,v in lst[:5]:
    print(k,v)


