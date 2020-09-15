import pytest
from leetcode.data_structure import *


# 귀찮아서 패스
class SolutionFirst:
    def insertionSortList(self, head: ListNode) -> ListNode:
        return ListNode()


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([4, 2, 1, 3], [1, 2, 3, 4]),
    ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
])
def test1(in_, out):
    assert list_node_to_list(Solution().insertionSortList(list_to_list_node(in_))) == out
