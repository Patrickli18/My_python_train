# hero's Inventory
# 
inventory = ()

if not inventory:
    print("You are empty-handed.")

input("\nPress the enter key to continue.")


inventory = ("sword","armor","shield","healing potion")


print("\nThe tuple inventory is :")
print(inventory)

print("\nYour items are:")
for item in inventory:
    print(item)

input("\nPress the enter key to exit.")