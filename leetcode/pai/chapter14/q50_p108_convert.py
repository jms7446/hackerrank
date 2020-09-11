from typing import List, Set, Dict
import pytest
from ..data_structure import *


# 76ms, 16.2MB (71%, 45%)
class SolutionFirst:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 0:
            return None
        mid = len(nums) // 2
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:]))


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([-10,-3,0,5,9], [0, -3, 9, -10, None, 5]),
])
def test1(in_, out):
    assert btree_to_list(Solution().sortedArrayToBST(in_)) == out
