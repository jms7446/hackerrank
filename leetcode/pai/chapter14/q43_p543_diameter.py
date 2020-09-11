from typing import List, Set, Dict
import pytest
from ..data_structure import *


# 48ms, 15.1MB (64%, 8%)
class SolutionFirst:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def calc_max_depth_and_diameter(node):
            if node is None:
                return 0, 0
            left_depth, left_diameter = calc_max_depth_and_diameter(node.left)
            right_depth, right_diameter = calc_max_depth_and_diameter(node.right)
            depth = max(left_depth, right_depth) + 1
            diameter = max(left_diameter, right_diameter, left_depth + right_depth)
            return depth, diameter
        return calc_max_depth_and_diameter(root)[1]


# 40ms, 15.8MB (93%, 61%)
class SolutionRefer:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def calc_diameter(node):
            nonlocal longest
            if node is None:
                return 0
            left_depth = calc_diameter(node.left)
            right_depth = calc_diameter(node.right)
            longest = max(longest, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        longest = 0
        calc_diameter(root)
        return longest


Solution = SolutionRefer


@pytest.mark.parametrize(['in_', 'out'], [
    ([1, 2, 3, 4, 5], 3),
])
def test1(in_, out):
    assert Solution().diameterOfBinaryTree(list_to_btree(in_)) == out
