"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730570002"

word: str = (input("Enter a 5-character word "))
char: str = (input("Enter a single character "))
number: int = 0

if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

if (len(char) != 1):
    print("Error: Character must be a single character. ")
    exit()

print("Searching for " + char + " in " + word)

if char == word[0]:
    print(char + " found at index 0")
    number = number + 1

if char == word[1]:
    print(char + " found at index 1")
    number = number + 1

if char == word[2]:
    print(char + " found at index 2")
    number = number + 1

if char == word[3]:
    print(char + " found at index 3")
    number = number + 1

if char == word[4]:
    print(char + " found at index 4")
    number = number + 1

if number == 0:
    print("No instances of " + char + " found in " + word)
else: 
    if number == 1:
        print(str(number) + " instance of " + char + " found in " + word)
    else:
        print(str(number) + " instances of " + char + " found in " + word)
    
