# Password
# if boolean is True, return the password string
print("Welcome to System Security Inc.") 
print("-- where secrity is our middle name \n")

password = input("Enter your password to continue: ")

if password == "secret":
    print("Access granted. Welcome!")
else:
    print("Access denied. Incorrect password.")
input("\nPress Enter to exit.")

