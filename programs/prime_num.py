num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        print( i, "num**0.5:", num ** 0.5)
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
