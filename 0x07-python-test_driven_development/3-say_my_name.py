#!/usr/bin/python3
"""
This is a module for a function that prints
First and last name
"""
def say_my_name(first_name, last_name=""):
    """
    Prints a string with first_name and last_name

    Parameters:
    first_name(str): The first name to print
    last_name(str): The last name to print (default empty str)

    Raise:
    TypeError: When first_name or last_name is not a string

    Return:
    None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    message = "My name is {} {}"
    print(message.format(first_name, last_name))
