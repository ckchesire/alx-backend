#!/usr/bin/env python3
"""LIFOCache module to implement a LIFO caching system.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache, caching system that evicts the last added item (LIFO).
    """

    def __init__(self):
        """Initialize cache by calling parent constructor.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """LIFO eviction strategy.
           - Discards the most recently added item if cache exceeds MAX_ITEMS.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key and self.last_key in self.cache_data:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")
        self.last_key = key

    def get(self, key):
        """Retrieve item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
