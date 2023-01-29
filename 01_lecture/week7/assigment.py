Smallest = None
Largest = None
while True :
    sval = input('Input a value:')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    if Smallest is None:
        Smallest = fval
    elif fval < Smallest:
        Smallest = fval
    if Largest is None:
        Largest = fval
    elif fval > Largest:
        Largest = fval
print('All done')
print (Largest , Smallest)