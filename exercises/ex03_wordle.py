"""EX03 - Wordle."""

__author__ = "730470086"

counter: int = 0

def contains_char (word: str = input("Enter a word ") , character: str = input("Enter a single charaacter ")) -> bool:
    """Returns True if character is in word."""
    while counter < len(word):
        track: int = 0
        existence; bool = False
        while ((existence is False) & (track < len(word))):
            if word[counter] == character[counter]:
                existence = True 
            else:
                track += 1
    if existence is True:
        return True
    else:
        return False