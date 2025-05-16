#!/usr/bin/env python3
"""LFUCache module that implements a LFU caching system."""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache is a caching system that evicts the least frequently used item.
    If multiple items have the same frequency, it evicts the least recently
    used.
    """

    def __init__(self):
        """Initialize the cache, frequency tracker, and usage order."""
        super().__init__()
        self.freq = {}
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using LFU eviction strategy.
        If multiple keys have the same frequency, use LRU to decide which one
        to discard.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.freq.values())
            lfu_keys = [k for k in self.freq if self.freq[k] == min_freq]
            for k in self.order:
                if k in lfu_keys:
                    discard = k
                    break
            self.cache_data.pop(discard)
            self.freq.pop(discard)
            self.order.remove(discard)
            print(f"DISCARD: {discard}")

        self.cache_data[key] = item
        self.freq[key] = 1
        self.order.append(key)

    def get(self, key):
        """
        Retrieve item by key and update frequency and usage order.
        Return None if key is not found or is None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
