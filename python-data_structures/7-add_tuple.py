#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples.

    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.

    Returns:
        tuple: A new tuple with the sum of the two tuples.
    """
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
