#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
import io
import sys
import models.rectangle as r
from models.rectangle import Rectangle
from models.base import Base as b


class TestRectangle(unittest.TestCase):
    """Rectangle class tests"""

    def setUp(self):
        b._Base__nb_objects = 0
        self.o0 = Rectangle(10, 2)
        self.o1 = Rectangle(2, 10)
        self.o2 = Rectangle(10, 2, 0, 0, 12)
        self.o3 = Rectangle(4, 6)
        self.o4 = Rectangle(2, 2)
        b._Base__nb_objects = 0
        self.o5 = Rectangle(4, 6, 2, 1, 12)
        self.o6 = Rectangle(5, 5, 1)
        self.o7 = Rectangle(2, 3, 2, 2)
        self.o8 = Rectangle(3, 2, 1, 0)
        b._Base__nb_objects = 0
        self.o9 = Rectangle(10, 10, 10, 10)
        b._Base__nb_objects = 0
        self.o10 = Rectangle(10, 10, 10, 10)
        b._Base__nb_objects = 0
        self.o11 = Rectangle(10, 2, 1, 9)
        self.o12 = Rectangle(1, 1)

    def test_module_rectangle_doc(self):
        self.assertTrue(len(r.__doc__) > 10)

    def test_class_rectangle_doc(self):
        self.assertTrue(len(Rectangle.__doc__) > 10)

    def test_init_rectangle_doc(self):
        self.assertTrue(len(Rectangle.__init__.__doc__) > 10)

    def test_rectangle_id1(self):
        self.assertEqual(self.o0.id, 1)

    def test_rectangle_id2(self):
        self.assertEqual(self.o1.id, 2)

    def test_rectangle_id3(self):
        self.assertEqual(self.o2.id, 12)

    def test_type_error_width(self):
        with self.assertRaises(TypeError) as er:
            o = Rectangle("hello", 2)

        self.assertEqual(
            "width must be an integer",
            str(er.exception)
        )

    def test_type_error_heigth(self):
        with self.assertRaises(TypeError) as er:
            o = Rectangle(10, "world")

        self.assertEqual(
            "height must be an integer",
            str(er.exception)
        )

    def test_type_error_width_zero(self):
        with self.assertRaises(ValueError) as er:
            o = Rectangle(0, 2)

        self.assertEqual(
            "width must be > 0",
            str(er.exception)
        )

    def test_type_error_heigth_zero(self):
        with self.assertRaises(ValueError) as er:
            o = Rectangle(2, 0)

        self.assertEqual(
            "height must be > 0",
            str(er.exception)
        )

    def test_type_error_x_zero(self):
        with self.assertRaises(ValueError) as er:
            o = Rectangle(10, 10, -1, 2)

        self.assertEqual(
            "x must be >= 0",
            str(er.exception)
        )

    def test_type_error_y_zero(self):
        with self.assertRaises(ValueError) as er:
            o = Rectangle(10, 10, 2, -2)

        self.assertEqual(
            "y must be >= 0",
            str(er.exception)
        )

    def test_area_doc(self):
        self.assertTrue(len(r.Rectangle.area.__doc__) > 10)

    def test_area1(self):
        o = r.Rectangle(3, 2)
        self.assertEqual(
            o.area(),
            6
        )

    def test_area2(self):
        o = r.Rectangle(2, 10)
        self.assertEqual(
            o.area(),
            20
        )

    def test_area3(self):
        o = r.Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(
            o.area(),
            56
        )

    def test_display1(self):
        cO = io.StringIO()
        sys.stdout = cO
        self.o3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            cO.getvalue(),
            '####\n####\n####\n####\n####\n####\n'
        )

    def test_display2(self):
        cO = io.StringIO()
        sys.stdout = cO
        self.o4.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            cO.getvalue(),
            '##\n##\n'
        )

    def test_string1(self):
        self.assertEqual(
            str(self.o5),
            "[Rectangle] (12) 2/1 - 4/6"
        )

    def test_string2(self):
        self.assertEqual(
            str(self.o6),
            "[Rectangle] (1) 1/0 - 5/5"
        )

    def test_display3(self):
        cO = io.StringIO()
        sys.stdout = cO
        self.o7.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            cO.getvalue(),
            '\n\n  ##\n  ##\n  ##\n'
        )

    def test_display4(self):
        cO = io.StringIO()
        sys.stdout = cO
        self.o8.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            cO.getvalue(),
            ' ###\n ###\n'
        )

    def test_string_update0(self):
        self.assertEqual(
            str(self.o9),
            "[Rectangle] (1) 10/10 - 10/10"
        )

    def test_string_update1(self):
        self.o9.update(89)
        self.assertEqual(
            str(self.o9),
            "[Rectangle] (89) 10/10 - 10/10"
        )

    def test_string_update2(self):
        self.o9.update(89, 2)
        self.assertEqual(
            str(self.o9),
            "[Rectangle] (89) 10/10 - 2/10"
        )

    def test_string_update3(self):
        self.o9.update(89, 2, 3)
        self.assertEqual(
            str(self.o9),
            "[Rectangle] (89) 10/10 - 2/3"
        )

    def test_string_update4(self):
        self.o9.update(89, 2, 3, 4)
        self.assertEqual(
            str(self.o9),
            "[Rectangle] (89) 4/10 - 2/3"
        )

    def test_string_update5(self):
        self.o9.update(89, 2, 3, 4, 5)
        self.assertEqual(
            str(self.o9),
            "[Rectangle] (89) 4/5 - 2/3"
        )

    def test_string_update6(self):
        self.assertEqual(
            str(self.o10),
            "[Rectangle] (1) 10/10 - 10/10"
        )

    def test_string_update7(self):
        self.o10.update(height=1)
        self.assertEqual(
            str(self.o10),
            "[Rectangle] (1) 10/10 - 10/1"
        )

    def test_dictionary11(self):
        self.assertEqual(
            str(self.o11),
            "[Rectangle] (1) 1/9 - 10/2"
        )

    def test_dictionary_object11(self):
        self.assertEqual(
            str(self.o11),
            "[Rectangle] (1) 1/9 - 10/2"
        )

    def test_dictionary_ob11(self):
        self.assertEqual(
            str(self.o11.to_dictionary()),
            "{'x': 1, 'y': 9, 'id': 1, \
'height': 2, 'width': 10}"
        )

    def test_dictionary_type11(self):
        self.assertTrue(
            isinstance(
                self.o11.to_dictionary(),
                dict
            )
        )

    def test_dictionary_object12(self):
        self.assertEqual(
            str(self.o12),
            "[Rectangle] (2) 0/0 - 1/1"
        )

    def test_dictionary_object12_update(self):
        self.o12.update(**self.o11.to_dictionary())
        self.assertEqual(
            str(self.o12),
            "[Rectangle] (1) 1/9 - 10/2"
        )

    def test_dictionary12(self):
        self.assertFalse(self.o11 == self.o12)


if __name__ == "__main__":
    unittest.main()
