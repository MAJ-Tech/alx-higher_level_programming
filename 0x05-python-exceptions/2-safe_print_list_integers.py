#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ''' Safe print a list of integers '''
    printed_elements = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end=" ")
            printed_elements += 1

        except(TypeError, ValueError, IndexError):
            continue

    print()
    return printed_elements
