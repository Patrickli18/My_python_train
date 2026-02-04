#Read It

print("Opening and closin the file...")
text_file = open("day04/read_it.txt", "r")
text_file.close()

print("\nReading characters from the file...")
text_file = open("day04/read_it.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()



print("\nReading the entire file at onces...")
test_file = open("day04/read_it.txt", "r")
whole_thing = test_file.read()
print(whole_thing)
test_file.close()

print("\nReading chareacters from a line...")
text_file = open("day04/read_it.txt", "r")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()



print("\nReading one lin at a time...")
text_file = open("day04/read_it.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nRead the entire file into a list...")
text_file = open("day04/read_it.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("\nLooping through the file object...")
text_file = open("day04/read_it.txt", "r")
for line in text_file:
    print(line)
text_file.close()

input("\n\nPress the enter key to exit.")

