from typing import List, Set, Dict
import pytest
# from ..data_structure import *


# TODO 정신이 맑을 때 다시 로직 고민
class SolutionFirst:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_map = {word: idx for idx, word in enumerate(words)}
        for idx, word in enumerate(words):
            for i, c in enumerate(word):
                pass


Solution = SolutionFirst


@pytest.mark.parametrize(['in_', 'out'], [
    (["abcd","dcba","lls","s","sssll"], [[0,1],[1,0],[3,2],[2,4]]),
    (["bat","tab","cat"], [[0,1],[1,0]]),
    (["a",""], [[0,1],[1,0]]),
])
def test1(in_, out):
    assert Solution().palindromePairs(in_) == out
