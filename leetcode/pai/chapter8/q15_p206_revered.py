from leetcode.pai.data_structure import *


class SolutionFirst:
    """
    36ms, 15.3MB (76%, 65%)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        rev = None
        while node:
            node.next, rev, node = rev, node, node.next
        return rev


class SolutionRecursive:
    """
    36ms, 19.7MB (76%, 7%)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None) -> ListNode:
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)


Solution = SolutionRecursive


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    (list_to_list_node([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1]),
])
def test1(in_, out):
    assert list_node_to_list(Solution().reverseList(in_)) == out
