
print("Select operation: \n1. Add\n2. Subtract\n3. Multiply\n4 Divide", )


select_operation = input("Enter your choice (1/2/3/4): ")

select_operation = int(select_operation)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if select_operation == 1 :
    print("Result of Addition of num1, num2", num1+num2)

elif select_operation == 2 :
    print("Result of subtract of num1, num2", num1-num2)


elif select_operation == 3 :
    print("Result of multiplication of num1, num2", num1*num2)

elif select_operation == 4 :
    if num2 != 0:
        print("Result of division:", num1 / num2)
    else:
        print("Error: cannot divide by zero")

else:
    print("you have entered wrong input, please enter in (1,2,3,4)")