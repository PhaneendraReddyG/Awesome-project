my_list = ['a', 'b', 'c', 'd','f','a', 'b', 'c', 'd','e']

my_dict = {}
for item in my_list:
    if item in my_dict:
        my_dict[item] += 1
    else:
        my_dict[item] = 1

print(my_dict)





