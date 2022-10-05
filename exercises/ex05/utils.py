"""Funtions to be tested with test functions."""

__author__ = "730574292"


def only_evens(list_input: list[int]) -> list[int]:
    """Function takes a list of integers and returns a list of the even integers."""
    evens: list[int] = list()
    i: int = 0

    while i < len(list_input):
        if list_input[i] % 2 == 0:
            evens.append(list_input[i])
        i += 1

    return evens


def concat(input_one: list[int], input_two: list[int]) -> list[int]:
    """Function takes two list of integers and returns list of all of the integers of both lists in order of first list then second list."""
    final_list: list[int] = list()
    i: int = 0

    while i < len(input_one):
        final_list.append(input_one[i])
        i += 1
    
    i = 0
    
    while i < len(input_two):
        final_list.append(input_two[i])
        i += 1

    return final_list


def sub(list_input: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Function takes a list of ints and a start and end index. It then returns a new list of values in the list between these indices (end not included)."""
    final_list: list[int] = list()
    start_tmp: int = 0  # Will hold a copy of the starting index given by the user. 

    if start_idx > 0:
        start_tmp = start_idx

    while start_tmp < end_idx and start_tmp < len(list_input):
        final_list.append(list_input[start_tmp])
        start_tmp += 1
    
    return final_list