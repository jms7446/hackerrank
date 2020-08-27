import sys
from collections import namedtuple


################################################################################
# Tree
################################################################################

class TreeNode:
    def __init__(self, value, parent=None, children=None):
        self.value = value
        self.parent = parent
        self.children = children or []

    def __repr__(self):
        root_rep = ', root' if self.parent is None else ''
        return f'TreeNode({self.value}, #{len(self.children)}{root_rep})'


class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    @classmethod
    def from_values_and_edges(cls, values, edges, root_idx=0):
        nodes = [TreeNode(value) for value in values]
        for n1, n2 in edges:
            nodes[n1].children.append(nodes[n2])
            nodes[n2].children.append(nodes[n1])

        root = nodes[root_idx]
        stack = [root]
        while stack:
            node = stack.pop()
            for child in node.children:
                child.parent = node
                child.children.remove(node)
                if child.children:
                    stack.append(child)
        return cls(root)

    def iter_preorder(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            yield node
            sorted_children = sorted(node.children, key=lambda x: x.value, reverse=True)
            for child in sorted_children:
                stack.append(child)

################################################################################


NINF = -10000000

Score = namedtuple('Score', ('white', 'black', 'gray'))


def calc_score(population, child_scores):
    # children can be either black or gray
    white = population + sum(max(s.black, s.gray) for s in child_scores)

    # children must be gray
    # (if white exists then becomes gray, and if black exists then that black child violate rule).
    black = sum(s.gray for s in child_scores)

    # there are at least one white, and no black
    # this case is more complex, because of 'at least' constraint.
    gray = sum(max(s.white, s.gray) for s in child_scores)
    white_gray_diffs = max(s.white - s.gray for s in child_scores)
    if white_gray_diffs < 0:
        gray += 2 * white_gray_diffs

    return Score(white, black, gray)


def solve(values, edges):
    tree = Tree.from_values_and_edges(values, edges)
    for node in reversed(list(tree.iter_preorder())):
        if not node.children:
            node.score = Score(node.value, 0, NINF)
        else:
            child_scores = [child.score for child in node.children]
            node.score = calc_score(node.value, child_scores)
    return max(tree.root.score)


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    values = [int(x) for x in stdin.readline().split()]
    edges = [[int(x) - 1 for x in stdin.readline().split()] for _ in range(N - 1)]
    print(solve(values, edges))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
7
1000 3000 4000 1000 2000 2000 7000
1 2
2 3
4 3
4 5
6 2
6 7
""".strip()
    assert get_output_with_stdin(main, in_str) == "14000"


def test_main2():
    in_str = """
1
1000 
""".strip()
    assert get_output_with_stdin(main, in_str) == "1000"
