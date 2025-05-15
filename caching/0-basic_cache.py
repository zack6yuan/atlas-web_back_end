#!/usr/bin/env python3
""" Basic Dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache Class 
    
    Methods:
    put --> assigns key item value to dictionary
    get --> get value of self.cache_data
    """

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
        if key is None and item is None:
            return
        if item not in self.cache_data:
            self.cache_data[key] = item


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
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data:
            return self.cache_data[key]