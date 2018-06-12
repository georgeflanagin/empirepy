#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Exploit the built in complex type for locations
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
        p = complex(x,y)


    @property
    def x(self) -> float:
        return p.real

    
    @property
    def y(self) -> float:
        return p.imag


    def __minus__(self, other:Location) -> float:
        """
        Compute the Cartesian distance between two locations.
        Take into account the seams in the world. 
        """

        try:
            x_dist = abs(self.x - other.x)
            if x_dist > half_x: x_dist = abs(other.x - self.x)
            y_dist = abs(self.y - other.y)
            if y_dist > half_y: y_dist = abs(other.y - self.y)
            return abs(complex(x_dist, y_dist))

        except Exception as e:
            try:
                return self - Location(other)
            except Exception as e:
                return NotImplemented


