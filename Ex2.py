def func2(base, exp):
    if exp == 1: return base
    return base * func2(base, exp-1)

print(func2(16,2))