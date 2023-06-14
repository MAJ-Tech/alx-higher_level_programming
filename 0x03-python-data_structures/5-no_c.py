#!/usr/bin/python3

def no_c(my_string):
    edited_output = my_string.translate({ord(i): None for i in 'cC'})
    return edited_output
