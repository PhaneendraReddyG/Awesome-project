# list_a = [10,20,30,40,50]

# sum_of_list= 0

# for i in (list_a):
#     sum_of_list += i
# print("Sum of lelements",sum_of_list)


# salaries = [15000,14000,25000,30000,23000,22400]

# for i in salaries:
#     if i > 20000:
#         print(f"salary is greater than 20000:{i}")

# list_a = [10,20,30,40,50]
"""using for loop"""
# sum_of_list= 0
# for i in range(len(list_a)):
#     sum_of_list += list_a[i]
# print("Sum of lelements",sum_of_list)


# list_a = [10,20,30,40,50]

# i = 0
# sum_total = 0

# while i < len(list_a):
#     sum_total += list_a[i]
#     i = i+1
# print(sum_total)

"""Finding maximum and minmum numbers in a list"""

# l = list(input("Enter the list:"))

# l = [10,2,88888,90,67]
# print(l)
# mini = l[0]
# maxi = l[0]
# for i in l:
#     if i > maxi:
#         maxi = i
#     elif i < mini:
#         mini = i
# print(mini,maxi)
"""simple way"""
# l = [10,2,88888,90,67]

# new=sorted(l)
# print(new)
# print(new[0],new[-1])

"""Remove duplicates in a given list and create a new list """

# l = [10,20,10,30,20,10,30]

# my_set = set(l)
# l = list(my_set)
# print(l)
# print(my_set)
"""ACTUAL WAY"""
# inpu = input("Enter the l list:").split(',')

# l = [int(item) for item in inpu]

# newL = []

# for i in l:
#     if i in newL:
#         continue
#     else:
#         newL.append(i)
# print(l)
# print(newL)

"""Count the number of occurences of a specific element in a list"""
"simple way"
# x = int(input("enter x:"))
# l = [1,2,4,3,2,5,2,3,3,3,3,2]

# newl= l.count(x)
# print(f"Count of {x} = {newl}")
"""Actual way"""

# inp = input("enter the list:").split(",")

# l = [int(item) for item in inp]

# x = int(input("enter the nubmer to check in the list :"))

# c = 0

# for i in l:
#     if i==x:
#         c += 1

# print(f"count of {x}= {c}")

"""find uninon and intersection of below sets"""

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# uset= s1.union(s2)
# iset = s1.intersection(s2)

# print(uset)
# print(iset)

"""Practice with dictionaries"""

my_dict = dict()

print(my_dict)
name = input("Enter the NAME:")
Age = int(input("enter the age:"))
city = input("enter the city:")

my_dict['name']= name
my_dict['Age']=Age
my_dict['city']=city
print(my_dict)


for i,j in my_dict.items():
    print(i,j)