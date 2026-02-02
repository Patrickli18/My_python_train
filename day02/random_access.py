# Random Access

import random
word = "index"

print(f"The word is: {word}")
# Accessing characters by index

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randint(low, high - 1)
    print("word[",position,"]\t", word[position])

input("\n\nPress Enter to exit..." )