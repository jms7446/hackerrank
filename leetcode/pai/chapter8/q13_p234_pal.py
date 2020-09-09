from typing import List, Set, Dict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionFirst:
    """
    72ms, 24MB (79%, 51%)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        def list_len(list_node: ListNode) -> int:
            s = 0
            while list_node:
                s += 1
                list_node = list_node.next
            return s

        size = list_len(head)
        node, pre_node = head, None
        for _ in range(size // 2):
            pre_node, node.next, node = node, pre_node, node.next
        half_reverse_node = pre_node
        if size % 2 == 1:
            node = node.next
        half_forward_node = node
        for _ in range(size // 2):
            if half_forward_node.val != half_reverse_node.val:
                return False
            half_forward_node = half_forward_node.next
            half_reverse_node = half_reverse_node.next
        return True


class SolutionRefer:
    """
    72ms, 24MB (79%, 54%)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, rev, slow = rev, slow, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


Solution = SolutionRefer


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    (ListNode(1, ListNode(2)), False),
    (ListNode(1, ListNode(2, ListNode(2, ListNode(1)))), True),
    (ListNode(0, ListNode(2, ListNode(2, ListNode(1)))), False),
    (ListNode(0, ListNode(1, ListNode(2, ListNode(1, ListNode(0))))), True),
])
def test1(in_, out):
    assert Solution().isPalindrome(in_) == out
