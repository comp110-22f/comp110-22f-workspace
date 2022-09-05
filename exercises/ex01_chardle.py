"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730470086"

word: str = input("Enter a 5-character word: ")
if word != len(4):
    exit( print("Error: Word must contain 5 characters")) 

character: str = input("Enter a single character: ")
if character != len(0):
    exit( print("Error: Character must be a single character")) 
print("Searching for " + character + " in " + word)

if character == word [0]:
    print(character + " found at index 0")
if character == word [1]:
    print(character + " found at index 1")
if character == word [2]:
    print(character + " found at index 2")
if character == word [3]:
    print(character + " found at index 3")
if character == word [4]:
    print(character + " found at index 4")
