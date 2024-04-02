#!/usr/bin/python3

def best_score(a_dictionary):
    """
    a function that returns a key with the biggest integer value.
    """
    if not a_dictionary:
        return None
    max_score = max(a_dictionary, key=lambda k: int(a_dictionary[k]))
    return max_score
