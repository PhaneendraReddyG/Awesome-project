candies =10

for i in range(0,candies):
    if candies - i ==5:
        print("Only 5 candies left and stopped distribution:", i)
        continue
    print("Giving a candy to friend!:",i)

# message = "Hello, World!"

# # for char in message:
# #     print(char)

# # length= len(message)

# # for i in range(length):
# #     print(i)

# for i in range(11,100):
#     for j in range(1,11):
#         print(f"{i}*{j} = {i * j}")