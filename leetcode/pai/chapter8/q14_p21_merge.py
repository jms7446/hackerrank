from leetcode.pai.linked_list import *


class SolutionFirst:
    """
    40ms, 14MB (63%, 15%)
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        node = head
        while l1 and l2:
            node.next = l1 if l1.val < l2.val else l2
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return head.next


class SolutionRefer:
    """
    40ms, 14MB (63%, 8%)
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


Solution = SolutionRefer


import pytest


@pytest.mark.parametrize(['in1', 'in2', 'out'], [
    (list_to_list_node([1, 2, 4]), list_to_list_node([1, 3, 4]), [1, 1, 2, 3, 4, 4]),
])
def test1(in1, in2, out):
    assert list_node_to_list(Solution().mergeTwoLists(in1, in2)) == out
