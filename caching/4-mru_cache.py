#!/usr/bin/env python3
""" MRU (Most Recently Used) Caching """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRU Cache Class
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        
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
        Discard MRU item and print according to format
        """
        if not key or not item:
            return
        
        removed_item = 0
        
        if key in self.cache_data:
            self.cache_data.pop(key)
            self.cache_data[key] = item
            
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed_item, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(removed_item))
            
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
        key || item (none) --> return None
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        if key is None or key not in self.cache_data:
            return None
