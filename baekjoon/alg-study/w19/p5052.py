import sys


class TrieNode:
    def __init__(self, children=None):
        self.exist = False
        self.children = children or {}


class NoDupPrefixStore:
    """"중복된 prefix를 가지는 word는 저장하지 않는 store"""
    def __init__(self):
        self.trie_root = TrieNode()

    def insert(self, word: str) -> bool:
        """return sucess/fail"""
        node = self.trie_root
        for idx, c in enumerate(word):
            if node.exist:
                # we found a substring of this word. So we shouldn't insert this word.
                return False
            if c in node.children:
                if idx == len(word) - 1:
                    # this word is subtring of other word. So we shouldn't insert this word.
                    return False
                else:
                    node = node.children[c]
            else:
                node.children[c] = TrieNode()
                node = node.children[c]
        node.exist = True
        return True


def solve(N, words):
    store = NoDupPrefixStore()
    for word in words:
        if not store.insert(word):
            return False
    return True


def main():
    stdin = sys.stdin
    T = int(stdin.readline())
    for _ in range(T):
        N = int(stdin.readline())
        nums = [stdin.readline().strip() for _ in range(N)]
        print('YES' if solve(N, nums) else 'NO')


if __name__ == "__main__":
    main()

from util import *
import pytest


def test_main():
    in_str = """
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
    """.strip()
    out_str = """
NO
YES
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main2():
    in_str = """
1
5
113
12340
123440
12345
98346
    """.strip()
    out_str = """
YES
    """.strip()
    assert mock_io(main)(in_str) == out_str


def test_main2():
    in_str = """
1
3
97625999
91125426
911
    """.strip()
    out_str = """
NO
    """.strip()
    assert mock_io(main)(in_str) == out_str


