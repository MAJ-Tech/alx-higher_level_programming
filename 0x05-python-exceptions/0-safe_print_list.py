#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ''' Prints A list of any tyPE '''
    printed_elements = 0
    try:
        for i in range(x):
            print(my_list[i], end=' ')
            printed_elements += 1
    except IndexError:
        pass
    finally:
        print()
    return printed_elements
