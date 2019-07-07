def isprime(n):
    if n <= 1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
        else:
            return True


n = 14
if isprime(n):
    print ("Given number is prime")
else:
    print("Given number is NOT prime")
