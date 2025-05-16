#!/usr/bin/env python3
"""Module that implements LRU caching system.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system.
        - evicts the least recently used item (LRU).
    """

    def __init__(self):
        """Initialize the cache
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """LRU eviction strategy
            - Discards the least recently used item if cache exceeds MAX_ITEMS.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Retrieve item by key and update its usage order.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data.get(key)
