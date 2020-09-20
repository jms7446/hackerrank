from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(1, 9):
            num = i
            for j in range(i + 1, 10):
                num = num * 10 + j
                if num > high:
                    break
                if num >= low:
                    res.append(num)
        return sorted(res)


def test():
    assert Solution().sequentialDigits(100, 300) == [123, 234]
    assert Solution().sequentialDigits(1000, 13000) == [1234,2345,3456,4567,5678,6789,12345]
