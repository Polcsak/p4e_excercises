zork = 0
print('Before counting loop is', zork)
for thing in [1, 8, 78, 99, 15, 66, 141]:
    zork = zork + 1
    print(zork, thing)
print('Count after loop is', zork)