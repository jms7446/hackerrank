from typing import List, Set, Dict
import pytest
from collections import Counter


# 32ms, 13.8MB (63%, 78%)
class SolutionFirst:
    """
    """
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = Counter(S)
        return sum(counter[j] for j in J)


Solution = SolutionFirst


@pytest.mark.parametrize(['J', 'S', 'out'], [
    ("aA", "aAAbbbb", 3),
    ("z", "ZZ", 0),
])
def test1(J, S, out):
    assert Solution().numJewelsInStones(J, S) == out
