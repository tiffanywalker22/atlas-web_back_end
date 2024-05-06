#!/usr/bin/env python3
"""Create a class LRUCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A caching system that implements the LRU
    and inherits from BaseCaching

    Attributes:
        cache_data (dict): A dictionary to store cached data
        usage_order (list): A list to maintain the order
        of key usage for LRU

    Methods:
        put(key, item): Add an item to the cache using LRU
        get(key): Get an item from the cache
    """

    def __init__(self):
        """Initialize the LRUCache"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item to the cache using LRU

        Args:
            key: The key to associate with the item
            item: The item to be cached
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """Get an item from the cache

        Args:
            key: The key to retrieve the item

        Returns:
            The item associated with the key if it exists, otherwise None
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the usage order (move the key to the end of the list)
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
