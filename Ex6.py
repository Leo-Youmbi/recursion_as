def isprime(n,i=None):
    if i == None:
        i = n-1
    if i >= 2:
        if n%i == 0: 
            print(f"{n} is not prime")
            return False
        else:
            return isprime(n, i-1)
    print(f"{n} is prime")
    return True

print(isprime(8))
print(isprime(7))