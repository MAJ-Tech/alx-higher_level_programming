#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Makes copy of a list, replce element at certain index in copy
       while leaving originial unmodified.
    """
    new_list = my_list[:]
    if 0 <= idx < len(my_list):
        new_list[idx] = element
    return new_list
