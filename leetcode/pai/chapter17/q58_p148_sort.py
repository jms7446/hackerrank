from typing import List, Set, Dict
import pytest
from ..data_structure import *


# 280ms, 40.3MB (41%, 7%)
class SolutionFirst:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        fast, slow, half = head, head, None
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        left = self.sortList(head)
        right = self.sortList(slow)
        return self._merge(left, right)

    def _merge(self, left, right):
        if left and right:
            if left.val > right.val:
                left, right = right, left
            left.next = self._merge(left.next, right)
        return left or right


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([4, 2, 1, 3], [1, 2, 3, 4]),
    ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
])
def test1(in_, out):
    assert list_node_to_list(Solution().sortList(list_to_list_node(in_))) == out
