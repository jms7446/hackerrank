from typing import List, Set, Dict
import pytest


# 252ms, 17.3MB (67%, 34%)
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 10000
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def _search(self, key):
        hash_key = self._hash(key)
        chain = self.table[hash_key]
        for i, (k, v) in enumerate(chain):
            if k == key:
                return chain, i
        return chain, None

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        chain, idx = self._search(key)
        if idx is None:
            chain.append((key, value))
        else:
            chain[idx] = (key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        chain, idx = self._search(key)
        if idx is not None:
            return chain[idx][1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        chain, idx = self._search(key)
        if idx is not None:
            chain.pop(idx)


def test():
    hm = MyHashMap()
    hm.put(1, 1)
    hm.put(2, 2)
    assert hm.get(1) == 1
    assert hm.get(3) == -1
    hm.put(2, 1)
    assert hm.get(2) == 1
    hm.remove(2)
    assert hm.get(2) == -1

