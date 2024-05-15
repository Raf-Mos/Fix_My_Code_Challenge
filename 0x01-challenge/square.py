#!/usr/bin/python3
"""
Code defining square class
and its methods for calculating area and perimeter.
"""


class square():
    """My square class."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Init the square class."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Permiter of the Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Resturns a string representation of the suare."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Main function to execut the square class """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
