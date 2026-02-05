# Classy Citter

class Critter(object):
    """A virtual pet"""
    total = 0

    @staticmethod
    def status():
        print("\nThe total umber of critters is", Critter.total)

    def __init__(self,name):
        print("A critter has been born!")
        self.name = name
        Critter.total += 1

print("Accessing the class attributer critter.total:",end =" ")
print(Critter.total)

print("\nCreating critters.")
crit1= Critter("critter 1")
crit2= Critter("critter 2")
crit3= Critter("critter 3")
crit4= Critter("critter 4")
crit5= Critter("critter 5")

Critter.status()
print("Accessing the class attributer critter.total:",end =" ")
print(Critter.total)


input("\n\nPress the enter key to exit.")