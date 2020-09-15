from leetcode.data_structure import *


class SolutionFirst:
    """
    linked list 는 귀찮고 머리아프다.
    """
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse(n, m, node: ListNode, prev: ListNode = None):
            pass


Solution = SolutionFirst


import pytest


@pytest.mark.parametrize(['in_', 'm', 'n', 'out'], [
    (list_to_list_node([1, 2, 3, 4, 5]), 2, 4, [1, 4, 3, 2, 5]),
])
def test1(in_, m, n, out):
    assert list_node_to_list(Solution().reverseBetween(in_, m, n)) == out
