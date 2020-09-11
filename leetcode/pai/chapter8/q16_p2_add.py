from leetcode.pai.data_structure import *


class SolutionFirst:
    """
    72ms, 13.9MB (80%, 51%)
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        node = head = ListNode(0)
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            node.next = ListNode(val)
            node = node.next

        return head.next


Solution = SolutionFirst


import pytest


@pytest.mark.parametrize(['in1', 'in2', 'out'], [
    (list_to_list_node([2, 4, 3]), list_to_list_node([5, 6, 4]), [7, 0, 8]),
])
def test1(in1, in2, out):
    assert list_node_to_list(Solution().addTwoNumbers(in1, in2)) == out
