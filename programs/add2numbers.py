

import copy

a = int(input("Enter a value:"))
b = int(input("Enter b value:"))

b = copy.copy(a)
def add2nums(a,b):
    print(a+b)
add2nums(a,b)