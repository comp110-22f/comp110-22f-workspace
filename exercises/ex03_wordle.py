"""EX03 - Wordle."""

__author__ = "730470086"

def contains_char (word: str , character: str) -> bool:
    """Returns True if character is in word."""
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

def emojified (guess: str , secret: str) -> bool:
    """d"""

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"