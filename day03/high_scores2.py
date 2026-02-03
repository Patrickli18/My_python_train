# HighScores 2.0

scores = []

choice = None

while choice != "0":
    print(
        """
        High Scores 2.0

        0 - Quit
        1 - Add a new score
        2 - Display all scores
        """
    )
    choice = input("Choice: ")
    print()
    if choice == "0":
        print("Goodbye.")
    elif choice == "1":
        name = int(input("Enter the new score: "))
        score = input("Enter the player's name: ")
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    elif choice == "2":
        print("High Scores:")
        for score in scores:
            print(score)
        print()
    else:
        print("Invalid choice. Please try again.\n")
    
input("\n\nPress the enter key to exit.")