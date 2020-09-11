from typing import List, Set, Dict
from heapq import heappush, heappop, heapify
import pytest
from leetcode.pai.data_structure import *


# hack. to avoid comparision of ListNode, insert index to element in front of ListNode.
# 88ms, 17.5MB (99%, 82%)
class SolutionFirst:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapify(heap)
        root = ListNode(0)
        cur = root
        while heap:
            _, i, node = heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                node = node.next
                heappush(heap, (node.val, i, node))
        cur.next = None
        return root.next


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([l2ln([1,4,5]),l2ln([1,3,4]),l2ln([2,6])], [1,1,2,3,4,4,5,6]),
    ([], []),
    ([l2ln([])], []),
])
def test1(in_, out):
    assert ln2l(Solution().mergeKLists(in_)) == out
