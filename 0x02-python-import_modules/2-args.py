#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and the list of its arguments."""
    import sys

    num_arguments = len(sys.argv[1:])
    index = 1
    if num_arguments == 0:
        print("{} arguments.".format(num_arguments))
    elif num_arguments == 1:
        print("{} argument:".format(num_arguments))
    else:
        print("{} arguments:".format(num_arguments))
    for arg in sys.argv[1:]:
        print("{}: {}".format(index, arg))
        index += 1
