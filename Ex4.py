def func4(n):
    if n==0: 
        return n
    return f"{func4(n-1)}\n{n}"

print(func4(10))