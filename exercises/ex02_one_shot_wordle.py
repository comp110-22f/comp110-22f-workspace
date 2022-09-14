"""EX02 - One Shot Wordle - Basically Almost Wordle"""

__author__ = "730470086"


secret: str = "python"
word: str = input(f"What is your {len(secret)}-letter guess? ")
counter: int = 0
emoji: str = ""
track_alt: int = 0
existence: bool = False

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


while len(secret) != len(word):
    word: str = input(f"That was not {len(secret)} letters! Try again: ")

if len(secret) == len(word):
    if secret == word:
        while counter < len(secret):
            if word[counter] == secret[counter]:
                emoji += green_box
            counter = counter + 1
        print(emoji)
        print("Woo! You got it!")
        quit()
    else:
        while existence is False and counter < len(secret):
            if track_alt == counter:
                existence: bool = True
            else:
                track_alt += 1
        if existence is True:
            emoji += yellow_box
        else: 
            emoji += white_box
        print(emoji)
        print("Not quite. Play again soon!")
        quit()


if secret != word:
    while existence is False and counter < len(secret):
        if track_alt == counter:
            existence: bool = True
        else:
            track_alt += 1
    if existence is True:
        emoji += yellow_box
    else: 
        emoji += white_box




while counter < len(secret):
            if word[counter] == secret[counter]:
                emoji += green_box
            else: 
                emoji += white_box
            counter = counter + 1