import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")

    while True:
        target = random.randint(1, 10)
        attempts = 5
        print("\nI’m thinking of a number between 1 and 10.")
        print(f"You have {attempts} attempts. Good luck!")

        while attempts > 0:
            guess = int(input("\nEnter your guess: "))

            if not guess.isdigit():
                print("Please enter a valid number.")
                continue

            #guess = int(guess)
            if guess < 1 or guess > 10:
                print("Your guess must be between 1 and 10.")
                continue

            if guess < target:
                print("Too low!")
            elif guess > target:
                print("Too high!")
            else:
                print("You got it! Nice job!")
                break

            attempts -= 1
            print(f"{attempts} attempts remaining.")

        if attempts == 0:
            print(f"Out of attempts! The number was {target}.")

        if input("\nPlay again? (yes/no): ").strip().lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break


guess_the_number()
