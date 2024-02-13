#!/usr/bin/python3
""" Rectangle Module """


from models.base import Base


class Rectangle(Base):
    """ simple Rectangle
    Atrributes:
        number_of_instances: num of created instances
        print_symbol: # to draw rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor function for rectangle class
        :param:
        width: width of rectangle
        height: height if rectangle
        x:
        y:
        id:
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ alternative constructor retrun square w==h==s """
        return cls(size, size)

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        if type(value) is int:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter height """
        if type(value) is int:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def x(self):
        """ x getter """
        return (self.__x)

    def x(self, value):
        """ x setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def y(self):
        """ x getter """
        return (self.__y)

    def y(self, value):
        """ x setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ get the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ get the perimeter of rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def display(self):
        """ print rectangle as info for end usr """
        count = 0
        string = ""

        while count < self.__height:
            string += " " * self.__x + "#" * self.__width + "\n"
            count += 1
        for row in range(self.__y):
            string = "\n" + string
        print(string.rstrip())

    def __str__(self):
        """ print rectangle class string for debug or devepolper or eval"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height))
