#!/usr/bin/python3
for ten in range(10):
    for uni in range(ten + 1, 10):
        print("{:02d}".format(ten * 10 + uni), end=", " if ten != 8 else "\n")
