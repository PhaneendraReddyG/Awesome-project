input_A = input("Enter Input:")

input_lower = input_A.lower()

a = input_lower.count("a")
e = input_lower.count("e")
i = input_lower.count("i")
o = input_lower.count("o")
u = input_lower.count("u")
count_vowels = a+e+i+o+u

print("Number of Vowels:",count_vowels)