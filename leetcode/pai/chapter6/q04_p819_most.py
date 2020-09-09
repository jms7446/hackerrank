from typing import List, Set, Dict
import re
from collections import Counter


class SolutionFirst:
    """
    36ms, 14MB (73%, 12%)
    """
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        word_list = re.sub("[!?',;.]", ' ', paragraph.lower()).split()
        word_list = (word for word in word_list if word not in banned)
        counter = Counter(word_list)
        return counter.most_common(1)[0][0]


class SolutionImprove:
    """
    32ms, 13.9MB (89%, 30%)
    """
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        banned.add('')
        word_list = re.split("[!?',;. ]", paragraph.lower())
        word_list = (word for word in word_list if word not in banned)
        counter = Counter(word_list)
        return counter.most_common(1)[0][0]


Solution = SolutionImprove


import pytest


@pytest.mark.parametrize(['in_', 'banned', 'out'], [
    ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"], "ball"),
])
def test1(in_, banned, out):
    assert Solution().mostCommonWord(in_, banned) == out
