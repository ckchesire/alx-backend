#!/usr/bin/env python3
"""MRUCache module that implements a MRU caching system."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache - caching system that evicts the most recently used item (MRU).
    """

    def __init__(self):
        """Initialize the cache and usage tracking."""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        MRU eviction strategy.
         - Discards the most recently used item if cache exceeds MAX_ITEMS.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.usage_order[-2]
            self.usage_order.remove(mru_key)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Retrieve item by key and update its usage order.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
