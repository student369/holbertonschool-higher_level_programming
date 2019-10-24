#!/usr/bin/python3
"""Unittest for Base class"""
import models.base as b
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Base class tests"""
    def test_module_doc(self):
        self.assertTrue(len(b.__doc__) > 10)

    def test_class_doc(self):
        self.assertTrue(len(Base.__doc__) > 10)

    def test_init_doc(self):
        self.assertTrue(len(Base.__init__.__doc__) > 10)

    def test_base_id0(self):
        o = Base()
        self.assertEqual(o.id, 1)

    def test_base_id1(self):
        o = Base()
        self.assertEqual(o.id, 2)

    def test_base_id2(self):
        o = Base()
        self.assertEqual(o.id, 3)

    def test_base_id3(self):
        o = Base(12)
        self.assertEqual(o.id, 12)

    def test_base_id4(self):
        o = Base()
        self.assertEqual(o.id, 4)


if __name__ == "__main__":
    unittest.main()
