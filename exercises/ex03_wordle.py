"""EX03 - Wordle."""

__author__ = "730470086"

counter: int = 0

def contains_char (word: str , character: str) -> bool:
    """Returns True if character is in word."""
    assert len(character) == 1
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
            if existence is True:
                return True
            else:
                return False
        counter += 1
        track_alt = 0
