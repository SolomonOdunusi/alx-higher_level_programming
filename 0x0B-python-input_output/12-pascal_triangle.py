#!/usr/bin/python3
def pascal_triangle(n):
    """
    The func returns a list of lists of integers
    representing the Pascals triangle of n
    """
    if n <= 0:
        return ([])
    if n == 1:
        return ([[1]])
    if n == 2:
        return ([[1], [1, 1]])
    else:
        list_list = [[1], [1, 1]]
        for i in range(2, n):
            list_list.append([1])
            for j in range(1, i):
                list_list[i].append(
                        list_list[i - 1][j - 1] + list_list[i - 1][j])
            list_list[i].append(1)
        return (list_list)
