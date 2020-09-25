# Ceiling Function
import sys


class TreeNode:
    def __init__(self, v=None, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right


class Tree:
    def __init__(self, xs):
        self.root = None
        for x in xs:
            self.insert(x)

    def insert(self, v):
        if self.root is None:
            self.root = TreeNode(v)
            return
        node = self.root
        while True:
            if node.v < v:
                if node.right is None:
                    node.right = TreeNode(v)
                    break
                else:
                    node = node.right
            else:
                if node.left is None:
                    node.left = TreeNode(v)
                    break
                else:
                    node = node.left

    def traverse_index_preorder(self):
        def loop(node, idx):
            acc.append(idx)
            if node.left:
                loop(node.left, idx * 2)
            if node.right:
                loop(node.right, idx * 2 + 1)

        acc = []
        loop(self.root, 1)
        return tuple(acc)


def solve(xs_list):
    shapes = [Tree(xs).traverse_index_preorder() for xs in xs_list]
    return len(set(shapes))


def main():
    stdin = sys.stdin
    N, _ = [int(x) for x in stdin.readline().split()]
    xs_list = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    print(solve(xs_list))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
5 3
2 7 1
3 1 4
1 5 9
2 6 5
9 7 3
    '''.strip(),
     '''
4
     '''.strip()),
    ('''
3 4
3 1 2 40000
3 4 2 1
33 42 17 23
    '''.strip(),
     '''
2
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
