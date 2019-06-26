'''Finding average using a loop'''

count = 0
sum = 0
print('Before:', count, sum)
for value in [3,41,75,40,12,55,65]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After: Count, sum, average ', count, sum, sum/count)


'''Another way of doing it '''

'''Finding avg'''
#count = 0
#sum = 0
#print ('Before count and sum value:', count, sum)
#for value in [3,5,18,65,74,78]:
#   count = count + 1
#   sum = sum + value 
#   print('Current value of count, sum, value', count, sum, value)
#print('After the loop iteration the avg value is', sum/count)
