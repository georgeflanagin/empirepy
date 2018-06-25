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

import globaldata

g = globaldata.GlobalData()

class Ship:
    pass


class Ship:

    TYPES = [
        'pt', 'barge', 'ferry', 'minesweeper', 'destroyer',
        'freighter', 'liner', 'submarine', 'tanker', 'supertanker',
        'transport', 'cruiser', 'battleship', 'carrier'
        ]


    def __init__(self, **kwargs:dict) -> None:
        """
        Build a ship of a given type for a player.
        """
        self.ship_type = kwargs.get('ship_type')
        self.location = kwargs.get('location')
        self.owner = kwargs.get('owner')
        self.civilians = kwargs.get('civilians', 0)
        self.military = kwargs.get('military', 0)
        self.fuel = kwargs.get('ore', 0)
        

    
