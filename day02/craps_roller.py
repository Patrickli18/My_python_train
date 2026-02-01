# Craps Roller
# ランダムな数字を生成する
import random

diel1 = random.randint(1, 6)
diel2 = random.randrange(6) + 1

total = diel1 + diel2

print("You rolld a ", diel1 , " and a ", diel2, " for a total of ", total)

input("\n\n Press Enter to exit.")