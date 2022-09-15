"""EX03 - Wordle."""

__author__ = "730470086"

def contains_char (word: str , character: str) -> bool:
    """Returns True if character is in word."""
    assert len(character) == 1
    while counter < len(word):
        track: int = 0
        existence: bool = False
        counter: int = 0
        while ((existence is False) & (track < len(word))):
            if word[counter] == character:
                existence = True
            else:
                track += 1
        if existence is True:
            return True
        else:
            return False
    counter += 1
    track = 0