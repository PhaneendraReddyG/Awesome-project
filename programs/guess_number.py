import random
number = random.randint(1,100)

attempts =0
max_attempts=7


print(f"Guess the number in 1 to 100")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempts{attempts+1}: Enter your guess: "))
        attempts +=1
        if guess == number:
            print("congrats You've guess the Number")
            break
        elif guess < number: 
            print("your guess is too low")
        else:
            print("Your guess is too high ")
    except ValueError:
        print("X please enter a valid number ")

if attempts == max_attempts and guess != number:
    print(f"you ran out chances and the number was:{number}")