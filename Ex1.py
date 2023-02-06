def func1(a, b):
    if b == 1: return a 
    return a * func1(b, b/b)

print(func1(3,4))