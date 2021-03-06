#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list_is_empty(self):
        self.assertIsInstance(max_integer([]), type(None))

    def test_list_of_one_element(self):
        list_integers = [11]
        self.assertEqual(max_integer(list_integers), 11)

    def test_only_negative_numbers_in_the_list(self):
        list_integers = [-3, -2, -1]
        self.assertEqual(max_integer(list_integers), -1)

    def test_one_negative_number_in_the_list(self):
        list_integers = [1, 3, -1]
        self.assertEqual(max_integer(list_integers), 3)

    def test_max_in_the_middle(self):
        list_integers = [1, 3, 2]
        self.assertEqual(max_integer(list_integers), 3)

    def test_max_at_the_beginning(self):
        list_integers = [3, 2, 1]
        self.assertEqual(max_integer(list_integers), 3)

    def test_max_at_the_end(self):
        list_integers = [1, 2, 3]
        self.assertEqual(max_integer(list_integers), 3)


if __name__ == "__main__":
    unittest.main()
