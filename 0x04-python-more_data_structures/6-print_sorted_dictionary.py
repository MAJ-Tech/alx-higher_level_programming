#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''
    A function that prints a dictionary by ordered keys.
    Parameters:
    a_dictionary(dictionary): dictionary to be printed.
    Returns:
    dictionary: None
    '''
    order_key = sorted(a_dictionary.keys())
    for key in order_key:
        print("{}: {}".format(key, a_dictionary[key]))
