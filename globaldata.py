#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This class is effectively a singleton representing 
    the game data.
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

import hashlib
import json
import time

import gkflib
from   gkflib import objectify

class GlobalData:

    ticks_per_day = 100
    seconds_per_tick = 24*60*60 / ticks_per_day

    island_sep = 5
    num_islands = 200
    x_dim = 1000
    y_dim = 1000
    half_x = x_dim / 2
    half_y = y_dim / 2

    max_players = 100
    max_island_dim = 40
    min_island_dim = 25
    ship_day_multiplier = 1.0
    update_base = 1.02
    update_ceiling = 100
    initial_update_cache = 100
    defender_advantage = 1.5

    ships = {
        "P":"PT boat",
        "b":"Barge",
        "f":"Ferry",
        "M":"Mine Sweeper",
        "D":"Destroyer",
        "F":"Freighter",
        "L":"Liner",
        "S":"Submarine",
        "T":"Tanker",
        "t":"Transport",
        "C":"Cruiser",
        "B":"Battleship",
        "+":"Carrier"
        }

    def attach_globals(key:str, **kwargs:dict) -> None:
        
        pass

    def __init__(self) -> None:
        return 

