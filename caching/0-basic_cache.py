#!/usr/bin/env python3
"""Task 0"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """ initialize BasicCache"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache

        Args:
            key: The key to associate with the item
            item: The item to be cached
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache

        Args:
            key: The key to retrieve the item

        Returns:
            Item associated with the key if exists, otherwise None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
