# Mood Computer
# elif program that suggests activities based on the user's mood.

import random

print("I sense your energy. Your true emotions are coming across my scren.")
print("You are ...")

mood = random.randint(1, 3)

if mood == 1:
    print(\
        """
        -------------------------------
        |                             |
        |                             |
        |      O              O       | 
        |            <>               |
        |      \___________/          |
        -------------------------------
        """) 
        
elif mood == 2:
    print(\
        """
        -------------------------------
        |                             |
        |                             |
        |      O              O       | 
        |            ----             |
        |         ___________         |
        -------------------------------
        """)       
    

elif mood == 3:
    print(\
        """
        -------------------------------
        |                             |
        |                             |
        |      O              O       | 
        |            ----             |
        |     .               .       |
        |        .         .          |
        |          .     .            |     
        |            . .              |
        -------------------------------
        """)       
else:
    print("Illegal mood value! You must be a really bad mood")
print("...today")

input("\n\nPress the enter key to exit.")