from typing import List, Set, Dict


class SolutionFirst:
    """
    """
    def xx(self, in_):
        return -1


Solution = SolutionFirst


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    (1, 1),
])
def test1(in_, out):
    assert Solution().xx(in_) == out
