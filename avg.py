'''Finding average using a loop'''

count = 0
sum = 0
print('Before:', count, sum)
for value in [3,41,75,40,12,55,65]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After: Count, sum, average ', count, sum, sum/count)
