#!/usr/bin/python3
"""
this is the main class
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''
    LRUCache class
    __init__(): Initializes the LRUCache object.
    put: Adds an item to the cache.
    get: Retrieves an item from the cache based on the key.
    '''

    def __init__(self):
        """
        this is the initialization method
        """
        super().__init__()

    def put(self, key, item):
        """
        this must assign to the dictionary
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        # Check if the number of items exceeds the maximum allowed
        if len(self.cache_data) > self.MAX_ITEMS:
            # Find and discard the most recently used item
            del self.cache_data[key]
            print(f"DISCARD: {key}\n")

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key) if key is not None else None