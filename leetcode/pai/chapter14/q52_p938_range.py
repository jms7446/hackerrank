import pytest
from leetcode.data_structure import *


# 228ms, 22BM (88%, 22%)
class SolutionFirst:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        acc = 0
        if L <= root.val <= R:
            acc += root.val
        if root.val > L:
            acc += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            acc += self.rangeSumBST(root.right, L, R)
        return acc


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'L', 'R', 'out'], [
    ([10,5,15,3,7,None,18], 7, 15, 32),
    ([10,5,15,3,7,13,18,1,None,6], 6, 10, 23),
])
def test1(in_, L, R, out):
    assert Solution().rangeSumBST(list_to_btree(in_), L, R) == out
