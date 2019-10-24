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

    def test_base_id5(self):
        o = Base(89)
        self.assertEqual(o.id, 89)

    def test_json_string0(self):
        self.assertTrue(Base.to_json_string(None))

    def test_json_string1(self):
        self.assertTrue(Base.to_json_string([]))

    def test_json_string2(self):
        self.assertTrue(
            Base.to_json_string([{'id': 12}])
        )

    def test_json_string3(self):
        self.assertIsInstance(
            Base.to_json_string([{'id': 12}]),
            str
        )

    def test_json_from_json0(self):
        self.assertEqual(
            Base.from_json_string(None),
            []
        )

    def test_json_from_json1(self):
        self.assertEqual(
            Base.from_json_string("[]"),
            []
        )

    def test_json_from_json2(self):
        self.assertTrue(
            Base.from_json_string('[{"id": 89}]')
        )

    def test_json_from_json3(self):
        self.assertIsInstance(
            Base.from_json_string('[{"id": 89}]'),
            list
        )


if __name__ == "__main__":
    unittest.main()
