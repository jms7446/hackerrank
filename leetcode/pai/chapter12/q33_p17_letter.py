from typing import List, Set, Dict
import pytest
from itertools import product


# 28ms, 13.8MB (82%, 79%)
class SolutionFirst:
    """
    """
    table = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = [self.table[c] for c in digits]
        return [''.join(cs) for cs in product(*letters)]


# 32ms, 13.8MB (61%, 78%)
class SolutionRecursion:
    """
    """
    table = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letterCombinations(self, digits: str) -> List[str]:
        def loop(idx, acc):
            if idx == len(digits):
                return acc
            new_acc = []
            for c in self.table[digits[idx]]:
                new_acc += [s + c for s in acc]
            return loop(idx + 1, new_acc)

        if not digits:
            return []
        return loop(0, [""])


Solution = SolutionRecursion


@pytest.mark.parametrize(['in_', 'out'], [
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("", [])
])
def test1(in_, out):
    assert sorted(Solution().letterCombinations(in_)) == sorted(out)
