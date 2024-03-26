#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    '''
    Replaces or adds key/value in a dictionary.

    :param a_dictionary: The dictionary to be updated.
    :param key: The key to be replaced or added.
    :param value: The value corresponding to the key.
    '''
    if key in a_dictionary.keys():
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
