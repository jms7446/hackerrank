from typing import List, Set, Dict
import pytest
from heapq import heappop, heappush, heapify
from collections import Counter


# 356ms, 28MB (49%, 6%)
class SolutionFirst:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums = [-n for n in nums]
        res = []

        counter = Counter(nums[:k])
        window = nums[:k]
        heapify(window)
        res.append(window[0])

        for i in range(k, len(nums)):
            # update
            heappush(window, nums[i])
            counter[nums[i]] += 1
            counter[nums[i-k]] -= 1

            # throw out that is now in window.
            while counter[window[0]] == 0:
                heappop(window)
            res.append(window[0])

        return [-n for n in res]


# 288ms, 26.4MB (99%, 55%)
class SolutionSecond:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        res = []
        max_val = max(nums[:k])
        res.append(max_val)
        for i in range(k, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
            elif nums[i-k] == max_val:
                max_val = max(nums[i-k+1:i+1])
            res.append(max_val)
        return res


Solution = SolutionSecond


@pytest.mark.parametrize(['in_', 'k', 'out'], [
    ([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]),
])
def test1(in_, out, k):
    assert Solution().maxSlidingWindow(in_, k) == out
