from typing import List, Set, Dict
import pytest
# from ..data_structure import *
from bisect import bisect_left


# 48ms, 18.6MB (33%, 30%)
class SolutionFirst:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        for xs in matrix:
            if not xs:
                continue

            if xs[0] > target:
                break
            idx = bisect_left(xs, target)
            if idx < len(xs) and xs[idx] == target:
                return True
        return False


# 40ms, 18.6MB (64%, 32%)
class SolutionSecond:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        for xs in matrix:
            if not xs:
                continue

            left = 0
            right = len(xs) - 1
            while left <= right:
                mid = (left + right) // 2
                if xs[mid] > target:
                    right = mid - 1
                elif xs[mid] < target:
                    left = mid + 1
                else:
                    return True

        return False


# 32ms, 18.6MB (93%, 15%)
class SolutionRefer:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            num = matrix[row][col]
            if num > target:
                col -= 1
            elif num < target:
                row += 1
            else:
                return True
        return False


Solution = SolutionRefer


@pytest.mark.parametrize(['in_', 'out'], [
    (5, True),
    (20, False),
])
def test1(in_, out):
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert Solution().searchMatrix(matrix, in_) == out
