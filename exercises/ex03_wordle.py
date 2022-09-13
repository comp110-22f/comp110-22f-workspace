"""Fully operational Wordle game where user gets six guesses!!"""

__author__ = "730574292"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(exp_len: int) -> str:
    """Prompts the user to provide a guess of the correct length (same length as the string that the user is trying to guess) and continues to prompt the user for a guess until it fits this parameter."""
    user_guess: str = input(f"Enter a {exp_len} character word: ")

    while len(user_guess) != exp_len:
        user_guess = input(f"That wasn't {exp_len} chars! Try again: ")
    
    return user_guess


def contains_char(word: str, char: str) -> bool:
    """This function takes an input of a word (string of any length) and a character (string containing one letter) and determines if the character is in the string. Returns a boolean."""
    assert len(char) == 1
    
    len_word: int = len(word)
    idx: int = 0
    while idx < len_word:
        if word[idx] == char:
            return True
        else: 
            idx += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of colored box emojis representing how close the user's guess was to the secret word."""
    assert len(guess) == len(secret)
    
    wordle_boxes = ""
    idx = 0

    while idx < len(secret):
        if guess[idx] == secret[idx]:
            wordle_boxes += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            wordle_boxes += YELLOW_BOX
        else:
            wordle_boxes += WHITE_BOX
        idx += 1
    
    return wordle_boxes


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret = "codes"
    win: bool = False
    turns: int = 1

    while turns <= 6 and not win:
        print(f"=== Turn {turns}/6 ===")
        user_guess: str = input_guess(len(secret))
        wordle_boxes: str = emojified(user_guess, secret)
        print(wordle_boxes)

        if user_guess == secret:
            win = True
        else:
            turns += 1

    if win:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()