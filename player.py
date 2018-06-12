#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This class is used to represent player data.
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

import location

"""
NOTE: I intend to move to msgpack, whereupon I will change
    these definitions.
"""
unserializer = json.reads
serializer = json.dumps

class Player:
    pass

class Player:

    __slots__ = [
        'number', 'home_island', 'email', 'phone',
        'password', 'salt', 
        'name', 'birth', 'death',
        'last_login', 'last_activity', 'last_seen', 'locked', 
        'map_x_offset', 'map_y_offset'
        ]

    @classmethod
    def import_data(cls, data) -> Player:
        kw = unserializer(data)
        player = Player(data)
        return player


    def __init__(self, **kwargs:dict) -> None:

        number = kwargs.get('number')
        home_island = kwargs.get('home_island')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        password = kwargs.get('password')
        salt = kwargs.get('salt')
        name = kwargs.get('name')
        birth = kwargs.get('birth')
        death = kwargs.get('death')
        last_login = kwargs.get('last_login')
        last_activity = kwargs.get('last_activity')
        last_seen = kwargs.get('last_seen')
        locked = kwargs.get('locked')

        map_x_offset = kwargs.get('map_x_offset')
        map_y_offset = kwargs.get('map_y_offset')


    def export_data(self) -> str:   
        """
        We only want the data elements.        
        """   
        return serializer(
            {_:getattr(self,_) for _ in Player.__slots__}
            )


    def check_password(self, password:str) -> bool:
        """
        Just hash and try the comparison. 
        """
        return (( hashlib.sha256(password + self.salt).hexdigest() ==
                self.password) and not self.locked)


    def player_coordinate(self, p:location.Location) -> location.Location:

        new_location = Location(p.x - self.map_x_offset, 
                                p.y - self.map_y_offset)

        new_x = (new_location.x 
                if new_location.x >= 0 
                else new_location.x + g.x_size )
        new_y = (new_location.y 
                if new_location.y >= 0
                else new_location.y + g.y_size )

        return location.Location(new_x, new_y)
        

    def absolute_coordinate(self, p:location.Location) -> location.Location:
        
        new_location = Location(p.x + self.map_x_offset,
                                p.y + self.map_y_offset)

        new_x = (new_location.x 
                if new_location.x <= g.x_size
                else new_location.x - g.x_size)
        new_y = (new_location.y
                if new_location.y <= g.y_size
                else new_location.y - g.y_size)
        
        return location.Location(new_x, new_y)

  
