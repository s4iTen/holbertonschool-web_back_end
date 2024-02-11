#!/usr/bin/python3
"""
this is the main class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class represents a simple caching
    __init__(): Initializes the BasicCache object.
    put: Adds an item to the cache.
    get: Retrieves an item from the cache based on the key.
    """
    def __init__(self):
        """ this is the Initialization function"""
        super().__init__()

    def put(self, key, item):
        """
        add item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key) if key is not None else None
