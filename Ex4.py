#A function that prints numbers from 0 to n using recursion 
def func2(n):
    if n==0: 
        return n
    return f"{func2(n-1)}\n{n}"

print(func2(10))