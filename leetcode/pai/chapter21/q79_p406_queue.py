from typing import List, Set, Dict
import pytest


# 88ms, 14.1MB (99%, 81%)
class SolutionFirst:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for pair in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(pair[1], pair)
        return res


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]], [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]),
])
def test1(in_, out):
    assert Solution().reconstructQueue(in_) == out
