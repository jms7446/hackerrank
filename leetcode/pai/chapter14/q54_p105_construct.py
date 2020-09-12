from typing import List, Set, Dict
import pytest
from ..data_structure import *


# 196ms, 87.1MB (43%, 28%)
class SolutionFirst:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def loop(preorder, inorder):
            if not preorder:
                return None
            root_val = preorder[0]
            root_idx = inorder.index(root_val)
            left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
            right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
            return TreeNode(root_val, left, right)

        return loop(preorder, inorder)


# 64ms, 19.2MB (81%, 55%)
class SolutionLeetCode:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def loop(p_start, p_end, i_start, i_end):
            if p_start >= p_end:
                return None
            root_val = preorder[p_start]
            root_idx = inorder_idx_map[root_val]        # because there is no duplicated value by problem constraint.
            cnt = root_idx - i_start
            left = loop(p_start + 1, p_start + 1 + cnt, i_start, root_idx)
            right = loop(p_start + 1 + cnt, p_end, root_idx + 1, i_end)
            return TreeNode(root_val, left, right)

        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}
        return loop(0, len(preorder), 0, len(inorder))


# 64ms, 18.1MB (81%, 85%)
class SolutionLeetCode2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def loop(start, end):
            nonlocal preorder_idx
            if start >= end:
                return None
            root_val = preorder[preorder_idx]
            preorder_idx += 1

            root_idx = inorder_idx_map[root_val]        # because there is no duplicated value by problem constraint.
            return TreeNode(root_val, loop(start, root_idx), loop(root_idx + 1, end))

        return loop(0, len(preorder))


Solution = SolutionLeetCode2


@pytest.mark.parametrize(['in1', 'in2', 'out'], [
    ([3,9,20,15,7], [9,3,15,20,7], [3,9,20,None,None,15,7]),
])
def test1(in1, in2, out):
    assert btree_to_list(Solution().buildTree(in1, in2)) == out
