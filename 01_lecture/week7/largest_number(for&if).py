# Finding largest number (for & if functions)

largest = -1
print('Largest number before loop is', largest)
for the_num in [8, 10, -8, 36, 158, 300, 44]:
    if the_num > largest :
        largest = the_num
    print (largest, the_num)
print('Largest number after loop is', largest)

# Finding smallest number

Smallest = None
for value in [8, 10, -8, 36, 158, 300, 44]:
    if Smallest is None:
        Smallest = value
    elif value < Smallest:
        Smallest = value
        