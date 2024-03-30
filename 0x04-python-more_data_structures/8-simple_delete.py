#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    A function that deletes a key in a dictionary.

    :Param a_dictionary: The dictionary to be updated.
    :Param key: The key to be deleted.

    Returns:
    Dictionary: A dictionary where the key is deleted
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
