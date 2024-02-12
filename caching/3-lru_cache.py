#!/usr/bin/python3
"""
this is the main class
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
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
        self.access_order = OrderedDict()

    def put(self, key, item):
        """
        this is the put method
        """
        if key is not None and item is not None:
            # Check if the cache is full
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item (LRU)
                lru_key = next(iter(self.access_order))
                del self.access_order[lru_key]
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item
            self.access_order[key] = None

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key) if key is not None else None
