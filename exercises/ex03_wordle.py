"""Wordle."""
__author__ = "730311638"


def contains_char(guess: str, character: str) -> bool:
    """Given string of any length, single character will be searched for in that string."""
    i: int = 0
    assert len(character) == 1
    while i < len(guess):
        if character == guess[i]:
            return True 
        i += 1
    return False 


def emojified(guess: str, secret: str) -> str:
    """Given 2 strings of equal length, returns a string of emojis coding whether correct letter was used."""
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    GREEN_BOX: str = "\U0001F7E9"
    EMOJI: str = ""
    i: int = 0 
    assert len(guess) == len(secret)
    while i < len(secret): 
        if guess[i] == secret[i]:
            EMOJI = EMOJI + GREEN_BOX
        if contains_char(secret, guess[i]) == True:
            EMOJI = EMOJI + YELLOW_BOX
        else: 
            EMOJI = EMOJI + WHITE_BOX
        i += 1
    return EMOJI


def input_guess(expected_length: int) -> str:
    """Given an integer, prompts the user for a guess and continues until they provide guess of expected length."""
    GUESS: str = input("Enter a " + str(expected_length) + " character word: ")
    while len(GUESS) != expected_length:
        GUESS = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    if len(GUESS) == expected_length:
        return GUESS


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    N: int = 1
    GUESS: str = ""
    while N <= 6 and GUESS != secret:
        print("=== Turn " + str(N) + "/6 ===")
        GUESS = input_guess(5)
        emoji: str = emojified(GUESS, secret)
        print(emoji)
        if GUESS == secret:
            number: str = str(N)
            print("You won in " + number + "/6 turns!")
        N = N + 1
    quit()



if __name__ == "__main__":
    main()  