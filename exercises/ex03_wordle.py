"""EX03 - Wordle."""

__author__ = "730470086"

def contains_char(word: str , character: str) -> bool:
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


def emojified(guess: str , secret: str) -> bool:
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
    else:
        while counter < len(secret):
            if guess[counter] == secret[counter]:
                emoji += green_box
            else:
                track: int = 0
                existence: bool = False
                while ((existence is False) & (track < len(secret))):
                    if guess[counter] == secret[track]:
                        existence = True
                    else:
                        track += 1
                if existence is True:
                    emoji += yellow_box
                else:
                    emoji += white_box
            counter += 1
            track = 0
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
    number: int = 5
    tries: int = 1
    turn: str = (f"=== Turn {tries}/6 ===")
    guess: str = input(f"Enter a {number} character word: ")
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    emoji: str = ""
    counter: int = 0
    while len(guess) != number:
        guess: str = input(f"That wasn't {number} chars! Try again: ")
    if len(guess) == number:
        print(f"{turn}")
        if guess == secret:
            while counter < len(secret):
                if guess[counter] == secret[counter]:
                    emoji += green_box
                counter = counter + 1
            print(f"{emoji}")
            print(f"You won in {tries}/6 turns!")
        else:
            while counter < len(secret):
                if guess[counter] == secret[counter]:
                    emoji += green_box
                else:
                    track: int = 0
                    existence: bool = False
                    while ((existence is False) & (track < len(secret))):
                        if guess[counter] == secret[track]:
                            existence = True
                        else:
                            track += 1
                    if existence is True:
                        emoji += yellow_box
                    else:
                        emoji += white_box
                tries += 1
                counter += 1
                track = 0
                guess: str = input(f"Enter a {number} character word: ")
            print(f"{emoji}")
