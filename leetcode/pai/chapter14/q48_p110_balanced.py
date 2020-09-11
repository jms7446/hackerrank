from typing import List, Set, Dict
import pytest
from ..data_structure import *


# 44ms, 18.4MB (96%, 42%)
class SolutionFirst:
    def isBalanced(self, root: TreeNode) -> bool:
        is_ok = True

        def get_depth(node):
            nonlocal is_ok

            if not node or not is_ok:
                return 0
            else:
                left_depth = get_depth(node.left)
                right_depth = get_depth(node.right)
                if abs(left_depth - right_depth) > 1:
                    is_ok = False
                return max(left_depth, right_depth) + 1
        get_depth(root)
        return is_ok


# 52ms, 18.7MB (78%, 18%)
class SolutionSecond:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_depth_and_check_balance(node: TreeNode) -> (bool, int):
            if not node:
                return True, 0
            else:
                left_ok, left_depth = get_depth_and_check_balance(node.left)
                if not left_ok:
                    return False, None
                right_ok, right_depth = get_depth_and_check_balance(node.right)
                if not right_ok:
                    return False, None
                if abs(left_depth - right_depth) > 1:
                    return False, None
                return True, max(left_depth, right_depth) + 1
        return get_depth_and_check_balance(root)[0]


Solution = SolutionSecond


@pytest.mark.parametrize(['in_', 'out'], [
    ([3, 9, 20, None, None, 15, 7], True),
    ([1,2,2,3,3,None,None,4,4], False),
])
def test1(in_, out):
    assert Solution().isBalanced(list_to_btree(in_)) == out
