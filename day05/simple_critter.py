# Simple Critter

class Critter(object):
    """A virtual pet"""
    def talk(self):
        print("Hi. I'm an instance of class Critter.")


crit = Critter()
crit.talk()

input("\n\nPress the enter key to exit.")
