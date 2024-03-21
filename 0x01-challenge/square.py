#!/usr/bin/python3
"""Module level Documentation"""


class Square():
    """Class Implementation of a square
    Attrs:
        width: width of the square
        height: height of the square
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Class intialisation
        Params:
            kwargs: key word arguments used during object instantiation
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.height = self.width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String rep of a square object"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
