''' Scripts to learn try and except structure '''

#Example 1
astr = "Hello Bisu"
try:
    istr = int(astr)
except:
    istr = -1
print('First',istr)

var1 = 123
try:
    istr1 = int(var1)
except:
    istr1 = -1
print('Second',istr1)


#example2
astr = "Bisu"
try:
    print('Hello')
    istr = int(astr)
    print('World')
except:
    istr = -1
print('Done', istr)


#example3
rawstr = input('Enter some value: ')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work!')
else:
    print('Not a number')
