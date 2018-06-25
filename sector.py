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
import globaldata

g = globaldata.Globals()

class Sector:
    pass

class Sector:
    __slots__ = [
        'owner', 'civ_pop', 'mil_pop', 'elevation', 
        'guns', 'shells', 'planes', 'ore', 'sample_rate',
        'efficiency', 'movement_time', 'update_time',
        'type', 'location', 'island', 'materiel', 'dock',
        'sector_type'
        ]

    
    TYPES = '!GEMR+UFC_^DP'
    FACTORIES = 'GEPDM'


    def __init__(self, island:int=0, coordinates:location.Location = complex(0,0))
        """
        Build an empty sector.
        """
        self.owner = 0
        self.civ_pop = 0
        self.mil_pop = 0
        self.elevation = 1
        self.location = coordinates
        self.island = island
        self.sector_type = '_'

        # Stuff in the sector.
        self.guns = 0
        self.shells = 0
        self.planes = 0
        self.ore = 0
        self.sample_rate = 0
        self.dock = 0

        self.efficiency = 0.01
        self.movement_time = 0
        self.update_time = 0

        # This class member is the acrual of production. If the
        # sector is a factory, then that item will be set to 
        # point to this value. 
        self.materiel = 0


    def designate(self, sector_type:str) -> bool:
        """
        Change the sector_type.
        """
        if sector_type in Sector.TYPES: 
            self.sector_type = sector_type
            return True

        return False


    def update(self, update_exp:int, update_base:float) -> tuple:
        """
        Grow the efficiency and civilian population of the
        sector until each reaches its limit, and efficiency
        becomes production in factory sectors.
        """
        
        delta_efficiency = ( 0 
            if self.efficiency == 1.0 
            else (1 - self.efficiency) * 100 )

        update_for_efficiency = min(update_exp - delta_efficiency, delta_efficiency)
        update_for_production = update_exp - update_for_efficiency        

        """ Grow the population """
        self.efficiency += update_for_efficiency
        limit_pop = g.max_civ_pop.get(self.sector_type, g.max_civ_pop['unowned'])
        self.civ_pop = min(self.civ_pop * 1.02 ** update_for_efficiency, limit_pop)
        
        if self.sector_type in Sector.FACTORIES:
            pass
            
        
