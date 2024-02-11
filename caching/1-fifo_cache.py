#!/usr/bin/python3
"""
this is the main class
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    __init__():Initializes the BasicCache object.
    put: Adds an item to the cache.
    get: Retrieves an item from the cache based on the key.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        add item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key) if key is not None else None
