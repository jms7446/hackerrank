import sys


class TrieNode:
    def __init__(self, children=None):
        self.exist = False
        self.children = children or {}


def check_and_insert(node: TrieNode, word: str):
    char_list = list(reversed(word))
    while char_list:
        if node.exist:
            return False
        c = char_list.pop()
        if c not in node.children:
            node.children[c] = TrieNode()
            node = node.children[c]
        elif not char_list:
            return False
        else:
            node = node.children[c]

    node.exist = True
    return True


def solve(N, words):
    trie_root = TrieNode()
    for word in words:
        if not check_and_insert(trie_root, word):
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


