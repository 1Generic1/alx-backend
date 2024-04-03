#!/usr/bin/python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and implements
    a caching system using FIFO eviction """

    def __init__(self):
        """ Initializes the FIFOCache """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.queue.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
