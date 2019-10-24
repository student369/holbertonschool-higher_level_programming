#!/usr/bin/python3
"""Unittest for Base class"""
from models import base as b
import unittest


class TestBase(unittest.TestCase):
    """Base class tests"""
    def setUp(self):
        o = b.Base(0)

    def tearDown(self):
        o = b.Base(0)

    def test_module_doc(self):
        self.assertTrue(len(b.__doc__) > 10)

    def test_class_doc(self):
        self.assertTrue(len(b.Base.__doc__) > 10)

    def test_init_doc(self):
        self.assertTrue(len(b.Base.__init__.__doc__) > 10)

    def test_base_id0(self):
        o = b.Base()
        self.assertEqual(o.id, 1)

    def test_base_id1(self):
        o = b.Base()
        self.assertEqual(o.id, 2)

    def test_base_id2(self):
        o = b.Base()
        self.assertEqual(o.id, 3)

    def test_base_id3(self):
        o = b.Base(12)
        self.assertEqual(o.id, 12)

    def test_base_id3(self):
        o = b.Base()
        self.assertEqual(o.id, 4)


if __name__ == "__main__":
    unittest.main(verbosity=1)
