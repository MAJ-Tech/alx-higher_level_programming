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
    def __init__(self, size=0, position=(0,0)):
        """
        The Constructor of the class Square

        Parameters:

        size (int): The size of the square
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for the instance attribute position.

        Returns:
           tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the instance attribute position.

        Parameters:
          value(tuple): A tuple of two positive integers.

        Raises:
          TypeError: If position is not a tuple two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            if not all(isinstance(i, int) and i >= 0 for i in value):
                raise TypeError("position must be tuple of 2 positive \
                       integers")
        self.__position = value

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
