"""Dictionary related utility functions."""

__author__ = "730574292"

from csv import DictReader
from io import TextIOWrapper

def read_csv_rows(csv_path: str) -> list[dict[str, str]]:
    """Function reads a CSV file and returns its contents as a list of dictionaries with one dictionary being one row."""
    open_csv: TextIOWrapper = open(file=csv_path, mode="r", encoding="utf8")
    result: list[dict[str, str]] = []

    csv_reader = DictReader(open_csv)

    for row in csv_reader:
        result.append(row)

    open_csv.close()
    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Function retrieves the values of a given column from the list (acting as a table) given. Returns all values of that column."""
    column_vals: list[str] = []

    for row in table:
        column_vals.append(row[column_name])

    return column_vals


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Function transforms a table, making columns rows and rows columns. Outputs new column-oriented table."""
    result: dict[str, list[str]] = {}
    column_names: list[str] = []

    for each in table[0]:
        column_names.append(each)

    for column in column_names:
        result[column] = column_values(table, column)

    return result


def head(table: dict[str, list[str]], n_rows: int) -> dict[str, list[str]]:
    """Function takes a column-oriented table and an number of rows to include. Returns dictionary with specified rows per column."""
    result: dict[str, list[str]] = {}

    for column in table: 
        included_vals: list = []
        i: int = 0
        while i < n_rows and i < len(table[column]):
            included_vals.append((table[column])[i])
            i += 1
        result[column] = included_vals

    return result


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Function takes a column-oriented table and column names and returns only the columns specified in a new table."""
    result: dict[str, list[str, str]] = {}

    for column in column_names:
        result[column] = table[column]

    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Function takes two column-oriented tables and combines them. Returns the combined column-oriented table."""
    result: dict[str, list[str]] = {}

    for column in table1:
        result[column] = table1[column]

    for column in table2:
        if column in result:
            for each in table2[column]:
                result[column].append(each)
        else: 
            result[column] = table2[column]
    
    return result


def count(values: list[str]) -> dict[str, int]:
    """Function counts the frequency of a string in a list. Returns a dictionary of the string (key) and its frequency (value)."""
    frequency: dict[str, int] = {}

    for each in values:
        if each in frequency:
            frequency[each] += 1
        else: 
            frequency[each] = 1

    return frequency