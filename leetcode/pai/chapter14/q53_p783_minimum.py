import pytest
from leetcode.data_structure import *

INF = float('inf')


# 32ms, 13.9MB (76%, 59%)
class SolutionFirst:
    def minDiffInBST(self, root: TreeNode) -> int:
        def find(node: TreeNode):
            nonlocal min_diff, pre_val
            if not node:
                return
            find(node.left)
            min_diff = min(min_diff, node.val - pre_val)
            pre_val = node.val
            find(node.right)

        min_diff = INF
        pre_val = -INF
        find(root)
        return min_diff


# 32ms, 13.8MB (76%, 75%)
class SolutionRefer:
    def minDiffInBST(self, root: TreeNode) -> int:
        min_diff = INF
        pre_val = -INF

        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            min_diff = min(min_diff, node.val - pre_val)
            pre_val = node.val

            node = node.right

        return min_diff


Solution = SolutionRefer


@pytest.mark.parametrize(['in_', 'out'], [
    ([4,2,6,1,3,None,None], 1),
])
def test1(in_, out):
    assert Solution().minDiffInBST(list_to_btree(in_)) == out
