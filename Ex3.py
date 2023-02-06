#A function that prints numbers from n to 0 using recursion
def func1(n):
    if n==0: 
        return n
    return f"{n}\n{func1(n-1)}"

print(func1(10))