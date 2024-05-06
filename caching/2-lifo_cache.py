#!/usr/bin/env python3
"""Create a class LIFOCache that inherits from BaseCaching
and is a caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching system that implements the LIFO
    and inherits from BaseCaching.

    Attributes:
        cache_data (dict): A dictionary to store cached data.

    Methods:
        put(key, item): Add an item to the cache using LIFO
        get(key): Get an item from the cache
    """

    def __init__(self):
        """Initialize the LIFOCache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache using LIFO

        Args:
            key: The key to associate with the item
            item: The item to be cached
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = list(self.cache_data.keys())[-1]
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache

        Args:
            key: The key to retrieve the item

        Returns:
            item associated with the key if it exists, otherwise None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
