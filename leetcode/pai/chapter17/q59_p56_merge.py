from typing import List, Set, Dict
import pytest


# 80ms, 15.7MB (98%, 43%)
class SolutionFirst:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return

        res = []
        intervals = sorted(intervals)
        pre_begin, pre_end = intervals[0]
        for begin, end in intervals[1:]:
            if begin > pre_end:
                res.append([pre_begin, pre_end])
                pre_begin, pre_end = begin, end
            else:
                pre_end = end if end > pre_end else pre_end
        res.append([pre_begin, pre_end])
        return res


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
    ([[1,4],[2,3]], [[1,4]]),
])
def test1(in_, out):
    assert Solution().merge(in_) == out
