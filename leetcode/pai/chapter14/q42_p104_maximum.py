from typing import List, Set, Dict
import pytest
from ..data_structure import *


# 44ms, 15.3MB (64%, 73%)
class SolutionFirst:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([3,9,20,None,None,15,7], 3),
])
def test1(in_, out):
    assert Solution().maxDepth(list_to_btree(in_)) == out
