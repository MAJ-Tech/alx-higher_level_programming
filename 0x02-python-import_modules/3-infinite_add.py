#!/usr/bin/python3

if __name__ == "__main__":
    """A program that prints the result of the addition of all arguments. """
    import sys

    result = 0
    for arg in sys.argv[1:]:
        result += int(arg)
    print("{}".format(result))
