# def sum(a,b):
#     print(a+b)
# sum(50,50)


# def sum(a,b):
#     return a+b
# result = sum(3,4)
# print(result)

def greet_user(name,greeting = "Hello"):
    return greeting + "," +name+"!"
greeting1 = greet_user("Phani")
greeting2 = greet_user("phaneendra","HEY!")

print(greeting1)
print(greeting2)
