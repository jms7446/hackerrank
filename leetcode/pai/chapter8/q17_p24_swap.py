from leetcode.data_structure import *


class SolutionFirst:
    """
    36ms, 13.5MB (44%, 100%)
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        root = ListNode(0, head)
        node = head
        prev = root
        while node and node.next:
            prev.next = node.next
            next = node.next.next
            node.next.next = node
            node.next = next

            prev = node
            node = node.next

        return root.next


class SolutionRecursion:
    """
    32ms, 13.8MB (69%, 74%)
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = head.next
        head.next = self.swapPairs(head.next.next)
        node.next = head
        return node


Solution = SolutionRecursion


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    (list_to_list_node([1, 2, 3, 4]), [2, 1, 4, 3]),
])
def test1(in_, out):
    assert list_node_to_list(Solution().swapPairs(in_)) == out
