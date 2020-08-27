
from ..tools import Tree


def test_Tree_iter_preorder():
    values = range(7)
    edges = [(0, 1), (1, 2), (3, 2), (3, 4), (5, 1), (5, 6)]
    tree = Tree.from_values_and_edges(values, edges)
    traversed = [node.value for node in tree.iter_preorder()]
    assert traversed == [0, 1, 2, 3, 4, 5, 6]
