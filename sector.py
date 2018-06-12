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

import location

class Sector:
    pass

class Sector:
    __slots__ = [
        'owner', 'civ_pop', 'mil_pop', 'elevation', 
        'guns', 'shells', 'planes', 'ore', 
        'efficiency', 'movement_time', 'update_time'
        'type', 'location', 'island'
        ]

    def __init__(self, **kwargs)
        self.owner = kwargs.get('owner', 0)
        self.civ_pop = kwargs.get('civ_pop', 0)
        self.mil_pop = kwargs.get('mil_pop', 0)
        self.elevation = kwargs.get('elevation', 1)
        self.guns = kwargs.get('guns', 0)
        self.shells = kwargs.get('shells', 0)
        self.planes = kwargs.get('planes', 0)
        self.ore = kwargs.get('ore', 0)
        self.efficiency = kwargs.get('efficiency', 0.01)
        self.movement_time = kwargs.get('movement_time', 0)
        self.update_time = kwargs.get('update_time', 0)
        self.type = kwargs.get('type', '_')
        self.location = kwargs.get('location', complex(0,0))
        self.island = kwargs.get('island', 0)

    @classmethod
    def import_data(cls, data:str) -> Sector:
        pass
