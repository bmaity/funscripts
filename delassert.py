#python program to demonstrate del and assert

a=[1,2,3]
print('The list before deleting any value.')
print(a)

#use del to delete second element of the list
del a[1]
print('The list after deleting second element')
print(a)

#demonstrating assert usage
#prints assertion error 
assert 5<3, "5 is not smaller than 3"
