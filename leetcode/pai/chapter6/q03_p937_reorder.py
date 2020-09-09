from typing import List
from operator import itemgetter


class SolutionFirst:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l_logs = []
        n_logs = []
        for log in logs:
            idx = log.find(' ')
            if log[idx + 1].isnumeric():
                n_logs.append(log, )
            else:
                l_logs.append(log)

        l_logs.sort(key=lambda x: itemgetter(1, 0)(x.split(' ', 1)))
        return l_logs + n_logs


Solution = SolutionFirst


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    (["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
     ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]),
])
def test1(in_, out):
    assert Solution().reorderLogFiles(in_) == out

