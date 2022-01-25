"""
Maze Solver - Vector

This module implements vectors to represent points, dimensions and bounds in 3D space and other math operations
involving vectors.

Author: shravan@usc.edu (5451873903)

"""

import math


class Vector(object):
    """
    Module that implements vectors in 3D space.
    """

    def __init__(self, x=0, y=0, z=0):
        """
        Method to initialize a 3D vector.

        Args:
            x(int): X co-ordinate of the vector. Defaults to 0.
            y(int): Y co-ordinate of the vector. Defaults to 0.
            z(int): Z co-ordinate of the vector. Defaults to 0.

        """
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """
        Method to represent a vector as a string.

        Returns:
            (str): String representation of a vector.

        """
        return "({}, {}, {})".format(self.x, self.y, self.z)

    @staticmethod
    def from_str(s):
        """
        Method to get a vector from a string.

        Args:
            s(str): String to get the vector from. Example: "10 10 10".

        Returns:
            (vector): Vector generated from the string.

        """
        coords = s.split(' ')
        return Vector(int(coords[0]), int(coords[1]), int(coords[2]))


def distance(p1, p2):
    """
    Returns the distance between two points (as an integer).

    Args:
        p1(Vector): Point to get the distance for.
        p2(Vector): Point to get the distance for.

    Returns:
        (distance): Distance between the two points.

    """
    return int(math.sqrt(((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2) + ((p2.z - p1.z) ** 2)))
