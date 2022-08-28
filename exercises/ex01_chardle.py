"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730311638"

initial_prompt: str = str(input("Enter a 5-character word character: "))

if len(initial_prompt) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = str(input("Enter a single character: "))

if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_character + " in " + initial_prompt)

if single_character == (initial_prompt)[1]:
    print( single_character + " found at index 1")

if single_character == (initial_prompt)[0]:
    print( single_character + " found at index 0 ")

if single_character == (initial_prompt)[2]:
    print( single_character + " found at index 2") 

if single_character == (initial_prompt)[3]:
    print( single_character + " found at index 3")

if single_character == (initial_prompt)[4]:
    print( single_character + " found at index 4")

count: int = 0

if initial_prompt[0] == single_character:
    count = count + 1

if initial_prompt[1] == single_character:
    count = count + 1

if initial_prompt[2] == single_character:
    count = count + 1

if initial_prompt[3] == single_character:
    count = count + 1

if initial_prompt[4] == single_character:
    count = count + 1

if count == 1:
    print( str(count) + " instance of " + single_character + " in " + initial_prompt)

if count > 1:
    print( str(count) + " instances of " + single_character + " in " + initial_prompt)

if count == 0:
    print("No instances of " + single_character + " in " + initial_prompt)









































