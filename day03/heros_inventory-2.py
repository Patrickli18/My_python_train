# Hero's Inventory 2.0

inventory = ("sword", "armor", "shield", "healing potion")
print("Your items are:")
for item in inventory:
    print(item)

print("You have", len(inventory), "items in your inventory.")

if "healing potion" in inventory:
    print("You will live to fight another day.")


intex = int(input("\nEnter the index number of the item you want to retrieve (0-3): "))
if 0 <= intex < len(inventory):
    print("You have selected:", inventory[intex])
else:
    print("Invalid index number.")

input("\nPress the enter key to exit.")