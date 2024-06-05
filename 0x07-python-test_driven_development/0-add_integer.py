#!/usr/bin/python3
""" This module contain a function ``add_integer`` that
adds two integers or floats."""


def add_integer(a, b=98):
    """
    Add two integers or floats after casting them to integers.

    Parameters:
    a:(int or float)- The first number to add.
    b:(int or flaot)- The second number to add, default is 98.

    Returns:
    int: The result of adding a and b.

    Raises:
    TypeError: If a or b are not integers or floats.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
