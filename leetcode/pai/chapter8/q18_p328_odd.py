from leetcode.pai.linked_list import *


class SolutionFirst:
    """
    40ms, 15.5MB (91%, 98%)
    """
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even
        node = head.next.next
        while node and node.next:
            odd.next = node
            odd = odd.next
            even.next = node.next
            even = even.next
            node = node.next.next
        if node:
            odd.next = node
            odd = odd.next
        odd.next = even_head
        even.next = None

        return head


Solution = SolutionFirst


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    (list_to_list_node([1, 2, 3, 4, 5]), [1, 3, 5, 2, 4]),
    (list_to_list_node([2, 1, 3, 5, 6, 4, 7]), [2, 3, 6, 7, 1, 5, 4]),
])
def test1(in_, out):
    assert list_node_to_list(Solution().oddEvenList(in_)) == out
