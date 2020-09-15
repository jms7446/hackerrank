import pytest
from leetcode.data_structure import *


# 388ms, 17.3MB (96%, 38%)
class SolutionFirst:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node, seed):
            nonlocal longest
            if not node:
                return 0

            left_length = dfs(node.left, node.val)
            right_length = dfs(node.right, node.val)
            longest = max(longest, left_length + right_length)

            if node.val == seed:
                return max(left_length, right_length) + 1
            else:
                return 0

        longest = 0
        dfs(root, None)
        return longest


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([5, 4, 5, 1, 1, None, 5], 2),
    ([1, 4, 5, 4, 4, None, 5], 2),
])
def test1(in_, out):
    assert Solution().longestUnivaluePath(list_to_btree(in_)) == out
