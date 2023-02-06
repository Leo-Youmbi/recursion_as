#A program that multiplies two numbers using recursion
def mul(a, b):
    if b == 1: 
        return a 
    return a * mul(b, b/b)

print(mul(3,4))