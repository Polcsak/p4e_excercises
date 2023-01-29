# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
sum = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    b=(float(line[20:]))
    sum = sum + b
    count = count + 1
print('Summary after loop is','Avg =', sum/count,'Sum =', sum, 'Count =', count)