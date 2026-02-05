# Attribute Critter

class Critter(object):
    """A virtual pet"""
    def __init__(self,name):
        print("A net critter has been born!")
        self.name = name
    def __str__(self):
        rep = "Critter objec\n"
        rep += "name:" + self.name + "\n"
        return rep
    
    def talk(self):
        print("\nHi. I'm ",self.name,"\n")


#main
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

print("\nPrinting crit1:")
print(crit1)
print("Directly accessng crit1.name:")
print(crit1.name)

print("\nPrinting crit2:")
print(crit2)
input("\n\nPress theenter key toexit.")