#!/usr/bin/python
def replace_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific index."""
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
