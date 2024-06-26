#!/usr/bin/env python3
""" LIFO Cache module """

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system that inherits from BaseCaching
        and uses LIFO eviction policy.
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                last_key = self.stack.pop()
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            if key not in self.cache_data:
                self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
