import pytest
from leetcode.data_structure import *


# 28ms, 14MB (82%, 23%)
class SolutionFirst:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# 32ms, 13.6MB (61%, 99%)
class SolutionIter:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root


Solution = SolutionIter


@pytest.mark.parametrize(['in_', 'out'], [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
])
def test1(in_, out):
    assert btree_to_list(Solution().invertTree(list_to_btree(in_))) == out
