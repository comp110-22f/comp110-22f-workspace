"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730557115"

greeting: str = str(input("Enter a 5-character word: "))

if len(greeting) != 5: 
    print("Error: Word must contain 5 characters.")
    exit()

letter: str = str(input("Enter a single character: "))

if len(letter) != 1: 
    print("Error: Character must be a single character. ")
    exit()
print("Searching for " + letter + " in " + greeting)

counter_man: int = 0  

if letter == greeting[0]:
    print(letter + " found at index 0")
    counter_man = counter_man + 1 
if letter == greeting[1]:
    print(letter + " found at index 1")
    counter_man = counter_man + 1 
if letter == greeting[2]:
    print(letter + " found at index 2")
    counter_man = counter_man + 1 
if letter == greeting[3]:
    print(letter + " found at index 3")
    counter_man = counter_man + 1 
if letter == greeting[4]:
    print(letter + " found at index 4")
    counter_man = counter_man + 1 

if counter_man == 1: 
    print(str(counter_man) + " instance of " + letter + " found in " + greeting) 
if counter_man > 1: 
    print(str(counter_man) + " instances of " + letter + " found in " + greeting) 
if counter_man == 0: 
    print("No instances of " + letter + " found in " + greeting)