"""One Shot Wordle."""
__author__ = "730311638"

SECRET: str = "python"
GUESS: str = input(f"What is your {len(SECRET)} letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(GUESS) != len(SECRET):
    GUESS = input(f"That was not {len(SECRET)} letters! Try again: ")
if GUESS == SECRET:
    print("Woo! You got it!")
else:
    print("Not quite. Play again!")

i: int = 0 
EMOJI: str = ""
alternate_i: int = 0
guessed_character: bool = False

while i < len(SECRET):
    if GUESS[i] == SECRET[i]:
        EMOJI = EMOJI + GREEN_BOX
    else:
        while alternate_i < len(SECRET): 
            if SECRET[alternate_i] == GUESS[i]: 
                guessed_character = True
            alternate_i = alternate_i + 1
        if guessed_character is True:
            EMOJI = EMOJI + YELLOW_BOX
        else: 
            EMOJI = EMOJI + WHITE_BOX
    i = i + 1
    guessed_character = False
    alternate_i = 0
print(EMOJI)