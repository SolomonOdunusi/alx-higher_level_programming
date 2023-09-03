#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix (list): List of lists
        div (int/float): Num to divide with

    Returns:
        list: List of lists of results of division.

    Raises:
        TypeError: If matrix is not a list of lists of ints or floats.
        TypeError: If matrix is not rectangular.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    len_of_row = set(len(row) for row in matrix)
    if len(len_of_row) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for row in matrix:
        new_list = [round((element / div), 2) for element in row]
        result.append(new_list)
    return (result)
