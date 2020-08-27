# sys.setrecursionlimit(1000000)


def str_findall(ptn, s):
    idx = s.find(ptn)
    while idx != -1:
        yield idx
        idx = s.find(ptn, idx + 1)


def iter_pair_in_order(xs, ys):
    for x in xs:
        for y in ys:
            if x < y:
                yield x, y


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
