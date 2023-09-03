#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """Matrix multiplication
    Args:
        m_a (list): matrix a
        m_b (list): matrix b
    Raises:
        TypeError: If m_a or m_b are not lists
        TypeError: If m_a or m_b are not lists of lists
        ValueError: If m_a or m_b are empty lists or matrices
        TypeError: If m_a or m_b contain a non int or float
        TypeError: If m_a or m_b are not rectangular
        ValueError: If m_a or m_b can't be multiplied
    Returns:
        list: matrix c
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return (m_c)
