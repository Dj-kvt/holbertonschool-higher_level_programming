#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The length of the lists.

    Returns:
        list: A new list containing the results of the division.
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
