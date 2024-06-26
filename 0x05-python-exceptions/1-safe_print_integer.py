#!/usr/bin/python3

def safe_print_integer(value):
    ''' Safe print a list of integers '''
    try:
        print("{:d}".format(value))
        return True
    except(ValueError, TypeError):
        return False
