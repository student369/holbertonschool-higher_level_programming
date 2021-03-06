#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
import io
import os
import sys
import models.square as s
from models.square import Square
from models.base import Base as b


class TestSquare(unittest.TestCase):
    """Square class tests"""

    def setUp(self):
        """Classes to use in the next tests"""
        b._Base__nb_objects = 0
        self.o0 = Square(5)
        self.o1 = Square(2, 2)
        self.o2 = Square(3, 1, 3)
        b._Base__nb_objects = 0
        self.o3 = Square(5)
        b._Base__nb_objects = 0
        self.o4 = Square(5)
        b._Base__nb_objects = 0
        self.o5 = Square(10, 2, 1)
        self.o6 = Square(1, 1)
        self.o7 = Square(11)
        self.o8 = Square(12)

    def test_module_square_doc(self):
        """Test of the module doc"""
        self.assertTrue(len(s.__doc__) > 10)

    def test_class_square_doc(self):
        """Test of the class doc"""
        self.assertTrue(len(Square.__doc__) > 10)

    def test_init_rectangle_doc(self):
        """Test of the constructor doc"""
        self.assertTrue(len(Square.__init__.__doc__) > 10)

    def test_string0(self):
        """Test of the string format of the Square"""
        self.assertEqual(
            str(self.o0),
            "[Square] (1) 0/0 - 5"
        )

    def test_init_area0(self):
        """Test of the area method"""
        self.assertTrue(self.o0.area(), 25)

    def test_display0(self):
        """Test of display method"""
        cO = io.StringIO()
        sys.stdout = cO
        self.o0.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            cO.getvalue(),
            '#####\n#####\n#####\n#####\n#####\n'
        )

    def test_string1(self):
        """Test of the string format of the Square"""
        self.assertEqual(
            str(self.o1),
            "[Square] (2) 2/0 - 2"
        )

    def test_init_area1(self):
        """Test of the area method"""
        self.assertTrue(self.o1.area(), 4)

    def test_display1(self):
        """Test of display method"""
        cO = io.StringIO()
        sys.stdout = cO
        self.o1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            cO.getvalue(),
            '  ##\n  ##\n'
        )

    def test_string2(self):
        """Test of the string format of the Square"""
        self.assertEqual(
            str(self.o2),
            "[Square] (3) 1/3 - 3"
        )

    def test_init_area2(self):
        """Test of the area method"""
        self.assertTrue(self.o2.area(), 9)

    def test_display2(self):
        """Test of display method"""
        cO = io.StringIO()
        sys.stdout = cO
        self.o2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            cO.getvalue(),
            '\n\n\n ###\n ###\n ###\n'
        )

    def test_size_object3(self):
        """Test of the string format of the Square"""
        self.assertEqual(
            str(self.o3),
            "[Square] (1) 0/0 - 5"
        )

    def test_size3(self):
        """Test to the access to a property"""
        self.assertTrue(self.o3.size, 5)

    def test_size_setted3(self):
        """Test to a property changed"""
        self.o3.size = 10
        self.assertEqual(
            str(self.o3),
            "[Square] (1) 0/0 - 10"
        )

    def test_type_error_size(self):
        """Test of non numeric error"""
        with self.assertRaises(TypeError) as er:
            self.o3.size = "9"

        self.assertEqual(
            "width must be an integer",
            str(er.exception)
        )

    def test_size_object4(self):
        """Test of the string format of the Square"""
        self.assertEqual(
            str(self.o4),
            "[Square] (1) 0/0 - 5"
        )

    def test_string_update4(self):
        """Test of update method"""
        self.o4.update(10)
        self.assertEqual(
            str(self.o4),
            "[Square] (10) 0/0 - 5"
        )

    def test_string_update5(self):
        """Test of update method"""
        self.o4.update(1, 2)
        self.assertEqual(
            str(self.o4),
            "[Square] (1) 0/0 - 2"
        )

    def test_string_update6(self):
        """Test of update method"""
        self.o4.update(1, 2, 3)
        self.assertEqual(
            str(self.o4),
            "[Square] (1) 3/0 - 2"
        )

    def test_string_update7(self):
        """Test of update method"""
        self.o4.update(1, 2, 3, 4)
        self.assertEqual(
            str(self.o4),
            "[Square] (1) 3/4 - 2"
        )

    def test_dictionary5(self):
        """Test of the string format of the Square"""
        self.assertEqual(
            str(self.o5),
            "[Square] (1) 2/1 - 10"
        )

    def test_dictionary_ob5(self):
        """Test of to_dictionary method"""
        self.assertEqual(
            str(self.o5.to_dictionary()),
            "{'id': 1, 'x': 2, 'size': 10, 'y': 1}"
        )

    def test_dictionary_type11(self):
        """Test of to_dictionary method"""
        self.assertTrue(
            isinstance(
                self.o5.to_dictionary(),
                dict
            )
        )

    def test_dictionary_object6(self):
        """Test of the string format of the Square"""
        self.assertEqual(
            str(self.o6),
            "[Square] (2) 1/0 - 1"
        )

    def test_dictionary_object6_update(self):
        """Test of update method"""
        self.o6.update(**self.o5.to_dictionary())
        self.assertEqual(
            str(self.o6),
            "[Square] (1) 2/1 - 10"
        )

    def test_dictionary12(self):
        """Test to verify if both objects are the same"""
        self.assertFalse(self.o5 == self.o6)

    def test_area1(self):
        """Test to the area function"""
        self.assertEqual(
            self.o7.area(),
            121
        )

    def test_load_file(self):
        """Test to the load file"""
        path = "Square.json"
        if os.path.exists(path):
            os.remove(path)
        list_square = [self.o8]
        Square.save_to_file(list_square)
        out = Square.load_from_file()
        ous = ""
        for sqloc in out:
            ous = sqloc
            break
        self.assertEqual(str(ous), "[Square] (4) 0/0 - 12")


if __name__ == "__main__":
    unittest.main()
