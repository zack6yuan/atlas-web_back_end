#!/usr/bin/env python3
""" FIFO Caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Cache Class
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Arguments:
        self --> instance of the class
        key --> unique identifier
        item --> key-value pair
        
        Methods:
        Assigns key item value to the dictionary
        key || item (none) --> nothing executed
        if num(items) of self.cache_data > BaseCaching.MAX_ITEMS...
        Discard first item and print according to format
        """
        if key is None and item is None:
            return
        if item not in self.cache_data:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(0)
            print("DISCARD: {}").format(key)
        
        
    def get(self, key):
        """
        Arguments:
        self --> instance of the class
        key --> uniqie identifier
        
        Methods:
        key || item (none) --> nothing executed
        
        Returns:
        Value in self.cache_data linked to key
        key || item (none) --> return None
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]