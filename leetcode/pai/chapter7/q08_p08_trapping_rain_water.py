from typing import List
from operator import itemgetter


class SolutionBySort:
    """First thought
    56ms, 15.4MB, runtime: 65%, memory: 5%
    """
    @staticmethod
    def calc_one_sided_area(heights):
        heights_with_idx = sorted(enumerate(heights), key=itemgetter(1, 0), reverse=True)
        area = 0
        cur_start = 0
        for idx, height in heights_with_idx:
            if idx >= cur_start:
                area += height * (idx - cur_start)
                cur_start = idx + 1
            else:
                area -= height
        return area

    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        highest_idx = max(enumerate(heights), key=itemgetter(1))[0]
        left_area = self.calc_one_sided_area(reversed(heights[:highest_idx]))
        right_area = self.calc_one_sided_area(heights[highest_idx+1:])
        return  left_area + right_area


class Solution:
    """Separate (no sort)
    44ms, 14.5MB, runtime: 97%, memory: 77%
    """
    def half_sized_area(self, heights):
        left_height = 0
        left_wall = 0
        area = 0
        for idx, height in enumerate(heights):
            if height >= left_height:
                area += left_height * (idx - left_wall)
                left_wall = idx + 1
                left_height = height
            else:
                area -= height
        return area

    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        highest_idx = max(enumerate(heights), key=itemgetter(1))[0]
        left_area = self.half_sized_area(heights[:highest_idx+1])
        right_area = self.half_sized_area(reversed(heights[highest_idx:]))
        return left_area + right_area


class SolutionTwoPointer:
    """Two pointer
    48ms, 14.6MB
    """
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        area = 0
        left_update = False
        while left <= right:
            if left_update:
                left_max = max(left_max, heights[left])
            else:
                right_max = max(right_max, heights[right])
            if left_max <= right_max:
                area += left_max - heights[left]
                left += 1
                left_update = True
            else:
                area += right_max - heights[right]
                right -= 1
                left_update = False
        return area


class Solution:
    """
    60ms, 14.4MB
    """
    def trap(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i in range(len(heights)):
            while stack and heights[i] > heights[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(heights[i], heights[stack[-1]]) - heights[top]

                area += distance * waters

            stack.append(i)

        return area


def test1():
    assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert Solution().trap([0, 5, 0, 10]) == 5
    assert Solution().trap([]) == 0
