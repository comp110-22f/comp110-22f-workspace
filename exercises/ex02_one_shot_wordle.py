"""EX02 - One Shot Wordle - Basically Almost Wordle"""

__author__ = "730470086"


secret: str = "python"
word: str = input("What is your 6-letter guess? ")
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


while len(secret) != len(word):
    word: str = input("That was not 6 letters! Try again: ")

while len(secret) == len(word):
    if secret == word:
        print("Woo! You got it!")
        quit()
    else:
        print("Not quite. Play again soon!")
        quit()




