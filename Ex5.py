def func5(string):
    n = len(string)
    if len(string) == 1: return string 
    return func5(string[1:])+string[0]

print(func5(string="Apple"))