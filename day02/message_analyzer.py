# Message Analyzer
# len() function and in operator usage

message = input("Enter a message: ")

print("Your message is", len(message), "characters long.")

print("\nThe most common letter in the English language is 'e'.")
if 'e' in message:
    print("Your message contains the letter 'e'.")
else:
    print("Your message does not contain the letter 'e'.")

input("\n\n Press Enter to exit.")