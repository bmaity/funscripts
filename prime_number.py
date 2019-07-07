#!/Users/bmaity/anaconda2/bin/python

def isprime(n):
	if n <= 1:
		return False
	for x in range(2,n):
		if n % x == 0:
			return False
		else:
			return True 

n=12

if isprime(n):
	print( "is prime")
else:
	print("not prime")

