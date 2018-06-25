#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Exploit the built in complex type for map locations
    in a rectilinear toroidial geometry.
"""


#pragma pylint=off
    
# Credits
__author__ =        'George Flanagin'
__copyright__ =     'Copyright 2017 George Flanagin'
__credits__ =       'None. This idea has been around forever.'
__version__ =       '1.0'
__maintainer__ =    'George Flanagin'
__email__ =         'me+git@georgeflanagin.com'
__status__ =        'continual development.'
__license__ =       'MIT'

import typing
from   typing import *

import math
import random
import os
import sys

import globaldata

g = globaldata.GlobalData()

class Location:
    pass

class Location:

    def __init__(self, x:float, y:float) -> None:
        """
        Wrap a complex number.
        """
        self.p = complex(x,y)


    @property
    def x(self) -> float:
        return self.p.real

    
    @property
    def y(self) -> float:
        return self.p.imag


    def __str__(self):
        return "({}, {})".format(self.x, self.y)


    def __sub__(self, other:Location) -> Tuple[float, float]:
        """
        Compute the Cartesian distance between two locations.
        Take into account the seams in the world.

        returns -- (dist, heading)
        """

        try:
            v_x = other.x
            v_y = other.y
            
            x_dist = abs(self.x - other.x)
            if x_dist > g.half_x: 
                x_dist = g.x_dim - x_dist
                v_x = other.x - g.x_dim

            y_dist = abs(self.y - other.y)
            if y_dist > g.half_y: 
                y_dist = g.y_dim - y_dist
                v_y = other.y - g.y_dim

            return abs(complex(x_dist, y_dist)), math.atan2(v_y, v_x)

        except Exception as e:
            try:
                return self - Location(other)
            except Exception as e:
                return NotImplemented


if __name__ == "__main__":
    here = Location(111,900)
    locations = range(0,1000)
    for _ in range(0,10):
        there = Location(random.choice(locations), random.choice(locations))
        d, h = here-there
        print("From {} to {} is {} in direction {}".format(here, there, d, h))
else:
    pass

