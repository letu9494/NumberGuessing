# Assignment Le Tu
# Number guessing game
# Randomly choose a number between 1 and 100 (inclusive)
# Have the player enter a guess via input
# Tell the player the guess is high, low, or correct
# If high or low, allow the player to enter another guess
# Give the player an option to quit at any time
# Reward the player for a correct guess (ex., "Good job!")
# Tell the player how many guesses it took to guess correctly


import random


def numberguessing():
    attempt = 0

    # Create option to quit
    print("If you want to quit anytime, just type in 'EXIT'.")
    # Select a random number between 1 and 100
    x = str(random.randint(1, 100))
    # Ask user to enter a guess number
    y = str(input("Enter your guess value: "))

    while True:

        if y == 'EXIT':
            break  # If user type in exit then quit the loop

        if x == y:
            print("Your guess is correct! Good Job!")
            attempt += 1  # Adds up attempt number
            break  # If the number is correct then quit the loop

        if x < y:
            print("Your guess number is too high")
            y = str(input("Enter your guess value: "))  # Ask the user to give another guess
            attempt += 1

        if x > y:
            print("Your guess is too low")
            y = str(input("Enter your guess value: "))  # Ask the user to give another guess
            attempt += 1

    print("The number of attempt:", attempt)  # Print out the total attempt


numberguessing()
