#!/usr/bin/python3
"""
0-square.py

This is a module for practicing my first python classes and methods
"""


class Square:

    """
    This is an empty class that defines a square

    Attributes:
    size (int): The size of the Squares
    """
    def __init__(self, size=0):
        """
        The Constructor of the class Square

        Parameters:

        size (int): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the Instance Attribute size

        Attributes:
        None

        Returns:
        size (int): Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A setter method for the Class attribute SIZE

        Attributes:
        size (int): size of the square

        Returns:
        None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        This instance method returns the area of the square.

        Returns:
          int: Area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This instance method prints the square with the character '#'.

        If size is equal to 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
