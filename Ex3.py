def func3(n):
    if n==0: 
        return n
    return f"{n}\n{func3(n-1)}"

print(func3(10))