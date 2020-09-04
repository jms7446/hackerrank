from typing import List, Set, Dict


class Solution:
    def func(self, d):
        return -1


from util import *
import pytest


@pytest.mark.parametrize(['input_', 'output'], [
    (1, 1),
])
def test_solution(input_, output):
    assert Solution().func(input_) == output
