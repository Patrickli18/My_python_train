# Guess My Number Game
#
# This program allows the user to guess a randomly generated number between 1 and 100.
# The program provides feedback on whether the guess is too low, too high, or correct.
# The game continues until the user guesses the correct number, and it counts the number of attempts.

import random


print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("\nTry to guess it in as few attempts as possible.\n")

# Generate a random number between 1 and 100

the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))

# Initialize the number of
tries = 1
# Loop until the user guesses the correct number
while guess != the_number:
    if guess < the_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess = int(input("Take a guess: "))
    tries += 1

print(f"Congratulations! You've guessed the number {the_number} in {tries} tries!")

input("\n\nPress the enter key to exit.")


