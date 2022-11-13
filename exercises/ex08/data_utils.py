"""Dictionary related utility functions."""

__author__ = "730311638"

from csv import DictReader
from fileinput import filename


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(data_rows: list[dict[str, str]], column_name: str) -> list[str]:
    """Produces a list of all values whose name is column_name."""
    result: list[str] = []
    i: int = 0
    while i < len(data_rows):
        for key in data_rows[i]:
            if key == column_name:
                result.append(data_rows[i][key])
        i += 1
    return result


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a list of rows into a dictionary of columns."""
    result: dict[str, list[str]] = {}
    i: int = 0
    value: list[str] = []
    while i < len(rows):
        for key in rows[i]:
            value = column_values(rows, key)
            result[key] = value
        i += 1
    return result
        

def head(x: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces a new column-based dict w only first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    i: int = 0
    for key in x: 
        n_values: list[str] = [] 
        while i < N:
            n_values.append(x[key][i])
            i += 1
        result[key] = n_values
        n_values = []
        i = 0
    return result


def select(x: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Produce a column based table w specific subset of original columns."""
    result: dict[str, list[str]] = {}
    i: int = 0
    value: list[str] = []
    while i < len(name):
        if name[i] in x:
                value = x[name[i]]
                result[name[i]] = value
        i += 1
    return result

# Not finished
def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines 2 column-based tables into one."""
    result: dict[str, list[str]] = {}
    values: list[str] = []
    value: list[str] = []
    for key in x:
        values = x[key]
        result[key] = values
    for key_2 in y:
        # need to add the given list to the already established parameter
        value = y[key_2]
        result[key_2] = value
    return result


def count(data: list[str]) -> dict[str, int]:
    """Counts the frequencies of data in given list."""
    result: dict[str, int] = {}
    for key in data:
        if key in result: 
            result[key] += 1
        else:
            result[key] = 1
    return result



    