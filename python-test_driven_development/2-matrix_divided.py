#!/usr/bin/python3
"""Matrix division module."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If rows of the matrix are not all the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists of float: New matrix with all values divided by div.
    """
    # Check div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check matrix
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        any(not all(isinstance(x, (int, float)) for x in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check row sizes
    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Divide elements
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
