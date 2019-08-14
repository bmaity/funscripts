import re
x = "My 2 favourite numbers are 2 and 19"
y = re.findall('[0-9]+',x)
print(y)

y= re.findall('[AEIOU]+',x)
print(y)
