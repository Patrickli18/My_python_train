# Property Critter

class Critter(object):
    """A virtual pet"""
    def __init__(self,name):
        print("A new critter has ben born!")
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,new_name):
        if new_name =="":
            print("A critter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")
    def talk(self):
        print("\nHi,I'm", self.name)

# main

crit = Critter("poochie")
crit.talk()


print("\nMy critter's nameis:",end=" ")
print(crit.name)


print("\nAttmpting to change my critter's name to Randolph...")
crit.name = "Randolph"


print("\nMy critter's nameis:",end=" ")
print(crit.name)

print("\nAttmpting to change my critter's name to Randolph...")
crit.name = ""


print("\nMy critter's nameis:",end=" ")
print(crit.name)

input("\n\nPress the enter key to exit.")