# Pizza Slicer Module

word = "pizza"

print(
    """
    Slicing 'Cheat sheet'
    0  1  2  3  4  5
    +--+--+--+--+--+
    | p| i| z| z| a|
    +--+--+--+--+--+
    -5  -4 -3  -2 -1
    """ 
)

print("Enter the beginning and ending indices to slice the word 'pizza'." )
print ("Press the enter key at 'Begin' to exit.")

start = None
while start != "":
    start = input("\nStart: ")
    if start :
        start = int(start)
        finish = int (input("Finish: "))
        print("word[",start,":",finish,"] is",end=" ")
        print(word[start:finish])
        
input("\n\nPress Enter to exit.")