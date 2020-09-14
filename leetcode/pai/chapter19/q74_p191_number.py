from typing import List, Set, Dict
import pytest
# from ..data_structure import *


# 36ms, 13.6MB (40%, 95%)
class SolutionFirst:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# 36ms, 14MB (40%, 18%)
class SolutionSecond:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


Solution = SolutionSecond


@pytest.mark.parametrize(['in_', 'out'], [
    (0b00000000000000000000000000001011, 3),
    (0b00000000000000000000000010000000, 1),
    (0b11111111111111111111111111111101, 31),
])
def test1(in_, out):
    assert Solution().hammingWeight(in_) == out
