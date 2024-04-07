#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and implements
    a caching system using LRU eviction """

    def __init__(self):
        """ Initializes the LRUCache """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            iru_key = self.usage_order.pop(0)
            del self.cache_data[iru_key]
            print("DISCARD:", iru_key)

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
