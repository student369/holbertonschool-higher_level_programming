#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        self.assertIsInstance(max_integer([]), type(None))
    def test_one_element(self):
        l = [11]
        self.assertEqual(max_integer(l), 11)
    def test_max_at_end(self):
        l = [1, 2, 3]
        self.assertEqual(max_integer(l), 3)
    def test_max_at_beginning(self):
        l = [3, 2, 1]
        self.assertEqual(max_integer(l), 3)
    def test_max_at_middle(self):
        l = [1, 3, 2]
        self.assertEqual(max_integer(l), 3)
    def test_one_negative(self):
        l = [1, 3, -1]
        self.assertEqual(max_integer(l), 3)
    def test_only_negatives(self):
        l = [-3, -2, -1]
        self.assertEqual(max_integer(l), -1)
    def test_not_imports(self):
        modu = __import__('6-max_integer')
        self.assertFalse("^[^__]" in list(dir(modu)))
    def test_not_max(self):
        fun = max_integer
        self.assertFalse("^[^__]" in list(dir(fun)))
    def test_only_integers(self):
        with self.assertRaises(TypeError) as ct:
            max_integer([1, 2, "3"])
        self.assertTrue("list must be a list of integers"\
                        in str(ct.exception))

if __name__ == "__main__":
    unittest.main()
