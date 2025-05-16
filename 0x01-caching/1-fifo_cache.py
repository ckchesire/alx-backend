#!/usr/bin/env python3
"""FIFOCache implements a FIFO caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Caching system that evicts the oldest item (FIFO).
    """

    def __init__(self):
        """Initialize by calling parent constructor
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Implements FIFO eviction strategy
            - Discards the oldest item if cache exceeds MAX_ITEMS.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.order.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """Retrieve item by key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
