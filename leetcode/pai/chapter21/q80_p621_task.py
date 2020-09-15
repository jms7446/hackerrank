from typing import List, Set, Dict
import pytest
from collections import defaultdict, Counter
from heapq import heapify, heappush, heappop
from itertools import count


class SolutionFirst:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lasts = defaultdict(lambda: -n-1)
        heap = [(-c, t) for (t, c) in Counter(tasks).items()]
        heapify(heap)

        step = 0
        while heap:
            stack = []
            while heap:
                nc, t = heappop(heap)
                if step - lasts[t] - 1 >= n:
                    lasts[t] = step
                    nc += 1
                    if nc != 0:
                        stack.append((nc, t))
                    break
                else:
                    stack.append((nc, t))
            while stack:
                heappush(heap, stack.pop())
            step += 1
        return step


class SolutionSecond:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1
                counter.subtract(task)
                counter += Counter()
            if not counter:
                break

            result += n - sub_count + 1
        return result


# TODO 나중에 코드를 살펴보자
class SolutionLeetCode:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        task_occ_dict = Counter(tasks)

        max_occ = max(task_occ_dict.values())
        number_of_taks_of_max_occ = sum((1 for task, occ in task_occ_dict.items() if occ == max_occ))

        # Make (max_occ-1) groups, each groups size is (n+1) to meet the requirement of cooling
        # Fill each group with uniform iterleaving as even as possible

        # At last, execute for the last time of max_occ jobs
        interval_for_schedule = (max_occ - 1) * (n + 1) + number_of_taks_of_max_occ

        # Minimal length is original length on best case.
        # Otherswise, it need some cooling intervals in the middle
        return max(len(tasks), interval_for_schedule)


Solution = SolutionLeetCode


@pytest.mark.parametrize(['in_', 'n', 'out'], [
    (["A","A","A","B","B","B"], 2, 8),
    (["A","A","A","B","B","B"], 0, 6),
    (["A","A","A","A","A","A","B","C","D","E","F","G"], 2, 16),
    (["A"], 1, 1),
])
def test1(in_, n, out):
    assert Solution().leastInterval(in_, n) == out
