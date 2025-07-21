# input statements

# name = input("please give your name: ", )

# age = int(input("Enter your age:"))

# height = float(input("enter your height in cms:"))

# print(type(height))
# print(type(age))
# print(type(name))


# print("Hello!", name, ", you're age is", age, "and your height is",height, "cm.")




# # outputs section
# t = (1,2,3,4,5,6)

# print(*t,t,*t,sep=",",end=".")


#Example -1 (str input)

# name = input("Enter your name:")

# print("Hello,", name,end="!")



#Example -2 (integer input)

# a_int = int(input("Enter a integer:"))

# print("You entered:", a_int )


#Example -3 (float input)


# a_float = float(input("Enter a float value:"))

# print("Value of Pi:",a_float )

#Example -4 (multiple inputs in a single line)


# a = int(input("Enter a value:"))

# b = int(input("Enter b value:"))

# c = int(input("Enter c value:"))

# result_sum = a+b+c
# print("Sum of Inputs:",result_sum,sep="" )


# another method using split

# a = input()
# x,y,z = a.split(" ")
# sum = int(x)+int(y)+int(z)
# print(sum)



#Example -5 (multiple inputs in a single line and use separate it)

# b = input()

# name,age = b.split(",")

# print("Name:",name, ",Age:",age,sep="")

# Example 6(End parameter in output)

# n = int(input("ENTER A NUMBER:"))

# print("Countdown: 5 4 3 2 1 ", end="Blast Off!")

# Example 7 (artimatic operations)

# x,y = input("Enter a and b values: ").split(",")

# a = int(x)
# b = int(y)

# print("Addition of a and b :", a+b,"subtraction of a and b :", a-b, "multliplication of a and b :", a*b, "division of a and b :", a/b, "floor division of a and b :", a//b, sep="\n")

# Example 7 (comparison operations)

# x,y = input("Enter a and b values: ").split(",")

# a = int(x)
# b = int(y)

# print(a>b,a<b,a==b,a!=b)

# Example 7 (logical operations)

# x,y = input("Enter a and b values: ").split(",")

# """
# What actually happens:

#     "False" is a non-empty string, and in Python any non-empty string evaluates to True when passed to bool().

#     So even though the content looks like the word False, it is still a string, and non-empty strings are truthy.

#     bool("False") → True   ✅
#     bool("")      → False  ✅ (only empty string is falsy)


# """

# a = bool(x)
# b = bool()

# print(type(a))
# print(type(b))
# print(a)

# print(b)
# print(x and y, x or y, not x)


# formated output

# x,y = input("Enter Name and age: ").split(",")

# print(f"Name: {x}, age: {y} years")


# taking Yes/No input and handling  case sensitivity

x = input("Enter Yes/No: ").strip().lower()

# print(x)
# if x in ("yes",):
#     print("You entered: Yes")
# elif x in ("no",):
#     print("You entered: No")
# else:
#     print("Invalid input.")
