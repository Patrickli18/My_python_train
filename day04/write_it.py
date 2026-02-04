# Write It

print("Creating a text file with the write() method."   )

text_file = open("day04/write_it.txt", "w")

text_file.write("This is the first line.\n")
text_file.write("This is the second line.\n")
text_file.write("This is the third line.\n")
text_file.close()

print("\nReading the newly created file...")
text_file = open("day04/write_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()


print("Creating a text file with the writelines() method.")
text_file = open("day04/write_it.txt", "w")
lines = ["First line.\n", "Second line.\n", "Third line.\n"]
text_file.writelines(lines)
text_file.close()

print("\nReading the newly created file...")
text_file = open("day04/write_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()
input("\n\nPress the enter key to exit.")

