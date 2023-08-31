#!/usr/bin/python3
"""
Contains a function that divides element by element 2 lists.
"""


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.
    Args:
        my_list_1 (list): The first list to divide.
        my_list_2 (list): The second list to divide.
        list_length (int): The number of elements to divide in the lists.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    newList = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            newList.append(result)
    return (newList)
