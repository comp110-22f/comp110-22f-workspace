"""EX03 - Wordle."""

__author__ = "730470086"

counter: int = 0

def contains_car (a: str = input("Enter a word") , b: str = input("Enter a single charaacter ")) -> bool:
    """Returns True if character is in word."""
    if a == b:
        while counter < len(a):
            return True
    else:
        return False
