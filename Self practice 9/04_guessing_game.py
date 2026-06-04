import random

print("Welcome to the Guessing Game!")
comp = random.randint(1, 100)
attempt = 0
while True:
    you = int(input("Guess a number between 1 and 100: "))
    attempt += 1
    if comp == you:
        print(f"Congratulations! You've guessed the number : ")
        print(f"Attempt: ", attempt)
        break

    elif comp > you:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

    
