#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and implements
    a caching system using MRU eviction """

    def __init__(self):
        """ Initializes the MRUCache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = next(reversed(self.cache_data))
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
