# Hangman Game
import random
HANGMAN = ("""
   ----
           |  |
           |  O
           | /|\\
           | / \\
           |
           ----
           """,
           """
           ----
           |  |
           |  O
           | /|\\
            | /
            |
            ----
            """,
            """
            ----
            |  |
            |  O
            | /|
             |
             |
             ----
             """,
             """
             ----
             |  |
             |  O
             |  |
              |
              |
              ----
              """,
              """
              ----
              |  |
              |  O
               |
               |
               |
               ----
               """,
               """
               ----
               |  |
               |  
                |
                |
                |
                ----
                """,
                """
                ----
                |  |
                |  
                |
                |
                |
                ----
                """)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("PYTHON", "JAVA", "JAVASCRIPT", "HANGMAN", "DEVELOPER", "PROGRAMMING")
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []
print("Welcome to Hangman!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)
    guess = input("\nEnter your guess: ").upper()
    while guess in used:
        print("You've already guessed that letter. Try again.")
        guess = input("Enter your guess: ").upper()
    used.append(guess)
    if guess in word:
        print("\nYes! The letter", guess, "is in the word!")
        new_so_far = ""
        for i in range(len(word)):
            if guess == word[i]:
                new_so_far += guess
            else:
                new_so_far += so_far[i]
        so_far = new_so_far
    else:
        print("\nSorry, the letter", guess, "isn't in the word.")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nCongratulations! You've guessed the word:", word)
print("\nThanks for playing Hangman. Goodbye!")

input("\n\nPress the enter key to exit.")