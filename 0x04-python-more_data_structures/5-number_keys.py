#!/usr/bin/python3

def number_keys(a_dictionary):
    '''
    Returns the number of keys in a dictionary.
    Parameters:
    a_dictionary (dictionary): dictionary to transverse.
    Returns:
    Int: numbers of key in the dictionary
    '''
    num_keys = 0
    for key in a_dictionary:
        num_keys += 1
    return num_keys
