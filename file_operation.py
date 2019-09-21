fname = input("Enter file name: ")
fh = open(fname)
line_count = 0
total = 0
avg = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line_count = line_count + 1
    number = float(line[21:])
    total = number + total
    avg = total/line_count
print('Average spam confidence:', avg)
