from typing import List, Set, Dict


class SolutionFirst:
    """
    32ms, 14MB (65%, 20%)
    """
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if p + c not in ('()', '[]', '{}'):
                    return False
        if stack:
            return False
        return True


class SolutionRefer:
    """
    32ms, 14MB (65%, 26%)
    """
    def isValid(self, s: str) -> bool:
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for c in s:
            if c not in table:
                stack.append(c)
            else:
                if not stack or table[c] != stack.pop():
                    return False
        return not stack


Solution = SolutionRefer


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
])
def test1(in_, out):
    assert Solution().isValid(in_) == out
