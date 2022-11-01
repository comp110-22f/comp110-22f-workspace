"""Contains three functions, invert(), favorite_color(), and count() for EX07 assignment."""

__author__ = "730574292"

INITIALIZE_DICT_VAL: int = 1        # Value used to initialize new values in dictionaries as we track frequency.
CHECK_IF_EMPTY: int = 0             # Value used to check if dictionary is empty.


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, this function takes the keys and makes them values and makes values keys."""
    result_dict: dict[str, str] = {}

    for each in input_dict:
        print(f"{each}: {(each in result_dict)}")
        if input_dict[each] in result_dict:
            raise KeyError("Error. Multiple dictionary keys cannot be the same.")
        result_dict[input_dict[each]] = each

    print(result_dict)
    return result_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Given a dictionary of pepole (key) and their favorite color (value), returns the most frequent favorite color."""
    color_frequency: dict[str, int] = {}

    dict_val: str = ""
    # dict_val originally keeps track of the first value in the dictionary.
    # Eventually, it will help keep track of the most frequent color. 
    for each in input_dict:
        if len(color_frequency) == CHECK_IF_EMPTY:
            dict_val = input_dict[each]

        if input_dict[each] not in color_frequency:
            color_frequency[input_dict[each]] = INITIALIZE_DICT_VAL
        else:
            color_frequency[input_dict[each]] += INITIALIZE_DICT_VAL

    fave_color_frequency: int
    # fave_color_frequency is a integer that will contain the number of times the most frequent color appears.

    if len(input_dict) > CHECK_IF_EMPTY:
        fave_color_frequency = color_frequency[dict_val]
        for each in color_frequency:
            if color_frequency[each] > fave_color_frequency:
                fave_color_frequency = color_frequency[each]
                dict_val = each

    return dict_val


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the frequency of values in a list and returns the occurances in a dictionary."""
    output: dict[str, int] = {}
    for each in input_list:
        if each not in output:
            output[each] = INITIALIZE_DICT_VAL
        else: 
            output[each] += INITIALIZE_DICT_VAL
    
    return output