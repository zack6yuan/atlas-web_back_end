#!/usr/bin/env python3
""" Basic Dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        self.cache_data = {}

    def put(self, key, item):
        """
        Arguments:
        self --> instance of the class
        key --> unique identifier
        item --> key-value pair
        
        Methods:
        Assigns key item value to the dictionary
        key || item (none) --> nothing executed
        """
        
        
        if (key, item) == None:
            return
        
        
    def get(self, key):
        """
        Arguments:
        self --> instance of the class
        key --> uniqie identifier
        
        Methods:
        key || item (none) --> nothing executed
        
        Returns:
        Value in self.cache_data linked to key
        """
        
        if (key == None or !(isinstance(key, self.cache_data)):
            
        