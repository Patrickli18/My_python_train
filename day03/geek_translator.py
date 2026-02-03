# Geek Translator

geek = {
    "404": "clueless. From the web error message 404, meaning page not found.",
    "Googling": "searching the Internet for background information on a person.",
    "Keyboard Plaque": "the collection of debris found in computer keyboards.",
    "Link Rot": "the process by which web page links become obsolete.",
    "Percussive Maintenance": "the act of striking an electronic device to make it work.",
    "Uninstalled": "being fired. Especially popular during the dot-bomb era."
}
choice = None
while choice != "0":
    print(
        """
        Geek Translator

        0 - Quit
        1 - Look up a Geek term
        2 - Add a Geek term
        3 - Redefine a Geek term
        4 - Delete a Geek term
        """
    )
    choice = input("Choice: ")
    print()
    
    # exit
    if choice == "0":
        print("Good-bye.")
    # look up a term
    elif choice == "1":
        term = input("What term do you want me to translate? ")
        if term in geek:
            definition = geek[term]
            print(f"\n{term}: {definition}\n")
        else:
            print("\nSorry, I don't know that term.\n")
    # add a term
    elif choice == "2":
        term = input("What term do you want to add? ")
        if term not in geek:
            definition = input("What is the definition? ")
            geek[term] = definition
            print(f"\n{term} has been added.\n")
        else:
            print("\nThat term is already defined.\n")

    # redefine a term
    elif choice == "3":
        term = input("What term do you want to redefine? ")
        if term in geek:
            definition = input("What is the new definition? ")
            geek[term] = definition
            print(f"\n{term} has been redefined.\n")
        else:
            print("\nThat term is not defined.\n")

    # delete a term
    elif choice == "4":
        term = input("What term do you want to delete? ")
        if term in geek:
            del geek[term]
            print(f"\n{term} has been deleted.\n")
        else:
            print("\nThat term is not defined.\n")

    # invalid choice
    else:
        print("\nSorry, that is not a valid choice.\n")
input("\n\nPress the enter key to exit.")