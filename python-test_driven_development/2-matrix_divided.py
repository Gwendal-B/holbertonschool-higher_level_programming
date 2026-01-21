#!/usr/bin/python3
"""Matrix division module."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div."""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix) or
            any(not all(isinstance(x, (int, float)) for x in row)
                for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(x / div, 2) for x in row] for row in matrix]
