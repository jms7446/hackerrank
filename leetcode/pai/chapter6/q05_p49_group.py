from typing import List, Set, Dict
from collections import defaultdict


class SolutionFirst:
    """
    96ms, 16.7MB (94%, 81%)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            map[k].append(s)
        return list(map.values())


Solution = SolutionFirst


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    (["eat","tea","tan","ate","nat","bat"], [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]),
    ([""], [[""]]),
    (["a"], [["a"]]),
])
def test1(in_, out):
    res = Solution().groupAnagrams(in_)
    res = sorted([sorted(l) for l in res])
    out = sorted([sorted(l) for l in out])
    assert res == out
