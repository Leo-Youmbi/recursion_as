#A function that reverse a string using recursion 
def rev(string):
    n = len(string)
    if len(string) == 1: 
        return string 
    return rev(string[1:])+string[0]

print(rev(string="Apple"))