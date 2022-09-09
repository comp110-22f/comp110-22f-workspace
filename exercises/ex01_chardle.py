"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730470086"

secret: str = "heels"
compare: str = "e"
counter = 0

word: str = input("Enter a 5-character word: ")
if len(word) != len(secret):
    exit( print("Error: Word must contain 5 characters")) 

character: str = input("Enter a single character: ")
if len(character) != len(compare):
    exit( print("Error: Character must be a single character."))
else:
    print("Searching for " + character + " in " + word)

if character == word [0]:
    print(character + " found at index 0")
    counter = counter + 1
if character == word [1]:
    print(character + " found at index 1")
    counter = counter + 1
if character == word [2]:
    print(character + " found at index 2")
    counter = counter + 1
if character == word [3]:
    print(character + " found at index 3")
    counter = counter + 1
if character == word [4]:
    print(character + " found at index 4")
    counter = counter + 1
    
if counter == 0:
    print("No instances of " + character + " found in " + word )
else:
    print( str(counter) + " instances of " + character + " found in " + word)



    
