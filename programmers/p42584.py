
from itertools import chain


def solution(prices):
    answer = [0] * len(prices)
    PRICE_LOW_BOUND = -1
    stack = []
    for step, price in enumerate(chain(prices[:-1], [PRICE_LOW_BOUND])):
        while stack and price < stack[-1][1]:
            old_step, _ = stack.pop()
            answer[old_step] = step - old_step
        stack.append((step, price))
    return answer


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    ([1, 2, 3, 2, 3], [4, 3, 1, 1, 0]),
])
def test_solution(in_, out):
    assert solution(in_) == out
