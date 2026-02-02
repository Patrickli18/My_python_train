# Hih Scores
scores = []
hcoice = None
while hcoice != "0":
    print(
        """
        High Scores Menu
        0 - Exit
        1 - Show Scores
        2 - Add a Score
        3 - Remove a Score
        4 - Sort Scores
        """
    )
    hcoice = input("Choice: ")
    print()
    # Exit
    if hcoice == "0":
        print("Goodbye.")
    # Show Scores
    elif hcoice == "1":
        print("High Scores:")
        for score in scores:
            print(score)
    # Add a Score
    elif hcoice == "2":
        score = int(input("Enter the score to add: "))
        scores.append(score)
        print(f"{score} has been added.")
    # Remove a Score
    elif hcoice == "3":
        score = int(input("Enter the score to remove: "))
        if score in scores:
            scores.remove(score)
            print(f"{score} has been removed.")
        else:
            print(f"{score} not found in the list.")
    # Sort Scores
    elif hcoice == "4":
        scores.sort(reverse=True)
        print("Scores have been sorted in descending order.")
    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")
# End of High Scores Program
input("\nPress the enter key to exit.")