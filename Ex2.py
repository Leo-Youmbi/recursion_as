#A program that computes the exponent of a number using recursion
def pow(base, exp):
    if exp == 1: 
        return base
    return base * pow(base, exp-1)

print(pow(16,2))