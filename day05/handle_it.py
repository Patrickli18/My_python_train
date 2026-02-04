# Handle It

#try/except

try:
    num = float(input ("Enter a number:"))
except:
    print("Something went wrong!")

print("*"*10)
try:
    num = float(input ("Enter a number:"))
except ValueError as e:
    print("That was not a number!")
    print(e)
else:
    print("You entered the number",num)