#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        self.assertIsInstance(max_integer([]), type(None))
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
