import sys
import math
from operator import mul
from functools import reduce
from functools import lru_cache
import inspect

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


@lru_cache(10000)
def nCr(n, r):
    if (n - r) < r:
        r = n - r
    numer = 1
    denom = 1
    for k in range(r):
        numer *= (n - k)
        denom *= (r - k)
    return numer // denom


@lru_cache(10000)
def permutations_with_dup(counts):
    return math.factorial(sum(counts)) // reduce(mul, (math.factorial(i) for i in counts if i >= 2), 1)


def eprint(*args, **kwargs):
    print(file=sys.stderr)
    print(*args, **kwargs, end='', file=sys.stderr)


def get_caller_filename():
    frame = inspect.stack()[2]      # We want caller's caller's name
    module = inspect.getmodule(frame[0])
    filename = module.__file__
    return filename


################################################################################
# KMP
################################################################################

class KMP:
    def __init__(self, ptn):
        self.ptn = ptn
        self.table = self.make_partial_match_table(ptn)

    @staticmethod
    def make_partial_match_table(ptn):
        table = [0] * len(ptn)
        cnd = 0
        for pos in range(1, len(ptn)):
            while cnd > 0 and ptn[pos] != ptn[cnd]:
                cnd = table[cnd - 1]
            if ptn[pos] == ptn[cnd]:
                cnd += 1
                table[pos] = cnd
        return table

    def search(self, in_str):
        ptn = self.ptn
        table = self.table
        len_ptn_minus1 = len(ptn) - 1
        j = 0
        for i, c in enumerate(in_str):
            while j > 0 and c != ptn[j]:
                j = table[j-1]
            if c == ptn[j]:
                if j == len_ptn_minus1:
                    yield i - len(ptn) + 1
                    j = table[j]
                else:
                    j += 1

################################################################################


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
