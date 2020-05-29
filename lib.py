"""
Geometron3D
Author: DracoY

The library file to contain classes and functions.
"""
import math

class locate:
    """ The class to locate a coordinate on Cartesian plane. """    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        """ Method to calculate distance between two locations. """
        a = (self.x - other.x) ** 2
        b = (self.y - other.y) ** 2
        c = (self.z - other.z) ** 2

        result = math.sqrt( a + b + c )
        return round(result, 2)

    def mid_pt(self, other):
        """ Method to find midpoint of two coordinates. """
        a = (self.x + other.x) / 2
        b = (self.y + other.y) / 2
        c = (self.z + other.z) / 2

        result = (a, b, c)
        return result

    def section(self, other, m, n):
        """ Method to find location using section formula. """
        a = (self.x * n  +  other.x * m) / (m + n)
        b = (self.y * n  +  other.y * m) / (m + n)
        c = (self.z * n  +  other.z * m) / (m + n)

        result = (a, b, c)
        return result

def to_locate(seq):
    """ Method to convert a sequence into locate object. """
    if len(seq) == 3:
        return locate( seq[0], seq[1], seq[2] )
    else:
        raise TypeError

# Constants
ORIGIN = locate(0, 0, 0)