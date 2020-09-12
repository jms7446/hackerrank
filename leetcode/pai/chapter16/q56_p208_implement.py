from typing import List, Set, Dict
import pytest


class TrieNode:
    def __init__(self):
        self.exist = False
        self.children = {}


# 164ms, 31.1MB (85%, 59%)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TrieNode()
                node = node.children[c]
        node.exist = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.exist

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


def test():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")
