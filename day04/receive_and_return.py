# Receive and REturn
def display(message):
    print(f"Message received: {message}")

def give_me_five():
    five = 5
    return five

def ask_yes_no(question):
    """Ask a yes or no question and return 'y' or 'n'."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


display("Here's a message for you.\n")

number = give_me_five()
print(f"The function gave me the number: {number}\n")
answer = ask_yes_no("Do you want to continue? (y/n): ")
print(f"You answered: {answer}\n")

input("\n\nPress the enter key to exit.")