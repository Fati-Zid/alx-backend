#!/usr/bin/env python3
"""
LFU Cache module

This module provides the LFUCache class which implements a caching system with
Least Frequently Used (LFU) eviction policy. The class inherits from BaseCaching.
"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """
    LFUCache is a caching system that inherits from BaseCaching
    and uses LFU eviction policy.
    """

    def __init__(self):
        """
        Initialize the cache

        The initialization method sets up the cache data structure,
        usage count dictionary, and order list.
        """
        super().__init__()
        self.usage_count = {}
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache

        If the cache exceeds the maximum size, the least frequently used item
        is discarded. If multiple items have the same frequency, the least
        recently used item among them is discarded.

        Args:
            key (str): the key to identify the cache item
            item (any): the value to cache

        Returns:
            None
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.usage_count[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu_key = min(self.usage_count, key=lambda k: (self.usage_count[k], self.order.index(k)))
                    self.order.remove(lfu_key)
                    del self.cache_data[lfu_key]
                    del self.usage_count[lfu_key]
                    print("DISCARD: {}".format(lfu_key))
                self.usage_count[key] = 1
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """
        Get an item by key

        Retrieves the value from the cache and updates the usage count and order.

        Args:
            key (str): the key to identify the cache item

        Returns:
            any: the value in self.cache_data linked to the key, or None if key is None or doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        self.usage_count[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]