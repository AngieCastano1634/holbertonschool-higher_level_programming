#!/usr/bin/python3
"""

Module that defines a rectangle with width and heigth

"""


class Rectangle:
    """
    Class Rectangle beginnig
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Inizialization of class Rectangle
        width = Rectangle width. Heigth = Rectangle Heigth
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves Rectangle's width
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the Rectangle height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the Rectangle's width
        value = new Rectangle's width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height
        value = Rectangles height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        return Rectangle's perimeter
        """
        if self.__height == 0:
            return 0
        if self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        str method
        """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for h in range(self.__height):
            string += str(self.print_symbol) * self.__width
            if h != self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """
        Returns the “official” string representation of a Rectangle object
        """
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        """
        delets a Rectangle object
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if __class__ != type(rect_1):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if __class__ != type(rect_2):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with width == height == size
        size = square's height and width
        """
        return cls(size, size)
