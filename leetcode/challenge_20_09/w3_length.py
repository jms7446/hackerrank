from typing import List, Set, Dict
import pytest


class SolutionFirst:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.rsplit(maxsplit=1)
        return len(words[-1]) if words else 0


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    ("Hello World", 5),
    ("a ", 1),
    ("", 0),
])
def test1(in_, out):
    assert Solution().lengthOfLastWord(in_) == out
