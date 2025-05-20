#!/usr/bin/env python3
""" LRU (Least Recently Used) Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Cache Class
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
        Discard LRU item and print according to format
        """
        if key is None or item is None:
            return
        if item not in self.cache_data:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_item = self.cache_data.popitem()
            print("DISCARD: {}".format(lru_item))
        
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
        return self.cache_data[key]
