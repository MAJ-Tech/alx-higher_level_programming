#!/usr/bin/python3
"""
This module divides all elements of a matrix and \
returns a new matrix of the divides integers and floats
"""


def matrix_divided(matrix, div):
    """
    This function divides all the elements of a matrix

    Parameters:
    matrix:([[int or floats],[int or floats]])- A matrix of list of lists of\
    integer or floats.
    div:(int or float)- A dividen of integer or float

    Returns:
    matrix: ([[int or floats]])- New matrix of the result of the division

    Raises:
    TypeError: if matrix or div is not integers or floats
    ZeroDivisionError: if div is equal to zero(0)
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers" +
                        "/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers" +
                        "/floats")
    if not all(all(isinstance(v, (int, float)) for v in r) for r in matrix):
        raise TypeError("Matrix must be a matrix (list of lists) of integers" +
                        "/floats")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(val/div, 2) for val in row]
        new_matrix.append(new_row)

    return new_matrix
