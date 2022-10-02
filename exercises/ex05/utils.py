"""Practice on Utils and Unit Tests."""


__author__ = "730553672"


def only_evens(evens: list[int]) -> list[int]:
    """When given a list of integers, returns the even integers."""
    return_list: list[int] = list()
    indices: int = 0
    while indices < len(evens):
        if evens[indices] % 2 == 0:
            return_list.append(evens[indices])
        else:
            return_list = return_list
        indices += 1
    return return_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Combines two lists without modifying the original two lists."""
    indices: int = 0
    new_list: list[int] = list()
    while indices < len(list_one):
        new_list.append(list_one[indices])
        indices += 1
    second_index: int = 0
    while second_index < len(list_two):
        new_list.append(list_two[second_index])
        second_index += 1
    return new_list


def sub(integer_list: list[int], start_indices: int, end_indices: int) -> list[int]:
    """When given a list, a start index, and end index, a new subset is created."""
    if start_indices < 0:
        start_indices = 0 
    if end_indices > len(integer_list):
        end_indices = len(integer_list)  
    if len(integer_list) == 0 or start_indices >= len(integer_list) or end_indices <= 0:
        return list()
    subset: list[int] = list()
    while start_indices < end_indices:
        subset.append(integer_list[start_indices])
        start_indices += 1
    return subset