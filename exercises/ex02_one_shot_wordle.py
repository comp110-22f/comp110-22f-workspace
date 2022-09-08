"""One-shot wordle - loops!"""

__author__ = "730557115"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
guess: str = str(input("What is your 6-letter guess? "))

# This tests to see if the length of the user's guess is the length of the secret word.
while len(guess) != len(secret_word):   
    guess = input (f"That was not {len(secret_word)} letters! Try again: ")

indexer: int = 0
result: str = ""

# Here the computer is checking if the letter in the guess fits the letter in the secret word
while indexer < len(secret_word): 
    if guess[indexer] == secret_word[indexer]: 
        result += GREEN_BOX
    else: 
        i: int = 0 
        placement: bool = False 
        while i < len(secret_word): 
            if guess[indexer] == secret_word[i]: 
                placement = True 
            i += 1
            # This should print the yellow box if correct letter!
        if placement:
            result += YELLOW_BOX 
            # If wrong placement and letter then prints white block..
        else: 
            result += WHITE_BOX
    indexer += 1
print(result)

if guess == secret_word:
    print("Woo! You got it! ")
else: 
    print("Not quite. Play again soon!")