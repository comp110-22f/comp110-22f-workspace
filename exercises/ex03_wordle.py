"""EX03 - Wordle."""

__author__ = "730470086"


def contains_char(word: str, character: str) -> bool:
    """Determines if character is in word."""
    assert len(character) == 1
    counter: int = 0
    while counter < len(word):
        if word[counter] == character:
            return True
        else:
            track: int = 0
            existence: bool = False
            while ((existence is False) & (track < len(word))):
                if word[counter] == character:
                    existence = True
                else:
                    track += 1
                    counter += 1
            track = 0
        if existence is True:
            return True
        else:
            return False


def emojified(guess: str, secret: str) -> str:
    """Provides emoji output."""
    assert len(guess) == len(secret)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    emoji: str = ""
    counter: int = 0
    if guess == secret:
        while counter < len(secret):
            if guess[counter] == secret[counter]:
                emoji += green_box
            counter = counter + 1
        return emoji
    while counter < len(secret):
        if guess[counter] == secret[counter]:
            emoji += green_box
        else:
            asses = contains_char(secret, guess[counter])
            if asses is True:
                emoji += yellow_box
            else:
                emoji += white_box
        counter += 1
    return emoji
        

def input_guess(number: int) -> str:
    """Prompts user for guess."""
    word: str = input(f"Enter a {number} character word: ")
    while len(word) != number:
        word: str = input(f"That wasn't {number} chars! Try again: ")
    if len(word) == number:
        return word


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    secret: str = "codes"
    counter: int = 1
    turn: str = (f"=== Turn {counter}/6 ===")
    while counter <= 6:
        print(f"{turn}")
        guess = input_guess(5)
        result = emojified(guess, secret)
        if guess == secret:
            print(f"You won in {counter}/6 turns!")
        else:
            counter += 1