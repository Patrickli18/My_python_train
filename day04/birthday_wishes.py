# Birthday Wishes 
def birhday1(name,age):
    print("Happy Birthday " + name + "!")
    print("You are now " + str(age) + " years old!")


def birthday2(name = "Jackson",age = 1):
    print("Happy Birthday " + name + "!")
    print("Wow! " + str(age) + " years old!")


# main code
print("Birthday Message 1:")
birhday1("Bob", 1)
print("#"*20)
birhday1("Alice", 30)
print("#"*20)
birhday1(name = "Eve", age = 65)
print("#"*20)
birhday1(age = 10, name = "Charlie")
print("#"*20)

print("\nBirthday Message 2:")
birthday2()
print("#"*20)
birthday2("Daisy", 5)
print("#"*20)
birthday2(name = "Frank")
print("#"*20)
birthday2(age = 100)
print("#"*20)
birthday2(name = "Grace", age = 45)
print("#"*20)

input("\n\nPress the enter key to exit.")

