# Alien Blaster

class player(object):
    """A player in a shooter gmae."""
    def blast(self,enemy):
        print("The player blasts an emeny.\n")
        enemy.die()

class alien(object):
    """An alien in a shooter game."""
    def die(self):
        print("The alien gasps and say,'Oh,this is it.This is the big one.\n"\
              "Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them...\n"\
                "Good-bye, cruel universe.'")


print("\t\tDeath of an Alien\n")
hero =player()

invader = alien()
hero.blast(invader)

input("\n\nPress the enter key to exit.")

