#taking two inputs at a time
x,y=input('Enter two values').split()
print('Number of boys:',x)
print('Number of girls:',y)
print()


#taking 3 inputs at a time
x,y,z=input('Enter a three values').split()
print('Number of students',x)
print('Number of boys',y)
print('Number of girls',z)
print()

#Taking two inputs at a time
a,b=input('Enter two values').split()
print('first number is {} and second number is {}'.format(a,b))
print()


#taking multiple inputs at a time 
#and type casting using list() function
x=list(map(int,input('enter a multiple value').split()))
print('List of students',x)
print()
