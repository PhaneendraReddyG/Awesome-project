a = input("input of a: ")

b = input("input of b: ")

c = input("input of c: ")

a = int(a)

b = int(b)

c = int(c)


print(a)

print(b)

print(c)
if a > b and a > c:
    print("a is the largest number", a)
elif b > c:
    print("b is the largest number", b)

else:
    print("c is the largest number", c)
