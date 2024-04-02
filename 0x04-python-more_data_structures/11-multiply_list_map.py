#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Return a list of all values multiply by a number
    without using a loop
    """
    new_list = list(my_list[:])
    new_list = list(map(lambda x: x * number, new_list))
    return new_list
