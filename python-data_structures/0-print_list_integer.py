#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list."""
    for i in range(len(my_list)):
        if i != len(my_list) - 1:
            print("{:d}".format(my_list[i]), end="\n")
        else:
            print("{:d}".format(my_list[i]), end="\n")
