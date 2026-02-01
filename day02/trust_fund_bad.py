# Trust Fund Buddy - Bad

print(
    """
           Trust Fund Buddy
    Totals your monthly spending so that your trust fund doesn't run out
    (and you're forced to get a real job).
    
    please enter the requested , monthly costs. Since you're rich, ignore pennies
    and use only dollar amounts.
    
"""
)

car = input("Lamborghini Tune-Ups: ")

rent = input("Manhattan Apartment: ")
jet = input("Private Jet Rental: ")
gifts = input("Gifts: ")
food = input("Dining Out: ")
staff = input("Personal Staff: ")
guru = input("Life Guru: ")
games = input("Computer Games: ")

total = int(car) + int(rent) + int(jet) + int(gifts) + int(food) + int(staff) + int(guru) + int(games)
print("\nYour trust fund buddy has calculated your total monthly spending.")
print("You are spending $", total, "per month.")

print("\n\nPress Enter to exit.")
