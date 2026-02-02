# Finicky Counter Module

count = 0
while True:
    count += 1
    if count >10:
        break
    if count ==5:
        continue
    print("Count is:", count)

input("\n\nPress the enter key to exit.")



username =""
while not username:
    username = input("Enter your username: ")
    