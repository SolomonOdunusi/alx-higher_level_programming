#!/usr/bin/env python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger:
    """Class to test the max_integer function
    """
    def test_positive_integers(self):
        """Function to test positive integers"""
        d_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(d_list), 5)

    def test_negative_integers(self):
        """Function to test negative integers"""
        d_list = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(d_list), -1)

    def test_reverse_list(self):
        """Function to test reverse list"""
        d_list = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(d_list), 5)
    
    def test_mixed_integers(self):
        """Function to test mixed integers"""
        d_list = [-1, 2, -3, 4, -5]
        self.assertEqual(max_integer(d_list), 4)

    def test_empty_list(self):
        """Function to test empty list"""
        d_list = []
        self.assertEqual(max_integer(d_list), None)

    def test_one_element(self):
        """Function to test one element"""
        d_list = [1]
        self.assertEqual(max_integer(d_list), 1)
    
    def test_floats(self):
        """Function to test floats"""
        d_list = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.assertEqual(max_integer(d_list), 5.0)

    def test_strings(self):
        """Function to test strings"""
        d_list = ["a", "b", "c", "d", "e"]
        self.assertEqual(max_integer(d_list), "e")

if __name__ == '__main__':
    unittest.main()
