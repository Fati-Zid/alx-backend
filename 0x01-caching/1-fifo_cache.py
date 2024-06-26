#!/usr/bin/env python3
""" FIFO Cache module """

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system that inherits from BaseCaching
        and uses FIFO eviction policy.
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                first_key = self.queue.pop(0)
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))
            if key not in self.cache_data:
                self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
