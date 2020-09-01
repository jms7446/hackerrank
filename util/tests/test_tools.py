
from util.tools import *


def test_Tree_iter_preorder():
    values = range(7)
    edges = [(0, 1), (1, 2), (3, 2), (3, 4), (5, 1), (5, 6)]
    tree = Tree.from_values_and_edges(values, edges)
    traversed = [node.value for node in tree.iter_preorder()]
    assert traversed == [0, 1, 2, 3, 4, 5, 6]


def test_combination():
    assert nCr(6, 2) == 15
    assert nCr(6, 4) == 15
    assert nCr(1, 1) == 1
    assert nCr(1, 0) == 1


def test_permutation_with_dup():
    assert permutations_with_dup((4, )) == 1
    assert permutations_with_dup((1, 1, 1, 1)) == 24
    assert permutations_with_dup((3, 1)) == 4
