"""A spin-off of Wordle where the user gets one guess."""
__author__ = "730574292"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
len_secret_word: int = len(secret_word)
user_guess: str = input(f"What is your {str(len_secret_word)}-letter guess? ")

while len(user_guess) != len_secret_word:
    user_guess = input(f"That was not {str(len_secret_word)} letters! Try again: ")

idx: int = 0
searching: bool = True         # The boolean variable, searching, keeps track if we are still searchinging to see which box should be printed (green, white, or yellow).
wordle_boxes: str = ""

while idx < len_secret_word:
    if user_guess[idx] == secret_word[idx]:
        wordle_boxes += GREEN_BOX             # Concatenates green box to output of wordle boxes. 
        searching = False
    else:
        tmp_idx: int = 0                         # Creates a temporary index variable for indexing through the guess for comparison against the secret word.
        while tmp_idx < len_secret_word and searching:
            if user_guess[idx] == secret_word[tmp_idx] and idx != tmp_idx:
                wordle_boxes += YELLOW_BOX     # Concatenate yellow box to output of wordle boxes. 
                searching = False
            else:
                tmp_idx += 1
        if searching:
            wordle_boxes += WHITE_BOX             # Concatenates white box to output of wordle boxes. 
    idx += 1
    searching = True

print(wordle_boxes)

if user_guess != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")