"""EX02 - One shot wordle."""

__author__ = "730570002"

secret_word: str = "python"
guess: str = input("What is you " + str(len(secret_word)) + "-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
sw_index: int = 0
inside_word: bool = False

while len(guess) != len(secret_word):
    guess = input("That was not " + str(len(secret_word)) + " letters! Try again: ")

#iterates through the length of both words and checks to see if the characters are equivalent at any given postition
while index <= (len(secret_word) - 1):
    if guess[index] == secret_word[index]:     
        print(GREEN_BOX, end = "")
    else:
        #iterates checking if the current letter of the guess matches any of the other characters in the secret word
        while sw_index <= (len(secret_word) - 1):
            if guess[index] == secret_word[sw_index]:
                print(YELLOW_BOX, end = "")
                inside_word = True
            sw_index += 1
        if inside_word == False:
            print(WHITE_BOX, end = "")
    inside_word = False
    sw_index = 0  
    index += 1

if guess == secret_word:
    print("\nWoo! You got it!")
else:
    print("\nNot quite. Play again soon!")
