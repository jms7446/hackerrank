import pytest
from leetcode.data_structure import *


# 36ms, 13.9MB (48%, 41%)
class SolutionFirst:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode, acc: int) -> (TreeNode, int):
            if node.right:
                right, acc = dfs(node.right, acc)
            else:
                right = None
            acc += node.val
            new_node = TreeNode(acc)
            if node.left:
                left, acc = dfs(node.left, acc)
            else:
                left = None
            new_node.left, new_node.right = left, right
            return new_node, acc

        return dfs(root, 0)[0]


# 28ms, 13.6MB (87%, 98%)
class SolutionRefer:
    acc = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.acc += root.val
            root.val = self.acc
            self.bstToGst(root.left)
        return root


Solution = SolutionRefer


@pytest.mark.parametrize(['in_', 'out'], [
    ([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8], [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]),
])
def test1(in_, out):
    assert btree_to_list(Solution().bstToGst(list_to_btree(in_))) == out
