def func7(n):
    if n<=1: return n
    return func7(n-1)+func7(n-2)

print(func7(6))