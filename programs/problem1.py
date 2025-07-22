#print number from 1 to N
"""
Take a positive integer N as input and print all numbers from 1 to N
"""

# n = int(input("Enter the N:"))

# for i in range(1,n+1):
#     print(i)

i =1

# while i<= n:
#     print(i)
#     i += 1

"""
Take a positive integer N as input and calculate the sum of N natural numbers
"""

# n = int(input("Enter the N:"))


# i = 1
# sum = 0
# while i<= n:
#     sum = sum +i
#     i +=1
# print(sum)

# sum = 0
# for i in range(1,n+1):
#     # print(sum,i)
#     sum = sum+i
# print(sum)




"""
Take a positive integer N as input and Print all the even number from 1 to N numbers

"""

# n = int(input("Enter the N:"))

# i= 1
# without continue
# while i<= n:
#     if (i %2 ==0):
#         print(i)
#     i += 1
"""with continue"""
# while i <= n:
#     if not (i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

"""with for loop"""

# n = int(input("Enter the N:"))
# i=1
# for i in range(i,n+1):
#     if i% 2 == 0:
#         print(i)
#     i+= 1


"""
Take a positive integer N as input and Print all the odd number from 1 to N numbers

"""

# n = int(input("Enter the N value:"))

# i =1

# while i <= n:
#     if i % 2 !=0:
#         print(i)
#     i+=1


"""
Take a positive integer N as input and Print all the multiplication of N from 1 to N numbers

"""

# n = int(input("Enter the N value:"))

# i =1
# print(f"Mutliplication table of {n}")
"""Using while loop"""
# while i<= 10:

#     print(f"{n} * {i} =  {i * n}")
#     i+=1

"""using for loop"""

# n = int(input("Enter the N value:"))

# i =1
# print(f"Mutliplication table of {n}")

# for i in range(1,11):
#     print(f"{n} * {i} =  {i * n}")
#     i +=1


"""
Take a positive integer N as input and Calculate it's factorial

"""

n = int(input("Enter the N :"))

factorial =1

while n > 0:
    factorial = factorial * n
    n -=1
    print(n,factorial)
print(factorial)
