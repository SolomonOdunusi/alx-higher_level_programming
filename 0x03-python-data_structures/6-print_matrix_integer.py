#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print("{:d}".format(row[column]), end="")
             if index != len(row) - 1:
                print(" ", end="")
        print()
