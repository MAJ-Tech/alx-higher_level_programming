#!/usr/bin/python3
def uppercase(str):
    capital = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            capital += chr(ord(char) - 32)
        else:
            capital += char
    print("{}".format(capital))
