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
        if item in self.cache_data:
            self.cache_data.update(item)
        if key or item is None:
            pass


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
        for (key, value) in self.cache_data:
            return value[key]
        if (key is None) or  not isinstance (key, self.cache_data):
            return None
