import pytest
from leetcode.data_structure import *


# 96ms, 14.8MB (64%, 68%)
class SolutionFirst:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            t1, t2 = t2, t1
        if t2 is None:
            return t1

        # now t1 and t2 is not None
        return TreeNode(t1.val + t2.val, self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right))


Solution = SolutionFirst


@pytest.mark.parametrize(['x', 'y', 'out'], [
    ([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [3, 4, 5, 5, 4, None, 7]),
])
def test1(x, y, out):
    assert btree_to_list(Solution().mergeTrees(list_to_btree(x), list_to_btree(y))) == out
