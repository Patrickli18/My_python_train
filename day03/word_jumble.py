# Word Jumble Game

import random
WORDS = ['python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone']
word = random.choice(WORDS)
crrect = word
jumble = ''
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Welcome to Word Jumble!\n")
print("Here is the jumbled word:", jumble)

guess = input("\nYour guess: ")
while guess != crrect and guess != "":
    print("Sorry, that's not it.")
    print("Try again.")
    guess = input("Your guess: ")
if guess == crrect:
    print("Congratulations! You guessed it!")

input("\nPress the enter key to exit.")