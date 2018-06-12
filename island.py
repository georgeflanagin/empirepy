#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is a base class for manipulating all sqlite databases.
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

import json

import globaldata
import location

class Island:
    pass


class Island:
    
    def __init__(self, **kwargs:dict) -> None:

        self.number = kwargs.get('number', 0)
        self.discovered_by = kwargs.get('discovered_by', 0)
        self.name = kwargs.get('name', 'unnamed')
        self.lower_left = kwargs.get('lower_left', complex(0,0))
        self.top_right = kwargs.get('top_right', complex(0,0))

        """ 
        Experience has shown that pre-calculating a number of values
        makes for cleaner code.
        """

        self.x_dim = self.top_right.x - self.lower_left.x
        self.y_dim = self.top_right.y - self.lower_left.y
        self.top_left = location.Location(self.lower_left.x, self.top_right.y)
        self.lower_right = location.Location(self.top_right.x, self.lower_left.y) 
        self.left = self.lower_left.x
        self.right = self.top_right.x
        self.bottom = self.lower_left.y
        self.top = self.top.right.y


    @classmethod
    def import_data(cls, data:str) -> Island:
        kw = json.reads(data)
        return Island(data)


    def __matmul__(self, other:Island) -> bool
        """
        Determine if these two islands meet the minimum separation
        requirements. Returns True if they are sufficiently far
        apart, and False otherwise.
        """
        g = globaldata.GlobalData()
        if not isinstance(other, Island): return NotImplemented

        if ( self.top + g.island_sep < other.bottom or 
             self.bottom > other.top + g.island_sep ): return True
        if ( self.left > other.right + g.island_sep or 
             self.right + g.island_sep < other.left ): return True
        
        return False


                
        
        
