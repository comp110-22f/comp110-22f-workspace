"""EX02 - One shot wordle."""

__author__ = "730570002"

secret_word: str = "python"
guess: str = input("What is you " + str(len(secret_word)) + "-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0 
sw_index: int = 0  # the index of the secret_word
inside_word: bool = False

# testing whether or not the guess is the same length as the secret_word
while len(guess) != len(secret_word):
    guess = input("That was not " + str(len(secret_word)) + " letters! Try again: ")

# iterates through the length of both words and checks to see if the characters are equivalent at any given postition
while index <= (len(secret_word) - 1):
    if guess[index] == secret_word[index]:     
        print(GREEN_BOX, end="")
    else:
        # iterates through checking if a letter of the guess matches any of the other letters in the secret word
        while sw_index <= (len(secret_word) - 1):
            if guess[index] == secret_word[sw_index]:
                print(YELLOW_BOX, end="")
                inside_word = True
            sw_index += 1
        if inside_word is False:
            print(WHITE_BOX, end="")
    # resets the inside_word and sw_index back to their original values and shifts the index by 1 to the next character in the guess
    inside_word = False
    sw_index = 0  
    index += 1

if guess == secret_word:
    print("\nWoo! You got it!")
else:
    print("\nNot quite. Play again soon!")
