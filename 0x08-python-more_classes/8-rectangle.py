#!/usr/bin/python3
""" Module 7-rectangle

Module that contains the class Rectangle
and a methods
"""


class Rectangle:
    """ Rectangle class

    A empty Rectangle class.

    Attributes:
        width (int): The rectangle width
        height (int): The rectangle height
        number_of_instances (int): The
            number of instances 0 by default.
        print_symbol (any): The symbol to print
            # by default.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Return a rectangle object

        Args:
            width (int): The rectangle width
            height (int): The rectangle height                             """
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """int: The width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""
        return (self.height * self.width)

    def perimeter(self):
        """Return a rectangle perimeter"""
        if self.height == 0 or self.width == 0:
            return (0)
        return (2 * (self.height + self.width))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the most biggest rectangle

        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an \
instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an \
instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return (rect_1)
        elif rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    def __str__(self):
        """Return a symbol like a character rectangle"""
        if self.height == 0 or self.width == 0:
            return ("")
        rec = ""
        for i in range(self.height):
            for j in range(self.width):
                rec = rec + str(self.print_symbol)
            rec = rec + "\n"
        return(rec[:-1])

    def __repr__(self):
        """Return a string representation
        of the Rectangle
        """
        return("Rectangle({:s}, {:s})"
               .format(str(self.width), str(self.height)))

    def __del__(self):
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
