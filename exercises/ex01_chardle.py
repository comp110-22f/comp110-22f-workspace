"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730574292"

user_word: str = input("Enter a 5-character word: ")
user_char: str = input("Enter a single character: ")

if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

if len(user_char) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + user_char + " in " + user_word)

char_instances: int = 0

if user_word[0] == user_char:
    print(user_char + " found at index 0")
    char_instances += 1
if user_word[1] == user_char:
    print(user_char + " found at index 1")
    char_instances += 1
if user_word[2] == user_char:
    print(user_char + " found at index 2")
    char_instances += 1
if user_word[3] == user_char:
    print(user_char + " found at index 3")       
    char_instances += 1
if user_word[4] == user_char:
    print(user_char + " found at index 4")
    char_instances += 1
    
if char_instances == 0:
    print("No instances of " + user_char + " found in " + user_word)
else:
    if char_instances > 1:
        print(str(char_instances) + " instances of " + user_char + " found in " + user_word)
    else:
        print(str(char_instances) + " instance of " + user_char + " found in " + user_word)
