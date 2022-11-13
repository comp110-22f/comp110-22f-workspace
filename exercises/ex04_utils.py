"""List Functions."""
__author__ = "730311638"


def all(xs: list[int], number: int) -> bool:
    """Given a list of integers and an integer, return bool whether or not all int in list are the same as the integer."""
    counter: int = 0
    if len(xs) == 0:
        return False
    while counter < len(xs):
        if xs[counter] == number:
            counter = counter + 1
        else:
            return False 
    return True


def max(input: list[int]) -> int:
    """Given a list of integers, the largest integer is returned."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    i_2: int = 1
    first_check: int = input[i]
    second_check: int = input[i_2]
    while i < len(input) and len(input) != 0: 
        if first_check > second_check:
            highest = first_check
        else: 
            highest = second_check
        i = i + 1
        i_2 = i_2 + 1
    return highest


def is_equal(one: list[int], two: list[int]) -> bool:
    """Given two lists of int values, return True is every element at every index is equal."""
    i: int = 0
    if len(one) != len(two):
        return False
    while i < len(one) and i < len(two):
        if one[i] == two[i]:
            i = i + 1
        else: 
            return False
    return True