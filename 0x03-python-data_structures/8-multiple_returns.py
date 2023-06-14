#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns tuple with len of string and first char"""
    len_sen = len(sentence)
    if sentence:
        first_char = sentence[0]
    else:
        first = None
    return (len_sen, first_char)
